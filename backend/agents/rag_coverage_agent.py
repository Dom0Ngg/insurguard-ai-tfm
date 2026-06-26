from typing import Dict, Any
from backend.agents.base_agent import BaseAgent


class RAGCoverageAgent(BaseAgent):
    def __init__(self):
        super().__init__("Agente RAG de coberturas")

    def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        claim_type = input_data.get("claim_type", "").lower()

        if "coche" in claim_type or "auto" in claim_type or "vehiculo" in claim_type:
            coverage_result = "Posiblemente cubierto"
            sources = ["Condiciones generales - Seguro Auto", "Cláusula 4.2 Coberturas básicas"]
        else:
            coverage_result = "Revisión manual requerida"
            sources = ["No se ha encontrado una cobertura específica en la base documental simulada"]

        return {
            "status": "success",
            "output": {
                "coverage_result": coverage_result,
                "sources": sources,
                "rag_answer": "Según la documentación consultada, el siniestro podría estar cubierto, aunque requiere validación final por un analista."
            }
        }
