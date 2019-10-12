'''话机设置
@Auther: lin
@Date: 2019-10-09 17:30:29.281894'''
class Phone:
    def __init__(self, core):
        self.core = core

    def create_exten(self,extenNumber,password,areaCode,type,allow):
        """
        增话机

        Args:
        	extenNumber (String):必须  话机号码。3-6 位数字，要求唯一
		password (String):必须  话机密码。3-6 位数字
		areaCode (String):必须  话机区号。以 0 开头 3-4 位数字
		type (Integer):必须  话机类型。1: 分机， 2: 软电话
		allow (Integer):必须  语音编码。1: G729， 2: [G729,alaw,ulaw]， 3: [alaw,ulaw,G729]
		
        """
        method = 'POST'
        apiname = 'create_exten'
        return self.core.run(apiname, method, extenNumber=extenNumber, password=password, areaCode=areaCode, type=type, allow=allow)

    def update_exten(self,extenNumber,password=None,areaCode=None,type=None,allow=None):
        """
        改话机

        Args:
        	extenNumber (String):必须  话机号码。3-6 位数字
		password (String):可选  话机密码。3-6 位数字
		areaCode (String):可选  话机区号。以 0 开头 3-4 位数字
		type (Integer):可选  话机类型。1: 分机，2: 软电话
		allow (Integer):可选  语音编码。1: G729， 2: [G729,alaw,ulaw]， 3: [alaw,ulaw,G729]
		
        """
        method = 'POST'
        apiname = 'update_exten'
        return self.core.run(apiname, method, extenNumber=extenNumber, password=password, areaCode=areaCode, type=type, allow=allow)

    def delete_exten(self,extenNumber):
        """
        除话机

        Args:
        	extenNumber (String):必须  话机号码。3-6 位数字
		
        """
        method = 'POST'
        apiname = 'delete_exten'
        return self.core.run(apiname, method, extenNumber=extenNumber)

    def list_extens(self,areaCode=None,type=None,offset=None,limit=None):
        """
        询话机列表

        Args:
        	areaCode (String):可选  话机区号。以 0 开头 3-4 位数字
		type (Integer):可选  话机类型。1: 分机， 2: 软电话
		offset (Integer):可选  偏移量。 范围 0-10000，默认值为 0
		limit (Integer):可选  查询条数。范围 10-100，默认值为 10
		
        """
        method = 'GET'
        apiname = 'list_extens'
        return self.core.run(apiname, method, areaCode=areaCode, type=type, offset=offset, limit=limit)

    def describe_exten(self,extenNumber):
        """
        询话机详情

        Args:
        	extenNumber (String):必须  话机号码。3-6 位数字
		
        """
        method = 'GET'
        apiname = 'describe_exten'
        return self.core.run(apiname, method, extenNumber=extenNumber)
