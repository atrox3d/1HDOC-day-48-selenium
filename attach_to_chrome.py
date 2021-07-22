import sys
import os
from seleniumhelper import attach_session

try:
    url = sys.argv[1]
    _url = sys.argv[2]
    session_id = sys.argv[2]
    if not url.startswith("https://"):
        url = "https://" + url
except:
    raise SystemExit(f"syntax: {os.path.basename(sys.argv[0])} URL")


# url = "https://www.google.com"
driver = attach_session(url, _url, session_id)
input("* ---> PREMI UN TASTO PER USCIRE ...")
# driver.close()
