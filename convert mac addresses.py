from tkinter import *

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




window=Tk()
window.title('Добро пожаловать')
window.geometry('250x50')
lbl_utm=Label(window, text='Мак для ютм')
lbl_utm.grid(column=0,row=0)
btn=Button(window,text='скопировать в буфер обмена',command=mac)
btn.grid(column=6,row=0)

window.mainloop()
 
