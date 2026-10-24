import urllib.request as u,time,datetime as d
r=["# Status\n","|URL|Code|ms|","|-|-|-|"]
for l in open("urls.txt"):
    l=l.strip()
    if not l:continue
    t=time.time()
    try:c=u.urlopen(l,timeout=10).status
    except Exception as e:c=getattr(e,"code","ERR")
    r.append(f"|{l}|{c}|{int((time.time()-t)*1000)}|")
r.append(f"\nUpdated: {d.datetime.now(d.timezone.utc):%Y-%m-%d %H:%M} UTC")
open("STATUS.md","w").write("\n".join(r)+"\n")
