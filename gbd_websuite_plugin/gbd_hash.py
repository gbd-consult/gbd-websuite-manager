import hashlib
import ast
import os
import json

from .gws_api import gws_api_call


class GbdManagerHash():
    """Build a Hash for all files distributed by the Manager"""

    def load_hash_list(self, url, authcfg, title):
        '''load the hash list from the server'''
        print('url: ', url)
        print('auth: ', authcfg)
        print('title: ', title)
        try:
            answ = gws_api_call(url,
                                'fsRead',
                                {'path': title + '/hash_list.json'},
                                authcfg)

            print('downloaded: ', answ)
            
            try: 
                x = answ['data']
                y = x.decode('UTF-8')
                mydata = ast.literal_eval(y)
                print('mydata: ', mydata)
                return(mydata)
            except TypeError:
                try:
                    #answ['error']
                    print('nicht vorhanden')
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
                print('layer schon bekannt')
                if hashList[lay_id][0] == m:
                    print('nicht verändert')
                    return(m, None)
                else:
                    print('verändert')
                    return(m, True)
            else:
                return(m, True)
        else:
            return(m, True)

    def save_hash_list(self, url, authcfg, title, hashList, projDir):
        '''Sends the hash list to the server'''
        print(hashList)
        hashList = json.dumps(hashList)

        answ = gws_api_call(url,
                            'fsWrite',
                            {'path': '/'
                            + title
                            + '/hash_list.json',
                            'data': hashList},
                            authcfg)

        print(answ)

        with open(os.path.join(projDir, 'hash_list.json'), 'w') as f:
            f.write(hashList)


    
