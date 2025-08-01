# University Record Management System

This project is a comprehensive, graphical user interface (GUI) application for managing and querying a university database. Built with Python and `tkinter`, it provides full CRUD (Create, Read, Update, Delete) capabilities for all major entities and a suite of advanced, user-friendly reports.

---

## Features

-   **Graphical User Interface**: A modern, tabbed interface for easy navigation and management.
-   **Full CRUD Operations**: Manage records for Students, Lecturers, Courses, Non-Academic Staff, Research Projects, Publications, and Student Organizations.
-   **User-Friendly Forms**: Uses dropdown menus for selecting related data (like programs or departments), so you never need to know the underlying database IDs.
-   **Relationship Management**: Easily manage memberships for entities like Research Projects and Student Organizations.
-   **Advanced Reporting**: A dedicated tab for running complex, pre-defined queries with clear input fields and results tables.

---

## 1. Prerequisites

Before you begin, ensure you have the following installed on your system:

-   **MySQL Server**: The database for this project.
-   **Python 3.12.x**: This project requires Python version 3.12.
-   **tkinter**: The GUI toolkit for Python. This often needs to be installed separately.
-   **pip**: Python's package installer (usually comes with Python).
-   **Git**: For cloning the repository.
-   **Visual Studio Code (VS Code)**: Recommended editor for this project, with the Python extension installed.

### Installing Python 3.12.x

If you don't have Python 3.12 installed, follow these instructions for your operating system:

#### Windows:

1.  Go to the official Python website: [python.org/downloads/windows/](https://python.org/downloads/windows/)
2.  Download the latest Python 3.12.x installer (e.g., "Windows installer (64-bit)").
3.  Run the installer.
4.  **Important**: On the first page of the installer, make sure to check the box that says "Add Python 3.12 to PATH" or "Add python.exe to PATH".
5.  Click "Install Now".
6.  After installation, open Command Prompt or PowerShell and type `python --version` or `py --version` to verify it's 3.12.x.

#### macOS:

-   **Using Homebrew (Recommended)**:
    1.  If you don't have Homebrew, install it from [brew.sh](https://brew.sh).
    2.  Open Terminal and run:
        ```bash
        brew install python@3.12
        ```
    3.  Verify by opening a new terminal window and typing: `python3.12 --version`.

-   **Using the official installer**:
    1.  Go to [python.org/downloads/macos/](https://www.python.org/downloads/macos/)
    2.  Download the macOS 64-bit universal2 installer for Python 3.12.x.
    3.  Run the installer package.
    4.  Verify by opening Terminal and typing `python3 --version`.

#### Linux:

The method varies by distribution.

-   **Debian/Ubuntu**:
    ```bash
    sudo apt update
    sudo apt install python3.12 python3.12-venv python3-pip
    ```
    (You might need to add a PPA like `deadsnakes` if 3.12 isn't in the default repositories: `sudo add-apt-repository ppa:deadsnakes/ppa`)

-   **Fedora**:
    ```bash
    sudo dnf install python3.12
    ```
-   Verify by opening a terminal and typing `python3.12 --version` or `python3 --version`.

### Installing tkinter

`tkinter` is required for the application's GUI. The installation method depends on your OS and how you installed Python.

#### Windows:

`tkinter` is included by default with the official Python installer from python.org. When installing, ensure the "tcl/tk and IDLE" option is checked. If you installed Python without it, re-run the installer, choose "Modify," and select the option to add it.

#### macOS:

-   **Using Homebrew (Recommended)**: If you installed Python via Homebrew, you must install `tkinter` separately. Run the following command:
    ```bash
    brew install python-tk@3.12
    ```
-   **Using the official installer**: The installer from python.org for macOS already includes `tkinter`. No extra steps are needed.

#### Linux:

You must install `tkinter` using your distribution's package manager.

-   **Debian/Ubuntu**:
    ```bash
    sudo apt install python3.12-tk
    ```
-   **Fedora**:
    ```bash
    sudo dnf install python3-tkinter
    ```

---

## 2. Database Setup

The database is the foundation of this project. You must import the provided database export in the repo before running the application. The `university_db_export.sql` file is a self-contained export that includes the database schema (all tables and relationships) and all the populated data.

### Importing the Database

You can import the database using a GUI tool like MySQL Workbench or via the command line.

#### Option A: Using the Command Line (Recommended)

1.  Open your terminal or command prompt.
2.  Navigate to the directory where you have saved the `university_db_export.sql` file.
3.  Run the following command, replacing `your_mysql_user` with your MySQL username. You will be prompted for your password.
    ```bash
    mysql -u your_mysql_user -p < university_db_export.sql
    ```
    This command will create the `university_db` database and import all the tables and data automatically.

#### Option B: Using MySQL Workbench

1.  Open MySQL Workbench and connect to your local MySQL server instance.
2.  From the top menu bar, click on **Server**, then select **Data Import**.
3.  In the Data Import screen, select the option **Import from Self-Contained File**.
4.  Click the "..." button and navigate to your `university_db_export.sql` file.
5.  The "Default Target Schema" can be left blank, as the script will create the database.
6.  Click the **Start Import** button at the bottom right.

---

## 3. Application Setup

Follow these steps to set up the Python application on your local machine.

### 1. Clone the Repository

```bash
git clone [https://github.com/Bondok-devo/CSCK542-Databases-and-Information-Systems.git](https://github.com/Bondok-devo/CSCK542-Databases-and-Information-Systems.git)
cd CSCK542-Databases-and-Information-Systems
```

### 2. Create and Activate a Virtual Environment

Using a virtual environment is crucial. We'll name it `.venv`.

1.  Navigate to the project root directory.
2.  Create the virtual environment:
    (Note: Replace `python3.12` with the command that runs your Python 3.12 installation. On Windows, it might be `py -3.12` or just `python`)
    ```bash
    python3.12 -m venv .venv
    ```
3.  Activate the virtual environment:
    -   **macOS/Linux**:
        ```bash
        source .venv/bin/activate
        ```
    -   **Windows (Command Prompt)**:
        ```bash
        .\.venv\Scripts\activate
        ```
    -   **Windows (PowerShell)**:
        ```powershell
        .\.venv\Scripts\Activate.ps1
        ```
    Your terminal prompt should now start with `(.venv)`.

### 3. Install Dependencies

With the virtual environment activated, install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Configure VS Code Python Interpreter

To ensure VS Code uses the correct interpreter from your virtual environment:

1.  Open your project folder in VS Code.
2.  Open the Command Palette (`⇧⌘P` on macOS, `Ctrl+Shift+P` on Windows/Linux).
3.  Type `Python: Select Interpreter` and select it.
4.  Choose the interpreter that includes `.venv` in its path (e.g., `Python 3.12.x ('.venv')`).
5.  If it's not listed, choose "Enter interpreter path..." and manually find it at `.venv/bin/python` (or `.\.venv\Scripts\python.exe` on Windows).
6.  Check the bottom-left corner of the VS Code status bar; it should now show `('.venv')`.

### 5. Environment Configuration (.env file)

This application uses an `.env` file to store database credentials securely. The `.env` file is already included in the repo for ease of use.

1.  Create a file named `.env` in the root of your project directory.
2.  Add the following content, replacing the placeholder values with your own MySQL credentials.
    ```env
    DB_HOST=localhost
    DB_USER=root
    DB_PASSWORD=your_mysql_password
    DB_NAME=university_db
    ```

---

## 4. Running the Application

Once the database and application setup are complete, run the main GUI program from your activated virtual environment:

```bash
python gui_app.py
```

This will launch the "University Record Management System" application in its own graphical window.

## 5. Running the Tests

1. Run the Integration Test from your activated virtual environment:

```bash
python Intergration_Testing_advanced_queries.py
```

This will launch the Integration Test of the application.

2. Run the Unit Test from your activated virtual environment:

```bash
python test_app_logic.py
```

This will launch the Unit Test of the application.