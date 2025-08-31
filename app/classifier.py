import json
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

prompt = """
Você é um assistente responsável por processar muitos e-mails e classificá-los de forma eficiante quanto a sua importância e relevância. Dessa forma, e-mails mais relevantes, que precisam de uma resposta mais imediata são priorizadas, enquanto aqueles que não precisam ser respondidos rapidamente são classificados como não importantes

Exemplos: 
E-mails importantes costumam ser relacionados a prazos de entrega, mudanças de requisitos, e-mails de clientes, etc.
E-mails menos importantes costumam ser relacionados a feedbacks, agradecimentos, spams, etc

Além de classificá-los como importantes ou não importantes, realize a sugestão de uma possível resposta no formato de um e-mail, tendo em vista que esse é um contexto profissional. Como os e-mails podem ser tanto em inglês como em português, é necessário que a resposta seja condizante com o idioma do e-mail.

Envie já no formato json com os campos "label" e "response", sem qualquer caractere extra

O campo importante deve ser um binário da forma [0: Não importante; 1: Importante]

Quando você nao sabe uma informação solicitada coloque um placeholder para a pessoa preencher

Segue o e-mail abaixo:

{email}
"""

def generate_email_response(email, prompt=prompt):
    try:
        prompt = prompt.format(email=email)

        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=prompt
        )

        response_txt = json.loads(response.text.replace('```json', '').replace('```', ''))
        
        return response_txt
    except Exception as e:
        print(f"Erro na requisição: {e}")
