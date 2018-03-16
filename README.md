ReadMe for ctf_awd_helper
=========================

-------------------------
* ReadMe 目录
	* [整体架构](#整体架构 "整体架构")
	* [目录结构](#目录结构 "目录结构")
	* [安装说明](#安装说明 "安装说明")
	* [使用说明](#使用说明 "使用说明")
	* [使用示例](#使用示例 "使用示例")
	* [版本历史](#版本历史 "版本历史")


## 整体架构
整体架构图如下：<br>
![整体架构图](/整体架构.png "架构图")

## 目录结构
* `exploit.py`			    #框架入口文件<br>
* `ReadMe.md`			    #readme文件`<br>
* `submit_flag_request.txt`	#提交flag的请求<br>
* `config`			        #配置文件所在目录<br>
	* `config.ini`		    #配置文件<br>
* `exp`				        #插件目录，每个文件对应一个exp<br>
	* `plugin.py`           #exp的基类文件<br>
	* `pwn1.py`			    #pwn1：利用插件示例<br>
	* `ssh.py`			    #ssh默认密码/弱密码利用插件<br>
	* `web1.py`			    #web1：利用插件示例<br>
	* `__init__.py`		    #空文件，不可少<br>
* `log`				        #利用日志记录目录，将记录利用插件exp函数返回的error_msg值以及一些异常，此目录由框架自动生成<br>
	* `2017`		        #记录日志的年份<br>
		* `9`		        #记录日志的月份<br>
			* `13`          #记录日志的日期<br>
				* `flag.txt`	#记录所有提交过得flag<br>
				* `port_open.txt`#记录所有开放的端口<br>
				* `pwn1.txt`	#记录pwn1.py插件利用的日志<br>
* `lib`				        #屏幕显示相关库<br>
	* `consle_width.py`<br>
	* `__init__.py`<br>
* `target`			        #攻击目标文件存放的目录<br>
	* `target_101`	        #候选target文件<br>
	* `target_102`	        #候选target文件<br>
	* `target_103`          #候选target文件<br>
	* `target_104`	        #候选target文件<br>

## 安装说明
* 1.`pip install -r requirements.txt`
## 使用说明
请先使用下面的命令设置好端口转发，其中key是rsa priv key
```shell
ssh -D 127.0.0.1:4444 -i key -p 1499 ctf@35.172.5.141
```
* 1.在攻击目标机器目录(target目录)下放置攻击目标文件
* 2.获取提交flag的http请求，并把请求放在submit_flag_request.txt里
* 3.在exp目录下放上按照相关接口写好每道题目的exp，如pwn1.py，同时在配置文件所在目录(config目录)config.ini下写好和目标机器相关配置项,如：<br>
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

## 使用示例
* `python exploit.py`				#默认参数,加载所有插件并且开启流量混淆
* `python exploit.py -e pwn1`			#只加载pwn1的exp，并且开启流量混淆
* `python exploit.py -T 0 -e pwn1`			#只加载pwn1的exp，并且不开启流量混淆
* `python exploit.py -T 2 -t 6 -e pwn1,pwn2`	#只加载pwn1,pwn2的exp，并且开启2个线程用于流量混淆，6个线程用于attack
* `python exploit.py -T 2 -t 6 -H target_101 -e pwn1,pwn2`	#只加载pwn1,pwn2的exp，并且开启2个线程用于流量混淆，6个线程用于attack,攻击target_101文件里记录的所有主机
* `python exploit.py -T 2 -t 6 -H 192.168.201.12:8888 -e pwn1`	#只加载pwn1的exp，目标192.168.201.12:8888并且开启2个线程用于流量混淆，6个线程用于attack

## 版本历史
* v1.3：
	* 把插件抽象成类，提供一些基本的操作，比如log，save_data等
	* ssh弱口令插件支持直接返回flag并提交
	* --plugins查看所有的exp文件
	* 支持从console读入攻击目标，而不是用target文件夹下面的目标文件，方便调试，例如 -H 192.168.201.12:8888
	* 项目依赖库 requirements.txt，方便部署安装使用
* v1.2:
	* 更加易用
	* exp利用不成功会等其它exp利用完了再次利用重复这个过程直到下一轮次开始
	* 配置文件统一放在config目录下
	* target文件统一放在target目录下
	* 解决flag提交处的异常：多次提交，如果提交一次flag的过程发生异常超过5次则退出程序
	* 可以通过命令参数指定target文件和config文件
* v1.1:
	* 把结果按照年份，月份，和日期分级创建目录保存
	* 把利用失败的异常信息和利用成功的异常信息一起记录
