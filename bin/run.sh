#!/usr/bin/env bash

activate_venv() {
    source ~/software/venvs/monitor/bin/activate
}

export_env() {
    export FLASK_APP=nexo-webapp
    export FLASK_ENV=development
}

activate_venv
export_env
flask init-db
flask run
