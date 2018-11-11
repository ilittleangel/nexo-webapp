# Nexo Web Application

Flask application for Nexo Ecosystem


## How to start

Export the environment variables
```bash
export FLASK_APP=nexo-webapp
export FLASK_ENV=development
```

Activate virtual enviroment
```bash
source ~/myenv/bin/activate 
```

Initialize the database if it is the first time
```bash
flask init-db
```

Run the Flask application
```bash
flask run
```

And open http://127.0.0.1:5000 in a browser.
