import os
class InstaGram():
	def Login(user,pas):
		from requests import (post,get,Session);from user_agent import generate_user_agent;from  random import (choice,randint);from time import sleep;req = get("https://www.instagram.com/api/v1/web/accounts/login/ajax/",headers={'user-agent':str(generate_user_agent())}).cookies.get_dict();mid = req['mid'];csrf = req['csrftoken'];ig_did = req['ig_did'];ds = ''.join(choice('1234567890') for i in range(int(randint(10,11))));print("-"*38+"\n[~] Login in progress...");sleep(2);login=post("https://www.instagram.com/api/v1/web/accounts/login/ajax/",headers={'accept':'*/*','accept-encoding':'gzip, deflate, br','accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7','content-length':'321','content-type':'application/x-www-form-urlencoded','cookie':f'mid={mid}; ig_did={ig_did};csrftoken={csrf}; ds_user_id={ds}; rur="ASH,{ds},1706962089:01f7d81286a041d0f9393edae56c5d0f069d740b29aef8270f729efdba61423df98086b3"','origin':'https://www.instagram.com','referer':'https://www.instagram.com/accounts/login/?__coig_restricted=1','sec-ch-prefers-color-scheme':'dark','sec-ch-ua':'"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Linux"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','user-agent':str(generate_user_agent()),'viewport-width':'980','x-asbd-id':'198387','x-csrftoken':str(csrf),'x-ig-app-id':'936619743392459','x-ig-www-claim':'hmac.AR2lZ6PfEzH1iXfHfCOswttdqH2gbtYywELaivmqD5s1Coik','x-instagram-ajax':'1006907988','x-requested-with':'XMLHttpRequest',},data = {'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:'+pas,'username':user,'queryParams': '{}','optIntoOneTap': False,'stopDeletionNonce': "",'trustedDeviceRecords': '{}'});
		if "userId" in login.text:
			Coki = login.cookies.get_dict();csrf=Coki['csrftoken'];sis=Coki['sessionid'];ds_user=Coki['ds_user_id']
			return {"msg":True,"csrf":csrf,"mid":mid,"ig_did":ig_did,"sis":sis,"ds_user":ds_user}
		elif 'ip_block' in login.text:
			return {"msg":"Ip"}
		elif 'challenge' in login.text:
			return {"msg":'challenge'}
		elif '"user":true' in login.text:
			return {"msg":"user_true"}
		elif '"user":false' in login.text:
			return {"msg":"user_false"}
		elif "message" in login.text:
			return {"msg":"msg"}
		else:
			return {"msg":'Error',"Errors":login.text}
	def Get_Id_Following(csrf,mid,ig_did,ds_user,sis,User):
		from requests import (post,get,Session);from user_agent import generate_user_agent;from  random import (choice,randint);from time import sleep
		hea={'accept':'*/*','accept-encoding':'gzip, deflate, br','accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7','cookie':f'mid={mid}; ig_did={ig_did}; ig_nrcb=1; datr=H9vzYq35j3WCu3W5Jw-BuqMb; dpr=1.75; csrftoken={csrf}; ds_user_id={ds_user}; shbid="2195,10851247180,1693733333:01f781e1606e53e58d1108b28b348650b4413de9e963e2af156f7f8349ac2dcc009bb77c"; shbts="1662197333,10851247180,1693733333:01f7922667728add527198adb9bb332520bd0b4a233ecb4c650da3524912630fa3ac7645"; sessionid={sis}; rur="RVA,10851247180,1693912293:01f78ed1bfb4b31b309a892edebcbf222a838f50d84e29bcbbf806e997099b1b5deca4b9"','origin':'https://www.instagram.com','referer':'https://www.instagram.com/','sec-ch-ua':'"Chromium";v="105", "Not)A;Brand";v="8"','sec-ch-ua-mobile':'?1','sec-ch-ua-platform':'"Android"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-site','user-agent':str(generate_user_agent()),'x-asbd-id':'198387','x-csrftoken':str(csrf),'x-ig-app-id':'1217981644879628','x-ig-www-claim':'hmac.AR16wNjyuckc0qk4ogcBIWjOuYHm4V6EFi8U2XCJriHI4KVv','x-instagram-ajax':'1006141724'}
		FD = get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={User}",headers={'accept':'*/*','accept-encoding':'gzip, deflate, br','accept-language':'ar,en;q=0.9','origin':'https://www.instagram.com','referer':'https://www.instagram.com/','sec-ch-ua':'"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-site','user-agent': str(generate_user_agent()),'x-csrftoken':str(csrf),'x-ig-app-id':'936619743392459','x-ig-www-claim':'hmac.AR1cjP7xqazJ469Nhp3UMEg014y0pAUnf-plXYyvO3tupGkS'}).json()
		IID = FD['data']['user']['id']
		cont =FD['data']['user']['edge_follow']['count']
		re = get(f'https://i.instagram.com/api/v1/friendships/{IID}/following/?count={cont}',headers=hea).json()['users']
		for i in re:
				uss = i['username']
				sleep(int(randint(9,20)))
				rr = get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={uss}",headers={'accept':'*/*','accept-encoding':'gzip, deflate, br','accept-language':'ar,en;q=0.9','origin':'https://www.instagram.com','referer':'https://www.instagram.com/','sec-ch-ua':'"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-site','user-agent': str(generate_user_agent()),'x-csrftoken':str(csrf),'x-ig-app-id':'936619743392459','x-ig-www-claim':'hmac.AR1cjP7xqazJ469Nhp3UMEg014y0pAUnf-plXYyvO3tupGkS'}).json();rr['data']['user']['id'];InstaGram.Following(csrf,mid,ig_did,ds_user,sis,rr['data']['user']['id'],uss)
		
	def Following(csrf,mid,ig_did,ds_user,sis,Id,uss):
		    from requests import (post,get,Session);from user_agent import generate_user_agent;from  random import (choice,randint)
		    had = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-GB,en-US;q=0.9,en;q=0.8','content-length': '0','content-type': 'application/x-www-form-urlencoded','cookie': f'ig_did={ig_did}; mid={mid}; ig_nrcb=1; csrftoken={csrf}; ds_user_id={ds_user}; sessionid={sis}; rur=RVA','origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36','x-csrftoken': str(csrf),'x-ig-app-id': '936619743392459','x-ig-www-claim': 'hmac.AR2Ba9nmJROdSoghzs45qrHKC88BhLBeE0C1g5XLvznnHW1d','x-instagram-ajax': '0edc1000e5e7','x-requested-with': 'XMLHttpRequest'}
		    follo = post(f'https://www.instagram.com/web/friendships/{Id}/follow/',headers=had);US = uss.upper()
		    if follo.status_code == 200:
		    	print('\033[2;36m'+f"- DONE FOLLOWING =>"+'\033[1;31m'+"{US}")
		    elif follo.status_code == 400:
		    	print('\033[1;31m'+"- YOUR ACCOUNT CAN'T FOLLOWING USERS"+'\033[2;36m'+"=> "+'\033[1;31m'+"{US} !")
		    else:
		    	print('\033[1;33m'+"DON'T FOLLOWING !")
	def Story(csrf,mid,ig_did,ds_user,sis,User):
		from requests import (post,get,Session);from user_agent import generate_user_agent;from  random import (choice,randint);from time import sleep
		FD = get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={User}",headers={'accept':'*/*','accept-encoding':'gzip, deflate, br','accept-language':'ar,en;q=0.9','origin':'https://www.instagram.com','referer':'https://www.instagram.com/','sec-ch-ua':'"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-site','user-agent': str(generate_user_agent()),'x-csrftoken':str(csrf),'x-ig-app-id':'936619743392459','x-ig-www-claim':'hmac.AR1cjP7xqazJ469Nhp3UMEg014y0pAUnf-plXYyvO3tupGkS'}).json();IID = FD['data']['user']['id'];cont = FD['data']['user']['edge_follow']['count'];hea = {'accept':'*/*','accept-encoding':'gzip, deflate, br','accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7','cookie':f'mid=YvPaYAABAAG3pnL6OA7VEBlLVuDo; ig_did=47F0CEA6-3B69-4576-A88E-23F3CE15444E; ig_nrcb=1; datr=H9vzYq35j3WCu3W5Jw-BuqMb; dpr=1.75; csrftoken=BoAPbH25tOOL4jUvTQTtrbEqLN44pjnT; ds_user_id=10851247180; shbid="2195,10851247180,1693733333:01f781e1606e53e58d1108b28b348650b4413de9e963e2af156f7f8349ac2dcc009bb77c"; shbts="1662197333,10851247180,1693733333:01f7922667728add527198adb9bb332520bd0b4a233ecb4c650da3524912630fa3ac7645"; sessionid={sis}; rur="RVA,{ds_user},1693912293:01f78ed1bfb4b31b309a892edebcbf222a838f50d84e29bcbbf806e997099b1b5deca4b9"','origin':'https://www.instagram.com','referer':'https://www.instagram.com/','sec-ch-ua':'"Chromium";v="105", "Not)A;Brand";v="8"','sec-ch-ua-mobile':'?1','sec-ch-ua-platform':'"Android"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-site','user-agent':str(generate_user_agent()),'x-asbd-id':'198387','x-csrftoken':str(csrf),'x-ig-app-id':'1217981644879628','x-ig-www-claim':'hmac.AR16wNjyuckc0qk4ogcBIWjOuYHm4V6EFi8U2XCJriHI4KVv','x-instagram-ajax':'1006141724'}
		re = get(f'https://i.instagram.com/api/v1/friendships/{IID}/following/?count={cont}',headers=hea).json()['users']
		for i in re:
			uuss = i['username']
			hd = {'accept':'*/*','accept-encoding':'gzip, deflate, br','accept-language':'ar,en;q=0.9','origin':'https://www.instagram.com','referer':'https://www.instagram.com/','sec-ch-ua':'"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-site','user-agent': str(generate_user_agent()),'x-csrftoken':str(csrf),'x-ig-app-id':'936619743392459','x-ig-www-claim':'hmac.AR1cjP7xqazJ469Nhp3UMEg014y0pAUnf-plXYyvO3tupGkS'};id_user = get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={uuss}",headers=hd).json()['data']['user']['id'];d = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language':'en-US,en;q=0.9,ar;q=0.8','cookie':f"sessionid={sis};ds_user_id={ds_user};csrftoken={csrf};",'user-agent':str(generate_user_agent())};surl = f'https://www.instagram.com/graphql/query/?query_hash=c9c56db64beb4c9dea2d17740d0259d9&variables=%7B%22reel_ids%22%3A%5B%22{id_user}%22%5D%2C%22tag_names%22%3A%5B%5D%2C%22location_ids%22%3A%5B%5D%2C%22highlight_reel_ids%22%3A%5B%5D%2C%22precomposed_overlay%22%3Afalse%2C%22show_story_viewer_list%22%3Atrue%2C%22story_viewer_fetch_count%22%3A50%2C%22story_viewer_cursor%22%3A%22%22%2C%22stories_video_dash_manifest%22%3Afalse%7D';
			try:
				DF = get(surl,headers=d).json();stry =  len(DF["data"]["reels_media"][0]["items"])
				for i in range(0,stry):
					id_story=DF["data"]["reels_media"][0]["items"][i]['id'];taken_at_timestamp = DF["data"]["reels_media"][0]["items"][i]['taken_at_timestamp'];heades = {'accept':'*/*','accept-encoding':'gzip, deflate, br','accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7','content-length':'127','content-type':'application/x-www-form-urlencoded','cookie':f"sessionid={sis};ds_user_id={ds_user};csrftoken={csrf};",'origin':'https://www.instagram.com','referer':'https://www.instagram.com/','sec-ch-ua':'"Chromium";v="105", "Not)A;Brand";v="8"','sec-ch-ua-mobile':'?1','sec-ch-ua-platform':'"Android"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-site','user-agent':str(generate_user_agent()),'x-asbd-id':'198387','x-csrftoken':str(csrf),'x-ig-app-id':'1217981644879628','x-ig-www-claim':'hmac.AR16wNjyuckc0qk4ogcBIWjOuYHm4V6EFi8U2XCJriHI4Cpd','x-instagram-ajax':'1006164169',}
					Data = {'reelMediaId':str(id_story),'reelMediaOwnerId':str(id_user),'reelId':str(id_user),'reelMediaTakenAt':str(taken_at_timestamp),'viewSeenAt':str(taken_at_timestamp)}
					sleep(int(randint(7,17)))
					sry = post("https://www.instagram.com/stories/reel/seen",headers=heades,data=Data)
					US = uuss.upper()
					if sry.status_code == 200:
						print('\033[2;36m'+f"- THE STORY HAS BEEN SEEN "+'\033[1;31m'+"=> "+'\033[2;36m'+f"{US}")
					else:
						print('033[1;33m'+f"- The Story Has Not Been Seen "+'\033[1;31m'+"=> "+'033[1;33m'+f"{US}")
				
			except:
				pass
			
	def Like_Story(csrf,mid,ig_did,ds_user,sis,User):
		from requests import (post,get,Session);from user_agent import generate_user_agent;from  random import (choice,randint);from time import sleep
		FD = get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={User}",headers={'accept':'*/*','accept-encoding':'gzip, deflate, br','accept-language':'ar,en;q=0.9','origin':'https://www.instagram.com','referer':'https://www.instagram.com/','sec-ch-ua':'"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-site','user-agent': str(generate_user_agent()),'x-csrftoken':str(csrf),'x-ig-app-id':'936619743392459','x-ig-www-claim':'hmac.AR1cjP7xqazJ469Nhp3UMEg014y0pAUnf-plXYyvO3tupGkS'}).json();IID = FD['data']['user']['id'];cont = FD['data']['user']['edge_follow']['count'];hea = {'accept':'*/*','accept-encoding':'gzip, deflate, br','accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7','cookie':f'mid=YvPaYAABAAG3pnL6OA7VEBlLVuDo; ig_did=47F0CEA6-3B69-4576-A88E-23F3CE15444E; ig_nrcb=1; datr=H9vzYq35j3WCu3W5Jw-BuqMb; dpr=1.75; csrftoken=BoAPbH25tOOL4jUvTQTtrbEqLN44pjnT; ds_user_id=10851247180; shbid="2195,10851247180,1693733333:01f781e1606e53e58d1108b28b348650b4413de9e963e2af156f7f8349ac2dcc009bb77c"; shbts="1662197333,10851247180,1693733333:01f7922667728add527198adb9bb332520bd0b4a233ecb4c650da3524912630fa3ac7645"; sessionid={sis}; rur="RVA,{ds_user},1693912293:01f78ed1bfb4b31b309a892edebcbf222a838f50d84e29bcbbf806e997099b1b5deca4b9"','origin':'https://www.instagram.com','referer':'https://www.instagram.com/','sec-ch-ua':'"Chromium";v="105", "Not)A;Brand";v="8"','sec-ch-ua-mobile':'?1','sec-ch-ua-platform':'"Android"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-site','user-agent':str(generate_user_agent()),'x-asbd-id':'198387','x-csrftoken':str(csrf),'x-ig-app-id':'1217981644879628','x-ig-www-claim':'hmac.AR16wNjyuckc0qk4ogcBIWjOuYHm4V6EFi8U2XCJriHI4KVv','x-instagram-ajax':'1006141724'}
		re = get(f'https://i.instagram.com/api/v1/friendships/{IID}/following/?count={cont}',headers=hea).json()['users']
		for i in re:
			uuss = i['username']
			hd = {'accept':'*/*','accept-encoding':'gzip, deflate, br','accept-language':'ar,en;q=0.9','origin':'https://www.instagram.com','referer':'https://www.instagram.com/','sec-ch-ua':'"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-site','user-agent': str(generate_user_agent()),'x-csrftoken':str(csrf),'x-ig-app-id':'936619743392459','x-ig-www-claim':'hmac.AR1cjP7xqazJ469Nhp3UMEg014y0pAUnf-plXYyvO3tupGkS'};id_user = get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={uuss}",headers=hd).json()['data']['user']['id'];d = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language':'en-US,en;q=0.9,ar;q=0.8','cookie':f"sessionid={sis};ds_user_id={ds_user};csrftoken={csrf};",'user-agent':str(generate_user_agent())};surl = f'https://www.instagram.com/graphql/query/?query_hash=c9c56db64beb4c9dea2d17740d0259d9&variables=%7B%22reel_ids%22%3A%5B%22{id_user}%22%5D%2C%22tag_names%22%3A%5B%5D%2C%22location_ids%22%3A%5B%5D%2C%22highlight_reel_ids%22%3A%5B%5D%2C%22precomposed_overlay%22%3Afalse%2C%22show_story_viewer_list%22%3Atrue%2C%22story_viewer_fetch_count%22%3A50%2C%22story_viewer_cursor%22%3A%22%22%2C%22stories_video_dash_manifest%22%3Afalse%7D';
			try:
				DF = get(surl,headers=d).json();stry =  len(DF["data"]["reels_media"][0]["items"])
				for i in range(0,stry):
					id_story=DF["data"]["reels_media"][0]["items"][i]['id'];taken_at_timestamp = DF["data"]["reels_media"][0]["items"][i]['taken_at_timestamp'];heades = {'accept':'*/*','accept-encoding':'gzip, deflate, br','accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7','content-length':'28','content-type':'application/x-www-form-urlencoded','cookie':f'mid=Y9C6wQABAAGdLQv-MCkdTCQh3eT8; ig_did=F4FBD7AC-4297-4977-8D7F-480FD15702A5; datr=0LrQY0KimobRI_ynMmIj1Y78; ds_user_id={ds_user}; dpr=1.75; csrftoken={csrf}; sessionid={sis}; rur="NAO,57949618010,1707583888:01f70bcdb8e261ccc092c4230bac21f549cb89436128d5f488d1185aa661811db95de0ee"','origin':'https://www.instagram.com','referer':f'https://www.instagram.com/stories/{User}/{id_story}/','sec-ch-prefers-color-scheme':'dark','sec-ch-ua':'"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Linux"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','user-agent':str(generate_user_agent()),'viewport-width':'980','x-asbd-id':'198387','x-csrftoken':str(csrf),'x-ig-app-id':'936619743392459','x-ig-www-claim':'hmac.AR2lZ6PfEzH1iXfHfCOswttdqH2gbtYywELaivmqD5s1CljA','x-instagram-ajax':'1006943746','x-requested-with':'XMLHttpRequest',}				
					sleep(int(randint(9,17)))
					sry = post("https://www.instagram.com/api/v1/story_interactions/send_story_like",headers=heades,data={'media_id':str(id_story)})
					US = uuss.upper()
					if sry.status_code == 200 and 'ok' in sry.text:
						print('\033[2;36m'+f"- THE STORY HAS BEEN LIKED ❤ ️ "+'\033[1;31m'+"=> "+'\033[2;36m'+f"{US}")
					else:
						print('033[1;33m'+f"- The Story Has Not Been LIKED 🖤  ".upper()+'\033[1;31m'+"=> "+'033[1;33m'+f"{US}")
			except:pass
	def People_Story(csrf,mid,ig_did,ds_user,sis,User):
			from requests import (post,get);from user_agent import generate_user_agent;from time import sleep
			try:
				hd = {'accept':'*/*','accept-encoding':'gzip, deflate, br','accept-language':'ar,en;q=0.9','origin':'https://www.instagram.com','referer':'https://www.instagram.com/','sec-ch-ua':'"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-site','user-agent': str(generate_user_agent()),'x-csrftoken':str(csrf),'x-ig-app-id':'936619743392459','x-ig-www-claim':'hmac.AR1cjP7xqazJ469Nhp3UMEg014y0pAUnf-plXYyvO3tupGkS'};id_user = get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={User}",headers=hd).json()['data']['user']['id'];d = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language':'en-US,en;q=0.9,ar;q=0.8','cookie': f'mid={mid}; ig_did={ig_did}; datr=0LrQY0KimobRI_ynMmIj1Y78; dpr=1.75;csrftoken={csrf}; ds_user_id={id_user}; sessionid={sis}; rur="ASH\05457949618010\0541706958903:01f755c5c04b92ebe6ad066a0cc64d7e45b22ee306354e0fdfdaf491add6da380544546e','user-agent':str(generate_user_agent())};surl = f'https://www.instagram.com/graphql/query/?query_hash=c9c56db64beb4c9dea2d17740d0259d9&variables=%7B%22reel_ids%22%3A%5B%22{id_user}%22%5D%2C%22tag_names%22%3A%5B%5D%2C%22location_ids%22%3A%5B%5D%2C%22highlight_reel_ids%22%3A%5B%5D%2C%22precomposed_overlay%22%3Afalse%2C%22show_story_viewer_list%22%3Atrue%2C%22story_viewer_fetch_count%22%3A50%2C%22story_viewer_cursor%22%3A%22%22%2C%22stories_video_dash_manifest%22%3Afalse%7D';DF = get(surl,headers=d).json();stry= len(DF["data"]["reels_media"][0]["items"])
				for i in range(0,stry):
					id_story = DF["data"]["reels_media"][0]["items"][i]['id']
					taken_at_timestamp = DF["data"]["reels_media"][0]["items"][i]['taken_at_timestamp']
					Id_Story=post(f"https://www.instagram.com/api/v1/media/{id_story}/list_reel_media_viewer/",headers={'accept':'*/*','accept-encoding':'gzip, deflate, br',
'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7','content-length':'29','content-type':'application/x-www-form-urlencoded','cookie':f'mid={mid}; ig_did={ig_did}; datr=0LrQY0KimobRI_ynMmIj1Y78; dpr=1.75;csrftoken={csrf}; ds_user_id={id_user}; sessionid={sis}; rur="ASH,57949618010,1706958903:01f755c5c04b92ebe6ad066a0cc64d7e45b22ee306354e0fdfdaf491add6da380544546e"','origin':'https://www.instagram.com','referer':f'https://www.instagram.com/stories/{User}/{id_story}/','sec-ch-prefers-color-scheme':'dark','sec-ch-ua':'"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Linux"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36','viewport-width':'980','x-asbd-id':'198387','x-csrftoken':str(csrf),'x-ig-app-id':'936619743392459','x-ig-www-claim':'hmac.AR2lZ6PfEzH1iXfHfCOswttdqH2gbtYywELaivmqD5s1Coik','x-instagram-ajax':'1006907761','x-requested-with':'XMLHttpRequest'},data={'include_blacklist_sample': 'true'}).json();P=0
				for i in Id_Story['users']:
					us = i['username']
					P+=1
					print("\033[1;97m"+"UserName :- ".upper()+'\033[1;33m'+us+'\n'+"\033[1;97m"+'ID :- '.upper()+'\033[1;33m'+i['pk']+'\n'+"\033[1;97m"+'Name :- '.upper()+'\033[1;33m'+i['full_name']);print("\033[1;97m"+"~"*30)
				print("- This People has Seen Your Story ... "+str(P));sleep(2)
				input("- Back ? : ".upper());InstaGram.Start()
			except IndexError as e:
				print("[×] ",e);sleep(3);os.system('clear');InstaGram.Start()	
			
	def Start():
		try:
			import requests,user_agent,getpass,cfonts;from cfonts import render
			from time import sleep;from random import choice
		except ModuleNotFoundError:
			os.system('pip install requests')
			os.system('pip install user_agent')
			os.system('pip install time')
			os.system('pip install getpass')
			os.system('pip install python-cfonts');os.system('clear')
		output = render('IG-Alaa',colors=[str(choice(['red','green','white','black','blue'])), str(choice(['red','green','white'])), str(choice(['red','green','white']))],align='left',space='0');print(output);print('\033[2;32m'+"_"*47)
		Choose=input("\033[1;97m"+"["+'\033[2;36m'+"1"+"\033[1;97m"+"]"+" Login Register with your Instagram account •".upper()+"\n"+"\033[1;97m"+"["+"\033[2;36m"+"2"+"\033[1;97m"+"]"+" Following From user Following •".upper()+"\n"+"\033[1;97m"+"["+'\033[2;36m'+"3"+"\033[1;97m"+"]"+" Watch their followers' stories •".upper()+'\n'+"\033[1;97m"+"["+'\033[2;36m'+"4"+"\033[1;97m"+"]"+" Like the stories of followers •".upper()+'\n'+"\033[1;97m"+"["+'\033[2;36m'+"5"+"\033[1;97m"+"]"+" See Who Wiche The Your Story •".upper()+"\n"+"~"*47+"\n"+'\033[1;33m'+"["+'\033[2;36m'+"®"+'\033[1;33m'+"]"+"\033[1;97m"+" Choose : ".upper())
		if Choose =='1':
				os.system("clear");os.system(f"rm -rf api.json")
				from getpass import getpass;from json import (dumps,loads)
				user=input("\033[1;97m"+"["+'\033[2;36m'+"~"+"\033[1;97m"+"]"+" Enter Your account username : ".upper());pas=getpass("\033[1;97m"+"["+'\033[2;36m'+"~"+"\033[1;97m"+"]"+" Enter Your account Password : ".upper())
				Log = InstaGram.Login(user,pas)
				if Log['msg'] == True:
					print("\033[1;97m"+"["+'\033[2;32m'+"√"+"\033[1;97m"+"]"+'\033[2;36m'+" login successfully ...".upper())
					cookies = 'cookies'
					Cooki={}
					Cooki[cookies]= {'mid':Log['mid'],'csrf':Log['csrf'],'sis':Log['sis'],'ds_user':Log['ds_user'],'ig_did':Log['ig_did']}
					with open('api.json','w') as c:
						c.write(dumps(Cooki))
					sleep(3);os.system('clear');InstaGram.Start()
				elif Log['msg'] == 'Ip':
					print('\033[1;33m'+'[•]'+'\033[1;31m'+' Your ip is Blocked from login •'.upper());sleep(4);os.system("clear");InstaGram.Start()
				elif Log['msg'] == 'challenge':
					print('\033[1;31m'+'[-]'+'\033[1;33m'+' you account is secure •'.upper());sleep(4);os.system("clear");InstaGram.Start()
				elif Log['msg'] == 'user_true':
					print('\033[1;33m'+"[=]"+'\033[1;31m'+" Your password is worng !".upper());sleep(4);os.system("clear");InstaGram.Start()
				elif Log['msg'] == 'user_false':
					print('\033[1;33m'+"[=]"+'\033[1;31m'+" UserName is worng !".upper());sleep(4);os.system("clear");InstaGram.Start()
				elif Log['msg'] == 'Error':
					print(Log['Errors'])
		elif Choose == '2':
			from json import (dumps,loads)
			try:
				with open('api.json','r') as c:
					Cooki = loads(c.read())
			except:
					input("\033[1;97m"+"["+'\033[1;31m'+"×"+'\033[1;97m'+"] You are not logged in account Instagram , please Login and try ...".upper());sleep(1);os.system('clear');InstaGram.Start()
			try:
					os.system('clear')
					User=input("\033[1;97m"+"["+'\033[1;33m'+"~"+'\033[1;97m'+"] Enter UserName to withdraw usernames : ".upper())
					InstaGram.Get_Id_Following(Cooki['cookies']['csrf'],Cooki['cookies']['mid'],Cooki['cookies']['ig_did'],Cooki['cookies']['ds_user'],Cooki['cookies']['sis'],User)
			except Exception as e:print("[×] ",e);sleep(3)
		elif Choose == '3':
			from json import (dumps,loads)
			try:
				with open('api.json','r') as c:
					Cooki = loads(c.read())
			except:
					input("\033[1;97m"+"["+'\033[1;31m'+"×"+'\033[1;97m'+"] You are not logged in account Instagram , please Login and try ...".upper());sleep(4);os.system('clear');InstaGram.Start()
			try:
				os.system('clear');User=input("\033[1;97m"+"["+'\033[1;33m'+"~"+'\033[1;97m'+"] Enter UserName to withdraw usernames : ".upper())
				InstaGram.Story(Cooki['cookies']['csrf'],Cooki['cookies']['mid'],Cooki['cookies']['ig_did'],Cooki['cookies']['ds_user'],Cooki['cookies']['sis'],User);os.system('clear');sleep(4);InstaGram.Start()
			
			
			except Exception as e:
				print("[×] ",e);sleep(4);InstaGram.Start()
		
		elif Choose == '4':
			from json import (dumps,loads)
			try:
				with open('api.json','r') as c:
					Cooki = loads(c.read())
			except:
					input("\033[1;97m"+"["+'\033[1;31m'+"×"+'\033[1;97m'+"] You are not logged in account Instagram , please Login and try ...".upper());sleep(4);os.system('clear');InstaGram.Start()
			try:
				os.system('clear');User=input("\033[1;97m"+"["+'\033[1;33m'+"~"+'\033[1;97m'+"] Enter UserName to withdraw usernames : ".upper())
				InstaGram.Story(Cooki['cookies']['csrf'],Cooki['cookies']['mid'],Cooki['cookies']['ig_did'],Cooki['cookies']['ds_user'],Cooki['cookies']['sis'],User);os.system('clear');sleep(4);InstaGram.Start()
			
			except Exception as e:
				print("[×] ",e);sleep(4);InstaGram.Start()
		elif Choose == '5':
			os.system('clear')
			from json import (dumps,loads)
			try:
				with open('api.json','r') as c:
					Cooki = loads(c.read())
			except:
					input("\033[1;97m"+"["+'\033[1;31m'+"×"+'\033[1;97m'+"] You are not logged in account Instagram , please Login and try ...".upper());sleep(4);os.system('clear');InstaGram.Start()
			User=input("\033[1;97m"+"["+'\033[1;31m'+"~"+'\033[1;97m'+"] Enter Your Account User : ".upper());print('\033[1;31m'+"~"*40)
			
			InstaGram.People_Story(Cooki['cookies']['csrf'],Cooki['cookies']['mid'],Cooki['cookies']['ig_did'],Cooki['cookies']['ds_user'],Cooki['cookies']['sis'],User)
			
InstaGram.Start()