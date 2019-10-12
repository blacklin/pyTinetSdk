'''外呼通话记录
@Auther: lin
@Date: 2019-10-09 17:30:29.466894'''
class CalledLog:
    def __init__(self, core):
        self.core = core

    def list_cdr_obs(self,hiddenType=None,customerNumber=None,cno=None,hotline=None,status=None,startTime=None,endTime=None,offset=None,limit=None):
        """
        查询外呼通话记录列表

        Args:
        	hiddenType (Integer):可选  是否隐藏号码。
 0: 不隐藏，1: 中间四位，2: 最后八位 3: 全部号码，4: 最后四位。默认值为 0
		customerNumber (String):可选  客户号码
		cno (String):可选  座席号，要求只能是 4-6 位数字
		hotline (String):可选  热线号码
		status (Integer):可选  接听状态。取值范围如下：
  0: 全部
  1: 客户未接听
  2: 座席未接听
  3: 双方接听
  默认值为0
		startTime (Long):可选  开始时间，时间戳格式精确到秒。默认值取当前月份第一天
		endTime (Long):可选  结束时间，时间戳格式精确到秒，开始时间和结束时间跨度不能超过一个月。默认值取当前时间
		offset (Integer):可选  偏移量，范围 0-10000。默认值为 0
		limit (Integer):可选  查询条数，范围 10-100。默认值为 10
		
        """
        method = 'GET'
        apiname = 'list_cdr_obs'
        return self.core.run(apiname, method, hiddenType=hiddenType, customerNumber=customerNumber, cno=cno, hotline=hotline, status=status, startTime=startTime, endTime=endTime, offset=offset, limit=limit)

    def describe_cdr_ob(self,mainUniqueId):
        """
        查询外呼通话记录详情

        Args:
        	mainUniqueId (String):必须  通话记录唯一标识
		
        """
        method = 'GET'
        apiname = 'describe_cdr_ob'
        return self.core.run(apiname, method, mainUniqueId=mainUniqueId)

    def describe_cdr_ob_details(self,mainUniqueId):
        """
        查询外呼通话记录明细

        Args:
        	mainUniqueId (String):必须  队列号
		
        """
        method = 'GET'
        apiname = 'describe_cdr_ob_details'
        return self.core.run(apiname, method, mainUniqueId=mainUniqueId)

    def copy_cdr_obs(self,scrollId,date,hiddenType=None,limit=None):
        """
        同步外呼通话记录

        Args:
        	scrollId (Integer):必须  每次请求返回的参数，作为下次请求的必须参数。
 for 循环第一次请求不需要传递此参数
		date (String):必须  指定同步某一天的通话记录。格式：yyyyMMdd, 例如：20180816
		hiddenType (Integer):可选  是否隐藏号码。
 0: 不隐藏，1: 中间四位，2: 最后八位，3: 全部号码，4: 最后四位。默认值为 0
		limit (Integer):可选  查询条数，范围 10-100。默认值为 10
		
        """
        method = 'GET'
        apiname = 'copy_cdr_obs'
        return self.core.run(apiname, method, scrollId=scrollId, date=date, hiddenType=hiddenType, limit=limit)

    def copy_cdr_ob_details(self,scrollId,date,limit=None):
        """
        同步外呼通话记录明细

        Args:
        	scrollId (Integer):必须  每次请求返回的参数，作为下次请求的必须参数。
 for 循环第一次请求不需要传递此参数
		date (String):必须  指定同步某一天的通话记录。格式：yyyyMMdd, 例如：20180816
		limit (Integer):可选  查询条数，范围 10-100。默认值为 10
		
        """
        method = 'GET'
        apiname = 'copy_cdr_ob_details'
        return self.core.run(apiname, method, scrollId=scrollId, date=date, limit=limit)
