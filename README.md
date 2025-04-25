# Dictionary GUI Application

This project is a graphical user interface (GUI) application that allows users to input English words and visualize the loudness of their phonemes. The application fetches phonetic data from an external dictionary API and displays the corresponding loudness levels in a bar chart.

## Project Structure

```
dictionary_gui_app
├── src
│   ├── app.py            # Main entry point of the GUI application
│   ├── phoneme_utils.py  # Functions for phoneme processing
│   ├── api_utils.py      # API interaction functions
│   └── plot_utils.py     # Functions for plotting loudness data
├── requirements.txt      # List of dependencies
└── README.md             # Documentation for the project
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd dictionary_gui_app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python app.py
   ```

2. Enter English word(s) in the input field and click the "Submit" button to see the phonetic transcription and loudness plot.

3. To exit the application, close the window or click the "Exit" button.

## Dependencies

- Tkinter: For creating the GUI.
- Matplotlib: For plotting the loudness data.
- Requests: For making API calls to fetch phonetic data.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.
