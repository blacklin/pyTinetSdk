'''语音导航设置
@Auther: lin
@Date: 2019-10-09 17:30:29.300894'''
class IVRSetting:
    def __init__(self, core):
        self.core = core

    def list_ivrs(self,extenNumber):
        """
        询语音导航列表

        Args:
        	extenNumber (String):必须  话机号码。3-6 位数字
		
        """
        method = 'GET'
        apiname = 'list_ivrs'
        return self.core.run(apiname, method, extenNumber=extenNumber)

    def list_ivr_nodes(self,ivrId):
        """
        询语音导航节点列表

        Args:
        	ivrId (Integer):必须  语音导航id
		
        """
        method = 'GET'
        apiname = 'list_ivr_nodes'
        return self.core.run(apiname, method, ivrId=ivrId)
