try:
	mainmenudat=Eklips.ReadProp(f"{Eklips.Resource.resfol}/data/scenes/mainmenu.sol")["info"]
except Exception as e:
	mainmenudat={"options": f"reset/r/exit_error/ShowCrashLog{e}/exit_back/goback/exit", "menu_anchor": ""}

Eklips.UI.blit(Eklips.Resource.load(f"{Eklips.Resource.resfol}/media/icon.png"), [50,50], layer=2,add_bg=0,size=[222,222])
opty=0
if mainmenudat["menu_anchor"]=="":
	opty=270
if not "OptData" in data:
	data["OptData"]={}
opts=delta*30
optdata=data["OptData"]
for i in mainmenudat["options"].split("_"):
	dat = i.split("/")
	nm = Eklips.Data["Lang"].get(dat[0])
	act=dat[1]

	if not i in optdata:
		optdata[i] = [0,0,[255,255,255]]
	
	optx=optdata[i][1]
	color=optdata[i][2]
	optt=Eklips.Resource.render(nm,color=color)

	if optdata[i][0]:
		if optdata[i][1] < 15:
			optdata[i][1]+=opts
		if optdata[i][1] < 15+opts:
			Eklips.UI.blit(bg, [50+optx,opty], layer=3, clip=(50+optx,opty,120+optt.get_width(),50),add_bg=0)
		if optdata[i][2][0] > 175:
			optdata[i][2][0]-=5
		if optdata[i][2][1] < 125:
			optdata[i][2][1]+=5
		if optdata[i][2][2] > 175:
			optdata[i][2][2]-=5
	else:
		if optdata[i][1] > 0:
			optdata[i][1]-=opts
		if optdata[i][1] > -opts:
			Eklips.UI.blit(bg, [50+optx,opty], layer=3, clip=(50+optx,opty,120+optt.get_width(),50),add_bg=0)
		if optdata[i][2][0] < 255:
			optdata[i][2][0]+=5
		if optdata[i][2][1] < 255:
			optdata[i][2][1]+=5
		if optdata[i][2][2] < 255:
			optdata[i][2][2]+=5
	
	Eklips.UI.blit(Eklips.Resource.load(f"{Eklips.Resource.resfol}/media/ui/{dat[2]}.png"), [50+optx,opty], size=(50,50),layer=4,add_bg=0)
	option=Eklips.UI.blit(optt,[120+optx,opty+7],layer=4,add_bg=0)
	optdata[i][0]=option["hovering"]

	if option["click"][0] and optdata[i][1] > 10:
		data["OptData"]={}
		try:
			Eklips.Execute(f"{Eklips.Resource.resfol}/data/scripts/menu_option/{act}.sol", gl=globals(),lc=locals())
		except Exception as e:
			print("Main menu broken options", e)
			optdata[i][2][0]=0
			optdata[i][2][1]=0
			optdata[i][2][2]=0
		
		bgr=1
		
		if act=="goback":
			Eklips.Scene = "main"
		
		if act=="r": ; Only hardcoded stuff
			loadscr = 1
			loading = 0
			loadno = 0
			loadskp = 0
		
		if act.startswith("ShowCrashLog"):
			ekhl.error(sol_ver+filesolmesg, act.lstrip("ShowCrashLog"), running, ISTRACEBACK=0)
	
	opty+=55