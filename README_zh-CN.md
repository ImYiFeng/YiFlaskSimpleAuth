# YiFlaskSimpleAuth
这是一个 Flask 学习过程中的产物，本项目实现了简单的账户登录、注册和管理，使用 SQLAlchemy 实现了增删改查操作。

[English](./README.md)

# 警告！这是学习过程中的产物，并不完善。

## 学习笔记
想要查看学习笔记，请访问[有道云笔记](https://note.youdao.com/s/UbftD0FH)。

如果有任何建议，欢迎提交issue。

## 特色

- **Flask 和 MySQL**：该项目使用 Flask 作为后端，MySQL 数据库，通过 SQLAlchemy 进行数据库操作。
- **登录和注册**：实现了基础的登录和注册功能。
  - *登录*：验证输入的密码是否正确以及用户名是否存在。
  - *注册*：检查用户名是否已存在，验证输入的密码是否匹配。~~还有人机验证功能，虽然只是个 checkbox 没有任何作用。（我是不是人类用得着你管）~~
- **管理员功能**：提供了一个管理员账户 'admin'，用于删除用户账户和修改用户密码。

## 如何设置

### 0. 安装 Python
[在这里](https://www.python.org/downloads/)下载并安装 Python。

### 1. 部署项目
使用 git 克隆仓库：
```git
git clone https://github.com/ImYiFeng/YiFlaskSimpleAuth.git
```

### 2. 安装依赖
使用 pip 安装所需的包：
```python
pip install -r requirements.txt
```

### 3. 安装 MySQL
[在这里](https://dev.mysql.com/downloads/mysql/)下载并安装 MySQL。

### 4. 创建 MySQL 数据库
你可以使用 Navicat 或 MySQL 命令行来创建数据库。

- **Navicat**（推荐）：[下载 Navicat](https://www.navicat.com/)
- **MySQL 命令行**：
  - 连接到数据库：
    ```
    mysql -u username -p
    ```
  - 创建数据库：
    ```
    CREATE DATABASE DATABASE_NAME;
    ```

### 5. 修改 config.json
使用你的数据库配置修改 `config.json`：
```json
{
    "HOSTNAME": "",
    "PORT": "",
    "USERNAME": "",
    "PASSWORD": "",
    "DATABASE": ""
}
```

### 6. 运行项目
启动应用程序：
```python
python app.py
```