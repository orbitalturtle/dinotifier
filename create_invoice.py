import rpc_pb2 as lnrpc, rpc_pb2_grpc as rpcstub
from detect_tx import macaroon, stub

import json
import pyqrcode

def create_invoice():
    request = lnrpc.Invoice(
        value=500
    )
    
    response = stub.AddInvoice(request, metadata=[('macaroon', macaroon)])
