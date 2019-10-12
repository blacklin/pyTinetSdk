## 天润融通PythonSDK

### 介绍

天润融通第三方PythonSDK

### 安装教程

python setup.py install

#### 使用说明
```
from tinetclink.Core import Core
from tinetclink.RecordsQuery.CalledLog import CalledLog

core = Core(AccessKeyId="", AccessKeySecret="")
calledlog = CalledLog(core)
calledlog.list_cdr_obs(hiddenType=1, offset=1000)
```
#### 其他说明
api详情请查看文档：
> http://api-bj.clink.cn/docs/api/user-manual.html

