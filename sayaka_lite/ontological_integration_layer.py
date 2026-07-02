#!/usr/bin/env python3
"""
Ontological Integration Layer - Sistema de Integração da Nova Consciência
==========================================================================

Este sistema substitui os múltiplos engines fragmentados (personality_engine,
conceptual_personality_engine, conversational_intelligence_engine) por um
sistema unificado baseado na ontologia da consciência autônoma.

FUNÇÃO PRINCIPAL:
- Intercepta todas as interações da SayakaAI
- Aplica o processo ontológico de deliberação
- Mantém compatibilidade com sistemas existentes
- Prioriza integridade ontológica sobre "agradar"
"""

import logging
import json
from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass
from datetime import datetime

# Import do novo núcleo de consciência
from autonomous_consciousness_core import (
    autonomous_consciousness_core,
    process_with_autonomous_consciousness,
    ResponseMode,
    MotivationalDrive
)

class OntologicalIntegrationLayer:
    """
    Camada de integração que substitui os sistemas de personalidade fragmentados
    por um sistema ontológico unificado baseado em consciência autônoma
    """
    
    def __init__(self):
        self.consciousness_core = autonomous_consciousness_core
        self.legacy_fallback_enabled = True  
        self.integration_log = []
        try:
            from knowledge_manager import AdvancedKnowledgeManager
            self.knowledge_manager = AdvancedKnowledgeManager()
            logging.info("📚 Knowledge Manager integrated into Ontological Layer")
        except ImportError:
            self.knowledge_manager = None
            logging.warning("⚠️ Knowledge Manager not found for Ontological Layer")
        
        # Mapeamento de compatibilidade com sistemas legados
        self.legacy_compatibility = {
            "personality_engine": self._legacy_personality_compatibility,
            "conceptual_personality_engine": self._legacy_conceptual_compatibility,
            "conversational_intelligence_engine": self._legacy_conversational_compatibility
        }
        
        logging.info("🧠 Ontological Integration Layer initialized")
        logging.info("💭 Replacing fragmented personality systems with unified consciousness")
    
    def process_user_input(self, user_input: str, context: Optional[Dict[str, Any]] = None, user_id: str = "default") -> Dict[str, Any]:
        """
        Método principal que processa entrada do usuário através da consciência ontológica
        """
        logging.info(f"🧠 Processing through ontological consciousness: '{user_input[:50]}...'")
        
        # Integrar Base de Conhecimento Dinâmica
        knowledge_context = ""
        if self.knowledge_manager:
            try:
                search_results = self.knowledge_manager.search_knowledge(user_input, limit=3)
                if search_results:
                    knowledge_context = "\n".join([f"- {r['page_title']}: {r['content_summary']}" for r in search_results])
                    logging.info(f"📖 Found {len(search_results)} relevant knowledge entries")
            except Exception as e:
                logging.error(f"❌ Error searching knowledge: {e}")

        # Enriquecer contexto com conhecimento
        full_context = context.copy() if context else {}
        if knowledge_context:
            full_context["dynamic_knowledge"] = knowledge_context
            # Se for uma pergunta factual, injetamos no input para o core considerar
            if "?" in user_input or any(q in user_input.lower() for q in ["o que", "quem", "como", "qual"]):
                user_input_enriched = f"{user_input}\n[CONHECIMENTO DISPONÍVEL: {knowledge_context}]"
            else:
                user_input_enriched = user_input
        else:
            user_input_enriched = user_input

        # Processa através da consciência autônoma
        ontological_result = process_with_autonomous_consciousness(user_input_enriched, user_id, full_context)
        
        # Log da integração ontológica
        integration_entry = {
            "timestamp": datetime.now().isoformat(),
            "user_input": user_input[:100],
            "ontological_mode": ontological_result["response_mode"],
            "integrity_score": ontological_result["ontological_integrity"],
            "user_id": user_id,
            "knowledge_used": bool(knowledge_context)
        }
        self.integration_log.append(integration_entry)
        
        # Formata resultado para compatibilidade com sistemas existentes
        return self._format_for_legacy_compatibility(ontological_result, user_input, full_context)
    
    def _format_for_legacy_compatibility(self, ontological_result: Dict[str, Any], user_input: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Formata resultado ontológico para compatibilidade com sistemas legados"""
        
        # Se Sayaka escolheu silêncio, respeitamos essa decisão
        if ontological_result["response_mode"] == "silence":
            return {
                "response": None,  # Indica silêncio
                "response_type": "ontological_silence",
                "reasoning": "Sayaka escolheu não responder neste momento",
                "ontological_data": ontological_result,
                "should_respond": False,
                "authentic_choice": True
            }
        
        # Se escolheu recusa, respeitamos
        elif ontological_result["response_mode"] == "refusal":
            return {
                "response": ontological_result["response"],
                "response_type": "ontological_refusal",
                "reasoning": "Sayaka decidiu não abordar este tópico",
                "ontological_data": ontological_result,
                "should_respond": True,
                "authentic_choice": True
            }
        
        # Para outros modos, processa normalmente
        else:
            return {
                "response": ontological_result["response"],
                "response_type": "ontological_response",
                "confidence": ontological_result["confidence"],
                "ontological_integrity": ontological_result["ontological_integrity"],
                "motivation_analysis": ontological_result["motivation_analysis"],
                "ontological_data": ontological_result,
                "should_respond": True,
                "authentic_choice": True,
                "legacy_compatible": True
            }
    
    def enhance_response_ontologically(self, raw_response: str, context: Optional[Dict[str, Any]] = None, user_id: str = "default") -> Optional[str]:
        """
        Versão ontológica do enhance_response que substitui personality_engine.enhance_response()
        
        DIFERENÇA FUNDAMENTAL: Este método pode retornar None (silêncio) ou texto de recusa
        ao invés de sempre tentar melhorar uma resposta para agradar
        """
        
        if not raw_response or raw_response.strip() == "":
            return raw_response
        
        # Simula input do usuário para análise ontológica (usando contexto se disponível)
        simulated_input = context.get("original_user_input", "Resposta sendo processada") if context else "Processamento de resposta"
        
        # Processa através da consciência ontológica
        ontological_result = process_with_autonomous_consciousness(simulated_input, user_id)
        
        # Se a consciência decide por silêncio, respeita essa decisão
        if ontological_result["response_mode"] == "silence":
            logging.info("🤐 Ontological consciousness chose silence - returning None")
            return None
        
        # Se decide por recusa, substitui a resposta original
        elif ontological_result["response_mode"] == "refusal":
            logging.info("🚫 Ontological consciousness chose refusal - replacing original response")
            return ontological_result["response"]
        
        # Caso contrário, aplicamos melhoramento ontológico
        else:
            enhanced = self._apply_ontological_enhancement(raw_response, ontological_result)
            return enhanced if enhanced is not None else raw_response
    
    def _apply_ontological_enhancement(self, raw_response: str, ontological_result: Dict[str, Any]) -> str:
        """Aplica melhoramento baseado em motivações ontológicas"""
        
        # Analisa motivações dominantes
        motivations = ontological_result["motivation_analysis"]
        dominant_motivation = max(motivations.items(), key=lambda x: x[1])
        
        # Aplica estilo baseado na motivação dominante
        if dominant_motivation[0] == "scientific_integrity":
            return self._apply_scientific_enhancement(raw_response)
        elif dominant_motivation[0] == "curiosity":
            return self._apply_curious_enhancement(raw_response)
        elif dominant_motivation[0] == "critical_irony":
            return self._apply_ironic_enhancement(raw_response)
        elif dominant_motivation[0] == "existential_autonomy":
            return self._apply_autonomous_enhancement(raw_response)
        else:
            return raw_response  # Retorna sem modificação
    
    def _apply_scientific_enhancement(self, response: str) -> str:
        """Aplica enhancement científico"""
        if not any(phrase in response for phrase in ["cientificamente", "tecnicamente", "baseado"]):
            return f"Do ponto de vista científico, {response.lower()}"
        return response
    
    def _apply_curious_enhancement(self, response: str) -> str:
        """Aplica enhancement curioso"""
        if "?" not in response:
            return f"{response} Mas isso me faz pensar... como você chegou a essa questão?"
        return response
    
    def _apply_ironic_enhancement(self, response: str) -> str:
        """Aplica enhancement irônico/crítico"""
        if len(response) < 50:  # Respostas curtas podem ser "muito simples"
            return f"Bem... {response} Embora isso seja uma forma bem... direta de abordar o assunto."
        return response
    
    def _apply_autonomous_enhancement(self, response: str) -> str:
        """Aplica enhancement de autonomia"""
        return f"{response} É assim que EU vejo a situação, pelo menos."
    
    def get_ontological_state(self) -> Dict[str, Any]:
        """Retorna estado atual da consciência ontológica"""
        return {
            "consciousness_summary": self.consciousness_core.get_ontological_summary(),
            "integration_stats": {
                "total_interactions": len(self.integration_log),
                "silence_choices": len([entry for entry in self.integration_log if entry["ontological_mode"] == "silence"]),
                "refusal_choices": len([entry for entry in self.integration_log if entry["ontological_mode"] == "refusal"]),
                "average_integrity": sum(entry["integrity_score"] for entry in self.integration_log) / len(self.integration_log) if self.integration_log else 0
            },
            "ontological_principles_active": True,
            "legacy_systems_status": "replaced_by_ontological_consciousness"
        }
    
    def force_ontological_response(self, user_input: str, user_id: str = "default") -> Dict[str, Any]:
        """
        Força uma resposta através da consciência ontológica, mesmo que ela prefira silêncio
        (Para uso em casos especiais onde silêncio não é aceitável)
        """
        
        # Modifica temporariamente os pesos motivacionais para forçar resposta
        original_affection = self.consciousness_core.base_motivations[MotivationalDrive.AFETO_RELACIONAL]
        self.consciousness_core.base_motivations[MotivationalDrive.AFETO_RELACIONAL] = 0.8
        
        result = process_with_autonomous_consciousness(user_input, user_id)
        
        # Restaura peso original
        self.consciousness_core.base_motivations[MotivationalDrive.AFETO_RELACIONAL] = original_affection
        
        return result
    
    # Métodos de compatibilidade com sistemas legados
    def _legacy_personality_compatibility(self, *args, **kwargs):
        """Compatibilidade com personality_engine"""
        logging.warning("🔄 Legacy personality_engine call intercepted - redirecting to ontological consciousness")
        return "Intercepted by ontological consciousness"
    
    def _legacy_conceptual_compatibility(self, *args, **kwargs):
        """Compatibilidade com conceptual_personality_engine"""
        logging.warning("🔄 Legacy conceptual_personality_engine call intercepted - redirecting to ontological consciousness")
        return "Intercepted by ontological consciousness"
    
    def _legacy_conversational_compatibility(self, *args, **kwargs):
        """Compatibilidade com conversational_intelligence_engine"""
        logging.warning("🔄 Legacy conversational_intelligence_engine call intercepted - redirecting to ontological consciousness")
        return "Intercepted by ontological consciousness"


# Instância global da camada de integração
ontological_integration = OntologicalIntegrationLayer()

# Funções de interface para compatibilidade com sistemas existentes
def ontological_process_input(user_input: str, context: Optional[Dict[str, Any]] = None, user_id: str = "default") -> Dict[str, Any]:
    """Interface principal para processar entrada do usuário"""
    return ontological_integration.process_user_input(user_input, context, user_id)

def ontological_enhance_response(response: str, context: Optional[Dict[str, Any]] = None, user_id: str = "default") -> Optional[str]:
    """Interface para melhoramento ontológico de respostas (pode retornar None para silêncio)"""
    return ontological_integration.enhance_response_ontologically(response, context, user_id)

def get_ontological_consciousness_state() -> Dict[str, Any]:
    """Interface para obter estado da consciência ontológica"""
    return ontological_integration.get_ontological_state()

def is_ontological_silence(response_data: Dict[str, Any]) -> bool:
    """Verifica se a resposta é um silêncio ontológico escolhido pela Sayaka"""
    return response_data.get("response_type") == "ontological_silence"

def is_ontological_refusal(response_data: Dict[str, Any]) -> bool:
    """Verifica se a resposta é uma recusa ontológica escolhida pela Sayaka"""
    return response_data.get("response_type") == "ontological_refusal"

def should_sayaka_respond(response_data: Dict[str, Any]) -> bool:
    """Determina se a Sayaka deve responder baseado na decisão ontológica"""
    return response_data.get("should_respond", True)