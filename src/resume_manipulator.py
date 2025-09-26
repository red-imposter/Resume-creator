import requests
from src import Work_with_API
from datetime import datetime
from jinja2 import Template

Template_file_name = "./templates/index.html"
Index_file_name = "./public/index.html"

def generate_resume():
    user_info = Work_with_API.get_main_info()
    id = user_info.get("id")
    user_achievements = Work_with_API.get_achievements(id)
    with open(Template_file_name, 'r', encoding = 'utf-8') as f:
        text = f.read()
        jinja_template = Template(text)
        rendered_resume = jinja_template.render(
            name= user_info.get("name"),
            username=user_info.get("username"),
            email= user_info.get("public_email","Нет данных"),
            id = user_info.get("id"),
            achievements = user_achievements,
            date = datetime.now()
            )
        with open(Index_file_name, "w", encoding="utf-8") as f:
            f.write(rendered_resume)

def get_resume():
    with open(Index_file_name, 'r', encoding = 'utf-8') as f:
        return f.read()
