from typing import Dict, Any
from backend.agents.base_agent import BaseAgent


class DocumentExtractionAgent(BaseAgent):
    def __init__(self):
        super().__init__("Agente de extracción documental")

    def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        description = input_data.get("description", "")

        extracted_data = {
            "claim_id": input_data.get("claim_id"),
            "customer_id": input_data.get("customer_id"),
            "claim_type": input_data.get("claim_type"),
            "claimed_amount": input_data.get("claimed_amount"),
            "detected_entities": {
                "dates": [],
                "amounts": [input_data.get("claimed_amount")],
                "documents": ["parte de siniestro simulado"]
            },
            "raw_text": description
        }

        return {
            "status": "success",
            "output": extracted_data
        }
