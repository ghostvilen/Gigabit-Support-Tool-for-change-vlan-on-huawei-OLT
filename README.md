Gigabit-Support-Tool-for-change-vlan-on-huawei-OLT

Конвертировать для UTM - приводит скопированный MAC-адрес с буфера обмена в формат хх:хх:хх:хх:хх:хх и кладет его в буфер обмена.

Конвертировать для bdcom - приводит скопированный MAC-адрес с буфера обмена в формат хххх.хххх.хххх и кладет его в буфер обмена.

Последнее - хранит и берет в буфер обмена последнее конвертированное значение MAC-адреса .

Все конвертированные значения отображаться возле каждой кнопки.

Внизу интерфейса есть надпись "Производитель роутера" если удалось определить туда записывает производителя роутера при конвертации для UTM , смене VLAN ,MAC за портом - если он есть там .

Поле для ввода MAC-адрес или s/n терминала.

Выпадающий список с OLTs сразу уже забит vlan`aми нужными .

Галочка работает при нажатии сменить vlan - при выполнении скрипта перезагружает онт.

"сменить vlan"- запускает скрипт который берет с поля ввода информацию про онт определяет EPON или GPON по выбранному из выпадающего списка OLT заходит на него по телнету и определяет нахождение ону терминала ,MAC-адрес за портом , сервис порт , меняет vlan и отключает Ethernet порт ону на 3 секунды и потом его включает. Заполняет графы "F/S/P ont ID", "МAC за терминалом" ,который сразу вносит в графу "Производитель роутера" и закрывает соединение по телнету. Кнопка "MAC за терминалом" отдельный скрип который смотрит мак за терминалом по телнету.

Также пишется лог файл "log_onu_change_vlan.txt" который сохраняет олт , терминал , место и дату .

Файл DB.env содержит логин и пароль для входа на олт : DB_USERNAME=ваш логин DB_PASSWORD=ваш пароль
