import os

from dotenv import load_dotenv
from flask import Flask, redirect, url_for
from flask_dance.consumer import OAuth2ConsumerBlueprint, oauth_authorized

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
gh_blueprint = OAuth2ConsumerBlueprint(
    "github",
    __name__,
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    scope=None,
    base_url="https://api.github.com/",
    authorization_url="https://github.com/login/oauth/authorize",
    token_url="https://github.com/login/oauth/access_token",
    redirect_url="/github_authorized",
    redirect_to=None,
    login_url=None,
    authorized_url=None,
    session_class=None,
    storage=None,
    rule_kwargs=None,
)
app.register_blueprint(gh_blueprint, url_prefix="/login")


@app.route("/")
def index():
    resp = gh_blueprint.session.get("/user")
    if not resp.ok:
        return redirect(url_for("github.login"))
    return "You are @{login} on GitHub".format(login=resp.json()["login"])


@app.route("/github_authorized")
def github_authorized():
    resp = gh_blueprint.session.get("/user")
    assert resp.ok
    return "You are @{login} on GitHub".format(login=resp.json()["login"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, ssl_context="adhoc", debug=True)
