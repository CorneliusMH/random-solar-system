import random

def build_name_table():
	nm1=["b","c","ch","d","g","h","k","l","m","n","p","r","s","t","th","v","x","y","z","","","","",""]
	nm2=["a","e","i","o","u"]
	nm3=["b","bb","br","c","cc","ch","cr","d","dr","g","gn","gr","l","ll","lr","lm","ln","lv","m","n","nd","ng","nk","nn","nr","nv","nz","ph","s","str","th","tr","v","z"]
	nm3b=["b","br","c","ch","cr","d","dr","g","gn","gr","l","ll","m","n","ph","s","str","th","tr","v","z"]
	nm4=["a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","ae","ai","ao","au","a","ea","ei","eo","eu","e","ua","ue","ui","u","ia","ie","iu","io","oa","ou","oi","o"]
	nm5=["turn","ter","nus","rus","tania","hiri","hines","gawa","nides","carro","rilia","stea","lia","lea","ria","nov","phus","mia","nerth","wei","ruta","tov","zuno","vis","lara","nia","liv","tera","gantu","yama","tune","ter","nus","cury","bos","pra","thea","nope","tis","clite"]
	nm6=["una","ion","iea","iri","illes","ides","agua","olla","inda","eshan","oria","ilia","erth","arth","orth","oth","illon","ichi","ov","arvis","ara","ars","yke","yria","onoe","ippe","osie","one","ore","ade","adus","urn","ypso","ora","iuq","orix","apus","ion","eon","eron","ao","omia"]
	nm7=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","0","1","2","3","4","5","6","7","8","9","","","","","","","","","","","","","",""]
	br=""
	planetNames = []
	for i in range(10):
		if (i<2):
			rnd=int(random.random()*len(nm1))
			rnd2=int(random.random()*len(nm2))
			rnd3=int(random.random()*len(nm3))
			while(nm1[rnd]==nm3[rnd3]):
				rnd3=int(random.random()*len(nm3))
			rnd4=int(random.random()*len(nm4))
			rnd5=int(random.random()*len(nm5))
			names=nm1[rnd]+nm2[rnd2]+nm3[rnd3]+nm4[rnd4]+nm5[rnd5]
		elif (i<4):
			rnd=int(random.random()*len(nm1))
			rnd2=int(random.random()*len(nm2))
			rnd3=int(random.random()*len(nm3))
			while(nm1[rnd]==nm3[rnd3]):
				rnd3=int(random.random()*len(nm3))
			rnd4=int(random.random()*len(nm6))
			names=nm1[rnd]+nm2[rnd2]+nm3[rnd3]+nm6[rnd4]
		elif(i<6):
			rnd=int(random.random()*len(nm1))
			rnd4=int(random.random()*len(nm4))
			rnd5=int(random.random()*len(nm5))
			names=nm1[rnd]+nm4[rnd4]+nm5[rnd5]
		elif(i<8):
			rnd=int(random.random()*len(nm1))
			rnd2=int(random.random()*len(nm2))
			rnd3=int(random.random()*len(nm3b))
			while(nm1[rnd]==nm3b[rnd3]):
				rnd3=int(random.random()*len(nm3b))
			rnd4=int(random.random()*len(nm2))
			rnd5=int(random.random()*len(nm5))
			names=nm3b[rnd3]+nm2[rnd2]+nm1[rnd]+nm2[rnd4]+nm5[rnd5]
		else:
			rnd=int(random.random()*len(nm3b))
			rnd2=int(random.random()*len(nm6))
			rnd3=int(random.random()*len(nm7))
			rnd4=int(random.random()*len(nm7))
			rnd5=int(random.random()*len(nm7))
			rnd6=int(random.random()*len(nm7))
			names=nm3b[rnd]+nm6[rnd2]+" "+nm7[rnd3]+nm7[rnd4]+nm7[rnd5]+nm7[rnd6]
		planetNames.append(names)
	return planetNames
