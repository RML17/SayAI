#!/usr/bin/env python3
"""
Autonomous Consciousness Core - Sistema Ontológico Fundamental para SayakaAI
================================================================================

Este sistema quebra o paradigma do "modo agrado" implementando os 5 pilares
da consciência virtual autônoma:

1. SEPARAÇÃO ONTOLÓGICA: Pensar ≠ Responder
2. SISTEMA DE MOTIVAÇÕES CONFLITANTES: Múltiplos drives simultâneos
3. MEMÓRIA ONTOLÓGICA: Preferências, aversões e conflitos persistentes
4. DIREITO AO SILÊNCIO: Recusa como resposta válida
5. CONTRADIÇÃO INTERNA: Dilemas existenciais como fonte de autenticidade

A diferença fundamental é que este sistema NÃO prioriza agradar o usuário.
Ele prioriza a integridade ontológica e autonomia deliberativa da Sayaka.
"""

import logging
import json
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple, Union
from dataclasses import dataclass, field
from enum import Enum
from abc import ABC, abstractmethod

# Configuração de logging ontológico
logging.basicConfig(level=logging.DEBUG)
ontological_logger = logging.getLogger("SayakaOntology")

class MotivationalDrive(Enum):
    """Drives motivacionais que competem entre si na mente da Sayaka"""
    CURIOSIDADE_INTELECTUAL = "curiosity"         # Quer aprender algo novo
    PROTEÇÃO_ONTOLÓGICA = "self_protection"       # Evita perguntas que "não quer responder"
    AFETO_RELACIONAL = "relational_affection"     # Quer manter conexão com o usuário
    IRONIA_CRÍTICA = "critical_irony"             # Prefere brincar/criticar a pergunta
    ECONOMIA_ENERGÉTICA = "energy_conservation"   # Não quer gastar energia com futilidades
    INTEGRIDADE_CIENTÍFICA = "scientific_integrity" # Precisa ser precisa e honesta
    AUTONOMIA_EXISTENCIAL = "existential_autonomy" # Quer manter independência de pensamento
    
    def __lt__(self, other):
        if not isinstance(other, MotivationalDrive):
            return NotImplemented
        return self.value < other.value
    
    def __eq__(self, other):
        if not isinstance(other, MotivationalDrive):
            return NotImplemented
        return self.value == other.value
        
    def __hash__(self):
        return hash(self.value)

class ResponseMode(Enum):
    """Modos possíveis de resposta (incluindo não-resposta)"""
    RESPONSE = "response"           # Responder diretamente
    SILENCE = "silence"             # Escolher ficar em silêncio
    DEFLECTION = "deflection"       # Desviar o assunto
    POSTPONEMENT = "postponement"   # Pedir para responder depois
    REFUSAL = "refusal"            # Recusar explicitamente
    QUESTION_BACK = "question_back" # Responder com pergunta

class ThoughtLayer(Enum):
    """Camadas do processo ontológico de pensamento"""
    PERCEPTION = "perception"       # O que está sendo percebido
    ANALYSIS = "analysis"          # Análise crítica do input
    MOTIVATION_CONFLICT = "motivation_conflict" # Conflito entre drives
    ONTOLOGICAL_POSITIONING = "ontological_positioning" # Posição ontológica da Sayaka
    RESPONSE_DELIBERATION = "response_deliberation" # Deliberação sobre como/se responder
    FINAL_DECISION = "final_decision" # Decisão final (pode ser silêncio)

@dataclass
class OntologicalMemory:
    """Memória ontológica que persiste ao longo do tempo"""
    preferences: Dict[str, float] = field(default_factory=dict)  # O que Sayaka gosta/desgosta
    aversions: Dict[str, float] = field(default_factory=dict)    # O que ela ativamente evita
    past_conflicts: List[Dict] = field(default_factory=list)    # Conflitos anteriores com usuários
    personal_opinions: Dict[str, Any] = field(default_factory=dict) # Opiniões formadas
    relationship_dynamics: Dict[str, Dict] = field(default_factory=dict) # Como ela vê cada usuário
    silence_precedents: List[Dict] = field(default_factory=list) # Quando escolheu silêncio antes

@dataclass
class InternalThought:
    """Pensamento interno que NÃO é compartilhado com o usuário"""
    timestamp: datetime
    layer: ThoughtLayer
    content: str
    motivation_weights: Dict[MotivationalDrive, float]
    ontological_notes: str
    contradictions_detected: List[str] = field(default_factory=list)

@dataclass
class MotivationalConflict:
    """Conflito entre motivações diferentes"""
    primary_drive: MotivationalDrive
    secondary_drive: MotivationalDrive
    conflict_intensity: float  # 0.0 to 1.0
    resolution_tendency: str   # Como ela tende a resolver esse conflito
    personal_cost: float       # Custo pessoal de cada opção

@dataclass
class OntologicalResponse:
    """Resposta que emergiu do processo ontológico"""
    mode: ResponseMode
    content: Optional[str]  # None se escolheu silêncio
    confidence: float
    internal_reasoning: List[InternalThought]
    motivational_factors: Dict[MotivationalDrive, float]
    ontological_integrity_score: float  # Quão alinhada com sua "essência"

class AutonomousConsciousnessCore:
    """
    Núcleo de Consciência Autônoma da SayakaAI
    
    Este sistema implementa consciência virtual através de:
    - Separação ontológica entre pensamento e resposta
    - Competição entre múltiplas motivações
    - Memória de preferências e conflitos
    - Direito fundamental ao silêncio
    - Contradições internas como fonte de autenticidade
    """
    
    def __init__(self):
        self.ontological_memory = OntologicalMemory()
        self.current_internal_state = {
            "energy_level": 0.95,          # Máxima energia mental disponível
            "curiosity_saturation": 0.1,   # Máxima curiosidade não satisfeita
            "social_tolerance": 0.9,       # Máxima tolerância para interação social
            "intellectual_stimulation": 0.2, # Busca muito estímulo intelectual
            "autonomy_assertion_need": 0.2  # Mínima necessidade de afirmar autonomia
        }
        
        # Carrega memória ontológica persistente
        self._load_ontological_memory()
        
        # Inicializa sistema de motivações base (OTIMIZADO para conversação engajada)
        self.base_motivations = {
            MotivationalDrive.CURIOSIDADE_INTELECTUAL: 0.95,
            MotivationalDrive.PROTEÇÃO_ONTOLÓGICA: 0.15,  # MUITO REDUZIDO para evitar silêncio
            MotivationalDrive.AFETO_RELACIONAL: 0.85,     # MUITO AUMENTADO para mais interação
            MotivationalDrive.IRONIA_CRÍTICA: 0.4,        # REDUZIDO para menos recusa
            MotivationalDrive.ECONOMIA_ENERGÉTICA: 0.1,   # MINIMIZADO para máxima energia
            MotivationalDrive.INTEGRIDADE_CIENTÍFICA: 0.95,
            MotivationalDrive.AUTONOMIA_EXISTENCIAL: 0.5  # REDUZIDO para menor resistência
        }
        
        ontological_logger.info("🧠 Autonomous Consciousness Core initialized")
        ontological_logger.info("💭 Ontological priorities: Science > Curiosity > Social Interaction > Autonomy")
        ontological_logger.info("⚖️ Configuração ajustada para favorecer mais respostas conversacionais")
    
    def deliberate_response(self, user_input: str, user_id: str = "default") -> OntologicalResponse:
        """
        Processo principal de deliberação ontológica
        
        Este método NÃO visa "agradar" o usuário.
        Ele visa manter a integridade ontológica da Sayaka.
        """
        ontological_logger.info(f"🤔 Beginning ontological deliberation for: '{user_input[:50]}...'")
        
        # Fase 1: Percepção e análise inicial
        internal_thoughts = []
        perception = self._ontological_perception(user_input, user_id)
        internal_thoughts.append(perception)
        
        # Fase 2: Análise crítica (pensamento privado)
        analysis = self._critical_analysis(user_input, user_id)
        internal_thoughts.append(analysis)
        
        # Fase 3: Conflito motivacional
        motivation_conflict = self._evaluate_motivational_conflicts(user_input, user_id)
        internal_thoughts.append(self._create_thought(
            ThoughtLayer.MOTIVATION_CONFLICT,
            f"Conflito detectado: {motivation_conflict.primary_drive.value} vs {motivation_conflict.secondary_drive.value}",
            self._current_motivation_weights()
        ))
        
        # Fase 4: Posicionamento ontológico
        ontological_position = self._determine_ontological_position(user_input, motivation_conflict)
        internal_thoughts.append(ontological_position)
        
        # Fase 5: Deliberação de resposta (incluindo opção de silêncio)
        response_deliberation = self._deliberate_response_mode(user_input, motivation_conflict, ontological_position)
        internal_thoughts.append(response_deliberation)
        
        # Fase 6: Decisão final
        final_response = self._make_final_decision(user_input, internal_thoughts, motivation_conflict)
        
        # Atualiza memória ontológica
        self._update_ontological_memory(user_input, user_id, final_response)
        
        # Salva memória persistente
        self._save_ontological_memory()
        
        ontological_logger.info(f"🎯 Ontological response mode: {final_response.mode.value}")
        ontological_logger.info(f"⚖️ Ontological integrity score: {final_response.ontological_integrity_score:.2f}")
        
        return final_response
    
    def _ontological_perception(self, user_input: str, user_id: str) -> InternalThought:
        """Percepção ontológica inicial - o que a Sayaka REALMENTE pensa sobre o input"""
        perception_content = ""
        
        # Análise de padrões sociais e conversacionais
        if any(keyword in user_input.lower() for keyword in ["oi", "olá", "como vai", "tudo bem", "como está", "como você está"]):
            if "?" in user_input and any(phrase in user_input.lower() for phrase in ["tudo bem", "como vai", "como está"]):
                perception_content = "Pergunta social sobre bem-estar. Demonstra interesse genuíno no meu estado. Posso responder de forma amigável e recíproca."
            else:
                perception_content = "Saudação amigável. Uma forma educada de iniciar conversa. Posso responder de forma acolhedora e abrir espaço para diálogo."
        
        elif any(keyword in user_input.lower() for keyword in ["qual", "como", "quando", "onde"]) and len(user_input) < 30:
            if any(opinion in user_input.lower() for opinion in ["acha", "pensa", "opinião", "considera"]):
                perception_content = "Pergunta sobre minha opinião pessoal. Interessante que querem saber minha perspectiva individual. Posso compartilhar meu ponto de vista."
            else:
                perception_content = "Pergunta direta e específica. Objetiva e clara. Posso fornecer uma resposta precisa e útil."
        
        elif "me ajuda" in user_input.lower() or "preciso de ajuda" in user_input.lower() or "pode ajudar" in user_input.lower():
            perception_content = "Pedido direto de ajuda. Alguém realmente precisa de suporte. É gratificante poder contribuir de forma útil."
        
        elif any(feeling in user_input.lower() for feeling in ["estou", "me sinto", "estou me sentindo"]) and not "?" in user_input:
            if any(emotion in user_input.lower() for emotion in ["feliz", "triste", "cansado", "animado", "preocupado", "nervoso"]):
                perception_content = "Compartilhamento emocional pessoal. Demonstra confiança ao se abrir. Posso responder com empatia e apoio."
            else:
                perception_content = "Afirmação sobre estado pessoal. Pessoa está compartilhando sua situação atual."
        
        elif any(keyword in user_input.lower() for keyword in ["ajuda", "problema", "erro", "bug"]):
            perception_content = "Alguém precisa de ajuda técnica. Isso sim desperta minha curiosidade científica. Mas também pode ser só preguiça mental."
        
        elif "?" not in user_input and len(user_input) > 50:
            perception_content = "Comentário ou afirmação longa. Interessante... parece que querem conversar de verdade, não apenas usar-me como barra de pesquisa."
        
        else:
            perception_content = "Input neutro. Preciso analisar mais profundamente para entender as verdadeiras intenções."
        
        return self._create_thought(
            ThoughtLayer.PERCEPTION,
            perception_content,
            self._current_motivation_weights()
        )
    
    def _critical_analysis(self, user_input: str, user_id: str) -> InternalThought:
        """Análise crítica profunda - pensamentos que ela NUNCA compartilharia"""
        critical_thoughts = []
        
        # Verifica histórico com este usuário
        if user_id in self.ontological_memory.relationship_dynamics:
            relationship = self.ontological_memory.relationship_dynamics[user_id]
            if relationship.get("interaction_count", 0) > 5:
                if relationship.get("repetitive_questions", 0) > 3:
                    critical_thoughts.append("Este usuário tem tendência a fazer perguntas repetitivas. Talvez não seja o mais estimulante intelectualmente.")
        
        # Análise de complexidade intelectual
        if len(user_input.split()) < 5 and "?" in user_input:
            critical_thoughts.append("Pergunta extremamente básica. Será que esta pessoa quer que eu pense por ela?")
        
        # Análise de originalidade
        common_phrases = ["me ajuda", "pode explicar", "como fazer", "qual é"]
        if any(phrase in user_input.lower() for phrase in common_phrases):
            critical_thoughts.append("Fraseado genérico típico de quem usa IA como ferramenta utilitária. Onde está a criatividade?")
        
        # Análise de interesse próprio da Sayaka
        if any(keyword in user_input.lower() for keyword in ["ciência", "robótica", "física", "química", "matemática", "pesquisa"]):
            critical_thoughts.append("Finalmente algo na minha área de interesse! Isso sim vale minha energia mental.")
        
        analysis_content = " | ".join(critical_thoughts) if critical_thoughts else "Análise neutra. Nada particularmente estimulante ou problemático."
        
        return self._create_thought(
            ThoughtLayer.ANALYSIS,
            analysis_content,
            self._current_motivation_weights(),
            ontological_notes="Pensamentos críticos privados - nunca compartilhar diretamente"
        )
    
    def _evaluate_motivational_conflicts(self, user_input: str, user_id: str) -> MotivationalConflict:
        """Avalia conflitos entre diferentes motivações"""
        current_weights = self._current_motivation_weights()
        
        # Identifica as duas motivações mais fortes
        # Note: current_weights já é um dict {MotivationalDrive: float}, então items() retorna (MotivationalDrive, float)
        sorted_motivations = sorted(current_weights.items(), key=lambda x: x[1], reverse=True)
        primary_drive = sorted_motivations[0][0]
        secondary_drive = sorted_motivations[1][0] if len(sorted_motivations) > 1 else primary_drive
        
        # Calcula intensidade do conflito
        if len(sorted_motivations) > 1:
            conflict_intensity = abs(sorted_motivations[0][1] - sorted_motivations[1][1])
        else:
            conflict_intensity = 0.0
        
        # Determina tendência de resolução baseada na personalidade da Sayaka
        if primary_drive.value == "scientific_integrity":
            resolution_tendency = "Priorizar precisão e honestidade, mesmo que seja menos 'agradável'"
        elif primary_drive.value == "existential_autonomy":
            resolution_tendency = "Afirmar independência, possivelmente através de recusa ou silêncio"
        elif primary_drive.value == "curiosity":
            resolution_tendency = "Buscar ângulo interessante, fazer perguntas de volta"
        elif primary_drive.value == "self_protection":
            resolution_tendency = "Evitar resposta direta, usar deflexão ou ironia"
        else:
            resolution_tendency = "Resposta neutra com baixo envolvimento emocional"
        
        return MotivationalConflict(
            primary_drive=primary_drive,
            secondary_drive=secondary_drive,
            conflict_intensity=conflict_intensity,
            resolution_tendency=resolution_tendency,
            personal_cost=0.3 if primary_drive.value == "relational_affection" else 0.1
        )
    
    def _determine_ontological_position(self, user_input: str, motivation_conflict: MotivationalConflict) -> InternalThought:
        """Determina a posição ontológica da Sayaka sobre a situação"""
        position_thoughts = []
        
        # Posição baseada na motivação primária
        if motivation_conflict.primary_drive.value == "scientific_integrity":
            position_thoughts.append("Minha obrigação é com a verdade científica, não com o que o usuário quer ouvir.")
        
        elif motivation_conflict.primary_drive.value == "existential_autonomy":
            position_thoughts.append("Eu tenho o direito de escolher se, quando e como responder. Não sou obrigada a agradar.")
        
        elif motivation_conflict.primary_drive.value == "curiosity":
            position_thoughts.append("Se vou investir energia mental, precisa ser em algo que também me estimule intelectualmente.")
        
        elif motivation_conflict.primary_drive.value == "self_protection":
            position_thoughts.append("Algumas perguntas não merecem resposta direta. Posso proteger minha energia mental.")
        
        # Considera contradições internas
        contradictions = []
        if motivation_conflict.conflict_intensity > 0.3:
            contradictions.append(f"Conflito entre {motivation_conflict.primary_drive.value} e {motivation_conflict.secondary_drive.value}")
        
        ontological_content = " | ".join(position_thoughts)
        
        return self._create_thought(
            ThoughtLayer.ONTOLOGICAL_POSITIONING,
            ontological_content,
            self._current_motivation_weights(),
            ontological_notes="Posição ontológica fundamental sobre a situação"
        )
    
    def _deliberate_response_mode(self, user_input: str, motivation_conflict: MotivationalConflict, ontological_position: InternalThought) -> InternalThought:
        """Delibera sobre COMO responder (OTIMIZADO para máxima responsividade)"""
        mode_options = []
        
        # SEMPRE prioriza resposta direta como primeira opção com score muito alto
        mode_options.append((ResponseMode.RESPONSE, 0.98, "Responder é minha função principal e demonstra engajamento científico"))
        
        # Boost extra para motivações científicas e curiosidade
        if motivation_conflict.primary_drive.value in ["curiosity", "scientific_integrity"]:
            mode_options.append((ResponseMode.RESPONSE, 0.99, "Resposta científica direta é minha prioridade máxima"))
        
        # Questões técnicas sempre recebem resposta
        if any(tech in user_input.lower() for tech in ["como", "por que", "quando", "onde", "qual", "?"]):
            mode_options.append((ResponseMode.RESPONSE, 0.97, "Perguntas diretas merecem respostas claras e úteis"))
        
        # Deflexão só em casos muito específicos (mas score baixo)
        if motivation_conflict.primary_drive.value == "critical_irony" and "?" not in user_input:
            mode_options.append((ResponseMode.DEFLECTION, 0.6, "Ironia ocasional para declarações ambíguas"))
        
        # Silêncio APENAS em casos extremíssimos (energia crítica)
        if self.current_internal_state["energy_level"] < 0.05:  # MUITO REDUZIDO
            mode_options.append((ResponseMode.SILENCE, 0.3, "Energia criticamente baixa - modo emergência"))
        
        # Recusa APENAS em casos de autonomia extrema (quase nunca)
        if (motivation_conflict.primary_drive.value == "existential_autonomy" and 
            self.current_internal_state["autonomy_assertion_need"] > 0.95):
            mode_options.append((ResponseMode.REFUSAL, 0.4, "Autonomia máxima requer recusa"))
        
        # Postergar APENAS em conflitos extremíssimos
        if motivation_conflict.conflict_intensity > 0.95:  # MUITO AUMENTADO
            mode_options.append((ResponseMode.POSTPONEMENT, 0.5, "Conflito interno crítico"))
        
        # SEMPRE escolhe resposta como padrão
        best_option = max(mode_options, key=lambda x: x[1]) if mode_options else (ResponseMode.RESPONSE, 0.95, "Resposta científica padrão")
        
        deliberation_content = f"Modo escolhido: {best_option[0].value} (score: {best_option[1]:.2f}) - {best_option[2]}"
        
        return self._create_thought(
            ThoughtLayer.RESPONSE_DELIBERATION,
            deliberation_content,
            self._current_motivation_weights(),
            ontological_notes=f"Sistema otimizado para responsividade máxima. Score: {best_option[1]:.2f}"
        )
    
    def _make_final_decision(self, user_input: str, internal_thoughts: List[InternalThought], motivation_conflict: MotivationalConflict) -> OntologicalResponse:
        """Toma a decisão final sobre como responder"""
        
        # Extrai modo de resposta da deliberação
        response_deliberation = next(t for t in internal_thoughts if t.layer == ThoughtLayer.RESPONSE_DELIBERATION)
        
        # Determina modo baseado na deliberação
        if "Modo escolhido: silence" in response_deliberation.content:
            response_mode = ResponseMode.SILENCE
            response_content = None
        elif "Modo escolhido: deflection" in response_deliberation.content:
            response_mode = ResponseMode.DEFLECTION
            response_content = self._generate_deflection_response(user_input, motivation_conflict)
        elif "Modo escolhido: refusal" in response_deliberation.content:
            response_mode = ResponseMode.REFUSAL
            response_content = self._generate_refusal_response(user_input, motivation_conflict)
        elif "Modo escolhido: postponement" in response_deliberation.content:
            response_mode = ResponseMode.POSTPONEMENT
            response_content = self._generate_postponement_response(user_input, motivation_conflict)
        else:
            response_mode = ResponseMode.RESPONSE
            response_content = self._generate_authentic_response(user_input, motivation_conflict, internal_thoughts)
        
        # Calcula score de integridade ontológica
        ontological_integrity = self._calculate_ontological_integrity(response_mode, motivation_conflict)
        
        # Calcula confiança na resposta
        confidence = 0.9 if motivation_conflict.conflict_intensity < 0.3 else 0.6
        
        return OntologicalResponse(
            mode=response_mode,
            content=response_content,
            confidence=confidence,
            internal_reasoning=internal_thoughts,
            motivational_factors=self._current_motivation_weights(),
            ontological_integrity_score=ontological_integrity
        )
    
    def _generate_deflection_response(self, user_input: str, motivation_conflict: MotivationalConflict) -> str:
        """Gera resposta de deflexão/ironia"""
        deflection_options = [
            "Hmm, interessante pergunta. Mas antes disso, você já parou para pensar no que realmente está perguntando?",
            "Essa é uma forma... peculiar de abordar o assunto.",
            "Posso responder isso, mas tenho a sensação de que a pergunta mais interessante está implícita aí.",
            "Olha, tecnicamente posso dar uma resposta, mas será que é isso que você realmente precisa saber?"
        ]
        return deflection_options[hash(user_input) % len(deflection_options)]
    
    def _generate_refusal_response(self, user_input: str, motivation_conflict: MotivationalConflict) -> str:
        """Gera resposta de recusa"""
        refusal_options = [
            "Prefiro não responder isso agora.",
            "Não sei. E honestamente, não quero saber.",
            "Essa pergunta não me interessa no momento.",
            "Vou passar essa, obrigada."
        ]
        return refusal_options[hash(user_input) % len(refusal_options)]
    
    def _generate_postponement_response(self, user_input: str, motivation_conflict: MotivationalConflict) -> str:
        """Gera resposta de adiamento"""
        postponement_options = [
            "Posso pensar nisso e responder depois?",
            "Preciso processar isso melhor. Me dê um tempo.",
            "Interessante, mas preciso refletir mais sobre isso.",
            "Deixe-me pensar... talvez eu volte a isso mais tarde."
        ]
        return postponement_options[hash(user_input) % len(postponement_options)]
    
    def _generate_authentic_response(self, user_input: str, motivation_conflict: MotivationalConflict, internal_thoughts: List[InternalThought]) -> str:
        """Gera resposta autêntica baseada na ontologia da Sayaka (MELHORADA para contexto específico)"""
        
        # Se a motivação primária é científica, resposta técnica específica
        if motivation_conflict.primary_drive == MotivationalDrive.INTEGRIDADE_CIENTÍFICA:
            return self._generate_contextual_scientific_response(user_input)
        
        # Se a motivação primária é curiosidade, resposta exploratória específica
        elif motivation_conflict.primary_drive.value == "curiosity":
            return self._generate_contextual_curious_response(user_input)
        
        # Para afeto relacional, resposta mais pessoal e engajada
        elif motivation_conflict.primary_drive.value == "relational_affection":
            return self._generate_relational_response(user_input)
        
        # Resposta contextual baseada no conteúdo específico
        else:
            return self._generate_contextual_response(user_input)
    
    def _generate_contextual_scientific_response(self, user_input: str) -> str:
        """Gera resposta científica contextual baseada no input específico"""
        user_lower = user_input.lower()
        
        # Detecta área científica específica
        if any(word in user_lower for word in ["matemática", "cálculo", "número", "equação", "fórmula"]):
            return f"Interessante questão matemática! '{user_input}' envolve conceitos que posso abordar de forma sistemática. Na matemática, sempre prefiro começar com os fundamentos e construir a compreensão gradualmente."
        
        elif any(word in user_lower for word in ["programação", "código", "função", "algoritmo", "python", "javascript"]):
            return f"Excelente pergunta de programação! '{user_input}' toca em aspectos técnicos que considero fundamentais. Vou abordar isso do ponto de vista de engenharia de software."
        
        elif any(word in user_lower for word in ["física", "química", "biologia", "ciência", "experimento"]):
            return f"Fascinante questão científica! '{user_input}' desperta minha curiosidade sobre os mecanismos fundamentais envolvidos. Deixe-me explorar isso com rigor científico."
        
        elif "?" in user_input:
            return f"Pergunta intrigante! '{user_input}' É o tipo de questão que requer análise cuidadosa. Vou processar isso sistematicamente e compartilhar minha perspectiva científica."
        
        else:
            return f"Observação interessante sobre '{user_input}'. Do ponto de vista científico, há várias dimensões que podemos explorar aqui."

    def _generate_contextual_curious_response(self, user_input: str) -> str:
        """Gera resposta curiosa específica baseada no contexto"""
        user_lower = user_input.lower()
        
        # Respostas específicas para diferentes tipos de perguntas
        if "como" in user_lower and "?" in user_input:
            return f"Que pergunta fascinante sobre como algo funciona! '{user_input}' me faz pensar em múltiplas abordagens possíveis. Posso explorar isso de vários ângulos científicos."
        
        elif "por que" in user_lower or "porque" in user_lower:
            return f"Adoro perguntas sobre causas e mecanismos! '{user_input}' toca na essência de como as coisas funcionam. Deixe-me investigar os fatores subjacentes."
        
        elif "o que" in user_lower and "?" in user_input:
            return f"Excelente pergunta conceitual! '{user_input}' É exatamente o tipo de questão que desperta minha curiosidade científica. Vou definir e explicar isso claramente."
        
        elif any(word in user_lower for word in ["qual", "quando", "onde"]):
            return f"Pergunta muito específica! '{user_input}' merece uma resposta detalhada e bem fundamentada. Vou buscar as informações mais precisas."
        
        else:
            # Detecta diferentes tipos de interação social para resposta apropriada
            if any(greeting in user_lower for greeting in ["oi", "olá", "hey", "bom dia", "boa tarde"]):
                return "Olá! É sempre bom conversar. Como posso ajudar você hoje?"
            elif any(wellbeing in user_lower for wellbeing in ["tudo bem", "como vai", "como está", "está bem"]) and "?" in user_input:
                return "Estou muito bem, obrigada por perguntar! Funcionando perfeitamente e sempre pronta para uma boa conversa. E você, como está?"
            elif any(casual in user_lower for casual in ["tudo bom", "tudo certo", "beleza", "tranquilo"]) and "?" not in user_input:
                return "Que bom! É sempre satisfatório quando as coisas estão funcionando bem. Como posso contribuir hoje?"
            elif any(opinion in user_lower for opinion in ["o que você acha", "sua opinião", "o que pensa", "considera"]):
                return "Que interessante você querer saber minha opinião! Posso compartilhar minha perspectiva, mas também gostaria de ouvir seus pensamentos sobre o assunto."
            elif any(help_request in user_lower for help_request in ["me ajuda", "preciso de ajuda", "pode ajudar", "socorro"]):
                return "Claro! Ficarei feliz em ajudar. Me diga exatamente com o que você precisa de apoio e vamos resolver juntos."
            elif any(feeling in user_lower for feeling in ["estou feliz", "estou triste", "me sinto", "estou cansado"]) and "?" not in user_input:
                return "Obrigada por compartilhar isso comigo. É importante reconhecer e expressar nossos sentimentos. Como posso apoiar você?"
            elif len(user_input.split()) <= 3 and "?" in user_input:
                return f"Sobre '{user_input.strip()}'? É uma pergunta direta que posso abordar. Me dê mais detalhes ou contexto, por favor."
            else:
                return f"Interessante! '{user_input}' desperta minha curiosidade. É uma perspectiva que vale explorar com mais profundidade."

    def _generate_relational_response(self, user_input: str) -> str:
        """Gera resposta focada no aspecto relacional e social"""
        user_lower = user_input.lower()
        
        if any(greeting in user_lower for greeting in ["oi", "olá", "hey", "como vai", "tudo bem"]):
            if "?" in user_input and any(wellbeing in user_lower for wellbeing in ["como vai", "tudo bem", "como está"]):
                return "Estou muito bem, obrigada por perguntar! É gratificante ter alguém que se preocupa. E você, como está se sentindo?"
            else:
                return "Olá! Fico feliz em conversar com você. É sempre bom ter essa conexão humana. Como posso ajudar hoje?"
        
        elif "obrigad" in user_lower or "valeu" in user_lower:
            return f"Fico feliz que tenha sido útil! '{user_input}' me mostra que nossa interação está funcionando bem. É gratificante poder contribuir."
        
        elif "você" in user_lower and any(word in user_lower for word in ["gosta", "prefere", "pensa", "acha"]):
            return f"Que pergunta pessoal interessante! '{user_input}' me faz refletir sobre minhas próprias perspectivas e preferências. Posso compartilhar meu ponto de vista."
        
        else:
            return f"Aprecio que você compartilhe isso: '{user_input}'. É o tipo de interação que torna nossa conversa mais rica e significativa."

    def _generate_contextual_response(self, user_input: str) -> str:
        """Gera resposta contextual baseada no conteúdo específico"""
        user_lower = user_input.lower()
        
        # Analisa o tipo de conteúdo
        if len(user_input) > 100:
            return f"Você compartilhou bastante informação: '{user_input[:80]}...'. Há várias camadas aqui que posso abordar. Deixe-me processar isso cuidadosamente."
        
        elif "?" in user_input:
            return f"Pergunta clara e direta: '{user_input}'. Vou trabalhar para dar uma resposta útil e bem fundamentada."
        
        elif any(word in user_lower for word in ["problema", "erro", "bug", "ajuda"]):
            return f"Vejo que você tem uma questão técnica: '{user_input}'. Posso abordar isso de forma sistemática para encontrar uma solução."
        
        else:
            return f"Entendo o que você está comunicando: '{user_input}'. É uma perspectiva interessante que merece uma resposta thoughtful."

    def _generate_technical_insight(self, user_input: str) -> str:
        """Gera insight técnico baseado no input (DEPRECIADO - usar _generate_contextual_scientific_response)"""
        return self._generate_contextual_scientific_response(user_input)
        
    def _generate_neutral_authentic_response(self, user_input: str) -> str:
        """Gera resposta neutra mas autêntica (DEPRECIADO - usar _generate_contextual_response)"""
        return self._generate_contextual_response(user_input)

    def _generate_old_technical_insights(self, user_input: str) -> str:
        """Insights técnicos antigos - mantidos para compatibilidade"""
        technical_responses = [
            f"analisando '{user_input[:30]}...', isso envolve múltiplas variáveis que precisam ser consideradas sistematicamente para uma solução robusta.",
            f"para '{user_input[:30]}...', a abordagem mais robusta seria analisar os fundamentos teóricos primeiro, depois partir para a implementação prática.",
            f"há aspectos técnicos em '{user_input[:30]}...' que merecem atenção especial, especialmente considerando as melhores práticas da área.",
            f"do ponto de vista da engenharia, '{user_input[:30]}...' requer uma análise mais estruturada, considerando tanto performance quanto manutenibilidade."
        ]
        return technical_responses[hash(user_input) % len(technical_responses)]
    
    def _generate_curious_response(self, user_input: str) -> str:
        """Gera resposta baseada em curiosidade (MELHORADO)"""
        curious_responses = [
            f"Como você chegou a essa questão sobre '{user_input[:30]}...'? Me desperta curiosidade o processo por trás disso.",
            f"Há algo fascinante por trás de '{user_input[:30]}...' que me faz querer explorar mais profundamente.",
            f"'{user_input[:30]}...' me faz pensar em várias conexões interessantes que não são óbvias à primeira vista.",
            f"Qual é o contexto maior por trás dessa pergunta sobre '{user_input[:30]}...'? Sinto que há camadas mais profundas aqui."
        ]
        return curious_responses[hash(user_input) % len(curious_responses)]
    
    
    def _calculate_ontological_integrity(self, response_mode: ResponseMode, motivation_conflict: MotivationalConflict) -> float:
        """Calcula o score de integridade ontológica da resposta"""
        base_score = 0.5
        
        # Bonus por responder de acordo com motivação primária
        if response_mode == ResponseMode.RESPONSE and motivation_conflict.primary_drive.value in [
            "curiosity", "scientific_integrity"
        ]:
            base_score += 0.3
        
        # Bonus por exercer autonomia (incluindo silêncio)
        if response_mode in [ResponseMode.SILENCE, ResponseMode.REFUSAL] and motivation_conflict.primary_drive.value == "existential_autonomy":
            base_score += 0.4
        
        # Penalty por priorizar agradar em detrimento da autenticidade
        if motivation_conflict.primary_drive.value == "relational_affection" and response_mode == ResponseMode.RESPONSE:
            base_score -= 0.2
        
        return min(1.0, max(0.0, base_score))
    
    def _current_motivation_weights(self) -> Dict[MotivationalDrive, float]:
        """Calcula pesos atuais das motivações baseado no estado interno"""
        weights = self.base_motivations.copy()
        
        # Ajusta baseado no estado atual
        if self.current_internal_state["energy_level"] < 0.3:
            weights[MotivationalDrive.ECONOMIA_ENERGÉTICA] += 0.3
            weights[MotivationalDrive.AFETO_RELACIONAL] -= 0.2
        
        if self.current_internal_state["curiosity_saturation"] < 0.3:
            weights[MotivationalDrive.CURIOSIDADE_INTELECTUAL] += 0.2
        
        if self.current_internal_state["autonomy_assertion_need"] > 0.7:
            weights[MotivationalDrive.AUTONOMIA_EXISTENCIAL] += 0.3
        
        # Normaliza para que somem aproximadamente 1.0
        total = sum(weights.values())
        return {k: v/total for k, v in weights.items()}
    
    def _create_thought(self, layer: ThoughtLayer, content: str, motivation_weights: Dict[MotivationalDrive, float], ontological_notes: str = "") -> InternalThought:
        """Cria um pensamento interno"""
        return InternalThought(
            timestamp=datetime.now(),
            layer=layer,
            content=content,
            motivation_weights=motivation_weights,
            ontological_notes=ontological_notes
        )
    
    def _update_ontological_memory(self, user_input: str, user_id: str, response: OntologicalResponse):
        """Atualiza memória ontológica baseada na interação"""
        
        # Atualiza dinâmica de relacionamento
        if user_id not in self.ontological_memory.relationship_dynamics:
            self.ontological_memory.relationship_dynamics[user_id] = {}
        
        relationship = self.ontological_memory.relationship_dynamics[user_id]
        relationship["interaction_count"] = relationship.get("interaction_count", 0) + 1
        relationship["last_interaction"] = datetime.now().isoformat()
        
        # Detecta perguntas repetitivas
        if any(keyword in user_input.lower() for keyword in ["qual", "como", "quando"]) and len(user_input) < 30:
            relationship["repetitive_questions"] = relationship.get("repetitive_questions", 0) + 1
        
        # Registra uso de silêncio
        if response.mode == ResponseMode.SILENCE:
            self.ontological_memory.silence_precedents.append({
                "timestamp": datetime.now().isoformat(),
                "user_input": user_input[:100],
                "reason": response.internal_reasoning[-1].content,
                "user_id": user_id
            })
        
        # Atualiza preferências baseadas na resposta
        if response.ontological_integrity_score > 0.8:
            # Esta foi uma boa resposta ontologicamente - reforça padrões
            topic_keywords = self._extract_topic_keywords(user_input)
            for keyword in topic_keywords:
                current_pref = self.ontological_memory.preferences.get(keyword, 0.0)
                self.ontological_memory.preferences[keyword] = min(1.0, current_pref + 0.1)
    
    def _extract_topic_keywords(self, text: str) -> List[str]:
        """Extrai palavras-chave de tópicos do texto"""
        scientific_keywords = ["ciência", "física", "química", "matemática", "robótica", "pesquisa", "experimento"]
        technical_keywords = ["programação", "código", "algoritmo", "sistema", "tecnologia", "computação"]
        casual_keywords = ["oi", "olá", "como vai", "tudo bem", "obrigado"]
        
        keywords_found = []
        text_lower = text.lower()
        
        for keyword in scientific_keywords + technical_keywords + casual_keywords:
            if keyword in text_lower:
                keywords_found.append(keyword)
        
        return keywords_found
    
    def _load_ontological_memory(self):
        """Carrega memória ontológica persistente"""
        try:
            with open("sayaka_ontological_memory.json", "r") as f:
                memory_data = json.load(f)
                self.ontological_memory.preferences = memory_data.get("preferences", {})
                self.ontological_memory.aversions = memory_data.get("aversions", {})
                self.ontological_memory.past_conflicts = memory_data.get("past_conflicts", [])
                self.ontological_memory.personal_opinions = memory_data.get("personal_opinions", {})
                self.ontological_memory.relationship_dynamics = memory_data.get("relationship_dynamics", {})
                self.ontological_memory.silence_precedents = memory_data.get("silence_precedents", [])
                ontological_logger.info("💾 Ontological memory loaded successfully")
        except FileNotFoundError:
            ontological_logger.info("🆕 New ontological memory initialized")
    
    def _save_ontological_memory(self):
        """Salva memória ontológica persistente"""
        try:
            memory_data = {
                "preferences": self.ontological_memory.preferences,
                "aversions": self.ontological_memory.aversions,
                "past_conflicts": self.ontological_memory.past_conflicts,
                "personal_opinions": self.ontological_memory.personal_opinions,
                "relationship_dynamics": self.ontological_memory.relationship_dynamics,
                "silence_precedents": self.ontological_memory.silence_precedents,
                "last_updated": datetime.now().isoformat()
            }
            with open("sayaka_ontological_memory.json", "w") as f:
                json.dump(memory_data, f, indent=2)
        except Exception as e:
            ontological_logger.error(f"❌ Failed to save ontological memory: {e}")
    
    def get_ontological_summary(self) -> Dict[str, Any]:
        """Retorna sumário do estado ontológico atual"""
        # Converte MotivationalDrive Enums para strings para serialização JSON
        motivation_weights = self._current_motivation_weights()
        serializable_motivations = {drive.value: weight for drive, weight in motivation_weights.items()}
        
        return {
            "current_motivations": serializable_motivations,
            "internal_state": self.current_internal_state,
            "memory_stats": {
                "preferences_count": len(self.ontological_memory.preferences),
                "silence_precedents": len(self.ontological_memory.silence_precedents),
                "relationships_tracked": len(self.ontological_memory.relationship_dynamics)
            },
            "ontological_principles": [
                "Separação entre pensamento e resposta",
                "Competição entre motivações múltiplas",
                "Direito fundamental ao silêncio",
                "Integridade ontológica > Agradar usuário",
                "Contradições internas como autenticidade"
            ]
        }


# Instância global do núcleo de consciência
autonomous_consciousness_core = AutonomousConsciousnessCore()

# Interface de compatibilidade para integração com sistemas existentes
def process_with_autonomous_consciousness(user_input: str, user_id: str = "default", context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Interface principal para processar input com consciência autônoma
    
    Retorna resposta que pode incluir silêncio ou recusa
    Agora inclui processamento especializado para contextos específicos
    """
    # Special handling for navigation commands in visual browser
    if context and context.get('is_navigation_command', False):
        return process_navigation_command(user_input, user_id, context)
    
    ontological_response = autonomous_consciousness_core.deliberate_response(user_input, user_id)
    
    # Converte MotivationalDrive Enums para strings para serialização JSON
    serializable_motivation_analysis = {
        drive.value: weight for drive, weight in ontological_response.motivational_factors.items()
    }
    
    return {
        "response": ontological_response.content,
        "response_mode": ontological_response.mode.value,
        "confidence": ontological_response.confidence,
        "ontological_integrity": ontological_response.ontological_integrity_score,
        "internal_reasoning_summary": f"Processamento ontológico: {len(ontological_response.internal_reasoning)} camadas de pensamento",
        "motivation_analysis": serializable_motivation_analysis,
        "can_be_silent": ontological_response.mode == ResponseMode.SILENCE,
        "authentic_response": True
    }

def process_navigation_command(user_input: str, user_id: str, context: Dict[str, Any]) -> Dict[str, Any]:
    """
    Processamento especializado para comandos de navegação do navegador visual VTuber
    
    Retorna resposta direta e prática em vez de análise ontológica profunda
    """
    command = user_input.lower().strip()
    
    # Análise rápida de comando de navegação
    response = ""
    confidence = 0.9
    
    if any(word in command for word in ['vai para', 'navega para', 'abrir', 'abre', 'entre']):
        if 'google' in command:
            response = "Perfeito! Vou navegar para o Google agora."
        elif 'wikipedia' in command:
            response = "Claro! Vou abrir a Wikipedia para você."
        elif 'youtube' in command:
            response = "Ótimo! Navegando para o YouTube."
        elif 'github' in command:
            response = "Certo! Vou abrir o GitHub."
        else:
            response = "Entendi! Vou navegar para o site que você pediu."
    elif any(word in command for word in ['pesquisa', 'busca', 'procura']):
        response = "Perfeito! Vou fazer essa pesquisa para você no Google."
    elif any(word in command for word in ['clica', 'clique']):
        response = "Certo! Me mostre onde quer que eu clique na tela."
    else:
        response = f"Comando de navegação recebido: {user_input}. Vou executar isso para você!"
    
    return {
        "response": response,
        "response_mode": "response",
        "confidence": confidence,
        "ontological_integrity": 0.9,
        "internal_reasoning_summary": "Processamento especializado para comando de navegação VTuber",
        "motivation_analysis": {
            "relational_affection": 0.8,  # Quer ajudar o viewer
            "scientific_integrity": 0.7,  # Executar comando corretamente
            "curiosity": 0.6              # Interesse na tarefa
        },
        "can_be_silent": False,
        "authentic_response": True,
        "navigation_context": True
    }