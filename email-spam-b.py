# Coded by Balta

import os
import sys
import smtplib
import getpass
from tqdm import tqdm
from colorama import Fore

if len(sys.argv) < 2:
    os.system("clear || cls")
    print("")

    loop = tqdm(total=10000, position=0, leave=False)
    for k in range(10000):
        loop.set_description(Fore.LIGHTRED_EX + 'Opening Script'.format(k))
        loop.update(1)
    loop.close()

    sys.stdout.write(f'''                                         
{Fore.LIGHTMAGENTA_EX}   ____           _ __    ____                    ___ {Fore.RESET}
{Fore.LIGHTBLUE_EX}  / __/_ _  ___ _(_) /___/ __/__  ___ ___ _  ____/ _ ){Fore.RESET}
{Fore.LIGHTCYAN_EX} / _//  ' \/ _ `/ / /___/\ \/ _ \/ _ `/  ' \/___/ _  |{Fore.RESET}
{Fore.LIGHTRED_EX}/___/_/_/_/\_,_/_/_/   /___/ .__/\_,_/_/_/_/   /____/ {Fore.RESET}
{Fore.LIGHTGREEN_EX}Author: Balta             {Fore.LIGHTRED_EX}/_/{Fore.RESET}{Fore.LIGHTGREEN_EX} v1.1                    {Fore.RESET}           
[{Fore.RED}!{Fore.RESET}] {Fore.LIGHTGREEN_EX}Asegúrese de que su gmail tenga aplicaciones menos seguras en (https://myaccount.google.com/lesssecureapps)
    ''' + Fore.RESET)

print("")

spamemail = input(f"[{Fore.LIGHTRED_EX}?{Fore.RESET}]{Fore.LIGHTGREEN_EX} Ingrese la dirección de Gmail del spammer: {Fore.RESET}")
spampassword = getpass.getpass(f"[{Fore.LIGHTRED_EX}?{Fore.RESET}]{Fore.LIGHTGREEN_EX} Ingrese la contraseña del spammer: {Fore.RESET}")

email = smtplib.SMTP("smtp.gmail.com", 587)
email.ehlo()
email.starttls()

try:
    email.login(spamemail, spampassword)
except smtplib.SMTPAuthenticationError:
    print("")
    print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] {Fore.LIGHTGREEN_EX}Es posible que el gmail o la contraseña sean incorrectos{Fore.RESET}")
    print(
        f"[{Fore.LIGHTRED_EX}!{Fore.RESET}]{Fore.LIGHTGREEN_EX} O tal vez no haya activado aplicaciones menos seguras (https://myaccount.google.com/lesssecureapps){Fore.RESET}")

    loop = tqdm(total=10000, position=0, leave=False)
    for k in range(10000):
        loop.set_description(Fore.LIGHTRED_EX + 'Closing'.format(k))
        loop.update(1)
    loop.close()
    exit()

print("")
print(
    f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] {Fore.LIGHTGREEN_EX} Gmail y la contraseña son correctos, las aplicaciones menos seguras están habilitadas{Fore.RESET}")
print("")
victimemail = input(
    f"{Fore.RESET}[{Fore.LIGHTRED_EX}?{Fore.RESET}] {Fore.LIGHTGREEN_EX}Ingrese la dirección de correo electrónico de la víctima: {Fore.RESET}")
message = input(
    f"[{Fore.LIGHTRED_EX}?{Fore.RESET}] {Fore.LIGHTGREEN_EX}Ingrese el mensaje que desea enviar: {Fore.RESET}")
number = int(input(
    f"[{Fore.LIGHTRED_EX}?{Fore.RESET}] {Fore.LIGHTGREEN_EX}Ingrese cuantas veces desea enviar este mensaje: {Fore.RESET}"))

print("")
print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}]{Fore.LIGHTGREEN_EX} ¡La información es correcta!{Fore.RESET}")
print("")

try:
    smtp_server = 'smtp.gmail.com'
    port = 587
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
        server.starttls()
    server.login(spamemail, spampassword)
    i = 0
    print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}]{Fore.LIGHTGREEN_EX} Porro rodante... {Fore.RESET}")
    print('')
    while i < number:
        i += 1
        server.sendmail(spamemail, victimemail, message)
        if i == 1:
            print((f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] {Fore.LIGHTGREEN_EX}''[%d] Email sent ') % (i))
        elif i == 2:
            print((f'{Fore.RESET}[{Fore.LIGHTRED_EX}+{Fore.RESET}] {Fore.LIGHTGREEN_EX}''[%d] Email enviado ') % (i))
        elif i == 3:
            print((f'{Fore.RESET}[{Fore.LIGHTRED_EX}+{Fore.RESET}] {Fore.LIGHTGREEN_EX}''[%d] Email enviado ') % (i))
        elif i == 4:
            print((f'{Fore.RESET}[{Fore.LIGHTRED_EX}+{Fore.RESET}] {Fore.LIGHTGREEN_EX}''[%d] Email enviado ') % (i))
        elif i == 5:
            print((f'{Fore.RESET}[{Fore.LIGHTRED_EX}+{Fore.RESET}] {Fore.LIGHTGREEN_EX}''[%d] Email enviado ') % (i))
        elif i == 6:
            print((f'{Fore.RESET}[{Fore.LIGHTRED_EX}+{Fore.RESET}] {Fore.LIGHTGREEN_EX}''[%d] Email enviado ') % (i))
        elif i == 7:
            print((f'{Fore.RESET}[{Fore.LIGHTRED_EX}+{Fore.RESET}] {Fore.LIGHTGREEN_EX}''[%d] Email enviado ') % (i))
        elif i == 8:
            print((f'{Fore.RESET}[{Fore.LIGHTRED_EX}+{Fore.RESET}] {Fore.LIGHTGREEN_EX}''[%d] Email enviado ') % (i))
        elif i == 9:
            print((f'{Fore.RESET}[{Fore.LIGHTRED_EX}+{Fore.RESET}] {Fore.LIGHTGREEN_EX}''[%d] Email enviado ') % (i))
        elif i == 0:
            print((f'{Fore.RESET}[{Fore.LIGHTRED_EX}+{Fore.RESET}] {Fore.LIGHTGREEN_EX}''[%d] Email enviado ') % (i))
        else:
            print((f'{Fore.RESET}[{Fore.LIGHTRED_EX}+{Fore.RESET}] {Fore.LIGHTGREEN_EX}''[%d] Email enviado ') % (i))
        sys.stdout.flush()
    print()
    print(f"{Fore.RESET}[{Fore.LIGHTRED_EX}!{Fore.RESET}] {Fore.LIGHTGREEN_EX}El correo electrónico se ha puesto en un porro")
    print()

    loop = tqdm(total=10000, position=0, leave=False)
    for k in range(10000):
        loop.set_description(Fore.YELLOW + 'Closing'.format(k))
        loop.update(1)
    loop.close()
    exit()

except KeyboardInterrupt:
    print()
    print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}]{Fore.LIGHTGREEN_EX} El correo electrónico no se ha incluido en un porro")

    loop = tqdm(total=10000, position=0, leave=False)
    for k in range(10000):
        loop.set_description(Fore.YELLOW + 'Closing'.format(k))
        loop.update(1)
    loop.close()
    exit()
