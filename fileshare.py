# coding=utf8
import sys
import requests
import json
import mimetypes
import argparse
import os
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


def main(wf):
    #url="https://www.sov2ex.com/api/search"
    parser = argparse.ArgumentParser()
    parser.add_argument('query' , nargs='?' , default=None)
    args = parser.parse_args(wf.args)
    
    query = args.query
    # query = u"测试"
    if os.path.exists(query):
        if query:
            result = upload(query)
            # print result
            if result["status"] == 0:
                data = result["data"]
                wf.add_item(title=data["url"] , 
                            arg = data["url"] , 
                            valid = True , 
                            icon = ICON_WEB)
            else:
                # msg = result["msg"]
                wf.add_item(title = "upload failed" , 
                            arg = "upload failed",
                            valid = True , 
                            icon = ICON_WEB)
    else:
        wf.add_item(title = "file path is wrong" , 
                    arg = query,
                    valid = True , 
                    icon = ICON_WEB)


    wf.send_feedback()
    return 0


if __name__ == u"__main__":
    wf = Workflow3()
    sys.exit(wf.run(main))
