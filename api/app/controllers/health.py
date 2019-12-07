# Controller for HealthCheck endpoint

from app import registry
from ..schemas import HealthSchema

@registry.handles(rule="/health", method="GET", response_body_schema=HealthSchema())
def get_health():
    return {"status": "OK"}
