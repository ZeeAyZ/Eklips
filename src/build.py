import os,shutil

gametxt=open("game.txt").read().split("\n")[1]
os.system("pyinstaller Sol.py --distpath=builds/dist --workpath=builds/work --noconfirm")
shutil.copy("game.txt", "builds/dist/Sol/game.txt")
shutil.copytree(gametxt, "builds/dist/Sol/"+gametxt)
shutil.copytree("classes", "builds/dist/Sol/classes")
shutil.copytree(".soleng", "builds/dist/Sol/.soleng")
shutil.copy("solhl.py", "builds/dist/Sol/solhl.py")
