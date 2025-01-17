# SQL Seer - A SQL Notebook

This utility is a lightweight interactive web-based SQL editor for various database types. Quickly run unlimited SQL queries across different databases simultaneously in a notebook format. Inspired by my heavy use of Jupyter Notebooks, I wanted a similar utility for quickly querying against databases.

This utility also ships with its own database so you can jump to adding data and querying as well if desired. Although it's designed to allow you to connect to and query an unlimited number of databases, no external database is technically required.


[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#) [![SQLite](https://img.shields.io/badge/SQLite-%2307405e.svg?logo=sqlite&logoColor=white)](#) [![HTML](https://img.shields.io/badge/HTML-%23E34F26.svg?logo=html5&logoColor=white)](#)  [![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=000)](#) [![FastAPI](https://img.shields.io/badge/FastAPI-009485.svg?logo=fastapi&logoColor=white)](#) [![HTMX](https://img.shields.io/badge/HTMX-36C?logo=htmx&logoColor=fff)](#)


![In Development](https://img.shields.io/badge/status-In%20Development-yellow)
### Open Development Tasks
 
| Task                                           | Status                          |
|------------------------------------------------|---------------------------------|
| Finalize query delivery logic against target databases | COMPLETED ✅                  |
| Cascading results windows                      | In Progress                     |
| Results export to CSV, Excel, and more         | In Progress                         |
| Implement Redis or local DB for caching of historical queries | Pending                         |
| Docker deployment                              | Pending                         |




### Supported Databases
- Postgres
- Oracle
- SQL Server
- SQLite (add your own connections if desired, but SQLite also comes included)


### Configuring Connections
Connections are created in the UI and automatically stored within the system's SQLite database. The database is auto-created the first time the application starts up. Connection details will remain stored there and can be updated or deleted in the UI automatically in the "Manage Connections" section.


### Dependencies
All library dependencies are included within requirements.txt. Simply run "pip install -r requirements.txt" in your virtual environment to build the dependencies.


### UI
- The UI is designed using Flowbite
- The editor built-in is built on top of Ace editor
- Customizable themes have been included to modify the look/feel of the editor as desired



![sql_seer_preview](https://github.com/user-attachments/assets/efb6eb39-5867-4d7f-a197-d18a62252d11)
![sql_seer_preview_manage_connections](https://github.com/user-attachments/assets/63631c23-4317-48d1-83f9-dc05152775de)
![sql_seer_preview_create_connection_details](https://github.com/user-attachments/assets/7f1556d3-4dfb-4e56-b1cd-b1f5ed6f5e35)





In accordance wih their attribution requirements, the favicon was designed using resources from Flaticon.com
 
