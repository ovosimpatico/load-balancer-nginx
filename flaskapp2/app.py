from flask import Flask, jsonify

app = Flask(__name__)

TAXA_DOLAR = 5.10
TAXA_EURO = 5.60

@app.route('/convertepradolareuro/<float:valor>', methods=['GET'])
def convertepradolareuro(valor):
    valor_dolar = valor / TAXA_DOLAR
    valor_euro = valor / TAXA_EURO
    resposta = {
        "conversao": {
            "real": valor,
            "dolar": valor_dolar,
            "euro": valor_euro
        }
    }
    return jsonify(resposta)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
