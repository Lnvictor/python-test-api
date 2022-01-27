from api.controller import find_cpf_in_blacklist
from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/<cpf>", methods=["POST"])
def index(cpf):
    is_present = find_cpf_in_blacklist(cpf)
    resp = {
        "status": "BLOCK" if is_present else "FREE"
    }

    return jsonify(resp), 200