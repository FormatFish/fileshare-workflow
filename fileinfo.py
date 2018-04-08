# coding=utf8
import sys
import requests
import json
import mimetypes
import argparse
import os
# import validators
from workflow import Workflow3, ICON_WEB , web
reload(sys)
sys.setdefaultencoding( "utf-8" )

def upload(filepath):
    # APIKey = "YOUR API KEY"
    # format = "json"
    #url = "http://domain.com/api/1/upload/?key="+ APIKey + "&format=" + format
    url = "http://tmp.link/openapi/v1"
    # data = {}
    data = {"model":1 , "action":"upload"}
    files = {
            'file': open(filepath, 'rb')
        }
    #files = 
    # print files
    r = requests.post(url , data = data , files = files)

    return json.loads(r.text)

def get_info(ukey):
    # APIKey = "YOUR API KEY"
    # format = "json"
    #url = "http://domain.com/api/1/upload/?key="+ APIKey + "&format=" + format
    url = "http://tmp.link/openapi/v1"
    # data = {}
    data = {"ukey":ukey , "action":"fileinfo"}

    r = requests.post(url , data = data)

    return json.loads(r.text)

def main(wf):
    #url="https://www.sov2ex.com/api/search"
    parser = argparse.ArgumentParser()
    parser.add_argument('query' , nargs='?' , default=None)
    args = parser.parse_args(wf.args)
    
    query = args.query
    if query:
        ukey = os.path.basename(query)
        result = get_info(ukey)
        # print result
        if result["status"] == 0:
            data = result["data"]
            wf.add_item(title=u"文件大小为 : " + data["size"] , 
                        subtitle = u"链接有效期为 : " + data["lefttime"],
                        arg = query , 
                        valid = True , 
                        icon = ICON_WEB)
        else:
            # msg = result["msg"]
            wf.add_item(title = "链接不存在或者链接错误" , 
                        arg = query,
                        valid = True , 
                        icon = ICON_WEB)
 


    wf.send_feedback()
    return 0


if __name__ == u"__main__":
    wf = Workflow3()
    sys.exit(wf.run(main))
