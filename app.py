# API - É um lugar para disponibilizar recursos e/ou funcionalidades
# 1. Objetivo - Criar uma api que disponibiliza a consulta, criação, edição e exclusão de livros.
# 2. URL base - localhost
# 3. Endpoints - 
'''- localhost/livros (GET)
    - localhost/livros/id (GET)
    - localhost/livros (POST)
    - localhost/livro/id (PUT)
    - localhost/livro/id (DELETE)'''
# 4. Quais recursos - Livros

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'Pai Rico, Pai Pobre',
        'autor': 'Robert T. Kiyosaki',
        'editora': 'Alta Books',
        'numero-paginas': 336,
        'preco': 49.05,
        'data-publicacao': '2018-09-05'
    },
    {
        'id': 2,
        'título': 'Do Mil ao Milhão. Sem Cortar o Cafezinho.',
        'autor': 'Thiago Nigro',
        'editora': 'HarperCollins',
        'numero-paginas': 192,
        'preco': 24.99,
        'data-publicacao': '2018-11-10'
    },
    {
        'id': 3,
        'título': 'O homem mais rico da Babilônia: com prefácio de Thiago Nigro',
        'autor': 'George S. Clason',
        'editora': 'HarperCollins',
        'numero-paginas': 176,
        'preco': 22.40,
        'data-publicacao': '2021-06-15'
    }
]

# Consultar (todos)
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# Consultar (id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

# Criar
@app.route('/livros', methods=['POST'])
def cadastrar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)
        
# Editar
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

# Excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)

# Inicializar a aplicação
app.run(port=5000, host='localhost', debug=True)