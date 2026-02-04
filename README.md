# Event Tracking Tool

## Overview
The Event Tracking Tool is a Python-based automation project designed to collect, process, and store event-related data in a structured and reliable manner.  
It follows a modular architecture that separates scraping logic, data handling, and configuration, making the system easy to maintain and extend.

This project is suitable for academic use, industrial training, and as a foundation for real-world data automation workflows.

---

## Key Features
- Automated event data collection
- Modular and readable code structure
- Centralized configuration management
- Sheet-based data storage for easy analysis
- Lightweight and extensible design

---

## Technology Stack
- Programming Language: Python
- Data Collection: Web scraping utilities
- Data Storage: Spreadsheet-based tracking
- Version Control: Git and GitHub

---

## Project Structure
Event_Tracking_tool/
├── main.py            Entry point of the application  
├── scraper.py         Event data scraping logic  
├── sheet_manager.py   Sheet read/write operations  
├── config.py          Configuration and constants  
├── requirements.txt   Project dependencies  
├── .gitignore         Ignored files and directories  
└── README.md          Project documentation  

---

## Installation

Clone the repository:
git clone https://github.com/Ojas15468/Event_Tracking_tool.git
cd Event_Tracking_tool

Create and activate a virtual environment (recommended):
python -m venv venv
source venv/bin/activate        (Linux/Mac)
venv\Scripts\activate           (Windows)

Install dependencies:
pip install -r requirements.txt

---

## Configuration
Update the configuration values in the config.py file as required.  
This may include target URLs, sheet identifiers, and authentication details.

For security reasons, sensitive credentials should not be hard-coded and should be managed using environment variables where possible.

---

## Usage
Run the application using:
python main.py

The application workflow:
1. Collects event data from configured sources  
2. Processes and formats the data  
3. Stores the output in the configured sheet  

---

## Use Cases
- Event monitoring and tracking
- Academic and industrial training projects
- Data automation practice
- Python scripting and scraping demonstrations

---

## Future Improvements
- Improved error handling and logging
- Command-line interface support
- Database integration
- Task scheduling and automation
- Unit testing and CI/CD setup

---

## Contributing
Contributions are welcome.  
Fork the repository, create a new branch, commit your changes, and open a pull request.

---

## License
This project is licensed under the MIT License.

---

## Author
Ojas  
GitHub: https://github.com/Ojas15468
