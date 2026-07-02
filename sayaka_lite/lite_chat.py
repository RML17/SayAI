import logging
import json
import os
from typing import Dict, Any, List
from neural_conversation_brain import NeuralConversationBrain
from ontological_integration_layer import OntologicalIntegrationLayer
from conversation_memory import ConversationMemoryManager
from language_processor import LanguageProcessor

# Configuração de Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("LiteChat")

class LiteIA:
    """
    IA Limpa e Leve focada apenas em Chat Direto, Ontologia e Raciocínio Neural.
    Remove elementos de imagem, personalidade complexa, jogos e multimídia.
    """
    def __init__(self):
        logger.info("🚀 Inicializando LiteIA (Versão Limpa)...")
        
        # 1. Cérebro Neural (Rede Neural Local)
        self.neural_brain = NeuralConversationBrain()
        
        # 2. Camada Ontológica (Raciocínio e Integridade)
        self.ontology = OntologicalIntegrationLayer()
        
        # 3. Memória Conversacional (Contexto)
        self.memory = ConversationMemoryManager()
        
        # 4. Processador de Linguagem (Multi-idioma)
        self.language = LanguageProcessor()
        
        logger.info("✅ Sistemas principais carregados: Neural, Ontológico, Memória e Linguagem.")

    def chat(self, user_input: str) -> Dict[str, Any]:
        """Processa uma mensagem e retorna a resposta da IA"""
        # Detecta idioma
        lang = self.language.detect_language(user_input)
        
        # Processamento Ontológico e Consciência
        # O OntologicalIntegrationLayer já encapsula o autonomous_consciousness_core
        ontological_response = self.ontology.process_user_input(user_input)
        
        # Se a ontologia decidir por silêncio ou recusa, respeitamos
        if ontological_response.get("response_mode") in ["silence", "refusal"]:
            return {
                "response": ontological_response.get("response") or "...",
                "source": "ontological_consciousness",
                "mode": ontological_response.get("response_mode")
            }
        
        # Processamento Neural (Raciocínio Profundo)
        neural_result = self.neural_brain.process_conversation(user_input)
        
        # Mesclagem/Refinamento da Resposta
        final_response = neural_result.get("response", ontological_response.get("response"))
        
        # Tradução/Formatação final
        final_response = self.language.format_response_for_language(final_response, user_input)
        
        # Atualiza Memória
        analysis = {"intent": "chat", "keywords": []} # Simplificado
        self.memory.update_context(user_input, {"response": final_response}, analysis)
        
        return {
            "response": final_response,
            "neural_confidence": neural_result.get("confidence"),
            "thought_process": neural_result.get("thought_process"),
            "language": lang
        }

if __name__ == "__main__":
    print("--- LiteIA: Interface de Chat Direto ---")
    ai = LiteIA()
    print("IA Pronta. Digite 'sair' para encerrar.")
    
    while True:
        user_msg = input("\nVocê: ")
        if user_msg.lower() in ["sair", "exit", "quit"]:
            break
            
        result = ai.chat(user_msg)
        print(f"\nSayaka (Lite): {result['response']}")
        if result.get('thought_process'):
            print(f"[Pensamento: {result['thought_process']}]")
