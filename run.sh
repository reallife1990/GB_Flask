#!/usr/bin/env bash
# exit on error

set -o errexit

pip install -r requirements.txt

flask db upgrade
flask create-admin
flask create-tags