   host = '********'
    connect = telnetlib.Telnet(host)
    connect.read_until(b'>>User name:')
    connect.write(b'admin*******\n')
    connect.read_until(b'>>User password:')
    connect.write(b'*********\n')
    connect.read_until(b'>')
    connect.write(b'ena\n')
    connect.write(b'con\n')

    cb =entry_user.get()
    fcb = cb.upper().replace('-', '').replace('.', '').replace(':', '').replace('  ', '')
    if len(fcb) < 13:
        mac = fcb[:4] + '-' + fcb[4:8] + '-' + fcb[8:12]
        connect.read_until(b'>')
        connect.write(f'display ont info by-mac {mac}\n'.encode())
    else:
        sn = fcb
        connect.read_until(b'>')
        connect.write(f'display ont info by-sn {sn}\n'.encode())

    x = connect.expect([b'Run state'])
    raw = str(x[2])
    index = raw.find('F/S/P')
    index_2 = index + 26
    port = raw[index_2:index_2+40]
    F = port[0]
    S = port[2]
    P = (port[4:5])
    ID = ''.join(filter(str.isdigit, port[-10:]))  # убираем все нецифровые символы из ID
    print("F: " + F + " S: " + S + " P: " + P + " ID: " + ID)

    connect.write(b'q')
    connect.read_until(b'#')
    connect.write(f'display service-port port {F}/{S}/{P} ont {ID}\n'.encode())
    connect.read_until(b':')
    connect.write(b'\n')

    try:
        print("Пробую найти сервис-порт")
        y = connect.expect([b'Total'])
    except:
        print('Не могу найти сервис-порт, возможно его нет либо что-то засрало логи олты')
        connect.close()
        quit()

    info = str(y[2])

    vlan1 = '1067'
    try:
        spi = info.find(vlan1)
        print('Поиск по влану: ' + vlan1)
        sp = info[spi-6:spi-1]
        sp = ''.join(filter(str.isdigit, sp))  # убираем все нецифровые символы из sp
        print(sp)
    except:
        print(f'Возможно за ону другой влан, не могу найти по {vlan1}')
        connect.close()
        quit()

    connect.write(f'undo service-port {sp}\n'.encode())
    connect.read_until(b'#')
    vlan2 = '2284'                                                           #!!!!!!! указать новый влан
    print(f'Новый влан: {vlan2}')
    
    if len(fcb) < 13:
            srv_set = f'service-port {sp} vlan {vlan2} epon {F}/{S}/{P} ont {ID} multi-service user-vlan 10 tag-transform translate\n' 
            connect.write(srv_set.encode()) 
            print(srv_set)
    else: 
            srv_set = f'service-port {sp} vlan {vlan2} gpon {F}/{S}/{P} ont {ID} gemport 1 multi-service user-vlan 10 tag-transform translate\n' 
            connect.write(srv_set.encode()) 
            print(srv_set)
    print(f'Влан изменен с: {vlan1} на {vlan2}')
    connect.read_until(b':')
    connect.write(b'\n')
    if len(fcb) < 13:
            connect.write(f'interface epon {F}/{S}\n'.encode())
            print(f'interface epon {F}/{S}')
    else:
            connect.write(f'interface gpon {F}/{S}\n'.encode())
            print(f'interface gpon {F}/{S}\n')
    connect.read_until(b'#')
    connect.write(f'ont port attribute {P} {ID} eth 1 operational-state off'.encode())
    print(f'ont port attribute {P} {ID} eth 1 operational-state off')
    connect.read_until(b'#', timeout=5)
    connect.write(f'ont port attribute {P} {ID} eth 1 operational-state on'.encode())
    print(f'ont port attribute {P} {ID} eth 1 operational-state on')
#telnet.read_until(b'#')
    connect.write(b'quit\n')
    print('quit')
    connect.close()
    print(port)
