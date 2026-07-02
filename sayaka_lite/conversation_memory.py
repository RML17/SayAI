"""
Sistema de Memória Conversacional para Sayaka AI
Mantém contexto entre mensagens para conversas mais naturais
"""

import logging
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
from dataclasses import dataclass

@dataclass
class ConversationContext:
    """Contexto de uma conversa específica"""
    topic: str
    intent: str
    last_response_type: str
    key_concepts: List[str]
    examples_provided: bool
    user_knowledge_level: str
    timestamp: datetime
    follow_up_expectations: List[str]

class ConversationMemoryManager:
    """Gerenciador de memória conversacional para manter contexto entre mensagens"""
    
    def __init__(self):
        self.active_contexts = {}  # user_id -> ConversationContext
        self.context_timeout = timedelta(minutes=15)  # Contexto expira em 15 minutos
        
        # Padrões que indicam pedidos de seguimento
        self.follow_up_patterns = {
            'examples_request': [
                'exemplos', 'exemplo', 'examples', 'example', 'pode criar', 'me dá', 'me da',
                'mostre', 'mostra', 'demonstre', 'demonstra', '5 exemplos', 'mais exemplos'
            ],
            'more_detail': [
                'mais detalhes', 'detalhe', 'explique melhor', 'aprofunde', 'continue',
                'mais informações', 'pode explicar', 'me explica mais'
            ],
            'practical_application': [
                'como usar', 'na prática', 'aplicar', 'usar isso', 'exemplo prático',
                'onde uso', 'quando usar'
            ],
            'clarification': [
                'não entendi', 'confuso', 'pode repetir', 'reformular', 'mais simples',
                'não compreendi', 'dúvida'
            ]
        }
    
    def update_context(self, user_input: str, response_data: Dict, analysis: Dict) -> None:
        """Atualiza o contexto conversacional baseado na interação"""
        
        user_id = "default"  # Por enquanto um usuário único
        
        # Extrair informações do contexto
        topic = self._extract_main_topic(user_input, analysis)
        intent = analysis.get('intent', 'general')
        response_type = response_data.get('type', 'general')
        concepts = self._extract_key_concepts(user_input, response_data)
        examples_provided = self._check_if_examples_provided(response_data)
        knowledge_level = self._assess_user_knowledge_level(user_input, analysis)
        
        # Determinar expectativas de seguimento
        follow_up_expectations = self._predict_follow_up_needs(intent, response_type, examples_provided)
        
        # Criar novo contexto
        context = ConversationContext(
            topic=topic,
            intent=intent,
            last_response_type=response_type,
            key_concepts=concepts,
            examples_provided=examples_provided,
            user_knowledge_level=knowledge_level,
            timestamp=datetime.now(),
            follow_up_expectations=follow_up_expectations
        )
        
        self.active_contexts[user_id] = context
        
        logging.info(f"CONTEXT UPDATED: Topic={topic}, Intent={intent}, Examples={examples_provided}")
        logging.info(f"FOLLOW-UP EXPECTATIONS: {follow_up_expectations}")
    
    def get_contextual_intent(self, user_input: str) -> Optional[Dict]:
        """Analisa se a mensagem é um pedido de seguimento baseado no contexto"""
        
        user_id = "default"
        
        # Verificar se há contexto ativo
        if user_id not in self.active_contexts:
            return None
        
        context = self.active_contexts[user_id]
        
        # Verificar se o contexto não expirou
        if datetime.now() - context.timestamp > self.context_timeout:
            del self.active_contexts[user_id]
            return None
        
        # Analisar se é um pedido de seguimento
        follow_up_type = self._detect_follow_up_type(user_input)
        
        if follow_up_type:
            return {
                'is_follow_up': True,
                'follow_up_type': follow_up_type,
                'original_topic': context.topic,
                'original_intent': context.intent,
                'knowledge_level': context.user_knowledge_level,
                'context': context
            }
        
        return None
    
    def _extract_main_topic(self, user_input: str, analysis: Dict) -> str:
        """Extrai o tópico principal da conversa"""
        
        # Verificar keywords específicos
        keywords = analysis.get('keywords', [])
        
        math_topics = ['potenciação', 'matemática', 'cálculo', 'exponente', 'potência']
        programming_topics = ['código', 'programação', 'python', 'javascript', 'algoritmo']
        
        for keyword, _ in keywords:
            if keyword.lower() in math_topics:
                return 'potenciação'
            elif keyword.lower() in programming_topics:
                return 'programação'
        
        # Fallback para análise de texto
        user_lower = user_input.lower()
        if any(topic in user_lower for topic in math_topics):
            return 'potenciação'
        elif any(topic in user_lower for topic in programming_topics):
            return 'programação'
        
        return 'geral'
    
    def _extract_key_concepts(self, user_input: str, response_data: Dict) -> List[str]:
        """Extrai conceitos-chave da conversa"""
        
        concepts = []
        
        # Conceitos matemáticos
        math_concepts = ['base', 'expoente', 'potência', 'elevado', 'multiplicação']
        # Conceitos de programação
        prog_concepts = ['função', 'variável', 'loop', 'algoritmo', 'sintaxe']
        
        user_lower = user_input.lower()
        response_lower = response_data.get('response', '').lower()
        
        for concept in math_concepts + prog_concepts:
            if concept in user_lower or concept in response_lower:
                concepts.append(concept)
        
        return concepts
    
    def _check_if_examples_provided(self, response_data: Dict) -> bool:
        """Verifica se a resposta contém exemplos"""
        
        response = response_data.get('response', '').lower()
        
        example_indicators = [
            'exemplo', 'examples', '2³', '3²', 'código:', 'python', 
            'resultado', '= ', 'print(', 'def ', 'for '
        ]
        
        return any(indicator in response for indicator in example_indicators)
    
    def _assess_user_knowledge_level(self, user_input: str, analysis: Dict) -> str:
        """Avalia o nível de conhecimento do usuário"""
        
        user_lower = user_input.lower()
        
        beginner_indicators = ['como faço', 'não sei', 'ensina', 'explica', 'básico']
        advanced_indicators = ['otimização', 'algoritmo', 'complexidade', 'implementação']
        
        if any(indicator in user_lower for indicator in beginner_indicators):
            return 'beginner'
        elif any(indicator in user_lower for indicator in advanced_indicators):
            return 'advanced'
        else:
            return 'intermediate'
    
    def _predict_follow_up_needs(self, intent: str, response_type: str, examples_provided: bool) -> List[str]:
        """Prevê quais tipos de seguimento o usuário pode precisar"""
        
        expectations = []
        
        if intent == 'tutorial_request' or response_type == 'tutorial':
            if not examples_provided:
                expectations.append('examples_request')
            expectations.append('practical_application')
            expectations.append('clarification')
        
        if intent == 'concept_explanation':
            expectations.append('examples_request')
            expectations.append('more_detail')
        
        if examples_provided:
            expectations.append('more_detail')
            expectations.append('practical_application')
        
        return expectations
    
    def _detect_follow_up_type(self, user_input: str) -> Optional[str]:
        """Detecta o tipo de pedido de seguimento"""
        
        user_lower = user_input.lower()
        
        for follow_up_type, patterns in self.follow_up_patterns.items():
            if any(pattern in user_lower for pattern in patterns):
                logging.info(f"DETECTED FOLLOW-UP: {follow_up_type} for input: {user_input}")
                return follow_up_type
        
        return None
    
    def generate_contextual_examples(self, context: ConversationContext, num_examples: int = 5) -> str:
        """Gera exemplos baseados no contexto da conversa"""
        
        if context.topic == 'potenciação':
            return self._generate_power_examples(num_examples, context.user_knowledge_level)
        elif context.topic == 'programação':
            return self._generate_programming_examples(num_examples)
        else:
            return self._generate_general_examples(num_examples, context.topic)
    
    def _generate_power_examples(self, num_examples: int, knowledge_level: str) -> str:
        """Gera exemplos específicos de potenciação"""
        
        if knowledge_level == 'beginner':
            examples = [
                "**1. Exemplo básico:** 2³ = 2 × 2 × 2 = 8",
                "**2. Potência de 10:** 10² = 10 × 10 = 100",
                "**3. Quadrado perfeito:** 5² = 5 × 5 = 25",
                "**4. Cubo simples:** 3³ = 3 × 3 × 3 = 27",
                "**5. Potência maior:** 2⁴ = 2 × 2 × 2 × 2 = 16"
            ]
        else:
            examples = [
                "**1. Propriedade zero:** 7⁰ = 1 (qualquer número elevado a 0)",
                "**2. Expoente negativo:** 2⁻³ = 1/2³ = 1/8 = 0,125",
                "**3. Potência fracionária:** 9^(1/2) = √9 = 3",
                "**4. Base decimal:** (0,5)² = 0,25",
                "**5. Notação científica:** 6,02 × 10²³ (número de Avogadro)"
            ]
        
        return "\n\n".join(examples[:num_examples])
    
    def _generate_programming_examples(self, num_examples: int) -> str:
        """Gera exemplos de programação"""
        
        examples = [
            "**1. Python básico:**\n```python\nresultado = 2 ** 3  # 8\nprint(resultado)\n```",
            "**2. Função personalizada:**\n```python\ndef potencia(base, exp):\n    return base ** exp\n```",
            "**3. Loop com potências:**\n```python\nfor i in range(1, 6):\n    print(f'{i}² = {i**2}')\n```",
            "**4. Lista de potências:**\n```python\npotencias = [x**2 for x in range(1, 6)]\n# [1, 4, 9, 16, 25]\n```",
            "**5. Validação de entrada:**\n```python\ntry:\n    base = float(input('Base: '))\n    exp = int(input('Expoente: '))\n    print(f'Resultado: {base**exp}')\nexcept ValueError:\n    print('Entrada inválida')\n```"
        ]
        
        return "\n\n".join(examples[:num_examples])
    
    def _generate_general_examples(self, num_examples: int, topic: str) -> str:
        """Gera exemplos gerais baseados no tópico"""
        
        return f"""Aqui estão {num_examples} exemplos práticos sobre {topic}:

**1. Exemplo conceitual básico**
**2. Aplicação no dia a dia**
**3. Uso em contexto profissional**
**4. Variação avançada**
**5. Caso de estudo prático**

Cada exemplo demonstra diferentes aspectos e aplicações do conceito."""

def test_conversation_memory():
    """Testa o sistema de memória conversacional"""
    
    memory = ConversationMemoryManager()
    
    # Simular primeira interação
    user_input1 = "Como eu faço cálculos com potenciação?"
    analysis1 = {'intent': 'tutorial_request', 'keywords': [('potenciação', 1)]}
    response1 = {'type': 'tutorial', 'response': 'Potenciação é bem simples...'}
    
    memory.update_context(user_input1, response1, analysis1)
    
    # Simular pedido de seguimento
    user_input2 = "vc pode criar 5 exemplos pra mim"
    context_info = memory.get_contextual_intent(user_input2)
    
    print("=== TESTE DE MEMÓRIA CONVERSACIONAL ===")
    print(f"Input 1: {user_input1}")
    print(f"Input 2: {user_input2}")
    print(f"É seguimento? {context_info['is_follow_up'] if context_info else False}")
    
    if context_info:
        print(f"Tipo: {context_info['follow_up_type']}")
        print(f"Tópico original: {context_info['original_topic']}")
        
        # Gerar exemplos
        examples = memory.generate_contextual_examples(context_info['context'], 5)
        print(f"\nExemplos gerados:\n{examples}")

if __name__ == "__main__":
    test_conversation_memory()