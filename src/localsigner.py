#
# This is a simple local signer class.  It expects to have the secret
# key passed in via the standard config next to the public_key.

import logging

from pytezos_core.key import Key

from src.signer import Signer

from pyhsm.convert import hex_to_bytes

class LocalSigner(Signer):
    def __init__(self, config):
        self.config = config

    def sign(self, pkh, sigreq):
        key = Key.from_encoded_key(self.config["keys"][pkh]["secret_key"])
        return key.sign(sigreq.get_payload())
