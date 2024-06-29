from flask import Flask, request, jsonify

app = Flask(__name__)

def calcular_cedulas(valor):
    cedulas_disponiveis = [100, 50, 20, 10, 5, 2]
    resultado = {str(cedula): 0 for cedula in cedulas_disponiveis}
    
    for cedula in cedulas_disponiveis:
        if valor >= cedula:
            quantidade = valor // cedula
            resultado[str(cedula)] = quantidade
            valor -= quantidade * cedula
    
    return resultado

@app.route('/api/saque', methods=['POST'])
def saque():
    dados = request.get_json()
    valor = dados.get('valor')
    
    if not isinstance(valor, int) or valor <= 0:
        return jsonify({'erro': 'Valor de saque inválido. Deve ser um inteiro positivo.'}), 400
    
    resultado = calcular_cedulas(valor)
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)
