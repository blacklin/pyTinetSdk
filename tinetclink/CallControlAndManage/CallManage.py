'''呼叫管理
@Auther: lin
@Date: 2019-10-09 17:30:29.391894'''
class CallManage:
    def __init__(self, core):
        self.core = core

    def spy(self,cno,spyType,spyNumber):
        """
        监听

        Args:
        	cno (String):必须  被监听座席号
		spyType (Integer):必须  监听类型
		spyNumber (String):必须  [监听对象]
		
        """
        method = 'POST'
        apiname = 'spy'
        return self.core.run(apiname, method, cno=cno, spyType=spyType, spyNumber=spyNumber)

    def threeway(self,cno,threewayType,threewayNumber):
        """
        三方

        Args:
        	cno (String):必须  被三方座席号
		threewayType (Integer):必须  三方类型
		threewayNumber (String):必须  [三方对象]
		
        """
        method = 'POST'
        apiname = 'threeway'
        return self.core.run(apiname, method, cno=cno, threewayType=threewayType, threewayNumber=threewayNumber)

    def whisper(self,cno,whisperType,whisperNumber):
        """
        耳语

        Args:
        	cno (String):必须  被耳语座席号
		whisperType (Integer):必须  耳语类型
		whisperNumber (String):必须  [耳语对象]
		
        """
        method = 'POST'
        apiname = 'whisper'
        return self.core.run(apiname, method, cno=cno, whisperType=whisperType, whisperNumber=whisperNumber)

    def disconnect(self,cno,disconnectType,disconnectNumber):
        """
        强拆

        Args:
        	cno (String):必须  被强拆座席号
		disconnectType (Integer):必须  强拆类型
		disconnectNumber (String):必须  [强拆对象]
		
        """
        method = 'POST'
        apiname = 'disconnect'
        return self.core.run(apiname, method, cno=cno, disconnectType=disconnectType, disconnectNumber=disconnectNumber)

    def barge(self,cno,bargeType,bargeNumber):
        """
        强插

        Args:
        	cno (String):必须  被强插座席号
		bargeType (Integer):必须  强插类型
		bargeNumber (String):必须  [强插对象]
		
        """
        method = 'POST'
        apiname = 'barge'
        return self.core.run(apiname, method, cno=cno, bargeType=bargeType, bargeNumber=bargeNumber)

    def pause_client(self,cno,operator=None):
        """
        置忙_2

        Args:
        	cno (String):必须  被置忙的座席号
		operator (String):可选  触发此置忙事件的对象
		
        """
        method = 'POST'
        apiname = 'pause_client'
        return self.core.run(apiname, method, cno=cno, operator=operator)

    def unpause_client(self,cno,operator=None):
        """
        置闲_2

        Args:
        	cno (String):必须  被置闲的座席号
		operator (String):可选  触发此置闲事件的对象
		
        """
        method = 'POST'
        apiname = 'unpause_client'
        return self.core.run(apiname, method, cno=cno, operator=operator)
