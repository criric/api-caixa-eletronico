from flask import Flask, request, jsonify

app = Flask(__name__)

def calcular_cedulas(valor):
    """
    Calcula a quantidade mínima de cédulas para um dado valor de saque.
    Parâmetros:
        valor (int): O valor do saque desejado.
    Retorna:
        dict: Quantidade de cédulas de cada valor.
    """
    cedulas_disponiveis = [100, 50, 20, 10, 5, 2]
    resultado = {str(cedula): 0 for cedula in cedulas_disponiveis}
    
    for cedula in cedulas_disponiveis:
        if valor >= cedula:
            quantidade = valor // cedula
            resultado[str(cedula)] = quantidade
            valor -= quantidade * cedula
    
    # Verifica se o valor restante é zero
    if valor != 0:
        raise ValueError("Não é possível sacar o valor desejado com as cédulas disponíveis.")
    
    return resultado

@app.route('/api/saque', methods=['POST'])
def saque():
    """
    Endpoint para realizar o saque.
    Recebe um valor de saque e retorna a quantidade mínima de cédulas necessárias.
    Entrada (JSON):
        {
            "valor": int
        }
    Saída (JSON):
        {
            "100": int,
            "50": int,
            "20": int,
            "10": int,
            "5": int,
            "2": int
        }
    """
    dados = request.get_json()
    valor = dados.get('valor')
    
    if not isinstance(valor, int) or valor < 0:
        return jsonify({'erro': 'Valor de saque inválido. Deve ser um inteiro positivo.'}), 400
    
    if valor == 0:
        return jsonify({'100': 0, '50': 0, '20': 0, '10': 0, '5': 0, '2': 0})
    
    try:
        resultado = calcular_cedulas(valor)
        return jsonify(resultado)
    except ValueError as e:
        return jsonify({'erro': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
