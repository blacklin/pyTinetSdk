'''满意度记录
@Auther: lin
@Date: 2019-10-09 17:30:29.502894'''
class Investigation:
    def __init__(self, core):
        self.core = core

    def list_investigations(self,hiddenType=None,customerNumber=None,hotline=None,startTime=None,endTime=None,offset=None,limit=None):
        """
        查询满意度调查记录列表

        Args:
        	hiddenType (Integer):可选  是否隐藏号码。
 0: 不隐藏，1: 中间四位，2: 最后八位，3: 全部号码，4: 最后四位。默认值为 0
		customerNumber (String):可选  客户号码
		hotline (String):可选  热线号码
		startTime (Long):可选  开始时间，时间戳格式精确到秒。默认值取当前月份第一天
		endTime (Long):可选  结束时间，时间戳格式精确到秒，开始时间和结束时间跨度不能超过一个月。默认值取当前时间
		offset (Integer):可选  偏移量，范围 0-10000。默认值为 0
		limit (Integer):可选  查询条数，范围 10-100。默认值为 10
		
        """
        method = 'GET'
        apiname = 'list_investigations'
        return self.core.run(apiname, method, hiddenType=hiddenType, customerNumber=customerNumber, hotline=hotline, startTime=startTime, endTime=endTime, offset=offset, limit=limit)
