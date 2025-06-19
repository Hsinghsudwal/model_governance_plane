import argparse
import yaml
from src.api.server import run_api_server
from src.agents.model_governor import ModelGovernor
from src.core.mcp.context_protocol import MCPContext
from src.monitoring.drift_detector import DriftDetector
from src.monitoring.metrics_collector import MetricsCollector

def load_config(config_path: str) -> dict:
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def main():
    parser = argparse.ArgumentParser(description='MCP Agent System')
    parser.add_argument('--config', type=str, default='config/config.yaml',
                      help='Path to configuration file')
    parser.add_argument('--api', action='store_true',
                      help='Run as API server')
    parser.add_argument('--port', type=int, default=5000,
                      help='API server port')
    args = parser.parse_args()
    
    # Load configuration
    with open(args.config, 'r') as f:
        config = yaml.safe_load(f)
    
    if args.api:
        run_api_server(config, port=args.port)
    else:
        # Original monitoring loop code
        model_governor = ModelGovernor(config)
        try:
            while True:
                model_governor.monitor_and_act()
        except KeyboardInterrupt:
            print("Shutting down MCP Agent System...")

if __name__ == "__main__":
    main()