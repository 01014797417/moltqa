import time, subprocess, os, requests, re, asyncio, sys, time
def update():
    cmd = subprocess.Popen(['screen', '-ls'], stdout=subprocess.PIPE)
    response, error = cmd.communicate()
    p = re.compile(r'\t\d+\.(.*?)\s*\(')
    sc = p.findall(response.decode('utf-8'))
    if not "moltqa" in sc:
       os.system("screen -dmS moltqa python3 moltqa.py")
       print("deeb")
    print(sc)
for x in range(360):
    try:
       update()
       time.sleep(59)
    except Exception as a:
       print(a)

os.system("screen -XS moltqa quit")

os.system("screen -dmS moltqa python3 deeb.py")
os.system("screen -dmS chmoltqa python3 ch.py")
sys.exit()
