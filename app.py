import flask
from flask_cors import CORS
from request_service import solve_error_prompts

app = flask.Flask(__name__)
CORS(app)

@app.route("/")
def index():
    with open("index.html", "r") as f:
        return f.read()

# Route for getting a list of error prompts to be solved for debugging
@app.route("/error_prompts", methods=["POST"])
def error_prompts():
    error_prompts = flask.request.json.get("error_prompts", [])
    responses = solve_error_prompts(error_prompts)
    return flask.jsonify({"responses": responses})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5501)
