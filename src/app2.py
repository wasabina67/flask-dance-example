import os

from dotenv import load_dotenv
from flask import Flask, redirect, url_for
from flask_dance import OAuth2ConsumerBlueprint, oauth_authorized

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
gh_blueprint = OAuth2ConsumerBlueprint()
app.register_blueprint(gh_blueprint, url_prefix="/login")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, ssl_context="adhoc", debug=True)
