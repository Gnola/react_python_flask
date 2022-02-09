## Set Up Flask

In **root directory**

```bash
mkdir flask-server
cd flask-server
touch server.py
```

## Set Up React

In **root directory**

```bash
npx create-react-app client
```

### Install Dependencies/Packages

In **/flask-server directory**

```bash
python3 -m venv venv # Creates virtual environment
source venv/bin/activate # Runs virtual environment
pip3 install Flask # Install Flask
pip3 install flask-cors # Might need
```

### Edit Files

#### `server.py`

```python
from flask import Flask
from flask_cors import CORS # Might need

app = Flask(__name__)
CORS(app) # Might need

@app.route("/members")
def members():
    return {"members": ["Member 1, Member 2, Member 3"]}

if __name__ == "__main__":
    app.run(debug=True)
```

#### `package.json`

```json
"proxy": "http://localhost/5000"
/* Removed because it wasnt working correctly */
```

---

### Run Locally

| Location      | Command              | Runs         | URL                             | Access |
| :------------ | :------------------- | :----------- | :------------------------------ | ------ |
| /flask-server |  `python3 server.py` | **Server**   | *http://localhost/5000/members* | Data   |
| /client       |  `npm start`         | **Frontend** | *http://localhost/3000*         | Site   |
