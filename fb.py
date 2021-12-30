#!/usr/bin/python
# By Kingtebe
import os,re,sys,requests

c = '\033[1;36m'
p = '\033[1;37m'
h = '\033[1;32m'
k = '\033[1;33m'
m = '\033[1;31m'
q = '\033[30m'
t = '\033[0;32m'
u = '\033[0;37m'
z = '\033[2;107m'
o = '\033[0m'
r = '\033[0;36m'

def get_token(cookie):
    url = "https://business.facebook.com/creatorstudio/home"
    headers = {
         "Host":"business.facebook.com",
         "cache-control":"max-age=0",
         "upgrade-insecure-requests":"1",
         "cookie":cookie,
         "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; CPH1853) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
    }
    req = requests.get(url,headers=headers)
    try:
        token = re.search('{"accessToken"\:"(EAA\w+)"',req.text).group(1)
        print(f"\n  {t}⏣ {p}Your FB token {q}: {r}"+token+f"{p}\n")
    except AttributeError:
        exit(f"  {r}~> {p}Cookie invalid \n")

if __name__=='__main__':
     os.system('cls' if os.name=='nt' else 'clear')
     print(f"\n{r}  {r}▄    ▄▄▄▄▄▄▄    ▄\n {r}▀▀▄─▄█████████▄─▄▀▀  {r}╔╗ {p}┬┌┬┐┌┐ ┌─┐┬ ┬   {r}╔═╗{p}┬ ┬┌─┐┌┐┌┌─┐┬\n {r}    ██ {k}▀{r}███{k}▀ {r}██      {r}╠╩╗{p}│ │ ├┴┐│ │└┬┘{q}───{r}║  {p}├─┤├─┤│││├┤ │\n {r}  ▄─▀████{k}▀{r}████▀─▄    {r}╚═╝{p}┴ ┴ └─┘└─┘ ┴    {r}╚═╝{p}┴ ┴┴ ┴┘└┘└─┘┴─┘\n {u}▀█    ██▀█▀██   █▀   {z}{q} By : Kingtebe | Yt : Bitboy Channel {o}{p}\n");cookie = input(f"  {t}⏣ {p}Cookie {q}: {r}")
     get_token(cookie)
