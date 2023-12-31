# Introduction
  This is the repository to demostrate my professional portfolio website which uses **Flask** and **Gunicorn** to deploy it to **Render**. 
## Getting Started
- **Fork the repository:** You should **fork the repository** and then **clone it** so you can manage your own repo and use this only as a template.
  ```
  $ git clone https://github.com/your_username/your-flask-project.git
  ```
  
  **WARNING:** If you change the file name (`main.py`) and the Flask **app** (`app = Flask(__name__)`) then remember to change Procfile:
  ```
  web: gunicorn <filename>:<app_name>
  ```

- **Install dependencies:**

  ```
  pip install -r requirements.txt
  ```

- **Set Environment Variables:** Ensure you have the required environment variables set, such as 'FLASK_KEY', 'OWN_EMAIL', 'OWN_PASSWORD' with your **own**.

- **Create** an account on render.com simply by signing up [via Github.](https://dashboard.render.com/login)

- **Deploy Your Project:**
    Create a web service and change the start command:
   <div align="center"><img src="example-render.gif" alt="GIF showing web service creation on render." /></div>

## Endpoints
|Route |Usage |
| :-:  | :-: |
|`/ `  | For Home page|
|`/about`  | For General Information About My Professional Life|
|`/articles`  | For Information About My Publication|
|`/contact`  | For Getting Touch with POST request via SMTPlib|
