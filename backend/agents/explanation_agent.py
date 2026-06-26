from typing import Dict, Any
from backend.agents.base_agent import BaseAgent


class ExplanationAgent(BaseAgent):
    def __init__(self):
        super().__init__("Agente explicador")

    def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        fraud_score = input_data.get("fraud_score", 0)
        risk_level = input_data.get("risk_level", "No calculado")
        coverage_result = input_data.get("coverage_result", "No evaluado")
        validation_issues = input_data.get("validation_issues", [])

        explanation = (
            f"El siniestro presenta un nivel de riesgo {risk_level}, "
            f"con un score de fraude de {fraud_score:.2f}. "
            f"El análisis de cobertura indica: {coverage_result}. "
        )

        if validation_issues:
            explanation += (
                "Además, se han detectado incidencias documentales que requieren revisión: "
                + "; ".join(validation_issues)
            )
        else:
            explanation += "No se han detectado incidencias documentales relevantes en esta primera validación."

        return {
            "status": "success",
            "output": {
                "explanation": explanation
            }
        }
