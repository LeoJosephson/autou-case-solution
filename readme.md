# **Case - AutoU**

Em um ambiente corporativo, onde funcionários recebem dezenas de e-mails diariamente, é fundamental contar com uma ferramenta capaz de identificar e priorizar as mensagens mais relevantes.

Este projeto implementa uma aplicação web que permite ao usuário inserir o conteúdo de um e-mail (digitando ou enviando um arquivo) e obter:

- **Uma sugestão automática de resposta.**

- **A classificação do e-mail como produtivo (importante) ou improdutivo (não importante).**



## 📂 Estrutura do Projeto
```
root/
│
├── app/ # Aplicação Flask
│ ├── static/ # CSS e JS
│ ├── templates/ # HTML
│ ├── app.py # Rotas Flask
│ └── classifier.py # Lógica de classificação
│
├── requirements.txt # Dependências Python
├── vercel.json # Configuração do deploy
└── README.md

```

# Instalação local

Passo a passo de como instalar o projeto localmente no Windows.

1. Clone esse projeto

    ``git clone https://github.com/LeoJosephson/autou-case-solution.git``

    ``cd autou-case-solution``

2. Crie e ative um ambiente virtual para não instalar as dependências globalmente

    `` Python -m venv .venv``

     `` .\.venv\Scripts/activate ``

3. Instale as dependências

    `` pip install -r requirements.txt ``

4. Crie um arquivo .env na raiz do projeto e defina-o da seguinte forma. Utilize o .env.example como base

| Nome               | Exemplo              | 
| ------------------ | ------------------   |
| FLASK_APP          | ./app/app.py         |
| GEMINI_API_KEY     | Sua chave do Gemini  | 

Para gerar sua chave API do Gemini: https://aistudio.google.com/apikey

# Execução do projeto

1. Para executar a aplicação

    `` flask run ``