# MCP Agent System

A full-stack ML Agent System that provides autonomous model governance, drift detection, and automated model lifecycle management.

## Features

- 🤖 Autonomous AI Agent for model governance
- 🔄 Automated drift detection and handling
- 📊 Model performance monitoring
- 🚀 Multiple deployment strategies (Direct, Canary, Blue-Green)
- 📈 MLflow integration for metrics tracking
- 🔍 Evidently integration for drift detection
- 🌐 REST API interface

## Project Structure


## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd model_governance_plane

```

## install dependencies:
pip install -r requirements.txt

## Monitoring
python main.py --config config/config.yaml

## API
python main.py --config config/config.yaml --api --port 5000
