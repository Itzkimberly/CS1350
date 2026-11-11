"""
HW 8 - Error Handling and Exceptions
  - Exception_Lecture1: practice_3_complete_pattern()
  - Exception_Lecture2: practice_2_custom_exceptions()
  - Exception_Lecture2: practice_3_complete_system()
"""
import os


# ---------------------------------------------------------------------------
# Exception_Lecture1: practice_3_complete_pattern()  (50 pts)
# ---------------------------------------------------------------------------
def practice_3_complete_pattern():
    """
    Practice with try-except-else-finally
    """
    print("\n" + "=" * 50)
    print("EXERCISE 3: Complete Exception Pattern")
    print("=" * 50)

    # TODO 1: File processor with complete error handling
    def process_file(filename):
        """
        Read file, process content, ensure file is closed.
        Return processed content or None.
        """
        file = None
        try:
            # Only the risky operation goes in the try block
            file = open(filename, 'r')
        except FileNotFoundError:
            print(f"  ❌ File '{filename}' not found")
            return None
        except PermissionError:
            print(f"  ❌ No permission to read '{filename}'")
            return None
        except OSError as e:
            # Other OS-level problems (e.g., path is a directory)
            print(f"  ❌ Could not open '{filename}': {e}")
            return None
        else:
            # File opened successfully, now process its content
            content = file.read()
            processed = content.upper().split()
            print(f"  ✅ Processed '{filename}' ({len(processed)} words)")
            return processed
        finally:
            # Always runs, even when a return statement fired above
            if file is not None:
                print(f"  Closing '{filename}'...")
                file.close()

    # Test with different scenarios
    test_files = ["exists.txt", "missing.txt", "/root/file"]
    for filename in test_files:
        result = process_file(filename)
        print(f"Processing '{filename}': {result}")

    # TODO 2: Resource manager
    class ResourceManager:
        def __init__(self, name):
            self.name = name
            self.resource = None

        def acquire(self):
            """Acquire resource - might fail."""
            if self.resource is not None:
                raise RuntimeError(f"{self.name} is already acquired")
            print(f"  Acquiring {self.name}...")
            self.resource = f"{self.name}-handle"

        def release(self):
            """Release resource - must always happen."""
            if self.resource is None:
                return  # Nothing to release; safe to call repeatedly
            print(f"  Releasing {self.name}...")
            self.resource = None

        def use(self):
            """Use resource - only if acquired."""
            if self.resource is None:
                raise RuntimeError(f"{self.name} has not been acquired")
            print(f"  Using {self.resource}")
            return f"result from {self.resource}"

    # Test resource management
    rm = ResourceManager("Database")

    # Normal flow
    print("\nResource test 1 (normal):")
    try:
        rm.acquire()
        result = rm.use()
    except RuntimeError as e:
        print(f"  ❌ Resource error: {e}")
    else:
        print(f"  ✅ Success: {result}")
    finally:
        rm.release()

    # Error flow: using the resource without acquiring it first
    print("\nResource test 2 (use without acquire):")
    try:
        result = rm.use()
    except RuntimeError as e:
        print(f"  ❌ Resource error: {e}")
    else:
        print(f"  ✅ Success: {result}")
    finally:
        rm.release()


# ---------------------------------------------------------------------------
# Exception_Lecture2: practice_2_custom_exceptions()  (50 pts)
# ---------------------------------------------------------------------------
def practice_2_custom_exceptions():
    """
    Practice creating and using custom exceptions
    """
    print("\n" + "=" * 50)
    print("EXERCISE 5: Custom Exceptions")
    print("=" * 50)

    # TODO 1: Create custom exceptions
    class GameError(Exception):
        """Base class for game exceptions."""
        pass

    class InvalidMoveError(GameError):
        """Invalid game move."""
        def __init__(self, position, reason):
            self.position = position
            self.reason = reason
            super().__init__(f"Invalid move at {position}: {reason}")

    class GameOverError(GameError):
        """Game has ended."""
        def __init__(self, winner):
            self.winner = winner
            if winner:
                message = f"Game is over, winner is {winner}"
            else:
                message = "Game is over, it was a draw"
            super().__init__(message)

    # TODO 2: Use custom exceptions
    class TicTacToe:
        def __init__(self):
            self.board = [[' ' for _ in range(3)] for _ in range(3)]
            self.current_player = 'X'
            self.game_over = False
            self.winner = None

        def make_move(self, row, col):
            # Game already finished
            if self.game_over:
                raise GameOverError(self.winner)

            # Bounds check comes BEFORE the taken check so we never index
            # outside the board (and negative indexes don't wrap around)
            if not (0 <= row < 3 and 0 <= col < 3):
                raise InvalidMoveError((row, col), "position is out of bounds")

            if self.board[row][col] != ' ':
                raise InvalidMoveError((row, col), "position is already taken")

            self.board[row][col] = self.current_player

            if self._check_winner():
                self.game_over = True
                self.winner = self.current_player
            elif all(cell != ' ' for r in self.board for cell in r):
                self.game_over = True  # Board full, draw
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

        def _check_winner(self):
            b = self.board
            lines = (
                [b[r] for r in range(3)]                          # rows
                + [[b[r][c] for r in range(3)] for c in range(3)]  # columns
                + [[b[i][i] for i in range(3)],                   # diagonal
                   [b[i][2 - i] for i in range(3)]]               # anti-diagonal
            )
            return any(line[0] != ' ' and line.count(line[0]) == 3
                       for line in lines)

    # Test the game
    game = TicTacToe()
    test_moves = [
        (0, 0),  # Valid
        (0, 0),  # Already taken
        (5, 5),  # Out of bounds
    ]

    for row, col in test_moves:
        try:
            game.make_move(row, col)
            print(f"✅ Move ({row}, {col}) successful")
        except InvalidMoveError as e:
            print(f"❌ Invalid move: {e}")
        except GameOverError as e:
            print(f"🏁 Game over: {e}")

    # Extra: play out a win to exercise GameOverError
    print("\nPlaying to a win:")
    for row, col in [(1, 0), (0, 1), (1, 1), (0, 2)]:  # O, X, O, X -> X wins
        try:
            game.make_move(row, col)
            print(f"✅ Move ({row}, {col}) successful")
        except InvalidMoveError as e:
            print(f"❌ Invalid move: {e}")
        except GameOverError as e:
            print(f"🏁 Game over: {e}")

    try:
        game.make_move(2, 2)
    except GameOverError as e:
        print(f"🏁 Game over: {e}")


# ---------------------------------------------------------------------------
# Exception_Lecture2: practice_3_complete_system()  (50 pts)
# ---------------------------------------------------------------------------
def practice_3_complete_system():
    """
    Build a complete error handling system
    """
    print("\n" + "=" * 50)
    print("EXERCISE 6: Complete Error Handler")
    print("=" * 50)

    class FileProcessor:
        def __init__(self):
            self.processed_files = []
            self.failed_files = []  # list of (filename, error message)

        def process_file(self, filename):
            """
            Process a single file with complete error handling.
            Returns True on success, False on failure.
            """
            file = None
            try:
                file = open(filename, 'r')
            except FileNotFoundError:
                print(f"  ❌ File not found: {filename}")
                self.failed_files.append((filename, "File not found"))
                return False
            except PermissionError:
                print(f"  ❌ Permission denied: {filename}")
                self.failed_files.append((filename, "Permission denied"))
                return False
            except Exception as e:
                print(f"  ❌ Unexpected error with {filename}: {e}")
                self.failed_files.append((filename, f"Unexpected error: {e}"))
                return False
            else:
                # File opened; read and process it. This is still guarded
                # because reading can fail too (bad encoding, I/O error).
                try:
                    content = file.read()
                    word_count = len(content.split())
                except Exception as e:
                    print(f"  ❌ Error reading {filename}: {e}")
                    self.failed_files.append((filename, f"Read error: {e}"))
                    return False
                print(f"  ✅ Processed {filename} ({word_count} words)")
                self.processed_files.append(filename)
                return True
            finally:
                # Always close the file if it was opened
                if file is not None:
                    file.close()

        def process_directory(self, directory):
            """
            Process all files in directory, collecting errors.
            """
            try:
                names = sorted(os.listdir(directory))
            except (FileNotFoundError, NotADirectoryError):
                print(f"  ❌ Directory not found: {directory}")
                self.failed_files.append((directory, "Directory not found"))
                return
            except PermissionError:
                print(f"  ❌ Permission denied: {directory}")
                self.failed_files.append((directory, "Permission denied"))
                return

            for name in names:
                path = os.path.join(directory, name)
                if os.path.isfile(path):
                    # Errors are recorded inside process_file, so one bad
                    # file never stops the rest of the directory
                    self.process_file(path)

        def get_report(self):
            """
            Get processing report.
            """
            total = len(self.processed_files) + len(self.failed_files)
            return {
                "total": total,
                "succeeded": len(self.processed_files),
                "failed": len(self.failed_files),
                "processed_files": list(self.processed_files),
                "failed_files": list(self.failed_files),
            }

    # Test the processor
    processor = FileProcessor()

    test_files = [
        "valid.txt",
        "missing.txt",
        "/root/restricted.txt"
    ]

    for filename in test_files:
        processor.process_file(filename)

    report = processor.get_report()
    print(f"Report: {report}")


# Run the practice
if __name__ == "__main__":
    practice_3_complete_pattern()
    practice_2_custom_exceptions()
    practice_3_complete_system()