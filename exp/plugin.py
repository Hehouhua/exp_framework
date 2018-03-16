#coding=utf-8
class plugin:
    param_count = 0
    timeout=1
    def __init__(self,custom_log_dir,args): 
        self.log_dir=custom_log_dir
        self.host = args[0]
        self.port = int(args[1])
        if self.param_count:
            self.args = args[2:]
        else:
            self.args = []
			
    def _write_log(self,filename,msg):
        try:
           with open(filename,'a') as f:
               f.write(msg)
        except:
            pass
			
    def _write_data(self,filename,data):
       try:
          with open(filename,'wb') as f:
              f.write(data)
       except:
           pass
		
	#just use self.log(__name__,"anything") to log anything you want		
    def log(self,filename,msg):
        import time
        now=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        param = "%s,%s,%s" % (self.host,self.port,self.args)
        self._write_log(self.log_dir+'/'+filename+"_debug.log",",".join([now,param,msg])+'\n')
		
    #just use self.save_data(__name__,"1.txt","anything") to write data you want
    def save_data(self,sub_dir,filename,data):
        import os
        if not os.path.exists(self.log_dir+"/"+sub_dir):
            os.makedirs(self.log_dir+"/"+sub_dir)
        self._write_data(self.log_dir+'/'+sub_dir+"/"+filename,data)
    
	#(self.host,self.port,self.args,flag,"Any string you want to record")
    def exp(self):
        if len(self.args) != self.param_count:
            error_msg = "\nparam_count not matched."
            self.log(__name__,error_msg)
            return False,self.host,self.port,self.args,flag,error_msg
        flag = "flag{this is flag}"
        return True,self.host,self.port,self.args,flag,'interface defined in plugin.py'
		
    def noexp(self):
        return self._noexp() 
    
        
    '''
    这是预定义的混淆流量函数，可以临时拿来用，尽可能发和题目有点关系的流量，推荐在exp函数基础上更改
    '''    
    def _noexp(self):
        import random
        import socket
        send=""
        for i in range(0,12):
            send=send+chr(random.randint(99,122))        
        send=send+"A"*32+"\x23\x16\x16\x27"
        for i in range(0,64):
            send=send+chr(random.randint(0,127))        
        try:
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((self.host,self.port))
            s.sendall(send)      
            s.close()
            return True,self.host,self.port,"confuse OK"
        except Exception,e:
            return False,self.host,self.port,str(e) 