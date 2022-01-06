from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@Cluster0.nkjbe.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('login.html')


@app.route("/idcheck", methods=["GET"])
def idcheck_get():
    id_list = list(db.ids.find({}, {'_id': False}))
    return jsonify({'id_list':id_list})

@app.route("/<username>")

