import rpc_pb2 as ln
import rpc_pb2_grpc as lnrpc
import codecs
import grpc
import os

# Due to updated ECDSA generated tls.cert we need to let gprc know that
# we need to use that cipher suite otherwise there will be a handhsake
# error when we communicate with the lnd rpc server.
os.environ["GRPC_SSL_CIPHER_SUITES"] = 'HIGH+ECDSA'

macaroon = codecs.encode(open('admin.macaroon', 'rb').read(), 'hex')

# Lnd cert is at ~/.lnd/tls.cert on Linux and
# ~/Library/Application Support/Lnd/tls.cert on Mac
cert = open(os.path.expanduser('tls.cert'), 'rb').read()
creds = grpc.ssl_channel_credentials(cert)
channel = grpc.secure_channel('192.168.1.159:10009', creds)
stub = lnrpc.LightningStub(channel)

request = ln.InvoiceSubscription()
for invoice in stub.SubscribeInvoices(request, metadata=[('macaroon', macaroon)]):
    print(invoice)
