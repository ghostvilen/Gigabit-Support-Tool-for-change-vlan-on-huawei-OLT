from tkinter import *


utm_1={'mac' : '123'}

def mac():
    c = Tk()
    c.withdraw()
    clip = c.clipboard_get()
    c.update()
    c.destroy()
    user_input =str(clip)
    mac = str(user_input).lower().replace(' ', '')
    mac_bez = mac.replace('.', '').replace(':','').replace('-','').replace('_','')
    step1 = 2
    utm=':'.join(mac_bez[i:i + step1] for i in range(0, 12 , step1))
    lbl_utm.configure(text=utm)
    tk = Tk()
    tk.withdraw()
    tk.clipboard_clear()
    tk.clipboard_append(f'{utm}')
    tk.update()
    tk.destroy()
    utm_1['mac']=f'{utm}'
    return utm_1

def just_copy_mac():
    tk = Tk()
    tk.withdraw()
    tk.clipboard_clear()
    tk.clipboard_append(utm_1['mac'])
    tk.update()
    tk.destroy()

def mac_bdcom():
    c = Tk()
    c.withdraw()
    clip = c.clipboard_get()
    c.update()
    c.destroy()
    user_input =str(clip)
    mac = str(user_input).lower().replace(' ', '')
    mac_bez = mac.replace('.', '').replace(':','').replace('-','').replace('_','')
    step2 = 4
    bdcom='.'.join(mac_bez[i:i + step2] for i in range(0, 12 , step2))
    lbl_bdcom.configure(text=bdcom)
    tk = Tk()
    tk.withdraw()
    tk.clipboard_clear()
    tk.clipboard_append(f'{bdcom}')
    tk.update()
    tk.destroy()
    utm_1['mac']=f'{bdcom}'
    return utm_1 





window=Tk()
window.title('MAC-converter')
window.geometry('400x100')
                            
lbl_utm=Label(window, text='Мак для ютм', bg="seagreen1",width=25)
lbl_utm.grid(column=0,row=0)
                        
btn=Button(window,text='Конвертировать для ютм',command=mac,bg="gold",width=25)
btn.grid(column=6,row=0)

                          
lbl_bdcom=Label(window, text='Мак для bdcom', bg="seagreen1",width=25)
lbl_bdcom.grid(column=0,row=3)


btn_3=Button(window,text='Конвертировать мак для бдком',command=mac_bdcom, bg="coral3")
btn_3.grid(column=6,row=3)


btn_2=Button(window,text='last_convert',command=just_copy_mac,bg="bisque",width=25)
btn_2.grid(column=6,row=5)



window.mainloop()
 
