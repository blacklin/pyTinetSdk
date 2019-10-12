'''座席设置
@Auther: lin
@Date: 2019-10-09 17:30:29.219894'''
class Agent:
    def __init__(self, core):
        self.core = core

    def create_client(self,cno,name,areaCode,password,permission,role=None,active=None,qnos=None,hiddenTel=None,wrapupTime=None,crmId=None,clidType=None,clid=None,clidArea=None,clidRule=None,recurrentselectionType=None,recurrentselectionValue=None,type=None,chatLimit=None,chatLimitNum=None):
        """
        增座席

        Args:
        	cno (Integer):必须  座席工号，4-6 位数字，要求唯一
		name (String):必须  座席名称，只允许输入中文、字母、数字、下划线，长度不超过 20 个字符
		areaCode (String):必须  所属区号
		password (String):必须  座席密码，采用AES加密，默认长度为 8 位。如果企业开启了密码安全设置，则需要按照设置的规则设置
		permission (object):必须  见permission 对象
		role (Integer):可选  座席角色，0: 普通座席；1: 班长座席，默认值为 0
		active (Integer):可选  启用状态，0: 停用；1: 启用，默认值为 1
		qnos (String[]):可选  所属队列号集合
		hiddenTel (Integer):可选  号码隐藏类型，0: 不隐藏；1: 隐藏规则与全局设置保持一致，默认值为 0
		wrapupTime (Integer):可选  整理时长，座席进行外呼操作后的整理时间。取值范围 3-300 秒，默认值为 30
		crmId (Integer):可选  CRM 编号，与第三方 CRM 系统对接时，可作为唯一标识
		clidType (Integer):可选  外显号码类型，0: 全部；2: 座席指定；3: 智能外显；默认值为 0
		clid (String[]):可选  可外显号码集合，当外显类型为非全部时为必填项
		clidArea (Object[]):可选  智能外显时且外显规则为自定义时有意义
                                          areaGroupId Integer 地区组id
                                          obClids String[] 外显号码
		clidRule (Integer):可选  外显规则，
                                        （全部）1:按次轮选；2: 按天轮选。
                                        （智能外显）1:动态；2: 自定义。
		recurrentselectionType (Integer):可选  轮选方式，1: 按次轮选；2: 按天轮选，当外显规则为轮选时为必选项
		recurrentselectionValue (Integer):可选  轮选值设置，当外显规则为轮选时为必填项
                                                 1: 按天轮选，每 n 次外呼更换一次外显号码，可设置 1-30 次
                                                 2: 按次轮选，每 n 次外呼更换一次外显号码，可设置 1-30 天
		type (Integer):可选  座席类型，1：全渠道、2：呼叫中心、3：在线客服；默认值为 2
		chatLimit (Integer):可选  在线客服座席会话上限开关，0：关闭、1：开启 ； 默认值为 0
		chatLimitNum (Integer):可选  在线客服座席会话上限； 默认值为 10
		
        """
        method = 'POST'
        apiname = 'create_client'
        return self.core.run(apiname, method, cno=cno, name=name, areaCode=areaCode, password=password, permission=permission, role=role, active=active, qnos=qnos, hiddenTel=hiddenTel, wrapupTime=wrapupTime, crmId=crmId, clidType=clidType, clid=clid, clidArea=clidArea, clidRule=clidRule, recurrentselectionType=recurrentselectionType, recurrentselectionValue=recurrentselectionValue, type=type, chatLimit=chatLimit, chatLimitNum=chatLimitNum)

    def update_client(self,cno,permission,name=None,areaCode=None,password=None,role=None,active=None,qnos=None,hiddenTel=None,wrapupTime=None,crmId=None,clidType=None,clid=None,clidArea=None,clidRule=None,recurrentselectionType=None,recurrentselectionValue=None,chatLimit=None,chatLimitNum=None):
        """
        新座席

        Args:
        	cno (Integer):必须  座席工号，4-6位数字，要求唯一
		permission (object):必须  见 permission 对象
		name (String):可选  座席名称，只允许输入中文，字母，数字，下划线，长度不超过 20 个字符
		areaCode (String):可选  所属区号
		password (String):可选  密码，采用AES加密， 465默认长度为 8 位。如果企业开启了密码安全设置，则需要按照设置的规则设置
		role (Integer):可选  座席角色，0: 普通座席；1: 班长座席。
		active (Integer):可选  启用状态， 0: 停用；1: 启用。
		qnos (String[]):可选  所属队列号集合
		hiddenTel (Integer):可选  号码隐藏类型，0: 不隐藏；1: 隐藏规则与全局设置保持一致。
		wrapupTime (Integer):可选  整理时长，座席进行外呼操作后的整理时间，取值范围 3-300 秒。
		crmId (Integer):可选  CRM 编号，与第三方 CRM 系统对接时，可作为唯一标识
		clidType (Integer):可选  外显号码类型，0: 全部；2: 座席指定；3: 智能外显；
		clid (String[]):可选  可外显号码集合，当外显类型非全部时需指定此参数值。
		clidArea (Object[]):可选  智能外显时且外显规则为自定义时有意义
                                         areaGroupId Integer 地区组id
                                         obClids String[] 外显号码
		clidRule (Integer):可选  外显规则，
                                        （全部）1:按次轮选；2: 按天轮选。
                                        （智能外显）1:动态；2: 自定义。
		recurrentselectionType (Integer):可选  轮选方式，1:查询队列详情轮选；2: 按天轮选。
		recurrentselectionValue (Integer):可选  轮选值设置。当外显规则为轮选时为必选项
                                                 1: 按天轮选，每n次外呼更换一次外显号码，可设置 1-30 次
                                                 2: 按次轮选，每n次外呼更换一次外显号码，可设置 1-30 天
		chatLimit (Integer):可选  在线客服座席会话上限开关，0：关闭、1：开启 ； 默认值为 0
		chatLimitNum (Integer):可选  在线客服座席会话上限； 默认值为 10
		
        """
        method = 'POST'
        apiname = 'update_client'
        return self.core.run(apiname, method, cno=cno, permission=permission, name=name, areaCode=areaCode, password=password, role=role, active=active, qnos=qnos, hiddenTel=hiddenTel, wrapupTime=wrapupTime, crmId=crmId, clidType=clidType, clid=clid, clidArea=clidArea, clidRule=clidRule, recurrentselectionType=recurrentselectionType, recurrentselectionValue=recurrentselectionValue, chatLimit=chatLimit, chatLimitNum=chatLimitNum)

    def delete_client(self,cno):
        """
        除座席

        Args:
        	cno (Integer):必须  座席工号，4-6 位数字
		
        """
        method = 'POST'
        apiname = 'delete_client'
        return self.core.run(apiname, method, cno=cno)

    def list_clients(self,qno=None,active=None,status=None,clid=None,bindTel=None,offset=None,limit=None):
        """
        询座席列表

        Args:
        	qno (String):可选  队列号
		active (Integer):可选  是否激活，1: 激活；0: 未激活
		status (Integer):可选  是否在线，1: 在线；0: 离线
		clid (String):可选  外显号码
		bindTel (String):可选  绑定电话
		offset (Integer):可选  偏移量，默认值为 0，最大范围 10000
		limit (Integer):可选  查询记录条数，默认值为 10，最大范围 100
		
        """
        method = 'GET'
        apiname = 'list_clients'
        return self.core.run(apiname, method, qno=qno, active=active, status=status, clid=clid, bindTel=bindTel, offset=offset, limit=limit)

    def describe_client(self,qno=None,active=None,status=None,clid=None,bindTel=None,offset=None,limit=None):
        """
        询座席详情

        Args:
        	qno (String):可选  队列号
		active (Integer):可选  是否激活，1: 激活；0: 未激活
		status (Integer):可选  是否在线，1: 在线；0: 离线
		clid (String):可选  外显号码
		bindTel (String):可选  绑定电话
		offset (Integer):可选  偏移量，默认值为 0，最大范围 10000
		limit (Integer):可选  查询记录条数，默认值为 10，最大范围 100
		
        """
        method = 'GET'
        apiname = 'describe_client'
        return self.core.run(apiname, method, qno=qno, active=active, status=status, clid=clid, bindTel=bindTel, offset=offset, limit=limit)

    def bind_client_tel(self,cno,tel,isBind=None):
        """
        定座席电话

        Args:
        	cno (String):必须  座席号
		tel (String):必须  电话号码
		isBind (Integer):可选  是否绑定 1: 是，0: 否
		
        """
        method = 'POST'
        apiname = 'bind_client_tel'
        return self.core.run(apiname, method, cno=cno, tel=tel, isBind=isBind)

    def unbind_client_tel(self,cno,tel,isBind=None):
        """
        绑座席电话

        Args:
        	cno (String):必须  座席号
		tel (String):必须  电话号码
		isBind (Integer):可选  是否绑定 1: 是，0: 否
		
        """
        method = 'POST'
        apiname = 'unbind_client_tel'
        return self.core.run(apiname, method, cno=cno, tel=tel, isBind=isBind)

    def delete_client_tel(self,cno,tel):
        """
        除座席电话

        Args:
        	cno (String):必须  座席号
		tel (String):必须  电话
		
        """
        method = 'POST'
        apiname = 'delete_client_tel'
        return self.core.run(apiname, method, cno=cno, tel=tel)

    def list_client_tels(self,cno,telType=None):
        """
        询座席电话列表

        Args:
        	cno (String):必须  座席号
		telType (Integer):可选  电话类型 1: 固话；2: 手机；3: 分机；4: 软电话
		
        """
        method = 'GET '
        apiname = 'list_client_tels'
        return self.core.run(apiname, method, cno=cno, telType=telType)

    def bind_client_tel_verification(self,cno,tel):
        """
        起绑定电话验证

        Args:
        	cno (String):必须  座席号
		tel (String):必须  电话
		
        """
        method = 'GET '
        apiname = 'bind_client_tel_verification'
        return self.core.run(apiname, method, cno=cno, tel=tel)

    def bind_client_tel_confirmed(self,cno,tel,verificationCode):
        """
        认绑定电话验证

        Args:
        	cno (String):必须  座席号
		tel (String):必须  电话号码
		verificationCode (String):必须  验证码
		
        """
        method = 'POST'
        apiname = 'bind_client_tel_confirmed'
        return self.core.run(apiname, method, cno=cno, tel=tel, verificationCode=verificationCode)
