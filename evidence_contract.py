from client.bcosclient import BcosClient
from client.datatype_parser import DatatypeParser
from web3 import Web3

class Evidence_Contract:

    def __init__(self, address: str):

        abi_file = "contracts/EvidenceFactory.abi"
        data_parser = DatatypeParser()
        data_parser.load_abi_file(abi_file)
        self.contract_abi = data_parser.contract_abi

        self.client = BcosClient()
        self.to_address = address


    def new_evidence_by_evi(self, evi: str):

        new_evidence = self.client.sendRawTransactionGetReceipt(self.to_address, self.contract_abi, "newEvidence", [evi])
        return {"result": new_evidence["logs"]}

    def get_evidence_by_address(self, address: str):

        addr = Web3.toChecksumAddress(address)
        evidence_msg = self.client.call(self.to_address, self.contract_abi, "getEvidence", [addr])
        return {"result": evidence_msg}

    def add_signatures_by_evi_address(self, address: str):
        addr = Web3.toChecksumAddress(address)
        signature = self.client.sendRawTransactionGetReceipt(self.to_address, self.contract_abi, "addSignatures", [addr])
        return {
            "result": signature["logs"]
        }

    def verifySigner_by_address(self, address: str):
        try:
            addr = Web3.toChecksumAddress(address)
            signature = self.client.call(self.to_address, self.contract_abi, "verify", [addr])
            return {
                "result": signature[0]
            }
        except:
            return {
                "address": False
            }

    def get_signer_by_index(self, index: int):
        signature = self.client.call(self.to_address, self.contract_abi, "getSigner", [index])
        return {
            "address": signature[0]
        }

    def get_signers_size(self):
        signers_size = self.client.call(self.to_address, self.contract_abi, "getSignersSize", [])
        return {
            "size": signers_size[0]
        }

    def get_signers(self):
        signers = self.client.call(self.to_address, self.contract_abi, "getSigners", [])
        return {
            "signers": signers[0]
        }

# contract_address = "0xa2a9d06c3478778e2302bac12115c128334915f4"
# a = Evidence_Contract(contract_address)
#
# # a.client.set_account_by_keystorefile("fengfeng.keystore")
# # a.client.set_account_by_keystorefile("fengfeng2.keystore")
# fengfeng_privkey = "d6f8c8f9106835ccc8f8d0bbc4b5bf32ff5f8941e69f9f50d075684d10dda7be"
# fengfeng2_privkey = "619834a32f41fc9dce7809c3063070af3d78fac577a0c12705984eed0b1a3cb"
#
# a.client.set_account_by_privkey(fengfeng2_privkey)
#
# print(a.client.keypair.address)
# print("new evidence")
#
# t = a.new_evidence_by_evi("Hello, world")
# print(t)
# print(a.get_evidence_by_address(t["result"][0]["address"]))
#
# print(a.add_signatures_by_evi_address(t["result"][0]["address"]))
# print(a.get_evidence_by_address(t["result"][0]["address"]))
#
# print("==================== 切换账户 ====================")
# print("==================== 添加多签用户 ====================")
#
# a.client.set_account_by_keystorefile("fengfeng.keystore")
#
# print(a.add_signatures_by_evi_address(t["result"][0]["address"]))
# print(a.get_evidence_by_address(t["result"][0]["address"]))