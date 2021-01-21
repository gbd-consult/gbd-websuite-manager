import hashlib
import ast
import os
import json

from .gws_api import gws_api_call


class GbdManagerHash():
    """Build a Hash for all files distributed by the Manager"""

    def load_hash_list(self, url, authcfg, title):
        '''load the hash list from the server'''

        try:
            answ = gws_api_call(url,
                                'fsRead',
                                {'path': title + '/hash_list.json'},
                                authcfg)
            
            try: 
                x = answ['data']
                y = x.decode('UTF-8')
                mydata = ast.literal_eval(y)
                return(mydata)
            except TypeError:
                try:
                    return(None)
                except:
                    pass
        except:
            pass

    def build_hash(self, data, hashList, lay_id):
        '''build the hash for the layers'''
        
        m = hashlib.md5(data)
        m = m.hexdigest()

        if hashList is not None:
            if lay_id in hashList:
                if hashList[lay_id][0] == m:
                    return(m, None)
                else:
                    return(m, True)
            else:
                return(m, True)
        else:
            return(m, True)

    def save_hash_list(self, url, authcfg, title, hashList, projDir):
        '''Sends the hash list to the server'''
        hashList = json.dumps(hashList)

        answ = gws_api_call(url,
                            'fsWrite',
                            {'path': '/'
                            + title
                            + '/hash_list.json',
                            'data': hashList},
                            authcfg)

        with open(os.path.join(projDir, 'hash_list.json'), 'w') as f:
            f.write(hashList)


    
