from fastapi import HTTPException, Security, Request
from fastapi.security.api_key import APIKeyHeader

from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN

from Crypto.Cipher import AES

api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)

#TODO: Add an actual API key

def check_api_key(api_key: str, request):
    file_in = open("key.bin", "rb")
    nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]
    key = nonce+tag+ciphertext
    file_in = open("api.bin", "rb")
    nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    decrypted = cipher.decrypt_and_verify(ciphertext, tag)
    val_key = bytes(decrypted).decode('utf-8')
    if val_key == api_key:
        return True
    return False


async def get_api_key(request: Request, api_key_header: str = Security(api_key_header)):
    if api_key_header is None:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Missing Authentication Token",
        )
    elif check_api_key(api_key_header, request):
        return api_key_header
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN,
            detail="Invalid API Key identifier specified",
        )