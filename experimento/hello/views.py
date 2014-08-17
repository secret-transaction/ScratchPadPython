from datetime import datetime, timedelta
from Crypto.Hash import SHA256
#from Crypto.PublicKey import RSA
#from Crypto.Signature import PKCS1_v1_5
# TODO: work on actual implementation later, priority is client completion
#from OpenSSL import crypto
from django import http

def home(request):
    return http.HttpResponse('Hello World!')
