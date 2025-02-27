# LoLLaneAssistant2.0

A Python-based desktop application built with Tkinter for selecting champions based on their roles (e.g., Support, ADC, Mid, Jungle, Top) in a game-like interface. The application features a loading screen with a progress bar and transitions to a champion selection window with lane-specific buttons and a fully functional search bar, pulling data from a SQL Server database.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Description

This project is a simple GUI application designed to simulate a champion selection interface, similar to those found in multiplayer online games like League of Legends. It starts with a loading screen featuring a progress bar, then transitions to a champion selection screen where users can filter champions by their lane roles via buttons or search for specific champions.

## Features

- **Loading Screen**: Displays a progress bar that fills up before transitioning to the main interface.
- **Champion Selection**: Interactive buttons for filtering champions by lane (Support, ADC, Mid, Jungle, Top).
- **Search Functionality**: A search bar that filters champions in real-time based on user input, with placeholder text that clears on focus.
- **Database Integration**: Connects to a SQL Server database (`lolchamps`) to fetch champion names and lane associations.
- **Custom Styling**: Uses a dark-themed UI with lane-specific icons and a canvas-based grid layout for displaying champions.

## Requirements

- **Python 3.x**
- **Tkinter** (usually included with Python)
- **pyodbc** (for SQL Server database connectivity)
- **time module** (standard library)

## Additional Dependencies

- **ODBC Driver 17 for SQL Server**: Required for `pyodbc` to connect to the SQL Server database.
- **Custom Lane Icons**: Located in the `Resources/Images/Lane_icons/` directory (included in the repository).
- **SQL Server Database**: A database named `lolchamps` with tables `Champions`, `ChampionLanes`, and `Lanes`. A sample script (`lolchamps.sql`) is provided in the repository.
 
## Installation

1. **Clone the Repository: git clone https://github.com/your-username/champion-selector.git cd champion-selector
2. **Ensure Python is Installed: Verify you have Python 3.x installed by running: python --version If not installed, download it from python.org.
3. **Install Dependencies: Install pyodbc using pip: pip install pyodbc
4. **Prepare Resources: Ensure the Resources/Images/Lane_icons/ folder contains the necessary PNG files (support.png, adc.png, mid.png, jungle.png, top.png).
5. **Set Up SQL Server:
- **Install SQL Server if not already present (e.g., SQL Server Express from Microsoft).
--Restore the provided database:
--Open SQL Server Management Studio (SSMS).
--Connect to your local SQL Server instance (e.g., MARCO or localhost).
--Open db/lolchamps.sql in SSMS (File > Open > File) and execute it to create and populate the lolchamps database.
--Modify the server name in main.py if your instance isn’t named MARCO
6. **Run the Application: python main.py

## Usage

1. Launch the application by running python main.py.
2. Click the "Start" button on the loading screen to initiate the progress bar.
3. Once the progress bar completes, the champion selection screen appears.
4. Use the lane buttons (Support, ADC, Mid, Jungle, Top) to filter champions or type in the search bar (search functionality is placeholder-only for now).
5. Customize or extend the select_champion method in the champ_Select class to implement actual champion selection logic.

## File Structure
LoLLaneAssistant2.0/
├── main.py                 Main application script
├── db/
│   └── lolchamps.sql       SQL script to create and populate the lolchamps database
├── Resources/
│   └── Images/
│       └── Lane_icons/     Folder containing lane icon images
│           ├── support.png
│           ├── adc.png
│           ├── mid.png
│           ├── jungle.png
│           └── top.png
└── README.md               This README file

## Contributing
Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (git checkout -b feature/your-feature).
3. Make your changes and commit them (git commit -m "Add your message").
4, Push to your branch (git push origin feature/your-feature).
5. Open a Pull Request.
** Please ensure your code follows PEP 8 style guidelines and includes comments where necessary.

## Potential Improvements

Implement the select_champion method to display champions on the canvas.
Add functionality to the search bar.
Include a database or list of champions.
Enhance UI with more interactive elements.
License
This project is licensed under the MIT License. See the LICENSE file for details. (Note: If you haven't added a license file yet, you can create one or specify a different license.)




















