import urllib.request
import urllib.parse
import json

def get_translate(word=None):
    if word == None:
        return
    else:
        url = 'http://fanyi.youdao.com/translate'
        data = {
            'from':'AUTO',
            'to':'AUTO',
            'smartresult':'dict',
            'client':'fanyideskweb',
            'salt':'1500092479607',
            'sign':'c98235a85b213d482b8e65f6b1065e26',
            'doctype':'json',
            'version':'2.1',
            'keyfrom':'fanyi.web',
            'action':'FY_BY_CL1CKBUTTON',
            'typoResult':'true'
        }

    data['i'] = word
    data = urllib.parse.urlencode(data).encode('utf8')
    response = urllib.request.urlopen(url,data)
    html = response.read().decode('utf8')
    content = json.loads(html)
    print('翻译结果: %s '% (content['translateResult'][0][0]['tgt']))

if __name__ == '__main__':
    # get_translate('我爱你')
    strwords = input('输入文本：')
    get_translate(strwords)