import time
import random

from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *

from seleniumhelper import get_chromedriver


def click_modifica():
    try:
        print("[+] cerco tasto modifica...")
        xpath = '//i[contains(text(), "arrow_drop_down")]'
        if modifica := driver.find_element_by_xpath(xpath):
            print("[*] trovato")
            print("[+] porta in vista...")
            driver.execute_script("arguments[0].scrollIntoView();", modifica)
            print("[+] click...")
            modifica.click()
            return True
    except NoSuchElementException:
        return False


def click_sposta_appuntamento():
    print("[+] cerco Sposta appuntamento...")
    xpath = '//div[contains(text(), "Sposta appuntamento")]'
    if sposta_appuntamento := driver.find_element_by_xpath(xpath):
        print("[*] trovato")
        print("[+] click...")
        sposta_appuntamento.click()
        return True
    return False


def check_siamo_spiacenti():
    print("[+] Controllo nessaggio errore...")
    xpath = '//div[contains(text(), "Siamo spiacenti")]'
    if siamo_spiacenti := driver.find_element_by_xpath(xpath):
        print("[*] trovato")
        return True
    return False


def click_torna_indietro():
    print("[+] cerco Torna indietro...")
    xpath = '//i[contains(text(), "keyboard_arrow_left")]'
    if torna_indietro := driver.find_element_by_xpath(xpath):
        print("[*] trovato")
        print("[+] click...")
        torna_indietro.click()
        return True
    return False


def aspetta(minuti=None, secondi=None):
    seconds = 0
    if minuti:
        seconds = minuti * 60
    if secondi:
        seconds += secondi

    for t in range(seconds, 0, -1):
        print(f"{t}, ", end="", flush=True)
        time.sleep(1)


class Break(Exception): pass


class Continue(Exception): pass


def notfound():
    print("[-] non trovato")
    if input("[+] tornare alla pagina iniziale e premere ENTER (q esce) ...").upper() == "Q":
        raise Break
    else:
        raise Continue


url = "https://www.ilpiemontetivaccina.it"
# url = "Vaccinazioni Covid-19.html"
# url = os.path.abspath(url)

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = get_chromedriver(options=options)
print(f"apertura {url} ...")
driver.get(url)
input("autenticati e premi un tasto ...")

loop = True
while loop:
    try:
        if not click_modifica():
            notfound()
        else:
            aspetta(secondi=random.randint(5))

        if not click_sposta_appuntamento():
            notfound()
        else:
            aspetta(secondi=random.randint(5))

        if check_siamo_spiacenti():
            aspetta(minuti=random.randint(10))
            if not click_torna_indietro():
                notfound()
            else:
                aspetta(minuti=random.randint(10))
        else:
            print("[*] ATTENZIONE!")
            print("[*] messaggio di errore non trovato!")
            input("[+] premere un tasto per uscire...")
            break
    except KeyboardInterrupt:
        # input("premi un tasto per terminare...")
        # driver.close()
        # exit()
        print("ctrl-c")
    except Break:
        break
    except Continue:
        continue
    except NoSuchElementException:
        print("[-] non trovato")
        input("[+] tornare alla pagina iniziale e premere un tasto ...")
        continue
    except Exception as e:
        print(repr(e))
input("premi un tasto per terminare...")
driver.close()
