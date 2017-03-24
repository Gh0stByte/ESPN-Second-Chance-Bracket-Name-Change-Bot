import requests
import random
import string
import json
import os
import http.cookiejar
import time
import http.cookies
import urllib


#CONFIG
base_url = 'http://games.espn.com/second-chance-bracket/2017/en/entryname'
bracket_id = '1861827'
timeout = 2
#You'll need the espn_s2 and espnAuth keyvalues from your logged in cookie. Use fiddler to grab them. 
my_cookies =  {
"espn_s2": "", 
"espnAuth": ""
}



s=requests.session()
requests.utils.add_dict_to_cookiejar(s.cookies, my_cookies)
s.verify=False

s.headers.update({'Referer':'http://games.espn.com/second-chance-bracket/2017/en/entryname?entryID=%s' % bracket_id,'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36','Content-Type':'application/x-www-form-urlencoded'})

lennys = ["( ͡° ͜ʖ ͡°)", "(⌐■_■)", "¯\_ツ_/¯", "ಠ_ಠ", "ʢ◉ᴥ◉ʡ", "^‿^", "(づ◔ ͜ʖ◔)づ", "⤜(ʘ_ʘ)⤏", "☞   ͜ʖ  ☞", "ᗒ ͟ʖᗕ", "ᕙ(⍜!⍜)ᕗ", "(♥╭͜ʖ╮♥)", "( ͡°ᗜ ͡°)", ">ツ>", "(ꔸ ͟ʖꔸ)", "(✧╭͜ʖ╮✧)",
		 "(☯ ͜つ☯)", "( ͡°Ѡ ͡°)", "【 ͡°‿ ͡°】", "¯\_ꖘᗜꖘ_/¯", "ᑫ□Ĺ̯□ᑷ", "(╭☞ᵔᗜᵔ)╭☞", "¯\_⏒ᴥ⏒_/¯", "¯\_⏒ᴥ⏒_/¯", "୧⏒ᴥ⏒୨", "(/͠- ͟ʖ ͝-\)", "¯\_>ヮ<_/¯", "¯\_>ヮ<_/¯", "(╯⇀ᴥ↼）╯︵ ┻━┻", "└[ ͠°෴ °]┘",
		  "⤜(ʘ_ʘ)⤏", "ᑫ⏓ ͜つ⏓ᑷ", "\( º ◞  º )/", "(งᴗ⍘ᴗ)ง", "⎝☉ ʖ̯☉⎠", "(✿_✿)", "(✧ᗜ✧)", "ᕕ(`◡´)ᕗ", "( ͡°෴ ͡°)", "ᕕ(`⏏´)ᕗ", "ᕕ(￣╭╮￣)ᕗ", "ᕕ(`▾´)ᕗ", "\(✧ᗜ✧)/", "⤜(♥ヘ♥)⤏", "ᕮ⇀ ͜つ↼ᕭ", "Lucky Winner", "Try Again!", "You're soo close!", "I'm a Gh0st", "Don't see anything", "t̸̨̨̧̨̨̛̛̛̛̛̛̛͙͚̩̣̘̝̱̪͚̭̱̳̩͈͇̫͓̳̬̖̤̫͓͔͎̝͙̤͈̙͎̪̗̥̺̞̲̟̱̳̲͍͙͖̙̩̹̳̮̗͉̘̙̼͔̜̪̞̫͓̖̼͉̪̖͎̲̹̲̱͍̳̞̮͉̥̦̬͚̙̞̹̠̫͇͍̭̩̰̖͌̌̉̍̌̐͌̌̓͂̇̃͊̏̂̔͐̄̈͛̈͋͋̂͒͛̍͑͆̅͛̌͊̎͆̓̇̾͋̔͊̃̊̑̽͑̇͌̋͋̽̈̃́̆̈́̃͊͋̔͊̐̑̀̾͛̔̽̈́̍̓̋̎̇̈́̓̇̒͑̄͑̉͆̾̽̓͗̀̾̽̀͆̓͐̆̈̍̾̑̓̓͒̽͗͋̐̂͗̃̔͌̎͑̇͌͆̒̈́̾͂̾̌̂̓̓͒̄͑̋̆̔̂̃̆͆͋̾̈́̏͛̆̎͋̈́͛̌͂̏̊͆͛͊̋͐̃́̊̈́͋̐̅̐̐́̿̑̎̆͛̚͘̚̕̕̕͘̚̚͘̚͘̕͜͜͜͝͝͝͝͠͝͝͠͠͝͝͠͠͠͝͝ͅͅͅͅͅë̵̢̨̡̢̢̨͎̗̪̼̣̤̪̠̰̯͚͎̰̪̟̘̦̺̟̲̜͔̺̺̞͉̠̺͇͔̜͍̰̫͙̲̪̠͍̱͔́̽͊̑̆̊͒̂̾͌̓͋͂̾͑͋͗̾͐̅̋̔̈́̇̈͐͒̏̾̏̇̂͘̕͘͘͜͝ͅs̸̨̧̧̡̨̢̧̡̙̺̖̠̹͓̙͈̞̜͔̩̰͓̺̙̘̻̬̠̺̪̯̣͉̦͍͚̣̤͉̺͚̻̜͍̪͚̤̟̟͖͙͚͛̃̈́̾̂̊͂́̒̉̏͋̈́͌͗̇̌͂̉̿̔̃̔͊̍̎͐̿̌̀̓̊͆̓͐͛͐͂͗̐͑̀̂̅͑͆̎̓͌͋̈́̀͒̀͌́́̊̋̐͗̑̽́̔͌̿̂̒̍͑̀̋͂̿̌̿̌̅̈́̍̍́̍̏͊͐̒̓͂̓̏͘͜͝͠͝͠͝͠͝͠ͅţ̷̡̢̨̧̧̨̧̡̢̧̢̧̡̢̢̧̧̛̼̠͓̗͔̦̮̟̗͓̠̟͇̟̭̝̮̱̪͕̯͍͔̟̳̩̠̩͉̠͈͎̗̗̭͈͎̟͔̜͍͎̫͓̘̞͚̦͎̰̘̰̼̲̖̪̫̣̣̯͙̞̜̭̘̺̰̜͇͖͖͓̘̜͔̮̦͙̬̱̱̪̪̠͚̯̣̼͈̮̜͎̞̻̙͈̻͇̱͓͙̣̞̠͔̞̠͇͔̤͖̖̺̪̹̙̖̲̝̠̘̰͕̩̟̥͚̭̜͙̳̣̰̫̩̙̜͔̣͔̹̲͇̝̪̙̪̗͇̭̬̰͕̟͕̞̟̥̻͖̻̟̯͖̪̹̹̩͈̺̪͙̦͎͓͎̙͙̖̬̮̹̪̗̫̘͔͎̠͓̠̭̲̔̊͌͒̽̀̈́̐͒̈̃̋̄̒̄̐͐̄̽̓͐͌͛̈́̌͂͋͐̈́̈́̑͌̊̿͂̀͒̀̅́͑͑͌́͑̏͐͛͑̊̀̿́̏̀̀̓̉̋̎͆̇̋͋̅̈̆̐͐̏̊͊̀̇͆̌͘͘̕͘͜͜͜͜͜͜͜͜͝͠͝͝ͅͅͅͅͅͅͅ"]

def random_face():
	return random.choice(lennys)

def change_face(face):
	data='nickname=%s&fansgroup=-1&incoming=1&entryID=%s' % (urllib.parse.quote_plus(face), bracket_id)
	r=s.post(base_url,data=data)
	
def main():
	while(1):
		currentFace = random_face()
		print("Changing Face to: ", currentFace)
		change_face(currentFace)
		print("Done!")
		time.sleep(timeout)
	
if __name__ == '__main__':
	main()
