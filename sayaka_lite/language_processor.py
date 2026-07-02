"""
Language Detection and Translation Module for Sayaka AI
Supports Portuguese, English, and Spanish
"""

import re
import logging
from typing import Dict, List, Tuple, Optional


class LanguageProcessor:
    """Language detection and translation processor for multi-language support"""
    
    def __init__(self):
        self.setup_language_data()
        
    def setup_language_data(self):
        """Initialize language detection patterns and translation dictionaries"""
        
        # Language detection patterns
        self.language_patterns = {
            'pt': {
                'keywords': [
                    'o', 'que', 'é', 'um', 'uma', 'de', 'da', 'do', 'na', 'no', 'para', 'por',
                    'com', 'como', 'sobre', 'isso', 'este', 'esta', 'esse', 'essa', 'qual', 'quais',
                    'onde', 'quando', 'porque', 'por que', 'quem', 'você', 'me', 'explique', 'diga',
                    'ajude', 'preciso', 'quero', 'posso', 'deve', 'tem', 'há', 'são', 'está', 'foi'
                ],
                'patterns': [
                    r'\bo que é\b', r'\bcomo funciona\b', r'\bpor que\b', r'\bvocê sabe\b',
                    r'\bme ajude\b', r'\bquero saber\b', r'\bpreciso de\b'
                ]
            },
            'en': {
                'keywords': [
                    'the', 'what', 'is', 'a', 'an', 'of', 'in', 'to', 'for', 'with', 'how', 'about',
                    'this', 'that', 'which', 'where', 'when', 'why', 'who', 'you', 'me', 'explain',
                    'tell', 'help', 'need', 'want', 'can', 'should', 'have', 'there', 'are', 'was'
                ],
                'patterns': [
                    r'\bwhat is\b', r'\bhow does\b', r'\bwhy do\b', r'\bdo you know\b',
                    r'\bhelp me\b', r'\bi want to know\b', r'\bi need\b'
                ]
            },
            'es': {
                'keywords': [
                    'el', 'la', 'que', 'es', 'un', 'una', 'de', 'del', 'en', 'para', 'por',
                    'con', 'como', 'sobre', 'esto', 'este', 'esta', 'cual', 'cuales',
                    'donde', 'cuando', 'porque', 'por qué', 'quien', 'tú', 'me', 'explica', 'dime',
                    'ayuda', 'necesito', 'quiero', 'puedo', 'debe', 'tiene', 'hay', 'son', 'está', 'fue'
                ],
                'patterns': [
                    r'\bqué es\b', r'\bcómo funciona\b', r'\bpor qué\b', r'\bsabes\b',
                    r'\bayúdame\b', r'\bquiero saber\b', r'\bnecesito\b'
                ]
            }
        }
        
        # Common technical terms translations
        self.technical_translations = {
            'database': {
                'pt': 'banco de dados',
                'en': 'database',
                'es': 'base de datos'
            },
            'system': {
                'pt': 'sistema',
                'en': 'system', 
                'es': 'sistema'
            },
            'management': {
                'pt': 'gerenciamento',
                'en': 'management',
                'es': 'gestión'
            },
            'function': {
                'pt': 'função',
                'en': 'function',
                'es': 'función'
            },
            'code': {
                'pt': 'código',
                'en': 'code',
                'es': 'código'
            },
            'error': {
                'pt': 'erro',
                'en': 'error',
                'es': 'error'
            },
            'implementation': {
                'pt': 'implementação',
                'en': 'implementation',
                'es': 'implementación'
            },
            'details': {
                'pt': 'detalhes',
                'en': 'details',
                'es': 'detalles'
            },
            'environment': {
                'pt': 'ambiente',
                'en': 'environment',
                'es': 'entorno'
            }
        }
        
        # Response templates by language
        self.response_templates = {
            'pt': {
                'thinking_intro': "Deixe-me pensar sobre isso para você?",
                'based_on_knowledge': "Com base no que sei sobre",
                'let_me_be_specific': "Deixe-me ser mais específica sobre",
                'here_what_you_should_do': "Aqui está o que você deve fazer",
                'review_and_test': "revise o código e teste em seu ambiente",
                'explanation_intro': "Posso explicar isso para você:",
                'technical_term': "termo técnico",
                'advantages': "vantagens",
                'disadvantages': "desvantagens",
                'example': "exemplo",
                'conclusion': "conclusão"
            },
            'en': {
                'thinking_intro': "Let me think about this for you?",
                'based_on_knowledge': "Based on what I know about",
                'let_me_be_specific': "Let me be more specific about",
                'here_what_you_should_do': "Here's what you should do",
                'review_and_test': "review the code and test it in your environment",
                'explanation_intro': "I can explain this for you:",
                'technical_term': "technical term",
                'advantages': "advantages",
                'disadvantages': "disadvantages",
                'example': "example",
                'conclusion': "conclusion"
            },
            'es': {
                'thinking_intro': "¿Déjame pensar en esto por ti?",
                'based_on_knowledge': "Basándome en lo que sé sobre",
                'let_me_be_specific': "Déjame ser más específica sobre",
                'here_what_you_should_do': "Esto es lo que debes hacer",
                'review_and_test': "revisa el código y pruébalo en tu entorno",
                'explanation_intro': "Puedo explicarte esto:",
                'technical_term': "término técnico",
                'advantages': "ventajas",
                'disadvantages': "desventajas",
                'example': "ejemplo",
                'conclusion': "conclusión"
            }
        }
    
    def detect_language(self, text: str) -> str:
        """Detect the language of input text with smart fallbacks"""
        if not text or not text.strip():
            return 'pt'  # Default to Portuguese for Brazilian users
            
        text_lower = text.lower()
        scores = {'pt': 0, 'en': 0, 'es': 0}
        
        # Strong Portuguese indicators get extra weight
        strong_pt_indicators = ['você', 'quem é', 'quanto é', 'cante', 'me fale', 'caraca', 'criador']
        for indicator in strong_pt_indicators:
            if indicator in text_lower:
                scores['pt'] += 5
        
        # Strong English indicators  
        strong_en_indicators = ['hello', 'what is', 'how are you', 'tell me about', 'can you', 'speak in english', 'do you', 'i want to', 'please tell me']
        for indicator in strong_en_indicators:
            if indicator in text_lower:
                scores['en'] += 10  # Higher weight for clear English
                
        # Strong Spanish indicators
        strong_es_indicators = ['qué es', 'cómo estás', 'háblame de']
        for indicator in strong_es_indicators:
            if indicator in text_lower:
                scores['es'] += 5
        
        # Score based on keyword frequency
        for lang, data in self.language_patterns.items():
            for keyword in data['keywords']:
                if keyword in text_lower:
                    scores[lang] += 1
            
            # Score based on pattern matching
            for pattern in data['patterns']:
                if re.search(pattern, text_lower):
                    scores[lang] += 3  # Patterns get higher weight
        
        # Log scores for debugging
        logging.info(f"LANGUAGE DETECTION SCORES for '{text}': {scores}")
        
        # Check for clear winners
        max_score = max(scores.values())
        if max_score == 0:
            logging.info("No language indicators found, defaulting to Portuguese")
            return 'pt'  # Default to Portuguese for Brazilian context
            
        # Only prefer Portuguese if there's a real tie (same score)
        # Otherwise, respect the highest scoring language
        winners = [lang for lang, score in scores.items() if score == max_score]
        detected = None
        if len(winners) == 1:
            detected = winners[0]  # Clear winner
        elif 'pt' in winners:
            detected = 'pt'  # Tie-breaker for Portuguese
        else:
            detected = max(scores.keys(), key=lambda k: scores[k])
        
        logging.info(f"DETECTED LANGUAGE: {detected} (winners: {winners})")
        return detected
    
    def translate_response(self, response: str, target_language: str) -> str:
        """Translate response to target language"""
        if target_language not in ['pt', 'en', 'es']:
            return response
            
        translated = response
        
        # Replace common English phrases with target language equivalents
        english_phrases = {
            "Let me guess, you want me to do the thinking for you?": {
                'pt': "Deixe-me adivinhar, você quer que eu faça o raciocínio por você?",
                'en': "Let me guess, you want me to do the thinking for you?",
                'es': "Déjame adivinar, ¿quieres que haga el razonamiento por ti?"
            },
            "Based on what I know about": {
                'pt': "Com base no que sei sobre",
                'en': "Based on what I know about", 
                'es': "Basándome en lo que sé sobre"
            },


            "in your environment": {
                'pt': "em seu ambiente",
                'en': "in your environment", 
                'es': "en tu entorno"
            },
            "You know what": {
                'pt': "Você sabe o que",
                'en': "You know what",
                'es': "Sabes qué"
            },
            "already know that": {
                'pt': "já sabe que",
                'en': "already know that",
                'es': "ya sabes que"
            },
            "we can advance": {
                'pt': "podemos avançar",
                'en': "we can advance",
                'es': "podemos avanzar"
            },
            "main advantages": {
                'pt': "principais vantagens",
                'en': "main advantages", 
                'es': "principales ventajas"
            },
            "that qualify": {
                'pt': "que qualificam",
                'en': "that qualify",
                'es': "que califican"
            },
            "decision making": {
                'pt': "tomada de decisão",
                'en': "decision making",
                'es': "toma de decisiones"
            }
        }
        
        # Replace exact phrase matches
        for english_phrase, translations in english_phrases.items():
            if english_phrase in translated:
                translated = translated.replace(english_phrase, translations[target_language])
        
        # Replace technical terms
        for english_term, translations in self.technical_translations.items():
            # Match whole words only
            pattern = r'\b' + re.escape(english_term) + r'\b'
            if re.search(pattern, translated, re.IGNORECASE):
                translated = re.sub(pattern, translations[target_language], translated, flags=re.IGNORECASE)
        
        return translated
    
    def format_response_for_language(self, response: str, user_input: str) -> str:
        """Format response according to detected language"""
        detected_language = self.detect_language(user_input)
        
        # Translate the response
        formatted_response = self.translate_response(response, detected_language)
        
        return formatted_response
    
    def get_template(self, template_key: str, language: str) -> str:
        """Get a response template for a specific language"""
        if language not in self.response_templates:
            language = 'en'  # Fallback to English
            
        return self.response_templates[language].get(template_key, template_key)
    
    def is_mixed_language(self, text: str) -> bool:
        """Check if text contains mixed languages"""
        detected_lang = self.detect_language(text)
        
        # Check for common mixed language patterns
        mixed_patterns = [
            (r'\b(Let me|Here\'s what|Based on)\b.*\b(você|sobre|que)\b', 'en_pt'),
            (r'\b(o que|como|sobre)\b.*\b(you|what|implementation)\b', 'pt_en'),
            (r'\b(qué es|cómo|sobre)\b.*\b(you|what|implementation)\b', 'es_en')
        ]
        
        for pattern, mix_type in mixed_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                return True
                
        return False
    
    def clean_mixed_language_response(self, response: str, user_language: str) -> str:
        """Clean and standardize mixed language responses"""
        if not self.is_mixed_language(response):
            return response
            
        # Apply language-specific cleaning
        cleaned = self.translate_response(response, user_language)
        
        return cleaned
