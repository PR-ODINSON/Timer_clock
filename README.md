# Countdown Timer

A simple yet visually appealing countdown timer desktop application built using Python and Tkinter. This project allows users to set a timer, view the remaining time dynamically, and receive notifications when the timer completes.

## Features

- **User Input**: Easily set hours, minutes, and seconds for the countdown.
- **Dynamic Timer**: Displays the remaining time in `HH:MM:SS` format and updates the elapsed time.
- **Notifications**:
  - Pop-up alert when the timer completes.
  - Desktop notification using the `plyer` library.
- **Modern Interface**: Clean and user-friendly dark theme with enhanced fonts and layout.

## Technologies Used

- **Python**: Core programming language.
- **Tkinter**: For building the graphical user interface.
- **Plyer**: To generate desktop notifications.
- **Threading**: Ensures the app remains responsive during the countdown.

## Prerequisites

- Python 3.x installed on your system.
- Required Python libraries:
  ```bash
  pip install plyer
  ```

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/countdown-timer.git
   ```
2. Navigate to the project directory:
   ```bash
   cd countdown-timer
   ```
3. Run the script:
   ```bash
   python countdown_timer.py
   ```

## Usage

1. Enter the desired time in hours, minutes, and seconds.
2. Click the "Start Timer" button to begin the countdown.
3. View the countdown and elapsed time in real-time.
4. Receive notifications when the time is up.


## Contributing

Feel free to fork the repository and make improvements. Pull requests are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details!

## Acknowledgements

- [Plyer Documentation](https://plyer.readthedocs.io/)
- [Tkinter Reference](https://docs.python.org/3/library/tkinter.html)

---

Enjoy using the Countdown Timer! If you have any suggestions or feedback, feel free to create an issue or reach out.

