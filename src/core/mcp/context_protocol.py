from typing import Dict, Any, Optional
from pydantic import BaseModel, Field
from datetime import datetime

class DatasetMetadata(BaseModel):
    name: str
    version: str
    hash: str
    created_at: datetime = Field(default_factory=datetime.now)
    features: Dict[str, str]
    rows: int
    columns: int

class ModelMetadata(BaseModel):
    name: str
    version: str
    algorithm: str
    parameters: Dict[str, Any]
    accuracy: float
    created_at: datetime = Field(default_factory=datetime.now)
    training_dataset: str
    training_duration: float
    
class RunMetadata(BaseModel):
    run_id: str
    model_version: str
    start_time: datetime
    end_time: Optional[datetime]
    status: str
    metrics: Dict[str, float]
    artifacts: Dict[str, str]

class MCPContext:
    def __init__(self):
        self.dataset_metadata = {}
        self.model_metadata = {}
        self.run_metadata = {}
    
    def register_dataset(self, metadata: DatasetMetadata):
        self.dataset_metadata[f"{metadata.name}:{metadata.version}"] = metadata
        
    def register_model(self, metadata: ModelMetadata):
        self.model_metadata[f"{metadata.name}:{metadata.version}"] = metadata
        
    def register_run(self, metadata: RunMetadata):
        self.run_metadata[metadata.run_id] = metadata