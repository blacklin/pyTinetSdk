"""
_配置管理接口
        _座席设置
        _队列设置
        _话机设置
        _号码设置
        _语音导航设置
"""
import datetime
import hmac
import base64
from urllib.parse import urlencode
import requests
from copy import deepcopy


class Core:
    def __init__(self, AccessKeyId, AccessKeySecret, http_head='https://', server_name='api-bj.clink.cn', expires=60):
        self.http_head = http_head
        self.server_name = server_name
        self.userinfo = {
            "AccessKeyId": AccessKeyId,
            "AccessKeySecret": AccessKeySecret
        }

        self.baseData = {
            "AccessKeyId": self.userinfo['AccessKeyId'],
            "Expires": expires,
        }

    def run(self, apiname, method, **kwargs):
        senddata = {}
        cpkwargs = deepcopy(kwargs)
        for k, v in cpkwargs.items():
            if not v:
                kwargs.pop(k)
        if method == 'GET':
            senddata.update(kwargs)
        senddata.update({
            "Timestamp": datetime.datetime.now().replace(microsecond=0).isoformat() + 'Z'
        })
        senddata.update(self.baseData)

        args = dict(sorted(senddata.items()))
        singatxt = method + self.server_name + '/' + apiname + '?' + urlencode(args)
        signature = self._hmac_sha1(singatxt)
        args.update({"Signature": signature.decode()})

        if method == 'GET':
            req = requests.get(self.http_head + self.server_name + "/" + apiname, params=args)
        elif method == 'POST':
            req = requests.post(self.http_head + self.server_name + "/" + apiname,  params=args,
                                json=kwargs)

        else:
            raise Exception("methods Error")
        return req.json()

    def _hmac_sha1(self, signtxt):
        objhmac = hmac.new(self.userinfo['AccessKeySecret'].encode(), signtxt.encode(), 'sha1')
        encrypts = objhmac.digest()
        signature = base64.b64encode(encrypts)
        return signature

