import requests as r
import json
import gzip
from .modules import umsgpack
import re

def gws_api_call(url, cmd, params, auth=None, binary=True, compress=True):
    """Call the Gws API.

    Args:
        url: the server url to be called
        cmd: a command value from the GwsServerApi list,
            see https://gws.gbd-consult.de/doc/latest/books/client-developer/en/apiref.html
        params: a dictionary of parameters (as documented above)
        auth: an optional tuple `(username, password)` for the Basic authorization
        binary: whether to use binary (msgpack), and not text (json) format
        compress: whether to gzip the request

    Returns:
        A dict with the server response. If case of an error, the dict contains
        an `error` subdict with the fields `status` (e.g. 404) and `info`. Otherwise, it
        contains the response data, as documented above.
    """

    data = {'cmd': cmd, 'params': params}
    headers = {}

    if binary:
        data = umsgpack.dumps(data)
        headers['content-type'] = 'application/msgpack'
    else:
        data = json.dumps(data).encode('utf8')
        headers['content-type'] = 'application/json'

    if compress:
        data = gzip.compress(data)
        headers['content-encoding'] = 'gzip'

    url = url.rstrip('/') + '/_'
    res = r.post(url, data=data, headers=headers, auth=auth)

    ct = res.headers.get('content-type', '').lower()

    if 'msgpack' in ct:
        return umsgpack.loads(res.content)
    if 'json' in ct:
        return json.loads(res.content)

    raise ValueError('Unexpected content-type ' + repr(ct))

#################################################################

#regex expression to filter characters that arent possible in a url

_UID_DE_TRANS = {
    ord('ä'): 'ae',
    ord('ö'): 'oe',
    ord('ü'): 'ue',
    ord('ß'): 'ss',
}

def as_uid(x) -> str:
    """Convert a value to an uid (alphanumeric string).""" 
    if not x:
        return ''
    x = str(x).lower().strip().translate(_UID_DE_TRANS)
    x = re.sub(r'[^a-z0-9]+', '_', x)
    return x.strip('_')
