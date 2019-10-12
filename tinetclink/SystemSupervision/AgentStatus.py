'''座席监控
@Auther: lin
@Date: 2019-10-09 17:30:29.512894'''
class AgentStatus:
    def __init__(self, core):
        self.core = core

    def agent_status(self,qnos=None,cnos=None,agentStatus=None,pauseTypes=None,offset=None,limit=None):
        """
        座席状态

        Args:
        	qnos (String[]):可选  所属队列号
		cnos (String[]):可选  座席号，4-6 位数字
		agentStatus (String[]):可选  座席状态，IDLE：空闲；PAUSE：置忙；WRAPUP：整理；CALLING：呼叫中；RINGING：响铃；BUSY：通话
		pauseTypes (Integer[]):可选  置忙类型，1：普通；2：休息；3：IM；4：强制
		offset (Integer):可选  偏移量，默认值为 0，最大范围10000
		limit (Integer):可选  查询记录条数，默认只为 10，最大范围100
		
        """
        method = 'GET'
        apiname = 'agent_status'
        return self.core.run(apiname, method, qnos=qnos, cnos=cnos, agentStatus=agentStatus, pauseTypes=pauseTypes, offset=offset, limit=limit)
