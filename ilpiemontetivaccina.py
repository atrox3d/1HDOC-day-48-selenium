import time
import random

from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *

from seleniumhelper import get_chromedriver


def banner(text, emptylines=0, char="#", width=80):
    # top line
    print(char * width)

    # top empty lines
    for el in range(int(emptylines / 2) if emptylines else 0):
        print(f"{char}{'':^{width - 2}}{char}")

    if isinstance(text, str):
        text = text.split("\n")
    else:
        try:
            iter(text)
        except TypeError:
            text = (text, )
    # text lines
    for textline in text:
        print(f"{char}{textline:^{width - 2}}{char}")

    # bottom empty lines
    for el in range(int(emptylines / 2) if emptylines else 0):
        print(f"{char}{'':^{width - 2}}{char}")

    # bottom line
    print(char * width)


def click_modifica():
    banner("area personale")
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
    banner("area personale")
    print("[+] cerco Sposta appuntamento...")
    xpath = '//div[contains(text(), "Sposta appuntamento")]'
    if sposta_appuntamento := driver.find_element_by_xpath(xpath):
        print("[*] trovato")
        print("[+] click...")
        sposta_appuntamento.click()
        return True
    return False


def check_siamo_spiacenti():
    banner("siamo spiacenti")
    print("[+] Controllo nessaggio errore...")
    xpath = '//div[contains(text(), "Siamo spiacenti")]'
    if siamo_spiacenti := driver.find_element_by_xpath(xpath):
        print("[*] trovato")
        print("[+] porta in vista...")
        driver.execute_script("arguments[0].scrollIntoView();", siamo_spiacenti)
       return True
    return False


def click_torna_indietro():
    banner("torna indietro")
    print("[+] cerco Torna indietro...")
    xpath = '//i[contains(text(), "keyboard_arrow_left")]'
    if torna_indietro := driver.find_element_by_xpath(xpath):
        print("[*] trovato")
        print("[+] porta in vista...")
        driver.execute_script("arguments[0].scrollIntoView();", torna_indietro)
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
    print()

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
            aspetta(secondi=random.randint(1, 10))

        if not click_sposta_appuntamento():
            notfound()
        else:
            aspetta(secondi=random.randint(1, 10))

        if check_siamo_spiacenti():
            aspetta(minuti=random.randint(1, 10))
            if not click_torna_indietro():
                notfound()
            else:
                aspetta(minuti=random.randint(1, 10))
        else:
            message = (
                "[*] ATTENZIONE!",
                "[*] messaggio di errore non trovato!"
            )
            banner(message)
            input("[+] premere un tasto per uscire...")
            break
    except KeyboardInterrupt:
        # input("premi un tasto per terminare...")
        # driver.close()
        # exit()
        print("ctrl-c")
        input("premi un tasto per terminare...")
        driver.close()
        exit()
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
