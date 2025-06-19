from flask import Flask
from ..agents.model_governor import ModelGovernor

def create_app(config):
    governor = ModelGovernor(config)
    return governor.app

def run_api_server(config, host='0.0.0.0', port=5000):
    app = create_app(config)
    app.run(host=host, port=port)