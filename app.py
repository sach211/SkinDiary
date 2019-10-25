from flask import Flask

app = Flask(__name__)       # create an app instance

           # at end point /
@post('/logUser')
def logUser():
    userId = request.forms.get('userId')
    timeStamp = request.forms.get('timeStamp')
    create_user(db, userId, timeStamp)
	return "User logged in!"

if __name__ == "__main__":  # on running python app.py
	app.run()
