'''通话录音
@Auther: lin
@Date: 2019-10-09 17:30:29.491894'''
class Record:
    def __init__(self, core):
        self.core = core

    def download_record_file(self,mainUniqueId,recordSide=None):
        """
        下载通话录音文件

        Args:
        	mainUniqueId (String):必须  通话记录唯一标识
		recordSide (Integer):可选  不传该参数时获取普通mp3格式通话录音，传参数时获取双轨录音的某一侧录音：1-客户侧，2-座席侧
		
        """
        method = 'GET'
        apiname = 'download_record_file'
        return self.core.run(apiname, method, mainUniqueId=mainUniqueId, recordSide=recordSide)

    def describe_record_file_url(self,mainUniqueId,recordSide=None):
        """
        查询通话录音地址

        Args:
        	mainUniqueId (String):必须  通话记录唯一标识
		recordSide (Integer):可选  不传该参数时获取普通mp3格式通话录音，传参数时获取双轨录音的某一侧录音：1-客户侧，2-座席侧
		
        """
        method = 'GET'
        apiname = 'describe_record_file_url'
        return self.core.run(apiname, method, mainUniqueId=mainUniqueId, recordSide=recordSide)
