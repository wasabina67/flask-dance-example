# flask-dance-example
Flask dance example

## Setup

[GitHub Quickstart](https://flask-dance.readthedocs.io/en/v1.3.0/quickstarts/github.html)

### Authorization callback URL

```
https://localhost:3000/login/github/authorized
```

### Create .env

```bash
cp -p .env.example .env
```

- SECRET_KEY
  - Flask secret key
- CLIENT_ID
  - The client ID for your application on GitHub
- CLIENT_SECRET
  - The client secret for your application on GitHub

## Run

```bash
python src/app.py
```

Open https://localhost:3000/
