from typing import Dict, Any, List

from backend.agents.document_extraction_agent import DocumentExtractionAgent
from backend.agents.validation_agent import ValidationAgent
from backend.agents.rag_coverage_agent import RAGCoverageAgent
from backend.agents.fraud_detection_agent import FraudDetectionAgent
from backend.agents.explanation_agent import ExplanationAgent

class OrchestratorAgent:
    def __init__(self):
        self.document_agent = DocumentExtractionAgent()
        self.validation_agent = ValidationAgent()
        self.rag_agent = RAGCoverageAgent()
        self.fraud_agent = FraudDetectionAgent()
        self.explanation_agent = ExplanationAgent()

    def analyze_claim(self, claim_data: Dict[str, Any]) -> Dict[str, Any]:
        agents_trace: List[Dict[str, Any]] = []

        document_result = self.document_agent.run(claim_data)
        agents_trace.append({
            "agent_name": self.document_agent.name,
            "status": document_result["status"],
            "output": document_result["output"]
        })

        extracted_data = document_result["output"]

        validation_result = self.validation_agent.run(extracted_data)
        agents_trace.append({
            "agent_name": self.validation_agent.name,
            "status": validation_result["status"],
            "output": validation_result["output"]
        })

        rag_result = self.rag_agent.run(extracted_data)
        agents_trace.append({
            "agent_name": self.rag_agent.name,
            "status": rag_result["status"],
            "output": rag_result["output"]
        })

        fraud_result = self.fraud_agent.run(extracted_data)
        agents_trace.append({
            "agent_name": self.fraud_agent.name,
            "status": fraud_result["status"],
            "output": fraud_result["output"]
        })

        explanation_input = {
            "fraud_score": fraud_result["output"]["fraud_score"],
            "risk_level": fraud_result["output"]["risk_level"],
            "coverage_result": rag_result["output"]["coverage_result"],
            "validation_issues": validation_result["output"]["issues"]
        }

        explanation_result = self.explanation_agent.run(explanation_input)
        agents_trace.append({
            "agent_name": self.explanation_agent.name,
            "status": explanation_result["status"],
            "output": explanation_result["output"]
        })

        return {
            "claim_id": claim_data.get("claim_id"),
            "global_risk_level": fraud_result["output"]["risk_level"],
            "fraud_score": fraud_result["output"]["fraud_score"],
            "coverage_result": rag_result["output"]["coverage_result"],
            "explanation": explanation_result["output"]["explanation"],
            "agents_trace": agents_trace
        }
