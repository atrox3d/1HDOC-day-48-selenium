import sys
import os
from seleniumhelper import create_detached_browser

try:
    url = sys.argv[1]
    if not url.startswith("https://"):
        url = "https://" + url
        print(f"INFO| fix url: {url}")
except:
    raise SystemExit(f"syntax: {os.path.basename(sys.argv[0])} URL")


# url = "https://www.ilpiemontetivaccina.it"
_url, session_id = create_detached_browser(url)
print(f"{url        = }")
print(f"{_url       = }")
print(f"{session_id = }")
print(f"autenticati sul sito e poi esegui:")
print(f"python attach_to_chrome.py {url} {_url} {session_id}")
