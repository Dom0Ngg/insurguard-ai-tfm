from typing import Dict, Any
from backend.agents.base_agent import BaseAgent


class ValidationAgent(BaseAgent):
    def __init__(self):
        super().__init__("Agente de validación")

    def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        issues = []

        if not input_data.get("claim_id"):
            issues.append("No se ha informado el identificador del siniestro.")

        if not input_data.get("customer_id"):
            issues.append("No se ha informado el identificador del cliente.")

        if input_data.get("claimed_amount", 0) <= 0:
            issues.append("El importe reclamado no es válido.")

        # La descripción original ahora viene como raw_text tras el agente de extracción
        raw_text = input_data.get("raw_text", "")

        if not raw_text or raw_text.strip() == "":
            issues.append("No existe descripción del siniestro.")

        validation_status = "valid" if not issues else "warning"

        return {
            "status": "success",
            "output": {
                "validation_status": validation_status,
                "issues": issues
            }
        }
    