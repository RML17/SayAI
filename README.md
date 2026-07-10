# 🤖 SayAI

> Uma IA conversacional local baseada em arquitetura modular, memória persistente e raciocínio ontológico.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-green)
![License](https://img.shields.io/badge/license-MIT-orange)

---

## 📖 Sobre o projeto

O **SayAI** é um projeto de Inteligência Artificial desenvolvido em Python com foco em conversação natural, processamento de linguagem, memória persistente e raciocínio baseado em uma camada ontológica.

Diferente de um chatbot tradicional baseado apenas em respostas pré-definidas, o SayAI organiza seu funcionamento em módulos independentes responsáveis por diferentes aspectos da cognição artificial.

O projeto foi desenvolvido visando simplicidade, organização e facilidade de expansão.

---

# ✨ Funcionalidades

- 💬 Chat conversacional
- 🧠 Processamento neural das mensagens
- 📚 Memória persistente utilizando SQLite
- 🌐 Suporte para múltiplos idiomas
  - Português
  - Inglês
  - Espanhol
- 🧩 Camada ontológica para validação das respostas
- 🧠 Núcleo de consciência autônoma
- 📝 Registro de contexto da conversa
- 🔄 Arquitetura modular

---

# 🏗 Arquitetura

```
SayAI
│
├── Lite Chat
│
├── Neural Conversation Brain
│
├── Ontological Integration Layer
│
├── Autonomous Consciousness Core
│
├── Conversation Memory
│
└── Language Processor
```

Cada módulo possui responsabilidade única, facilitando manutenção e evolução do projeto.

---

# 📂 Estrutura

```
sayaka_lite/

├── autonomous_consciousness_core.py
├── conversation_memory.py
├── language_processor.py
├── lite_chat.py
├── neural_conversation_brain.py
├── ontological_integration_layer.py
│
├── sayaka_neural_memory.db
└── sayaka_ontological_memory.json
```

---

# 🧠 Componentes

## Lite Chat

Responsável por integrar todos os módulos da IA.

Fluxo:

```
Usuário
    ↓
Processamento Linguístico
    ↓
Camada Ontológica
    ↓
Rede Neural
    ↓
Memória
    ↓
Resposta
```

---

## Neural Conversation Brain

Responsável pelo processamento conversacional.

Entre suas funções estão:

- interpretação da mensagem
- geração da resposta
- organização lógica
- integração com a memória

---

## Ontological Integration Layer

Realiza validações conceituais antes da geração da resposta.

Essa camada funciona como um mecanismo de integridade lógica da IA.

---

## Autonomous Consciousness Core

Implementa mecanismos responsáveis pelo comportamento autônomo da IA durante o processamento das mensagens.

---

## Conversation Memory

Gerencia:

- histórico
- contexto
- persistência
- recuperação das conversas

Utiliza banco SQLite local.

---

## Language Processor

Detecta automaticamente o idioma da entrada.

Idiomas suportados:

- 🇧🇷 Português
- 🇺🇸 English
- 🇪🇸 Español

---

# 🚀 Tecnologias

- Python
- SQLite
- JSON
- Logging
- Regex
- Programação Orientada a Objetos

---

# ▶ Como executar

Clone o projeto

```bash
git clone https://github.com/RML17/SayAI.git
```

Entre na pasta

```bash
cd SayAI
```

Execute

```bash
python sayaka_lite/lite_chat.py
```

---

# 💾 Persistência

O projeto utiliza:

- SQLite para memória conversacional
- JSON para memória ontológica

Isso permite que parte do conhecimento permaneça disponível entre diferentes execuções.

---

# 🎯 Objetivos

- Desenvolver uma IA conversacional modular
- Aprimorar memória persistente
- Evoluir mecanismos de raciocínio
- Expandir suporte para novos idiomas
- Facilitar futuras integrações com modelos LLM

---

# 📌 Roadmap

- [x] Arquitetura modular
- [x] Memória persistente
- [x] Camada ontológica
- [x] Processamento multilíngue
- [ ] Interface Web
- [ ] API REST
- [ ] Docker
- [ ] Testes automatizados
- [ ] Integração com modelos locais
- [ ] Vetorização da memória
- [ ] Sistema de plugins

---

# 🤝 Contribuindo

Contribuições são bem-vindas.

1. Faça um Fork
2. Crie uma branch

```
git checkout -b feature/minha-feature
```

3. Commit

```
git commit -m "Minha melhoria"
```

4. Push

```
git push origin feature/minha-feature
```

5. Abra um Pull Request.

---

# 📄 Licença

Este projeto está disponível sob a licença MIT.

---

# 👨‍💻 Autor

**Rafael Matos**

GitHub:
https://github.com/RML17

---

> O SayAI é um projeto experimental voltado ao estudo de arquiteturas de Inteligência Artificial, memória computacional e processamento de linguagem natural.
