import os

from dotenv import load_dotenv
from flask import Flask, redirect, url_for
from flask_dance.contrib.github import github, make_github_blueprint

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
gh_blueprint = make_github_blueprint(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
)
app.register_blueprint(gh_blueprint, url_prefix="/login")


@app.route("/")
def index():
    if not github.authorized:
        return redirect(url_for("github.login"))
    resp = github.get("/user")
    assert resp.ok
    return "You are @{login} on GitHub".format(login=resp.json()["login"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, ssl_context="adhoc", debug=True)
