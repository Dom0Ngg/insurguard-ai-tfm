from fastapi import FastAPI
from backend.app.schemas import ClaimInput, ClaimAnalysisResponse
from backend.agents.orchestrator_agent import OrchestratorAgent

app = FastAPI(
    title="InsurGuard AI",
    description="Plataforma multiagente para análisis inteligente de siniestros y detección de fraude",
    version="0.1.0"
)

orchestrator = OrchestratorAgent()


@app.get("/")
def root():
    return {
        "project": "InsurGuard AI",
        "status": "running",
        "description": "API base para arquitectura multiagente del TFM"
    }


@app.post("/claim-analysis", response_model=ClaimAnalysisResponse)
def analyze_claim(claim: ClaimInput):
    result = orchestrator.analyze_claim(claim.model_dump())
    return result