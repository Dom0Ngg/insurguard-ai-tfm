from typing import Dict, Any
from backend.agents.base_agent import BaseAgent


class FraudDetectionAgent(BaseAgent):
    def __init__(self):
        super().__init__("Agente de detección de fraude")

    def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        claimed_amount = input_data.get("claimed_amount", 0)
        fraud_score = 0.15

        if claimed_amount > 3000:
            fraud_score += 0.35

        if claimed_amount > 10000:
            fraud_score += 0.30

        fraud_score = min(fraud_score, 1.0)

        if fraud_score < 0.3:
            risk_level = "Bajo"
        elif fraud_score < 0.7:
            risk_level = "Medio"
        else:
            risk_level = "Alto"

        return {
            "status": "success",
            "output": {
                "fraud_score": fraud_score,
                "risk_level": risk_level,
                "model_used": "Reglas iniciales simuladas",
                "risk_factors": [
                    "Importe reclamado elevado" if claimed_amount > 3000 else "Importe dentro de rango normal"
                ]
            }
        }
