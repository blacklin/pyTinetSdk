'''号码设置
@Auther: lin
@Date: 2019-10-09 17:30:29.295894'''
class Number:
    def __init__(self, core):
        self.core = core

    def list_clid_numbers(self,extenNumber):
        """
        查询企业外显号码列表

        Args:
        	extenNumber (String):必须  话机号码。3-6 位数字
		
        """
        method = 'GET'
        apiname = 'list_clid_numbers'
        return self.core.run(apiname, method, extenNumber=extenNumber)

    def list_hotline_numbers(self,extenNumber):
        """
        查询企业热线号码列表

        Args:
        	extenNumber (String):必须  话机号码。3-6 位数字
		
        """
        method = 'GET'
        apiname = 'list_hotline_numbers'
        return self.core.run(apiname, method, extenNumber=extenNumber)
