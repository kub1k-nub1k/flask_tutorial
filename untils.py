from faker import Faker
import requests


def read_requirements_file():
    with open('requirements.txt', 'r') as file:
        requirements = file.readlines()
        return requirements


def generate_user_data(num_users):
    fake = Faker()
    user_data = []

    for _ in range(num_users):
        name = fake.name()
        email = fake.email()
        user_data.append(f"{name} - {email}")

    return user_data


def get_astronaut_info():
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        astronauts = data.get("people", [])
        astronaut_names = [astronaut["name"] for astronaut in astronauts]
        total_astronauts = data.get("number", 0)
        return astronaut_names, total_astronauts
    else:
        return None, None
