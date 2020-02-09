from flask import Flask
from flask import request
import os 

app = Flask(__name__)
prefix = os.environ.get('JUPYTERHUB_SERVICE_PREFIX', '/')
print(prefix)

@app.route("/services/gofer_nb")
def test():
    print("I GOT HERE")
    return "Hello world!"

@app.route("/services/gofer_nb/", methods=['POST'])
def post():
    print("I received a request")
    print(request.form)

if __name__ == "__main__":
	app.run(port=10101, threaded = True)
