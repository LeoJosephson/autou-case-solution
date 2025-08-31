from flask import Flask, request, jsonify, render_template
from pypdf import PdfReader
from .classifier import generate_email_response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    text = request.form.get("text", "").strip()
    file = request.files.get("file")

    content = ''

    if text and file:
        return jsonify({"error": "escolha apenas TEXTO ou ARQUIVO, não os dois."}), 400

    if not text and not file:
        return jsonify({"error": "você precisa escrever algo ou enviar um arquivo."}), 400

    # Caso texto
    if text:
        content = text
    else:  
        if not file or not file.filename:
            return jsonify({"error": "Nenhum arquivo recebido."}), 400

        
        # Caso arquivo
        if  file.filename.endswith(".txt"):
            try:
                    content = file.read().decode("utf-8", errors="replace")
            except Exception:
                    return jsonify({"error": "Falha ao ler o arquivo .txt."}), 400
        elif file.filename.endswith(".pdf"):
            content = ''
            try:
                reader = PdfReader(file)
                for page in reader.pages:
                    extracted = page.extract_text()
                    if extracted:
                        content += extracted
                if not content.strip():
                    return jsonify({"error": "Não foi possível extrair texto do PDF."}), 400
            except Exception:
                return jsonify({"error": "PDF inválido ou corrompido."}), 400
        else:
            return jsonify({"error": "Arquivo não suportado. Envie .txt ou .pdf."}), 415
    

    response = generate_email_response(content)
    generated_reply = response["response"]
    label = response["label"]
    return jsonify({"reply": generated_reply,
                    "label": label})


if __name__ == "__main__":
    app.run(debug=True)