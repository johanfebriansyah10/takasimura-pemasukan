from flask import Blueprint, jsonify, request
from app.control import getAllData, getDataById, createData, UpdateData, delete


routes = Blueprint('routes', __name__)

@routes.route('/pemasukan', methods=['GET'])
def getAllPemasukan():
  return jsonify(getAllData(), 200);

@routes.route('/pemasukan/<int:id>', methods=['GET'])
def getPemasukanById(id):
  item = getDataById(id)
  if not item:
    return jsonify({'message': 'item tidak ditemukan'}), 400
  return jsonify(item), 200

@routes.route('/pemasukan', methods=['POST'])
def create():
  newItem = request.json
  if not all(k in newItem for k in (
    'tanggal',
    'jumlah',
    'deskripsi',
    'kategori',
    'dompet'
  )):
    return jsonify({'message': 'kolom tidak ada'}), 400
  return jsonify(createData(newItem)), 201


@routes.route('/pemasukan/<int:id>', methods=['PUT'])
def update(id):
  uploadItem = request.json
  item = UpdateData(id, uploadItem)
  if not item:
    return jsonify({'message': 'Item tidak ditemukan'}),400
  return jsonify(item), 200


@routes.route('/pemasukan/<int:id>', methods=['DELETE'])
def deleteItem(id):
  if not getDataById(id):
    return jsonify({'message': 'Item tidak ditemukan'}), 400
  deleteItem(id)
  return jsonify({'message', 'item berhasil dihapus'}), 200