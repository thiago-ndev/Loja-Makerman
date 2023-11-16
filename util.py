import hashlib

def crypt_senha(senha):
   encoded_senha = senha.encode()
   senha_sha3 = hashlib.sha3_256(encoded_senha)
   return senha_sha3.hexdigest()


def raise_error(msg_erro, value_error):
    return {
        msg_erro: 'msg_error',
        value_error: 'value_error'
    }



