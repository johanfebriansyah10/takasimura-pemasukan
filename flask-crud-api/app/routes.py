from flask import Blueprint, request, jsonify
from app.models import Income
from app.db import db

api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/incomes', methods=['POST'])
def create_income():
    data = request.get_json()
    try:
        new_income = Income(
            date=data['date'],
            amount=data['amount'],
            description=data.get('description', ''),
            category=data['category'],
            wallet=data['wallet']
        )
        db.session.add(new_income)
        db.session.commit()
        return jsonify(new_income.to_dict()), 201
    except KeyError as e:
        return jsonify({"error": f"Missing field: {e}"}), 400


@api_blueprint.route('/incomes', methods=['GET'])
def get_incomes():
    incomes = Income.query.all()
    return jsonify([income.to_dict() for income in incomes]), 200


@api_blueprint.route('/incomes/<int:id>', methods=['GET'])
def get_income(id):
    income = Income.query.get(id)
    if not income:
        return jsonify({"error": "Income not found"}), 404
    return jsonify(income.to_dict()), 200


@api_blueprint.route('/incomes/<int:id>', methods=['PUT'])
def update_income(id):
    data = request.get_json()
    income = Income.query.get(id)
    if not income:
        return jsonify({"error": "Income not found"}), 404

    income.date = data.get('date', income.date)
    income.amount = data.get('amount', income.amount)
    income.description = data.get('description', income.description)
    income.category = data.get('category', income.category)
    income.wallet = data.get('wallet', income.wallet)

    db.session.commit()
    return jsonify(income.to_dict()), 200


@api_blueprint.route('/incomes/<int:id>', methods=['DELETE'])
def delete_income(id):
    income = Income.query.get(id)
    if not income:
        return jsonify({"error": "Income not found"}), 404

    db.session.delete(income)
    db.session.commit()
    return jsonify({"message": "Income deleted"}), 200
