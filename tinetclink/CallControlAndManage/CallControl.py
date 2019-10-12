'''呼叫控制
@Auther: lin
@Date: 2019-10-09 17:30:29.337894'''
class CallControl:
    def __init__(self, core):
        self.core = core

    def online(self,cno,bindType,bindTel,status=None,description=None):
        """
        上线

        Args:
        	cno (String):必须  座席工号，4-6 位数字
		bindType (Integer):必须  电话类型，1:电话；2:分机
		bindTel (String):必须  绑定电话
		status (Integer):可选  登录状态，1:空闲；2:置忙，默认值为1
		description (String):可选  状态描述，当status为2时需要给定参数值，描述需包含在企业自定义的置忙状态内
		
        """
        method = 'POST'
        apiname = 'online'
        return self.core.run(apiname, method, cno=cno, bindType=bindType, bindTel=bindTel, status=status, description=description)

    def offline(self,cno,unbindTel=None):
        """
        下线

        Args:
        	cno (String):必须  座席工号，4-6 位数字
		unbindTel (Integer):可选  是否下线同时解绑电话，0:不解绑；1:解绑，默认值为0
		
        """
        method = 'POST'
        apiname = 'offline'
        return self.core.run(apiname, method, cno=cno, unbindTel=unbindTel)

    def pause(self,cno,description=None):
        """
        置忙

        Args:
        	cno (String):必须  座席工号，4-6 位数字
		description (String):可选  置忙原因，如果是自定义状态，则状态描述需包含在企业自定义的置忙状态内，默认描述为置忙
		
        """
        method = 'POST'
        apiname = 'pause'
        return self.core.run(apiname, method, cno=cno, description=description)

    def unpause(self,cno):
        """
        置闲

        Args:
        	cno (String):必须  座席工号，4-6 位数字
		
        """
        method = 'POST'
        apiname = 'unpause'
        return self.core.run(apiname, method, cno=cno)

    def callout(self,cno,customerNumber,requestUniqueId=None,type=None,clid=None,clientTimeout=None,customerTimeout=None,userField=None):
        """
        外呼

        Args:
        	cno (String):必须  座席工号，4-6 位数字
		customerNumber (String):必须  客户电话，固话类型需要添加区号，手机类型不加 0，固话带分机以 “-” 分隔。
如果企业开启号码隐藏功能，可从弹屏事件中获取customerNumberKey的值，进行外呼
		requestUniqueId (String):可选  自定义请求id,如果传了这个参数那么将返回传入值，如果未传该值，那么系统将自动生成一个
		type (Integer):可选  外显方式，0：指定外显号码；1：指定外呼标识
		clid (String):可选  当外显方式为0时表示指定的外显号码，当外显类型为1时表示指定的外呼标识
		clientTimeout (Integer):可选  呼叫座席侧超时时间，取值范围 5-60s，默认 30s
		customerTimeout (Integer):可选  呼叫客户侧超时时间，取值范围 5-60s，默认 45s
		userField (String):可选  用户自定义变量，json格式字符串，例如：{"key":"value"}，需要进行urlEncode。传入的值会在通话记录中进行展示
		
        """
        method = 'POST'
        apiname = 'callout'
        return self.core.run(apiname, method, cno=cno, customerNumber=customerNumber, requestUniqueId=requestUniqueId, type=type, clid=clid, clientTimeout=clientTimeout, customerTimeout=customerTimeout, userField=userField)

    def callout_cancel(self,cno):
        """
        外呼取消

        Args:
        	cno (String):必须  座席工号，4-6 位数字
		
        """
        method = 'POST'
        apiname = 'callout_cancel'
        return self.core.run(apiname, method, cno=cno)

    def unlink(self,cno):
        """
        挂机

        Args:
        	cno (String):必须  座席工号，4-6 位数字
		
        """
        method = 'POST'
        apiname = 'unlink'
        return self.core.run(apiname, method, cno=cno)

    def refuse(self,cno):
        """
        拒接

        Args:
        	cno (String):必须  座席工号，4-6 位数字
		
        """
        method = 'POST'
        apiname = 'refuse'
        return self.core.run(apiname, method, cno=cno)

    def transfer(self,cno,transferType,transferNumber):
        """
        转移

        Args:
        	cno (String):必须  座席工号，4-6 位数字
		transferType (Integer):必须  转移类型，0：电话号码；1：座席号；2：分机号；3：语音导航节点；4：语音导航id
		transferNumber (String):必须  [转移对象]
		
        """
        method = 'POST'
        apiname = 'transfer'
        return self.core.run(apiname, method, cno=cno, transferType=transferType, transferNumber=transferNumber)

    def interact(self,cno,ivrId,ivrNode=None):
        """
        交互

        Args:
        	cno (String):必须  座席工号，4-6 位数字
		ivrId (Integer):必须  语音导航id
		ivrNode (String):可选  语音导航节点，如果不传此值则从语音导航的根节点开始
		
        """
        method = 'POST'
        apiname = 'interact'
        return self.core.run(apiname, method, cno=cno, ivrId=ivrId, ivrNode=ivrNode)

    def consult(self,cno,consultType,consultNumber):
        """
        咨询

        Args:
        	cno (String):必须  座席工号，4-6 位数字
		consultType (Integer):必须  咨询类型，0:电话号码；1:座席号；2:分机号
		consultNumber (String):必须  [咨询对象]
		
        """
        method = 'POST'
        apiname = 'consult'
        return self.core.run(apiname, method, cno=cno, consultType=consultType, consultNumber=consultNumber)

    def consult_cancel(self,cno):
        """
        咨询取消

        Args:
        	cno (String):必须  座席工号，4-6 位数字
		
        """
        method = 'POST'
        apiname = 'consult_cancel'
        return self.core.run(apiname, method, cno=cno)

    def consult_transfer(self,cno,limitTimeSecond=None,limitTimeAlertSecond=None,limitTimeFile=None):
        """
        咨询转移

        Args:
        	cno (String):必须  座席工号，4-6 位数字
		limitTimeSecond (Integer):可选  通话限制时间，单位：秒
		limitTimeAlertSecond (Integer):可选  提前提醒时间，单位：秒
		limitTimeFile (String):可选  提醒语音文件名称
		
        """
        method = 'POST'
        apiname = 'consult_transfer'
        return self.core.run(apiname, method, cno=cno, limitTimeSecond=limitTimeSecond, limitTimeAlertSecond=limitTimeAlertSecond, limitTimeFile=limitTimeFile)

    def consult_threeway(self,cno,limitTimeSecond=None,limitTimeAlertSecond=None,limitTimeFile=None):
        """
        咨询三方

        Args:
        	cno (String):必须  座席工号，4-6 位数字
		limitTimeSecond (Integer):可选  通话限制时间，单位：秒
		limitTimeAlertSecond (Integer):可选  提前提醒时间，单位：秒
		limitTimeFile (String):可选  提醒语音文件名称
		
        """
        method = 'POST'
        apiname = 'consult_threeway'
        return self.core.run(apiname, method, cno=cno, limitTimeSecond=limitTimeSecond, limitTimeAlertSecond=limitTimeAlertSecond, limitTimeFile=limitTimeFile)

    def unconsult(self,cno):
        """
        咨询接回

        Args:
        	cno (String):必须  座席工号，4-6 位数字
		
        """
        method = 'POST'
        apiname = 'unconsult'
        return self.core.run(apiname, method, cno=cno)

    def hold(self,cno):
        """
        保持

        Args:
        	cno (String):必须  座席工号，4-6 位数字
		
        """
        method = 'POST'
        apiname = 'hold'
        return self.core.run(apiname, method, cno=cno)

    def unhold(self,cno):
        """
        取消保持

        Args:
        	cno (String):必须  座席工号，4-6 位数字
		
        """
        method = 'POST'
        apiname = 'unhold'
        return self.core.run(apiname, method, cno=cno)

    def mute(self,cno,direction):
        """
        静音

        Args:
        	cno (String):必须  座席工号，4-6 位数字
		direction (String):必须  静音类型，in：座席侧静音，out：客户侧静音，all：双方全静音
		
        """
        method = 'POST'
        apiname = 'mute'
        return self.core.run(apiname, method, cno=cno, direction=direction)

    def unmute(self,cno,direction):
        """
        取消静音

        Args:
        	cno (String):必须  座席号
		direction (String):必须  静音类型，in：取消座席侧静音，out：取消客户侧静音，all：双方全取消静音
		
        """
        method = 'POST'
        apiname = 'unmute'
        return self.core.run(apiname, method, cno=cno, direction=direction)

    def dtmf(self,cno,digits,direction,duration=None,gap=None):
        """
        发送按键

        Args:
        	cno (String):必须  座席工号，4-6 位数字
		digits (String):必须  按键值，数字类型的字符串，最大 20 位，如：0123
		direction (String):必须  发送按键方向，in:座席侧；out:客户侧，all:双方
		duration (Integer):可选  按键持续毫秒数，取值 100-500 之间，默认值 100
		gap (Integer):可选  按键之间间隔毫秒数，取值 250-1000 之间，默认值 250
		
        """
        method = 'POST'
        apiname = 'dtmf'
        return self.core.run(apiname, method, cno=cno, digits=digits, direction=direction, duration=duration, gap=gap)

    def investigation(self,cno):
        """
        满意度调查

        Args:
        	cno (String):必须  座席工号，4-6 位数字
		
        """
        method = 'POST'
        apiname = 'investigation'
        return self.core.run(apiname, method, cno=cno)
