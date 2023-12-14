# YiFlaskSimpleAuth
A product of the learning process with Flask, this project is a simple account login, registration and management system that implements CRUD operations using SQLAlchemy.

[简体中文](./README_zh-CN.md)

# Warning! This is a product of the learning process and is not perfect.

## Learning Notes
For detailed learning notes, visit [Youdao](https://note.youdao.com/s/UbftD0FH) (In Chinese).

If anyone have suggestions, feel free to submit an issue.

## Features

- **Flask and MySQL**: This project uses Flask for the backend and a MySQL database, with SQLAlchemy for database operations.
- **Login and Registration**: Basic login and registration functionalities are implemented.
  - *Login*: Validates if the entered password is correct and if the username exists.
  - *Registration*: Checks for pre-existing usernames and verifies if the entered passwords match. ~~It also features a captcha verification, which is currently just a checkbox with no actual functionality.~~
- **Admin Capabilities**: An administrator account 'admin' is available to delete user accounts and modify user passwords.

## How To Setup

### 0. Install Python
Download and install Python [here](https://www.python.org/downloads/).

### 1. Deploy the project
Clone the repository using git:
```git
git clone https://github.com/ImYiFeng/YiFlaskSimpleAuth.git
```

### 2. Install dependencies
Install required packages using pip:
```python
pip install -r requirements.txt
```

### 3. Install MySQL
Download and install MySQL [here](https://dev.mysql.com/downloads/mysql/).

### 4. Create a MySQL database
You can use Navicat or MySQL command line for database creation.

- **Navicat** (recommended): [Navicat Download](https://www.navicat.com/)
- **MySQL Command Line**:
  - Connect to database:
    ```
    mysql -u username -p
    ```
  - Create database:
    ```
    CREATE DATABASE DATABASE_NAME;
    ```

### 5. Modify the config.json
Update `config.json` with your database configurations:
```json
{
    "HOSTNAME": "",
    "PORT": "",
    "USERNAME": "",
    "PASSWORD": "",
    "DATABASE": ""
}
```

### 6. Run the project
Start the application:
```python
python app.py
```
