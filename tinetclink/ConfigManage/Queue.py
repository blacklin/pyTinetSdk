'''队列设置
@Auther: lin
@Date: 2019-10-09 17:30:29.260894'''
class Queue:
    def __init__(self, core):
        self.core = core

    def create_queue(self,qno,name,maxWait=None,memberTimeout=None,queueTimeout=None,strategy=None,weight=None,wrapupTime=None,serviceLevel=None,joinEmpty=None,queueMembers=None,ibAllowed=None,chatStrategy=None,chatMaxWait=None,chatLocation=None):
        """
        增队列

        Args:
        	qno (String):必须  队列工号，4 位数字，要求唯一
		name (String):必须  座席名称，只允许输入中文，字母，数字，下划线，长度不超过 20 个字符
		maxWait (Integer):可选  最大等待数，设置范围 0-999，0 表示不做任何限制。默认值为 5
		memberTimeout (Integer):可选  座席超时时间，取值范围 20-60 秒。默认值为 25
		queueTimeout (Integer):可选  队列超时时间，取值范围 30-600 秒。默认值为 600
		strategy (Integer):可选  呼叫策略， 1: 顺序；2: 轮选；3: 平均；4: 随机；5: 技能优先，6: 最长空闲时间。默认值为 2
		weight (Integer):可选  队列优先级，取值范围 1-10。默认值为 1
                                            座席属于多个队列时，优先级高的队列的来电将优先接听；数值越高，优先级越高
		wrapupTime (Integer):可选  整理时长，取值范围 3-300 秒，整理期间座席不接受新的呼叫。默认值为 15
		serviceLevel (Integer):可选  服务水平秒数，取值范围 10-30 秒，低于此时间内接听的认为是高服务水平。默认值为 15
		joinEmpty (Integer):可选  队列中为空时是否可以join，1: 置忙；2: 通话中；4: 振铃；8: 无效；16: 整理
                                            如选多种状态则传对应数值的和，如选置忙和通话中，值为 3。默认值为 0，即都未选中
		queueMembers (Object[]):可选  队列内座席技能值设置。技能值 1-10，技能值 1 的优先级为最高
		ibAllowed (Integer):可选  是否允许呼入队列，0: 否；1: 是；默认值为 1
		chatStrategy (Integer):可选  在线客服分配策略，2：轮选；4：随机；5：技能优先；默认值为 2
		chatMaxWait (Integer):可选  在线客服最大排队数；默认值为 20
		chatLocation (Integer):可选  在线客服排队位置推送(小于该位置则推送)；默认值为 10
		
        """
        method = 'POST'
        apiname = 'create_queue'
        return self.core.run(apiname, method, qno=qno, name=name, maxWait=maxWait, memberTimeout=memberTimeout, queueTimeout=queueTimeout, strategy=strategy, weight=weight, wrapupTime=wrapupTime, serviceLevel=serviceLevel, joinEmpty=joinEmpty, queueMembers=queueMembers, ibAllowed=ibAllowed, chatStrategy=chatStrategy, chatMaxWait=chatMaxWait, chatLocation=chatLocation)

    def update_queue(self,qno,name,maxWait=None,memberTimeout=None,queueTimeout=None,strategy=None,weight=None,wrapupTime=None,serviceLevel=None,joinEmpty=None,queueMembers=None,ibAllowed=None,chatStrategy=None,chatMaxWait=None,chatLocation=None):
        """
        新队列

        Args:
        	qno (String):必须  队列工号，4位数字，要求唯一
		name (String):必须  座席名称，只允许输入中文，字母，数字，下划线，长度不超过20个字符
		maxWait (Integer):可选  最大等待数，设置范围 0-999，0 表示不做任何限制。默认值为 5
		memberTimeout (Integer):可选  座席超时时间，取值范围 20-60 秒。默认值为 25
		queueTimeout (Integer):可选  队列超时时间，取值范围 30-600 秒。默认值为 600
		strategy (Integer):可选  呼叫策略，1: 顺序；2: 轮选；3: 平均；4: 随机；5: 技能优先；6: 最长空闲时间。默认值为 2
		weight (Integer):可选  队列优先级，取值范围 1-10。默认值为 1
                                         座席属于多个队列时，优先级高的队列的来电将优先接听；数值越高，优先级越高
		wrapupTime (Integer):可选  整理时长，取值范围 3-300 秒，整理期间座席不接受新的呼叫。默认值为 15
		serviceLevel (Integer):可选  服务水平秒数，取值范围 10-30秒，低于此时间内接听的认为是高服务水平。默认值为 15
		joinEmpty (Integer):可选  队列中为空时是否可以join（设置了队列等待数，来电进入队列后处于等待状态，等待超时才溢出；如果勾选了这几个选项，认为座席不可用，直接溢出，减少客户等待时间），
                                          1: 置忙；2: 通话中；4: 振铃；8: 无效；16: 整理。
                                          如选多种状态则传对应数值的和，如选置忙和通话中，值为 3。默认值为 0
		queueMembers (Object[]):可选  队列内座席技能值设置。
                                          cno 座席号
                                          pernalty 技能值 1-10，技能值 1 的优先级为最高
		ibAllowed (Integer):可选  是否允许呼入队列，0: 否，1: 是；默认值为 1
		chatStrategy (Integer):可选  在线客服分配策略，2：轮选；4：随机；5：技能优先；默认值为 2
		chatMaxWait (Integer):可选  在线客服最大排队数；默认值为 20
		chatLocation (Integer):可选  在线客服排队位置推送(小于该位置则推送)；默认值为 10
		
        """
        method = 'POST'
        apiname = 'update_queue'
        return self.core.run(apiname, method, qno=qno, name=name, maxWait=maxWait, memberTimeout=memberTimeout, queueTimeout=queueTimeout, strategy=strategy, weight=weight, wrapupTime=wrapupTime, serviceLevel=serviceLevel, joinEmpty=joinEmpty, queueMembers=queueMembers, ibAllowed=ibAllowed, chatStrategy=chatStrategy, chatMaxWait=chatMaxWait, chatLocation=chatLocation)

    def delete_queue(self,qno):
        """
        除队列

        Args:
        	qno (String):必须  队列号
		
        """
        method = 'POST'
        apiname = 'delete_queue'
        return self.core.run(apiname, method, qno=qno)

    def list_queues(self,limit=None):
        """
        询队列列表

        Args:
        	limit (Integer):可选  查询记录条数，默认只为 10，最大范围100
		
        """
        method = 'GET'
        apiname = 'list_queues'
        return self.core.run(apiname, method, limit=limit)

    def describe_queue(self,qno):
        """
        询队列详情

        Args:
        	qno (String):必须  队列号
		
        """
        method = 'GET'
        apiname = 'describe_queue'
        return self.core.run(apiname, method, qno=qno)
