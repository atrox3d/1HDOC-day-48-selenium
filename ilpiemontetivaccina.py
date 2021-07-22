import sys
import os
import time

from selenium.webdriver.chrome.options import Options

from seleniumhelper import get_chromedriver


def click_modifica():
    print("[+] cerco tasto modifica...")
    xpath = '//i[contains(text(), "arrow_drop_down")]'
    if modifica := driver.find_element_by_xpath(xpath):
        print("[*] trovato")
        print("[+] porta in vista...")
        driver.execute_script("arguments[0].scrollIntoView();", modifica)
        print("[+] click...")
        modifica.click()
        return True
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
    if not click_modifica():
        print("[-] non trovato")
        input("[+] tornare alla pagina iniziale e premere un tasto ...")
        continue
    else:
        aspetta(secondi=5)

    if not click_sposta_appuntamento():
        print("[-] non trovato")
        input("[+] tornare alla pagina iniziale e premere un tasto ...")
        continue
    else:
        aspetta(secondi=5)

    if check_siamo_spiacenti():
        if not click_torna_indietro():
            print("[-] non trovato")
            input("[+] tornare alla pagina iniziale e premere un tasto ...")
            continue
        else:
            aspetta(minuti=2)
    else:
        print("[*] ATTENZIONE!")
        print("[*] messaggio di errore non trovato!")
        input("[+] premere un tasto per uscire...")
        break

input("premi un tasto per terminare...")
driver.close()
