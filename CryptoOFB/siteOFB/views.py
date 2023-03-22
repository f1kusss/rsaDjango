from django.shortcuts import render
from base64 import b64encode,b64decode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


key = get_random_bytes(16)

def start(request):
    if request.method == "POST":
        if 'encode' in request.POST:
            message = request.POST['message']
            answer = encode(message, key)
        else:
            message = request.POST['message_decode']
            answer = decode(message, key)

    else:
        answer = {}
    return render(request, 'index.html', answer)
def encode(data,key):

    # Шифрование
    data = data.encode()
    cipher = AES.new(key, AES.MODE_OFB)
    ct_bytes = cipher.encrypt(data)
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')

    result = {'answer':iv+ct}
    return(result)

def decode(b64,key):
    iv = b64decode(b64[0:24])
    ct = b64decode(b64[24:])
    cipher = AES.new(key, AES.MODE_OFB, iv=iv)
    pt = cipher.decrypt(ct)
    pt=pt.decode('UTF-8')
    return({"ans":pt})