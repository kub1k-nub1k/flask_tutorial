from flask import Flask, request

from untils import read_requirements_file
from untils import generate_user_data
from untils import get_astronaut_info

app = Flask(__name__)


@app.route("/requirements/")
def requirements_file():
    requirements = read_requirements_file()
    return "<br>".join(requirements)


@app.route("/generate-users/")
def users_generate():
    num_users = request.args.get('num_users', '100')

    error_mess = '<span style="color: red;">ERROR:</span>'

    if not num_users.isdigit():
        return f'{error_mess} num_users parameter must be a number'

    num_users = int(num_users)

    if num_users < 100:
        return f'{error_mess} The value of num_users must be at least 100.'
    elif num_users > 1000:
        return f'{error_mess} The value of num_users must not exceed 1000.'

    users = generate_user_data(num_users)
    return "<br>".join(users)


@app.route("/space/")
def space_info():
    name, quantity = get_astronaut_info()
    if name is not None and quantity is not None:
        return f"Number of astronauts: {quantity}<br>List of astronaut names:<br>{'<br>'.join(name)}"
    else:
        return "Unable to obtain information about the astronauts."


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
