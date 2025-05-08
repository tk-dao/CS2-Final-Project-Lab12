"""main.py
---------
Entry point for the TV Remote application.
"""

from logic import *

def main() -> None:
    """
    Launches the PyQt6 application window.
    """
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()

if __name__ == '__main__':
    main()
