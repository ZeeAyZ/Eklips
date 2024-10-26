try:
	mainmenudat=Sol.ReadProp(f"{Sol.Resource.resfol}/data/scenes/mainmenu.sol")["info"]
except Exception as e:
	mainmenudat={"options": f"reset/r_error/ShowCrashLog{e}", "menu_anchor": ""}

Sol.UI.blit(Sol.Resource.load(f"{Sol.Resource.resfol}/media/icon.png"), [50,50], size=(150,150))
if (Sol.Data["Engine"]["Transition"] == "" and Sol.Data["Engine"]["TAF"] < 1.7) or not "?" in Sol.Data["Engine"]["Transition"]:
	Sol.UI.blit(logotxt, [250,100], scale=2)

opty=0
if mainmenudat["menu_anchor"]=="":
	opty=275
for i in mainmenudat["options"].split("_"):
	dat = i.split("/")
	nm = Sol.Data["Lang"].get(dat[0])
	act=dat[1]
	
	if act=="CheckHasSave" and Sol.Save.val("Empty"):
		option=Sol.UI.button(Sol.Resource.render(nm), [50,opty], anchor=mainmenudat["menu_anchor"], disabled=1)
	else:
		option=Sol.UI.button(Sol.Resource.render(nm), [50,opty], anchor=mainmenudat["menu_anchor"])
	if option:
		try:
			Sol.Execute(f"{Sol.Resource.resfol}/data/scripts/menu_option/{act}.sol", gl=globals(),lc=locals())
		except Exception as e:
			print("Main menu broken options", e)
		
		bgr=1
		
		if act=="r": ; Only hardcoded thing for reloading game data if broken
			loadscr = 1
			loading = 0
			loadno = 0
			loadskp = 0
		
		if act.startswith("ShowCrashLog"):
			ekhl.error(sol_ver+filesolmesg, act.lstrip("ShowCrashLog"), ISTRACEBACK=0)
	
	opty+=50