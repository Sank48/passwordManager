from random import *
from tkinter import *
from tkinter import messagebox
import re
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

num = '0123456789'
string = 'abcdefghijklmnopqrstuvwxyz'
alphanum = '[{(ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789^!?@#$_&*-.abcdefghijklmnopqrstuvwxyz)}]'



def upload():
    gauth = GoogleAuth('settings.yaml')
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    file1 = drive.CreateFile({'title':'Passwords.txt'})
    file1.SetContentFile('passwords.txt')
    # with open('passwords.txt','r') as file:
    #     l=file.readlines()
    # for i in l:
    #     file1.SetContentString(i)
    file1.Upload()
    messagebox.showinfo(title='upload file',message='Your file has been uploaded')

def create():
    selection=var.get()
    if selection == '':
        res.delete(0.0,END)
        res.insert(END,"You haven't selected any option!! Select the type of password you like")
    else:
        try:
            length = int(e1.get())
        except:
            res.delete(0.0,END)
            res.insert(END,"Enter integer password length!!")
            return
        randpass = []
        for i in range(1,length+1):
            randpass.append(choice(selection))
        password = ''.join(randpass)
        res.delete(0.0,END)
        res.insert(END,password)

def update(uname, password):
    lin=''
    rep=''
    with open('passwords.txt','r+') as file:
        l=file.readlines()
    with open('passwords.txt','r+') as file:
        for line in file:
            if re.search(uname,line):
                res=re.search(r'password: \w.*',line)
                rep+=res.group(0).split()[1]
                lin+=line.replace(rep,password)
                break

    with open('passwords.txt','w') as file:
        d=0
        for lines in l:
            if re.search(uname,lines):
                d=1
            if d==1:
                file.write(lin)
                d=0
            else:
                file.write(lines)


def store():
    password=res.get(1.0, "end-1c")
    if password=='':
        uname.delete(0.0,END)
        uname.insert(END,"Please generate a password first.")
        return
    un=uname.get(1.0, "end-1c")
    if len(un)>20:
        uname.delete(0.0,END)
        uname.insert(END,"Username too long!!")
    else:
        if un=='':
            uname.delete(0.0,END)
            uname.insert(END,"Without entering a username or key your password won't gets saved!!")
        else:
            done=0
            found=0
            try:
                with open('passwords.txt','r+') as file:
                    t="username: "+un+' '
                    for line in file:
                        if found==0:
                            if re.search(t,line):
                                found=1
                                uname.delete(0.0,END)
                                ask=messagebox.askyesno(title='Replace username',message='This username exists\nDo you want to update password')
                if ask==True:
                    update(t,password)
                    done=1
                else:
                    uname.delete(0.0,END)
                    uname.insert(END,"Choose another username")
                    done=1
                if done==0:
                    f=open('passwords.txt','a')
                    text="\nusername: {:30}password: {:<15}".format(un,password)
                    f.write(text)
                    f.close()
                    uname.delete(0.0,END)
                    uname.insert(END,"Your password is saved in 'passwords.txt' file in this folder")
            except:
                f=open('passwords.txt','a')
                text="\nusername: {:30}password: {:<15}".format(un,password)
                f.write(text)
                f.close()
                uname.delete(0.0,END)
                uname.insert(END,"Your password is saved in 'passwords.txt' file in this folder")

def clear_uname():
    uname.delete(0.0,END)
def clear_pass():
    res.delete(0.0,END)

m = Tk()
m.geometry("1200x650")
m.title("Random password generator")
m.configure(bg='orange')
m.iconbitmap(r'F:\pythg\password\password.ico')
m.attributes('-alpha',0.9)      # for adding transparency
# bimg = PhotoImage(file='download.png')
# label1 = Label( m, image = bimg) 
# label1.place(x = 0, y = 0, relwidth=1, relheight=1) 
label2 = Label( m, bg='red') 
label2.place(x = 0, y = 0, relwidth=1, relheight=.11) 

h = Label(m, text="Password Generator", font=('Lucida Calligraphy',30,'bold'),fg='blue',bg='red')
h.place(relx=.32,rely=.02)
#h.grid(row=1,column=4,padx=200,pady=15)
key = Label(m, text = "Enter the length of password", font = ('Times New Roman', 20),fg='blue',bg='orange')
key.place(relx=.03,rely=.2)

e1 = Spinbox(m, width=40, from_=4,to=100)
e1.place(relx=.03, rely=.27)

op = Label(m, text='What type of password do you want??', font=('Times New Roman', 20), fg='blue',bg='orange')
op.place(relx=.62,rely=.2)
gen_label = Label(m, text='Write your own password or generate a random password.',font=('Times New Roman', 15), fg='blue', bg='orange')
gen_label.place(relx=.05, rely=.45)
rem_label = Label(m, text='Write a username or key to remmeber this password', font=('Times New Roman', 15), fg='blue',bg='orange')
rem_label.place(relx=.05,rely=.7)

res=Text(m,height=2,width=100,font=('Times New Roman', 15),fg='tomato',bg='black')
res.place(relx=.05, rely=.5)
uname=Text(m,height=2,width=100,font=('Times New Roman', 15),fg='tomato',bg='black')
uname.place(relx=.05, rely=.75)

var = StringVar()
op1 = Radiobutton(m, text = 'Numeric',font=('Imprint MT Shadow', 15, 'bold'),fg='black', bg='orange',variable=var,value=num)
op1.place(relx=.7, rely=.27)
op2 = Radiobutton(m, text = 'Alphabetical',font=('Imprint MT Shadow', 15, 'bold'),fg='black', bg='orange',variable=var,value=string)
op2.place(relx=.7,rely=.34)
op3 = Radiobutton(m, text = 'Alphanumeric',font=('Imprint MT Shadow', 15, 'bold'),fg='black', bg='orange',variable=var,value=alphanum)
op3.place(relx=.7, rely=.41)

gen_btn = Button(m, text = 'Generate', font=('Lucida Handwriting', 15),command = create,bg='yellow')
gen_btn.place(relx=.1, rely=.58)
clear_gen = Button(m, text = 'Clear Password field', font=('Lucida Handwriting', 15),command = clear_pass, bg='yellow')
clear_gen.place(relx=.5, rely=.58)
rem_btn = Button(m, text = 'Remember this password', font=('Lucida Handwriting', 15),command=store,bg='yellow')
rem_btn.place(relx=.1, rely=.83)
clear_rem = Button(m, text = 'Clear Username field', font=('Lucida Handwriting', 15),command = clear_uname,bg='yellow')
clear_rem.place(relx=.5, rely=.83)

upload_btn = Button(m, text = 'Upload my password file to google drive', font=('Lucida Handwriting', 15),command=upload,bg='yellow')
upload_btn.place(relx=.25,rely=.92)

exit_btn = Button(m, text = 'EXIT', font=('Lucida Handwriting', 15),command=lambda: sys.exit(),bg='orange')
exit_btn.place(relx=.9,rely=.9)
m.mainloop()
