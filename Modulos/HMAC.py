import hmac
import hashlib
import base64


def _Hmac(key,message):
    key = bytes(key, 'utf-8')
    message = bytes(message, 'utf-8')
    digester = hmac.new(key, message,hashlib.sha1)
    signature1 = digester.digest()
    signature2 = base64.urlsafe_b64encode(signature1)

    return str(signature2, 'UTF-8')

def CriaAck(K,I,Q,IDr):
    _I = (''.join(str(x) for x in I))
    _Q = (''.join(Q))
    ack = _Hmac(K.hexdigest(),_I+_Q+IDr)
    return ack


def CriaAck2(K, Nonce, IDs, IDr):
    ack = _Hmac(K.hexdigest(), Nonce+IDs+IDr)
    return ack

