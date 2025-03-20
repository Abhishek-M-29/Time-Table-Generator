# Time-Table-Generator

The repository of codes for a Time Table Generator project.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Abhishek-M-29/Time-Table-Generator.git
    cd Time-Table-Generator
    ```

2. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

3. Install the required dependencies:
    ```sh
    pip install mysql-connector-python
    ```

## Usage

1. Navigate to the project directory:
    ```sh
    cd Time-Table-Generator
    ```

2. Run the main script:
    ```sh
    python interface.py
    ```

3. The GUI will open. You can interact with the menu to generate and manage timetables.

## Code Structure

- **README.md**: This file.
- **Timetable.py**: Contains initial setup for the timetable generator.
    ```python
    # Creating a Timetable generator
    ```
- **interface.py**: Connects to a MySQL database and checks if the connection is successful.
    ```python
    import mysql.connector as sql

    con = sql.connect(host='localhost', user='root', passwd='admin', database='nothing')

    if con.is_connected():
        print('Done')
    ```
- **time_table.py**: Contains functions to generate and display timetables using Tkinter.
    ```python
    import random
    from tkinter import *

    # ... (functions for generating and displaying timetables)
    ```
- **tt_be.py**: Backend logic for generating timetables and interacting with the MySQL database.
    ```python
    import random
    import mysql.connector as sq

    # ... (functions for generating timetables and database interactions)
    ```
- **tt_fe.py**: Frontend logic to display the generated timetables using Tkinter.
    ```python
    import tkinter as tk
    import mysql.connector as sq
    import tt_be as be

    # ... (functions for displaying timetables)
    ```
- **ujnbhg.py**: Example of a Tkinter GUI with a menu bar.
    ```python
    from tkinter import *
    from tkinter import messagebox

    # ... (Tkinter GUI setup)
    ```

## Contributing

We welcome contributions! Here are some ways you can contribute:

- Report bugs or suggest features by opening an issue.
- Fork the repository, make changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
