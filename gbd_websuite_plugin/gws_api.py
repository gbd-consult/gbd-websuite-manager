import re
import json
import gzip
from .modules import umsgpack
from PyQt5.QtCore import QUrl, QByteArray
from PyQt5.QtNetwork import QNetworkRequest
from qgis.core import QgsNetworkAccessManager

def gws_api_call(url, cmd, params, authcfg = None, binary=True, compress=True):
    """Call the Gws API.

    Args:
        url: the server url to be called
        cmd: a command value from the GwsServerApi list,
            see https://gws.gbd-consult.de/doc/latest/books/client-developer/en/apiref.html
        params: a dictionary of parameters (as documented above)
        authcgf: an authcfg id for QGIS Authmanager
        binary: whether to use binary (msgpack), and not text (json) format
        compress: whether to gzip the request

    Returns:
        A dict with the server response. If case of an error, the dict contains
        an `error` subdict with the fields `status` (e.g. 404) and `info`. Otherwise, it
        contains the response data, as documented above.
    """

    data = {'cmd': cmd, 'params': params}

    #url = QUrl(url.url().rstrip('/') + '/_')
    req = QNetworkRequest(url)

    if binary:
        data = umsgpack.dumps(data)
        req.setRawHeader(   QByteArray(b'content-type'),
                            QByteArray(b'application/msgpack'))
    else:
        data = json.dumps(data).encode('utf8')
        req.setRawHeader(   QByteArray(b'content-type'),
                            QByteArray(b'application/json'))

    if compress:
        data = gzip.compress(data)
        req.setRawHeader(   QByteArray(b'content-encoding'),
                            QByteArray(b'gzip'))

    res = QgsNetworkAccessManager.instance().blockingPost(req, data, authcfg)

    content_type = str(res.rawHeader(QByteArray(b'content-type'))).lower()
    print(res.error())
    print(res.errorString())
    print(res.content())
    if res.error() == 0:
        if 'msgpack' in content_type:
            return umsgpack.load(str(res.content(), 'utf-8'))
        if 'json' in content_type:
            return json.loads(str(res.content(), 'utf-8'))

    raise ValueError('Unexpected content-type ' + repr(content_type))

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