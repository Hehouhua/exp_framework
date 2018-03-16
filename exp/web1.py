from plugin import plugin
import socket
class exploit(plugin):
    param_count = 0
    timeout = 2
    socket.setdefaulttimeout(timeout)
    def __init__(self,custom_log_dir,args):
        '''
        custom_log_dir:log所在的目录
        '''
        plugin.__init__(self,custom_log_dir,args)
        
    def exp(self):
        '''
        self.host:存放目标机器的ip
        self.port:存放目标端口
        self.args:除ip，端口外的其他参数，存放于list里，通过self.args[0],self.args[1]等引用
        '''
        if len(self.args) != self.param_count:
            error_msg = "\nparam_count not matched."
            self.log(__name__,error_msg)
            return False,self.host,self.port,self.args,flag,error_msg
        flag = "flag{this is flag}"
        return True,self.host,self.port,self.args,flag,'exploit success'
        
    def noexp(self):
        return self._noexp() 
        
if __name__ == '__main__':
    print  exploit('./',('127.0.0.1',80)).probe()