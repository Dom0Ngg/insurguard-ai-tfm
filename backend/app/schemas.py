from pydantic import BaseModel
from typing import Dict, Any, List, Optional


class ClaimInput(BaseModel):
    claim_id: str
    customer_id: str
    claim_type: str
    description: str
    claimed_amount: float


class ExtractedDocumentData(BaseModel):
    claim_id: str
    extracted_fields: Dict[str, Any]
    raw_text: Optional[str] = None


class AgentResult(BaseModel):
    agent_name: str
    status: str
    output: Dict[str, Any]


class ClaimAnalysisResponse(BaseModel):
    claim_id: str
    global_risk_level: str
    fraud_score: float
    coverage_result: str
    explanation: str
    agents_trace: List[AgentResult]