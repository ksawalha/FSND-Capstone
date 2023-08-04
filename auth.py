import os
from functools import wraps
from urllib.request import urlopen
import json
from flask import request
from jose import jwt


'''
Auth0 URL to get JWT
https://dev-karamsawalha.us.auth0.com/authorize?audience=karamcapstone&response_type=token&client_id=6el7BJBoNh04IO1XBLkrpoRjuYUrB0hC&redirect_uri=https://sample/callback

'''

# Authentication variables as an ENV variables
AUTH0_DOMAIN = os.environ['AUTH0_DOMAIN']
ALGORITHMS = [os.environ['ALGORITHMS']]
API_AUDIENCE = os.environ['API_AUDIENCE']
AUTH0_ISSUER = f'https://{AUTH0_DOMAIN}/'

class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


def get_token_auth_header():     #checking header and getting token
    auth_header = request.headers.get('Authorization', None)
    if auth_header is None:
        raise AuthError(
            {
                'code': 'unauthorized',
                'description': 'auth header is missing'
            }, 401
        )
    
    auth_header_parts = auth_header.split(' ')
    if len(auth_header_parts) != 2 or auth_header_parts[0].lower() != 'bearer':
        raise AuthError(
            {
                'code': 'unauthorized',
                'description': 'auth header is malformed'
            }, 401
        )

    return auth_header_parts[1]



def check_permissions(permission, payload):   #Checking payload permissions
    permissions = payload.get('permissions', None)
    if permissions is None:
        raise AuthError(
            {
                'code': 'unauthorized',
                'description': 'permissions are not included in the payload'
            }, 401
        )
    
    if permission not in permissions:
        raise AuthError(
            {
                'code': 'unauthorized',
                'description': 'requested permission is not in the payload permissions array'
            }, 401
        )
    
    return True



def verify_decode_jwt(token):        #Verifying Decoded JWT info
    try:
        unverified_headers = jwt.get_unverified_headers(token)
        kid = unverified_headers.get('kid', None)

    except:
        raise AuthError(
            {
                'code': 'unauthorized',
                'description': 'it should be an Auth0 token with key id (kid)'
            }, 401
        )

    if kid is None:
        raise AuthError(
            {
                'code': 'unauthorized',
                'description': 'it should be an Auth0 token with key id (kid)'
            }, 401
        )
    
    jwks_json = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    jwks = json.loads(jwks_json.read())

    rsa_key = {}
    for jwk in jwks['keys']:
        if jwk['kid'] == kid:
            rsa_key['kty'] = jwk['kty']
            rsa_key['kid'] = jwk['kid']
            rsa_key['use'] = jwk['use']
            rsa_key['n'] = jwk['n']
            rsa_key['e'] = jwk['e']

    if rsa_key:
        try:
            payload = jwt.decode(
                token=token,
                key=rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer=AUTH0_ISSUER,    
            )
            return payload

        except jwt.JWTClaimsError:
            raise AuthError(
                {
                    'code': 'unauthorized',
                    'description': 'claims error check audience and issuer'
                }, 401
            )
            
        except jwt.ExpiredSignatureError:
            raise AuthError(
                {
                    'code': 'unauthorized',
                    'description': 'expired signature'
                }, 401
            )

        except Exception:
            raise AuthError(
                {
                    'code': 'invalid_header',
                    'description': 'can not parese the token'
                }, 400
            )
        
    raise AuthError(
        {
            'code': 'invalid_header',
            'description': 'can not find the appropriate key'
        }, 401
    )



def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            payload = verify_decode_jwt(token)
            check_permissions(permission, payload)
            return f(*args, **kwargs)

        return wrapper
    return requires_auth_decorator
