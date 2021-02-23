from flask import Flask, jsonify, request
from evidence_contract import Evidence_Contract

app = Flask(__name__)
contract_address = "0xa2a9d06c3478778e2302bac12115c128334915f4"
a = Evidence_Contract(contract_address)

# a.client.set_account_by_keystorefile("fengfeng.keystore")
# a.client.set_account_by_keystorefile("fengfeng2.keystore")
fengfeng_privkey = "d6f8c8f9106835ccc8f8d0bbc4b5bf32ff5f8941e69f9f50d075684d10dda7be"
fengfeng2_privkey = "619834a32f41fc9dce7809c3063070af3d78fac577a0c12705984eed0b1a3cb"

@app.route("/new_evidence")
def new_evidence():

    data = request.get_json()
    if data is None:
        return jsonify({"error": "pleace input evidence by string."}), 400
    privkey = data["privkey"]
    evidence_string = data["evidenceString"]
    evidence = Evidence_Contract(contract_address)
    evidence.client.set_account_by_privkey(privkey)
    new_evi = evidence.new_evidence_by_evi(evidence_string)
    return jsonify(new_evi), 200


@app.route("/evidence/<address>")
def show_evidence(address):
    try:
        evidence = Evidence_Contract(contract_address)
        evi = evidence.get_evidence_by_address(address)
        return jsonify(evi), 200
    except Exception as e:
        return jsonify({"error": e}), 400

@app.route("/addsignatures")
def add_sinatures():
    data = request.get_json()
    # old_privkey = a.client.keypair.private_key
    privkey = data["privkey"]
    evidence_address = data["evidence_address"]
    evidence = Evidence_Contract(contract_address)
    evidence.client.set_account_by_privkey(privkey)
    result = evidence.add_signatures_by_evi_address(evidence_address)
    # evidence.client.set_account_by_privkey(old_privkey)
    return jsonify(result), 200

@app.route("/verifysigner")
def verify():
    pass





if __name__ == '__main__':
    app.run()