ReadMe for ctf_awd_helper
=========================

-------------------------
* ReadMe Ŀ¼
	* [����ܹ�](#����ܹ� "����ܹ�")
	* [Ŀ¼�ṹ](#Ŀ¼�ṹ "Ŀ¼�ṹ")
	* [��װ˵��](#��װ˵�� "��װ˵��")
	* [ʹ��˵��](#ʹ��˵�� "ʹ��˵��")
	* [ʹ��ʾ��](#ʹ��ʾ�� "ʹ��ʾ��")
	* [�汾��ʷ](#�汾��ʷ "�汾��ʷ")


## ����ܹ�
����ܹ�ͼ���£�<br>
![����ܹ�ͼ](/����ܹ�.png "�ܹ�ͼ")

## Ŀ¼�ṹ
* `exploit.py`			    #�������ļ�<br>
* `ReadMe.md`			    #readme�ļ�`<br>
* `submit_flag_request.txt`	#�ύflag������<br>
* `config`			        #�����ļ�����Ŀ¼<br>
	* `config.ini`		    #�����ļ�<br>
* `exp`				        #���Ŀ¼��ÿ���ļ���Ӧһ��exp<br>
	* `plugin.py`           #exp�Ļ����ļ�<br>
	* `pwn1.py`			    #pwn1�����ò��ʾ��<br>
	* `ssh.py`			    #sshĬ������/���������ò��<br>
	* `web1.py`			    #web1�����ò��ʾ��<br>
	* `__init__.py`		    #���ļ���������<br>
* `log`				        #������־��¼Ŀ¼������¼���ò��exp�������ص�error_msgֵ�Լ�һЩ�쳣����Ŀ¼�ɿ���Զ�����<br>
	* `2017`		        #��¼��־�����<br>
		* `9`		        #��¼��־���·�<br>
			* `13`          #��¼��־������<br>
				* `flag.txt`	#��¼�����ύ����flag<br>
				* `port_open.txt`#��¼���п��ŵĶ˿�<br>
				* `pwn1.txt`	#��¼pwn1.py������õ���־<br>
* `lib`				        #��Ļ��ʾ��ؿ�<br>
	* `consle_width.py`<br>
	* `__init__.py`<br>
* `target`			        #����Ŀ���ļ���ŵ�Ŀ¼<br>
	* `target_101`	        #��ѡtarget�ļ�<br>
	* `target_102`	        #��ѡtarget�ļ�<br>
	* `target_103`          #��ѡtarget�ļ�<br>
	* `target_104`	        #��ѡtarget�ļ�<br>

## ��װ˵��
* 1.`pip install -r requirements.txt`
## ʹ��˵��
����ʹ��������������úö˿�ת��������key��rsa priv key
```shell
ssh -D 127.0.0.1:4444 -i key -p 1499 ctf@35.172.5.141
```
* 1.�ڹ���Ŀ�����Ŀ¼(targetĿ¼)�·��ù���Ŀ���ļ�
* 2.��ȡ�ύflag��http���󣬲����������submit_flag_request.txt��
* 3.��expĿ¼�·��ϰ�����ؽӿ�д��ÿ����Ŀ��exp����pwn1.py��ͬʱ�������ļ�����Ŀ¼(configĿ¼)config.ini��д�ú�Ŀ��������������,�磺<br>
	`[pwn1]`<br>
	   `port=8888`
	   
`Usage: exploit.py [options]`<br><br>
`ctf_awd_helper: a fast tool to exploit many targets,any bug please contact houhua.he@meetsec.com`<br>
`Options:`<br><br>
`  -h, --help            show this help message and exit`<br>
`  -c CONFIG_FILE, --config=CONFIG_FILE,config file in Directory ./config/ to use(default:config.ini)`<br>
`  -H TARGET_FILE, --host=TARGET_FILE,target file in Directory ./target/ to use(default:target).Note:If you just want to test with a single ip and port immediately,you can use like this "-H 192.168.0.100:80"`<br>
`  -t SCAN_THREAD, --scanthread=SCAN_THREAD,Threads number to scan(default: 63)`<br>
`  -T CONFUSE_THREAD, --confusethread=CONFUSE_THREAD,Threads number to confuse(default: 15)`<br>
`  -e EXP, --exp=EXP     which exp to exploit,no .py needed,eg:pwn1,pwn2`<br>

## ʹ��ʾ��
* `python exploit.py`				#Ĭ�ϲ���,�������в�����ҿ�����������
* `python exploit.py -e pwn1`			#ֻ����pwn1��exp�����ҿ�����������
* `python exploit.py -T 0 -e pwn1`			#ֻ����pwn1��exp�����Ҳ�������������
* `python exploit.py -T 2 -t 6 -e pwn1,pwn2`	#ֻ����pwn1,pwn2��exp�����ҿ���2���߳���������������6���߳�����attack
* `python exploit.py -T 2 -t 6 -H target_101 -e pwn1,pwn2`	#ֻ����pwn1,pwn2��exp�����ҿ���2���߳���������������6���߳�����attack,����target_101�ļ����¼����������
* `python exploit.py -T 2 -t 6 -H 192.168.201.12:8888 -e pwn1`	#ֻ����pwn1��exp��Ŀ��192.168.201.12:8888���ҿ���2���߳���������������6���߳�����attack

## �汾��ʷ
* v1.3��
	* �Ѳ��������࣬�ṩһЩ�����Ĳ���������log��save_data��
	* ssh��������֧��ֱ�ӷ���flag���ύ
	* --plugins�鿴���е�exp�ļ�
	* ֧�ִ�console���빥��Ŀ�꣬��������target�ļ��������Ŀ���ļ���������ԣ����� -H 192.168.201.12:8888
	* ��Ŀ������ requirements.txt�����㲿��װʹ��
* v1.2:
	* ��������
	* exp���ò��ɹ��������exp���������ٴ������ظ��������ֱ����һ�ִο�ʼ
	* �����ļ�ͳһ����configĿ¼��
	* target�ļ�ͳһ����targetĿ¼��
	* ���flag�ύ�����쳣������ύ������ύһ��flag�Ĺ��̷����쳣����5�����˳�����
	* ����ͨ���������ָ��target�ļ���config�ļ�
* v1.1:
	* �ѽ��������ݣ��·ݣ������ڷּ�����Ŀ¼����
	* ������ʧ�ܵ��쳣��Ϣ�����óɹ����쳣��Ϣһ���¼
