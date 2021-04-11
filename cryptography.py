from cryptography.fernet import Fernet
key = Fernet.generate_key()
merah = '\x1b[1;33;41m'
tutupwarna = '\x1b[0m'
hijau = '\x1b[1;37;42m'

logo = f"""
 -- > Author   :> {merah}XploitSec-ID{tutupwarna}      < --
 -- > Coded by :> {merah}HeadlessMan{tutupwarna}       < --
 -- > Contact  :> {merah}t.me/headlessman7{tutupwarna} < --
"""
print(logo)

info = f"""
  =------ {merah}Info !{tutupwarna} ------=
   Example Using Tools ......
   Input Key File -> {hijau}kunci.key{tutupwarna}
   Input File for Encrypt -> {hijau}data.txt{tutupwarna}
   Input Name File Result Encrypt -> {hijau}resultenc.txt{tutupwarna}
   Input Name File Result Decrypt -> {hijau}resultdec.txt{tutupwarna}
  =------ +++++++++++++++++++++++++ ------=
"""
print(info)

keyus = input("Input Key File -> ")
fileus = input("Input File For Encrypt -> ")
encfileus = input("Input Name File Result Encrypt -> ")
decfileus = input("Input Name File Result Decrypt -> ")
with open(keyus, 'wb') as kunci: # Ngebuat File Key
     kunci.write(key+b'\n')

with open(keyus, 'rb') as kunci: # Ngebaca File Key
     key = kunci.read()

raven = Fernet(key)
with open(fileus,'rb') as sebelumenc: # Ngebaca File Yang Mau Di Encrypt
     ori = sebelumenc.read()

encrypt = raven.encrypt(ori) # Nge Encrypt File File.txt
with open(encfileus,'wb') as encryptfile: # Menulis Hasil Encrypt
     encryptfile.write(encrypt+b'\n')

with open(encfileus,'rb') as encfile: # Ngebaca File Hasil Encrypt
     encrypt2 = encfile.read()

decrypt = raven.decrypt(encrypt2) # Ngedecrypt File ResultEncrypt
with open(decfileus,'wb') as decfile: # Menulis Hasil Decrypt
     decfile.write(decrypt+b'\n')
