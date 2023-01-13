"""
    This is the main entrypoint and where the AuthServer is instantiated.
    The blueprints to all the routes are registered here.
"""
import argparse
from flask import Flask
from os import environ

from jade_front.common.config import Config
from jade_front.common.keyring import Keyring
from jade_front.services.jobs_blueprint import jobs_blueprint
from jade_front.services.results_blueprint import results_blueprint
from jade_front.services.requests_blueprint import requests_blueprint
from jade_front.services.code_blueprint import code_blueprint
from jade_front.services.projects_blueprint import projects_blueprint

from jade_front.server.server import Server


if __name__ == '__main__':
    jade_front_app = Flask(__name__)
    parser = argparse.ArgumentParser()

    parser.add_argument("-t", "--Tier", help="The set of configs to use.")
    args = parser.parse_args()

    Config.instantiate(args.Tier)
    Keyring.instantiate(args.Tier)
    Server.instantiate(jade_front_app)

    # registering the blueprints
    jade_front_app.register_blueprint(jobs_blueprint, url_prefix='/v1')
    jade_front_app.register_blueprint(results_blueprint, url_prefix='/v1')
    jade_front_app.register_blueprint(requests_blueprint, url_prefix='/v1')
    jade_front_app.register_blueprint(code_blueprint, url_prefix='/v1')
    jade_front_app.register_blueprint(projects_blueprint, url_prefix='/v1')


    jade_front_app.run(debug=True)
