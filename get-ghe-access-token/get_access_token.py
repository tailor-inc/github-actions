import time
import os
import sys

import jwt
import requests

APP_ID = os.environ['GITHUB_APP_ID']
APP_INSTALLATION_ID = os.environ['GITHUB_APP_INSTALLATION_ID']
PRIVATE_KEY = os.environ['GITHUB_APP_PRIVATE_KEY']

if not all([APP_ID, APP_INSTALLATION_ID, PRIVATE_KEY]):
    print('Error: app information not configured', file=sys.stderr)
    sys.exit(1)

now = int(time.time())

payload = {
    'iat': now - 60,
    'exp': now + 60 * 10,
    'iss': APP_ID,
}

token = jwt.encode(payload, key=PRIVATE_KEY, algorithm='RS256')

result = requests.post(
    f'https://api.github.com/app/installations/{APP_INSTALLATION_ID}/access_tokens',
    headers={'Authorization': 'Bearer {}'.format(token), 'Accept': 'application/vnd.github+json'},
)

print(result.json()['token'])
