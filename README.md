
# CS:GO Aim Assist

CS:GO Aim Assist is a project designed to provide auto-aim assistance for Counter-Strike: Global Offensive (CS:GO). This project uses a pre-trained YOLOv5 model to detect targets (e.g., players) in the game and moves the mouse cursor to the detected targets' positions.

## Overview

This project is for educational purposes to demonstrate the use of machine learning and computer vision in real-time applications. It captures screen frames, detects targets using the YOLOv5 model, and moves the mouse cursor to the detected target's location.

## Features

- Real-time screen capture
- Object detection using YOLOv5
- Mouse movement to detected targets

## Installation

### Prerequisites

- Python 3.9
- Git
- Conda (Miniconda or Anaconda)

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/csgo-aim-assist.git
   cd csgo-aim-assist
   ```

2. **Create and Activate Conda Environment**

   ```bash
   conda create --name myenv python=3.9
   conda activate myenv
   ```

3. **Install Project Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Clone and Install YOLOv5 Dependencies**

   ```bash
   cd yolov5
   pip install -r requirements.txt
   cd ..

## Usage

1. **Prepare an Image for Testing**

   Download an image with a person in it and save it to your desktop (e.g., `person.jpg`). Update the `capture_screen.py` file to load this image.

   ```python
   import cv2

   def capture_screen():
       img = cv2.imread('/path/to/your/desktop/person.jpg')
       return img
   ```

2. **Run the Main Script**

   ```bash
   python main.py
   ```

3. **Press 'q' to Quit**

   The script will display the captured screen with detected targets. Press 'q' to quit the display window.

## Project Structure

```
csgo-aim-assist/
│
├── yolov5/                   # Cloned YOLOv5 repository
│   ├── ...                   # YOLOv5 files and directories
│   └── requirements.txt      # YOLOv5 dependencies
│
├── src/                      # Source code
│   ├── __init__.py           # Make src a Python package (can be an empty file)
│   ├── capture_screen.py     # Screen capture module
│   ├── detect_target.py      # Object detection module
│   ├── move_aim.py           # Aim movement module
│   └── main.py               # Main script
│
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Modules

- **capture_screen.py**: Captures the screen or loads an image from your desktop.
- **detect_target.py**: Uses YOLOv5 to detect targets in the captured frame.
- **move_aim.py**: Moves the mouse cursor to the detected target's position.
- **main.py**: Integrates the modules to perform real-time detection and aiming.

## Disclaimer

This project is for educational purposes only. Using auto-aim assistance in online games like CS:GO is against the terms of service and can result in bans or other penalties. Always use such tools responsibly and ethically.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
