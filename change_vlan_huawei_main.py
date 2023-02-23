import telnetlib
import time
import sys
import re
from dotenv import load_dotenv

# Загрузка  .env файла
load_dotenv()
# Переменные содержащие логин и пароль 
db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')

#В случае неудачи включает alarm output all закрывает соединение и заканчивает скрипт.
def die(connect, message):
    print(message)
    connect.write(f'alarm output all\n')
    connect.close()
    sys.exit(1)
# тут должна быть гора кода которая читает из .tsv файла список олтов и заганяет его в сплывающий список и при выборе применяет в переменные ниже
host = #хост со списка .tsv файла
new_Vlan = #влан с файла .tsv сопоставимый олте
###########
connect=telnetlib.Telnet(host)
connect.read_until(b'>>User name:')
connect.write(b'{db_username}\n') #ввод логина из файла .env
connect.read_until(b'>>User password:')
connect.write(b'{db_password}}\n') #ввод пароля из файла .env
connect.read_until(b'>')
connect.write(b'ena\n')
connect.write(b'con\n')
connect.write(b'undo alarm output all\n') # выключает Fault Management Commands
###
mac_sn =  #пользовательский ввод с интерфейса entry_user.get()
mac_sn_clean = mac_sn.upper().replace('-', '').replace('.', '').replace(':', '').replace('  ', '').strip() #удаляем все лишние символы с строки пользовательского ввода
####
if len(mac_sn_clean) < 13:                                                                       #если пользовательский ввод меньше 13 символов, это епон и применяеться поиск по маку ону терминала
        mac = mac_sn_clean[:4] + '-' + mac_sn_clean[4:8] + '-' + mac_sn_clean[8:12]
        connect.read_until(b'>')
        connect.write(f'display ont info by-mac {mac}\n'.encode())

else:
        sn = mac_sn_clean                                                                         #или был введ серийный номер гпон терминала, то применяеться поиск по серийному номеру
        connect.read_until(b'>')
        connect.write(f'display ont info by-sn {sn}\n'.encode())
try:# поиск нужных параметров терминала для дальнейшей работы 
    x = connect.expect([b'Run state'])   
    raw = str(x[2])
    index = raw.find('F/S/P')
    index_2 = index + 26
    port = raw[index_2:index_2+40]
    F = ''.join(filter(str.isdigit, port[0]))
    S = ''.join(filter(str.isdigit, port[2]))
    P = ''.join(filter(str.isdigit, port[4:7]))
    ID =''.join(filter(str.isdigit, port[-10:]))
except:
    die('Что-то пошло не так...', connect)

connect.write(b'q')
connect.read_until(b'#')
# пользуясь нужными  параметрами запрашиваем сервис порт
connect.write(f'display service-port port {F}/{S}/{P} ont {ID}\n'.encode())
connect.read_until(b':')
connect.write(b'\n')
# пытаемся найти сервис порт в полученом выводе из терминала
try:
    y = connect.expect([b'Total'])
except:
    die('Что-то пошло не так...', connect)
info = str(y[2])
try:
    start = info.index('TYPE  PARA\\r\\n  -----------------------------------------------------------------------------\\r\\n') + len('TYPE  PARA\\r\\n  -----------------------------------------------------------------------------\\r\\n')
    end = len(info)
    substring = info[start:end]
    substring=substring.lstrip()
    sp=substring.split()[0]
except:
    die('Что-то пошло не так...', connect)
# удаляем найденный сервис порт 
try:
    connect.write(f'undo service-port {sp}\n'.encode())
    connect.read_until(b'#')
except:
    die('Что-то пошло не так...', connect)

#записываем сервис порт с нужным новым вланом 

if len(mac_sn_clean) < 13:
    try:
        srv_set = f'service-port {sp} vlan {new_Vlan} epon {F}/{S}/{P} ont {ID} multi-service user-vlan 10 tag-transform translate\n' 
        connect.write(srv_set.encode())
    except:
        die('Что-то пошло не так...', connect)

else:
    try:
        srv_set = f'service-port {sp} vlan {new_Vlan} gpon {F}/{S}/{P} ont {ID} gemport 1 multi-service user-vlan 10 tag-transform translate\n' 
        connect.write(srv_set.encode())
    except:
        die('Что-то пошло не так...', connect)
connect.read_until(b':')
connect.write(b'\n')


if len(mac_sn_clean) < 13:
    connect.write(f'interface epon {F}/{S}\n'.encode())
else:
    connect.write(f'interface gpon {F}/{S}\n'.encode())
connect.read_until(b'#')
connect.write(f'ont reset {P} {ID} \n'.encode())
connect.read_until(b':', timeout=1)
connect.write(f'y\n'.encode())
connect.write(b'quit\n')
connect.write(f'alarm output all\n'.encode())
#sys.exit(0)
