from fiscobcos.client.contractnote import ContractNote
from fiscobcos.client.bcosclient import BcosClient
import os
from eth_utils import to_checksum_address
from fiscobcos.client.datatype_parser import DatatypeParser
from fiscobcos.client.common.compiler import Compiler
from fiscobcos.client.bcoserror import BcosException, BcosError
from fiscobcos.client_config import client_config


class Evidence_Contract:

    def __init__(self, address: str):
        # 从文件加载abi定义
        # Now file has been complied. Use .abi directly.

        if os.path.isfile(client_config.solc_path) or os.path.isfile(client_config.solcjs_path):
            Compiler.compile_file("contracts/EvidenceFactory.sol")

        abi_file = "contracts/EvidenceFactory.abi"
        data_parser = DatatypeParser()
        data_parser.load_abi_file(abi_file)
        self.contract_abi = data_parser.contract_abi

        self.client = BcosClient()

        self.to_address = address


    def new_evidence_by_evi(self, evi: str):
        new_evidence = self.client.call(self.to_address, self.contract_abi, "newEvidence", [evi])
        return {"address": new_evidence[0]}

    def get_evidence_by_address(self, address: str):
        evidence_msg = self.client.call(self.to_address, self.contract_abi, "getEvidence", [address])
        return {"evicence_name": evidence_msg[0],
                "evidence_addr1": evidence_msg[1],
                "evidence_addr2": evidence_msg[2]}


    def add_signatures_by_address(self, address: str):
        signature = self.client.call(self.to_address, self.contract_abi, "addSignatures", [address])
        return {
            "is_or_not": signature[0]
        }


    def verify_by_address(self, address: str):
        signature = self.client.call(self.to_address, self.contract_abi, "verify", [address])
        return {
            "is_or_not": signature[0]
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
            "size": signers[0]
        }

