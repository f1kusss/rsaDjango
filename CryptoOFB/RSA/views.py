from django.shortcuts import render
from base64 import b64encode,b64decode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import rsa


def keys():
    (_keyPublic, _keyPrivate) = rsa.newkeys(512)
    return _keyPublic, _keyPrivate

def second(request):
    keyPublic, keyPrivate = keys()
    if request.method == "POST":
        if 'encode' in request.POST:
            message = request.POST['message']
            answer = crypto(message, keyPublic)
        else:
            message = request.POST['message_decode']

            answer = decrypto(message, keyPrivate)

    else:
        answer = {}
    return render(request, 'index.html', answer)



def keys():
    (_keyPublic, _keyPrivate) = rsa.newkeys(512)
    return _keyPublic, _keyPrivate

def crypto(message, key_public):
    msg = message.encode()
    crpt = rsa.encrypt(msg, key_public)
    crpt = b64encode(crpt).decode()
    return {"answer":crpt}#str(type(crpt))}

def decrypto(message, key_private):
    message = b64encode(message.encode())
    dcrpt = rsa.decrypt(message, key_private).decode()
    return {"ans":dcrpt}