# LoLLaneAssistant2.0

A Python-based desktop application built with Tkinter for selecting champions based on their roles (e.g., Support, ADC, Mid, Jungle, Top) in a game-like interface. The application features a loading screen with a progress bar and transitions to a champion selection window with lane-specific buttons and a fully functional search bar, pulling data from a SQL Server database.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Loading Screen**: Displays a "Start" button and a progress bar to transition to the champion selection screen.
- **Progress Bar**: Horizontal, determinate ttk.Progressbar (300 pixels long), filling from 0 to 100% over approximately 3 seconds.
- **Audio Effects**: Plays sound effects using pygame.mixer:
  - Single sound: button.mp3.
  - Dual sound combo: matchFound.mp3 and button.mp3 triggered by the "Start" button.
- **Champion Selection**: Interactive buttons for filtering champions by lane (Support, ADC, Mid, Jungle, Top).
- **Search Functionality**: A search bar that filters champions in real-time based on user input, with placeholder text that clears on focus.
- **Database Integration**: Connects to a SQL Server database (`lolchamps`) to fetch champion names and lane associations.
- **Custom Styling**: Uses a dark-themed UI with lane-specific icons and a canvas-based grid layout for displaying champions.
- **Scrollbar**: 
- **Champion Display Grid**: 10-column grid with 70x70 pixel canvases, each showing a resized 50x50 pixel champion icon and name (Arial, 8pt).
- **Top Frame Barrier**: Fixed 70-pixel-high top frame prevents champion frames from scrolling behind search and buttons.
- **Bottom Frame Barrier**: Fixed 70-pixel-high bottom frame ensures champion frames don’t scroll beyond the visible window.
- **Semi-Transparent Overlay**: A gold (#C8AA6E80) rectangle with a 5-pixel border surrounds the entire champion select frame, including the scrollbar.

## Requirements

- **Python 3.x**
- **Tkinter** (usually included with Python)
- **pyodbc** (for SQL Server database connectivity)
- **time module** (standard library)

## Additional Dependencies

- **ODBC Driver 17 for SQL Server**: Required for `pyodbc` to connect to the SQL Server database.
- **Lane Icons**: Located in the `Resources/Images/Lane_icons/` directory (included in the repository).
- **Champion Icons**: Located in the `Resources/Images/Champion_icons/` directory (included in the repository).
- **SQL Server Database**: A database named `lolchamps` with tables `Champions`, `ChampionLanes`, and `Lanes`. A sample script (`lolchamps.sql`) is provided in the repository.
- **pygame**: For audio playback of sound effects.
- **Pillow (PIL)**: For resizing and displaying champion icons.

## Installation

1. **Clone the Repository**: git clone https://github.com/ThatGui887/LoLLaneAssistant2.git 
2. **Ensure Python is Installed**: Verify you have Python 3.x installed by running: python --version If not installed, download it from python.org.
3. **Install Dependencies**: Install pyodbc using pip: pip install pyodbc, (pip install requests urllib3 six for downloading champion ioconsd)
   - Install pygame: `pip install pygame`
   - Install Pillow: `pip install Pillow`
4. **Prepare Resources**: Ensure the Resources/Images/Lane_icons/ and Resources/Images/Champ_icons/ folder contains the necessary PNG files (support.png, adc.png, Yasuo.png, Pantheon.png).
   - Ensure Resources/SoundFX/UI/ contains button.mp3 and matchFound.mp3.
5. **Set Up SQL Server**:
   - **Install SQL Server** if not already present (e.g., SQL Server Express from Microsoft).
   - Restore the provided database:
     - Open SQL Server Management Studio (SSMS).
     - Connect to your local SQL Server instance (e.g., MARCO or localhost).
     - Open db/lolchamps.sql in SSMS (File > Open > File) and execute it to create and populate the lolchamps database.
     - Modify the server name in main.py if your instance isn’t named MARCO
6. **Run the Application**: python main.py
7. **Use Download_icons.py to retrieve Champion Icons**:
   - Change the version of "http://ddragon.leagueoflegends.com/cdn/15.1.1/img/champion/" from 15.1.1 to the latest version everytime a new update releases.

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
│       ├── Lane_icons/     Folder containing lane icon images
│       │   ├── support.png
│       │   ├── adc.png
│       │   ├── mid.png
│       │   ├── jungle.png
│       │   ├── all.png
│       │   └── top.png
│       └── Champ_icons/    Folder containing champion icon images (populated separately)
│   └── SoundFX/
│       └── UI/             Folder containing sound effect files
│           ├── button.mp3
│           └── matchFound.mp3
└── README.md               This README file

## Contributing
Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (git checkout -b feature/your-feature).
3. Make your changes and commit them (git commit -m "Add your message").
4. Push to your branch (git push origin feature/your-feature).
5. Open a Pull Request.
** Please ensure your code follows PEP 8 style guidelines and includes comments where necessary.

## Potential Improvements

Implement the select_champion method to display champions on the canvas.
Add functionality to the search bar.
Include a database or list of champions.
Enhance UI with more interactive elements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
