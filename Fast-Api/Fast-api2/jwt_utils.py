from jwt import encode, decode, exceptions

SECRET = "misecret"

def createToken(data: dict) -> str:
    token: str = encode(payload=data, key=SECRET, algorithm='HS256')
    return token

def validate_token(token: str) -> dict:
    try:
        decoded = decode(token, key=SECRET, algorithms=['HS256'])
        return decoded
    except exceptions.DecodeError:
        raise Exception("Token inválido")
    except exceptions.ExpiredSignatureError:
        raise Exception("Token expirado")
