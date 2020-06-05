import hmac
import hashlib
import base64

msg = "13916834993JJHlXeDcFM".encode('utf-8')
secret = b"230664ae53cbe5a07c6c389910540729"
result = hmac.new(secret, msg=msg, digestmod=hashlib.sha256).hexdigest()

print(result)
