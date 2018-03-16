import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from fullmetal_api_client.clients.bsi import BSI
from jsonrpc2_base.plugins.client.signature_add import SignatureAdd
from jsonrpc2_base.plugins.client.debug_logger import DebugLogger

class BSIClient(object):
    """
    """
    @staticmethod
    def init():
        strAPIKey = "14733:QlOyhepEMIZDRIpksscvY9WplxxZBelsz90Ropvb8vPZeekGGxbFG841FC1hQmJ"
        dictParams = {
            "strJSONRPCRouterURL": "https://bsiintegration.bigstepcloud.com/api/"
        }

        """
        Instantiate the Python Client.
        """
        bsi = BSI.getInstance(
            dictParams,
            [
                SignatureAdd(strAPIKey, {}),
                DebugLogger(True, "DebugLogger.log")
            ]
        )

        return bsi