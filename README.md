## Flask MongoDB CRUD APP

## Project Setup

1. Create main (`flaskCRUD`) project folder

2. create virtual environment inside of it(IF NEEDED)

# Create virtual environment if needed
No virtual environment has been used in this project

```bash
#Linux and Mac
python -m venv venv

#windows users
python -m venv c:\path\to\myenv
```

3. Activate the virtual environment

```bash
# Linux and Mac
source venv/bin/activate

#Windows users
\venv\Scripts\activate.bat
```

4. Install all project dependencies

```bash
pip install requirements.txt

5. Setup the mongoDB cluster
```
## Project Structure

```
project_root_dir
│
|
|
|__ application
|    |__ __init__.py
|    |__ routes.py
|    
|    
|    
|
|
|
|__ DockerFile
|__ docker-compose.yml
|
|__ README.md
|
|
|__ run.py
```

# Tutorial Phases

1. Simple Hello world app and setup docker
2. Setup database connection [Sign Up For mongoDB cloud](https://account.mongodb.com/account/login)
3. Setup __init__.py file (project configurattions)
4. Create insert
5. Create retrieve
6. Implemet delete
7. Implement update functionality
8. Setup .gitignore file


## ScreenShots

# GET/users
![image](https://github.com/krish6388/flaskCRUDApp/assets/85309615/3e333655-0493-431d-b42e-648719b09d77)

# GET/users/id
![image](https://github.com/krish6388/flaskCRUDApp/assets/85309615/e063eac6-7c5e-46db-a6ec-6ee1ef6f3355)

# POST/users
![image](https://github.com/krish6388/flaskCRUDApp/assets/85309615/1453695a-ca12-40ea-8e54-250a7ede35e2)

# PUT/users/id
![image](https://github.com/krish6388/flaskCRUDApp/assets/85309615/5fff5b8b-bbca-4a5e-88a3-1e8c387a01c5)

# DELETE/users/id
![image](https://github.com/krish6388/flaskCRUDApp/assets/85309615/6601f74b-d48a-453f-8f7d-c69b173022cc)
