# LoLLaneAssistant2.0

A Python-based desktop application built with Tkinter for selecting champions based on their roles (e.g., Support, ADC, Mid, Jungle, Top) in a game-like interface. The application features a loading screen with a progress bar and transitions to a champion selection window with lane-specific buttons and a search bar.

Table of Contents

Description
Features
Requirements
Installation
Usage
File Structure
Contributing
License
Description
This project is a simple GUI application designed to simulate a champion selection interface, similar to those found in multiplayer online games like League of Legends. It starts with a loading screen featuring a progress bar, then transitions to a champion selection screen where users can filter champions by their lane roles via buttons or search for specific champions.

Features

Loading Screen: Displays a progress bar that fills up before transitioning to the main interface.
Champion Selection: Interactive buttons for selecting champions by lane (Support, ADC, Mid, Jungle, Top).
Search Functionality: A placeholder search bar for finding champions (to be fully implemented).
Custom Styling: Uses a dark-themed UI with lane-specific icons and a canvas-based layout.
Requirements

Python 3.x
Tkinter (usually included with Python)
time module (standard library)
Additional Dependencies

Custom lane icons located in the Resources/Images/Lane_icons/ directory (included in the repository).
Installation

Clone the Repository: git clone https://github.com/your-username/champion-selector.git cd champion-selector
Ensure Python is Installed: Verify you have Python 3.x installed by running: python --version If not installed, download it from python.org.
Prepare Resources: Ensure the Resources/Images/Lane_icons/ folder contains the necessary PNG files (support.png, adc.png, mid.png, jungle.png, top.png). These are referenced in the code.
Run the Application: python main.py
Usage

Launch the application by running python main.py.
Click the "Start" button on the loading screen to initiate the progress bar.
Once the progress bar completes, the champion selection screen appears.
Use the lane buttons (Support, ADC, Mid, Jungle, Top) to filter champions or type in the search bar (search functionality is placeholder-only for now).
Customize or extend the select_champion method in the champ_Select class to implement actual champion selection logic.
File Structure
champion-selector/
├── main.py                 Main application script
├── Resources/
│   └── Images/
│       └── Lane_icons/     Folder containing lane icon images
│           ├── support.png
│           ├── adc.png
│           ├── mid.png
│           ├── jungle.png
│           └── top.png
└── README.txt              This README file

Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Make your changes and commit them (git commit -m "Add your message").
Push to your branch (git push origin feature/your-feature).
Open a Pull Request.
Please ensure your code follows PEP 8 style guidelines and includes comments where necessary.

Potential Improvements

Implement the select_champion method to display champions on the canvas.
Add functionality to the search bar.
Include a database or list of champions.
Enhance UI with more interactive elements.
License
This project is licensed under the MIT License. See the LICENSE file for details. (Note: If you haven't added a license file yet, you can create one or specify a different license.)




















