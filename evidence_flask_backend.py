from flask import Flask, jsonify, request, render_template
from evidence_contract import Evidence_Contract
from flask_cors import CORS
import json

app = Flask(__name__)
contract_address = "0xa2a9d06c3478778e2302bac12115c128334915f4"
fengfeng_privkey = "d6f8c8f9106835ccc8f8d0bbc4b5bf32ff5f8941e69f9f50d075684d10dda7be"
fengfeng2_privkey = "619834a32f41fc9dce7809c3063070af3d78fac577a0c12705984eed0b1a3cb"
CORS(app)

@app.route("/new_evidence", methods=["GET", "POST"])
def new_evidence():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Pleace input [privkey, evidenceString] by string."}), 400
    privkey = data["privkey"]
    evidence_string = data["evidenceString"]
    evidence = Evidence_Contract(contract_address)
    evidence.client.set_account_by_privkey(privkey)
    new_evi = evidence.new_evidence_by_evi(evidence_string)
    return jsonify(new_evi), 200

@app.route("/evidence/<address>", methods=["GET", "POST"])
def show_evidence(address):
    try:
        evidence = Evidence_Contract(contract_address)
        evi = evidence.get_evidence_by_address(address)
        return jsonify(evi), 200
    except Exception as e:
        return jsonify({"error": e}), 400

@app.route("/addsignatures", methods=["GET", "POST"])
def add_sinatures():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "pleace input [privkey, evidenceAddress] by string."}), 400
    privkey = data["privkey"]
    evidence_address = data["evidenceAddress"]
    evidence = Evidence_Contract(contract_address)
    try:
        evidence.client.set_account_by_privkey(privkey)
    except:
        return jsonify({"error": "Please enter the correct private key."}), 400
    result = evidence.add_signatures_by_evi_address(evidence_address)
    return jsonify(result), 200

@app.route("/verifysigner", methods=["GET", "POST"])
def verify():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "pleace input [signerAddress,] by string."}), 400
    evidence = Evidence_Contract(contract_address)
    result = evidence.verifySigner_by_address(data["signerAddress"])
    return jsonify(result), 200

@app.route("/signer/<int:index>")
def showsigner(index):
    evidence = Evidence_Contract(contract_address)
    result = evidence.get_signer_by_index(index)
    return jsonify(result), 200

@app.route("/signer/lists")
def listsigner():
    evidence = Evidence_Contract(contract_address)
    result = evidence.get_signers()
    return jsonify(result), 200

@app.route("/signer/size")
def get_signer_size():
    evidence = Evidence_Contract(contract_address)
    result = evidence.get_signers_size()
    return jsonify(result), 200


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("tests.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0")


