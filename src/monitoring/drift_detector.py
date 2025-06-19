import numpy as np
from typing import Dict, Any
from evidently.model_profile import Profile
from evidently.model_profile.sections import DataDriftProfileSection

class DriftDetector:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.threshold = config['monitoring']['drift_detection']['threshold']
        
    def detect_drift(self, reference_data: np.ndarray, current_data: np.ndarray) -> Dict[str, Any]:
        data_drift_profile = Profile(sections=[DataDriftProfileSection()])
        data_drift_profile.calculate(reference_data, current_data)
        
        drift_report = {
            'has_drift': False,
            'metrics': {},
            'timestamp': None
        }
        
        # Extract drift metrics from Evidently report
        drift_metrics = data_drift_profile.json()
        if drift_metrics['data_drift']['data_drift_detected']:
            drift_report['has_drift'] = True
            drift_report['metrics'] = drift_metrics['data_drift']
            
        return drift_report