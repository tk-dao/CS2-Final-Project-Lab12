"""
logic.py
---------
Main application logic for the TV Remote GUI built with PyQt6.
Connects GUI elements to Television behavior using signals and slots.
"""

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import *
from remote import *
from television import *


class Logic(QMainWindow, Ui_tv_remote_gui, Television):
    """
    Main Logic class that integrates the GUI and television control.
    Inherits from QMainWindow, the generated UI class, and the Television logic class.
    """

    def __init__(self) -> None:
        """
        Initializes the GUI, sets up signals, and checks the power state.
        """
        QMainWindow.__init__(self)
        Television.__init__(self)
        self.setupUi(self)
        self.check_power()  # Set screen to black and disable channel label

        # Button connections
        self.power_button.clicked.connect(lambda: (self.power(), self.check_power()))
        self.channel_up_button.clicked.connect(lambda: (self.channel_up(), self.update_channel_display(), self.check_power()))
        self.channel_down_button.clicked.connect(lambda: (self.channel_down(), self.update_channel_display(), self.check_power()))
        self.volume_up_button.clicked.connect(lambda: (self.volume_up(), self.update_volume_slider()))
        self.volume_down_button.clicked.connect(lambda: (self.volume_down(), self.update_volume_slider()))
        self.mute_button.clicked.connect(lambda: (self.mute(), self.update_volume_slider()))

        self.channel_1.clicked.connect(lambda: (self.channel_set(1), self.check_power()))
        self.channel_2.clicked.connect(lambda: (self.channel_set(2), self.check_power()))
        self.channel_3.clicked.connect(lambda: (self.channel_set(3), self.check_power()))
        self.channel_4.clicked.connect(lambda: (self.channel_set(4), self.check_power()))
        self.channel_5.clicked.connect(lambda: (self.channel_set(5), self.check_power()))
        self.channel_6.clicked.connect(lambda: (self.channel_set(6), self.check_power()))

    def check_power(self) -> None:
        """
        Updates screen and label visibility based on the power status of the TV.
        Handles image loading errors with a fallback to black screen.
        """
        if self.get_status():
            self.channel_label.setVisible(True)
            try:
                self.screen.setPixmap(QPixmap(f"images/channel_{self.get_channel()}.png"))
            except Exception as e:
                print(f"Error loading channel image: {e}")
                self.screen.setPixmap(QPixmap("images/black_screen.png"))
            self.volume_slider.setVisible(True)
            if self.get_muted():
                self.mute_label.setVisible(True)
        else:
            self.channel_label.setVisible(False)
            try:
                self.screen.setPixmap(QPixmap("images/black_screen.png"))
            except Exception as e:
                print(f"Error loading black screen image: {e}")
            self.volume_slider.setVisible(False)
            self.mute_label.setVisible(False)

    def channel_set(self, channel_num: int) -> None:
        """
        Sets the channel to a specific number and updates the display.
        """
        self.set_channel(channel_num)
        self.update_channel_display()

    def update_channel_display(self) -> None:
        """
        Updates the channel label with the current channel.
        """
        self.channel_label.setText(f"Channel {self.get_channel()}")

    def update_volume_slider(self) -> None:
        """
        Updates the volume slider and mute label visibility.
        """
        if self.get_muted():
            self.mute_label.setVisible(True)
        else:
            self.mute_label.setVisible(False)
        self.volume_slider.setValue(self.get_volume())
