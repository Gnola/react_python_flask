from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Members API Route
@app.route("/members")
def members():
    return {"members": ["Member 1, Member 2, Member 3"]}

if __name__ == "__main__":
    app.run(debug=True) # for dev mode
