from flask import Flask
from flask.logging import create_logger
from flask import json
import logging

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

@app.route('/status')
def healthcheck():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )

    LOG.info(f"Status request successfull")
    return response

@app.route("/")
def hello():
    LOG.info(f"App running")

    return "Hello World, my name is Nguyen Duc Tri!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True) # specify port=80
