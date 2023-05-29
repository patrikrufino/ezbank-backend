from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/admin', methods=['POST'])
def create_admin():
    data = request.get_json()
    admin = Admin(nome=data['nome'], senha=data['senha'])
    db.session.add(admin)
    db.session.commit()
    return jsonify({'message': 'Admin criado com sucesso!'})

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    output = []
    for user in users:
        user_data = {
            'id': user.id,
            'nome': user.nome,
            'senha': user.senha,
            'conta': user.conta.numero
        }
        output.append(user_data)
    return jsonify({'users': output})

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(nome=data['nome'], senha=data['senha'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User criado com sucesso!'})

@app.route('/contas', methods=['GET'])
def get_contas():
    contas = Conta.query.all()
    output = []
    for conta in contas:
        conta_data = {
            'id': conta.id,
            'numero': conta.numero,
            'saldo': conta.saldo,
            'limite': conta.limite
        }
        output.append(conta_data)
    return jsonify({'contas': output})

@app.route('/contas/<int:conta_id>/sacar', methods=['POST'])
def sacar(conta_id):
    data = request.get_json()
    valor_saque = data['valor']

    conta = Conta.query.get(conta_id)

    if not conta:
        return jsonify({'message': 'Conta não encontrada!'}), 404

    saldo_atual = conta.saldo

    if valor_saque > saldo_atual:
        return jsonify({'message': 'Saldo insuficiente!'}), 400

    saldo_atual -= valor_saque
    conta.saldo = saldo_atual
    db.session.commit()

    return jsonify({'message': 'Saque realizado com sucesso!'})

@app.route('/contas/<int:conta_id>/depositar', methods=['POST'])
def depositar(conta_id):
    data = request.get_json()
    valor_deposito = data['valor']

    conta = Conta.query.get(conta_id)

    if not conta:
        return jsonify({'message': 'Conta não encontrada!'}), 404

    saldo_atual = conta.saldo

    saldo_atual += valor_deposito
    conta.saldo = saldo_atual
    db.session.commit()

    return jsonify({'message': 'Depósito realizado com sucesso!'})

@app.route('/contas/<int:conta_origem_id>/transferir/<int:conta_destino_id>', methods=['POST'])
def transferir(conta_origem_id, conta_destino_id):
    data = request.get_json()
    valor_transferencia = data['valor']

    conta_origem = Conta.query.get(conta_origem_id)
    conta_destino = Conta.query.get(conta_destino_id)

    if not conta_origem or not conta_destino:
        return jsonify({'message': 'Conta de origem ou destino não encontrada!'}), 404

    saldo_origem = conta_origem.saldo
    saldo_destino = conta_destino.saldo

    if valor_transferencia > saldo_origem:
        return jsonify({'message': 'Saldo insuficiente para a transferência!'}), 400

    saldo_origem -= valor_transferencia
    saldo_destino += valor_transferencia

    conta_origem.saldo = saldo_origem
    conta_destino.saldo = saldo_destino

    db.session.commit()

    return jsonify({'message': 'Transferência realizada com sucesso!'})

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bank.db'
db = SQLAlchemy(app)

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    senha = db.Column(db.String(100))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    senha = db.Column(db.String(100))
    conta_id = db.Column(db.Integer, db.ForeignKey('conta.id'))

class Conta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(20))
    saldo = db.Column(db.Float)
    limite = db.Column(db.Float)

@app.route('/')
def hello():
    return 'API do Banco'

with app.app_context():
    db.create_all()


@app.route('/populardb', methods=['POST'])
def popular_db():
    contas = [
        {'numero': '123456', 'saldo': 1000.0, 'limite': 5000.0},
        {'numero': '234567', 'saldo': 2500.0, 'limite': 5000.0},
        {'numero': '345678', 'saldo': 500.0, 'limite': 1000.0},
        # Adicione as outras contas aqui...
    ]

    for conta_data in contas:
        conta = Conta(numero=conta_data['numero'], saldo=conta_data['saldo'], limite=conta_data['limite'])
        db.session.add(conta)
    db.session.commit()

    return jsonify({'message': 'Banco de dados populado com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)
