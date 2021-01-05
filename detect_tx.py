import rpc_pb2 as ln
import rpc_pb2_grpc as lnrpc
import codecs
import grpc
import os
from spin import move_motor

# Due to updated ECDSA generated tls.cert we need to let gprc know that
# we need to use that cipher suite otherwise there will be a handhsake
# error when we communicate with the lnd rpc server.
os.environ["GRPC_SSL_CIPHER_SUITES"] = 'HIGH+ECDSA'

macaroon = codecs.encode(open(os.environ['ALICE_MACAROON_PATH'], 'rb').read(), 'hex')

# Lnd cert is at ~/.lnd/tls.cert on Linux and
# ~/Library/Application Support/Lnd/tls.cert on Mac
cert = open(os.path.expanduser(os.environ['ALICE_CERT_PATH']), 'rb').read()

creds = grpc.ssl_channel_credentials(cert)
channel = grpc.secure_channel('localhost:10001', creds)
stub = lnrpc.LightningStub(channel)

if __name__ == "__main__":
    request = ln.InvoiceSubscription()
    for invoice in stub.SubscribeInvoices(request, metadata=[('macaroon', macaroon)]):
        move_motor()
