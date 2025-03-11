from tkinter import *
import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from datetime import date
from ttkbootstrap.icons import Emoji
from ttkbootstrap.dialogs import Querybox
from pytubefix import YouTube
from pytubefix.cli import on_progress
from sys import argv
import os


#GLAVNI WINDOW SA MENIEM
root_main = tb.Window(themename="solar",)

root_main.title("MULTIPRAKTIK")
root_main.iconbitmap('')
root_main.geometry('500x450')

#funkcije
def choise(x):

    global count

    my_label.config(text=f"You selected: {x}")

    if(x == 'mp3'):
        root_main.withdraw()

        #WINDOW ZA YT--MP3
        mp3 = tb.Toplevel()

        mp3.title("YT--MP3")
        mp3.iconbitmap('')
        mp3.geometry('500x450')

        #style
        style = tb.Style()
        style.configure('info.Outline.TButton', font=("Helvetica", 18))

        #funkcije

        def distroj():
            mp3.destroy()
            root_main.update()
            root_main.deiconify()


        def check():
            label.config(text=f"Typed URL: {entry.get()}")
            label2.config(text=f"Typed path to file: {entry_path.get()}")

       
        def save():
            count = 0
            count += 1
            path=""
            empty=""
            f=open("save_mp3.txt", "r")
            if(f.read() == empty):
                print("file is empty")
                f.close()
                pass
            else:
               fl=open("save_mp3.txt", "r")
               path = fl.read() 
               fl.close()
               return path,count
       
    
        def download_yt():
            path, count = save() #assigning fansfn
            #yt download
            link=entry.get()
            yt = YouTube(link, use_po_token = True)

            #print("Title: ", yt.title)
            #print("Views: ", yt.views)

            #convertanje u mp3
            #only_audio=True
            video = yt.streams.filter(only_audio=True).first()

            #put do filea
            #print("Insert destination")
            if(count >= 1):
                if(path != ""):
                    destination=path
                else:
                    destination=entry_path.get()
            else:
                 destination=entry_path.get()


            #download
            out_file = video.download(output_path=destination)

            #saving file
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)

            #save in file
            file=open("save_mp3.txt", "w")
            path = destination
            file.write(path)
            file.close()

        #header
        label_title=tb.Button(mp3, bootstyle="info",                           
                            text="YT -- MP3 DOWNLOADER",
                            style="info.Outline.TButton",
                            command=distroj
                            )

        label_title.pack(pady=10)


         #header1
        label3=tb.Label(mp3, text="Insert URL: ")
        label3.pack(pady=0)

        #entry
        entry=tb.Entry(mp3, bootstyle="info",
                       width=50,
                       #text="Inssert URL: "
                       #font=("Helvetica", 18),
                       #foreground="red",
                       #width=5,
                       )
        entry.pack(pady=10)

        #header2
        label4=tb.Label(mp3, text="Insert path: ")
        label4.pack(pady=0)

        #entry path
        entry_path=tb.Entry(mp3, bootstyle="info",
                            width=50,
                            #text="Insert path"
                            #font=("Helvetica", 18),
                            #foreground="red",
                            #width=5,
                            )
        entry_path.pack(pady=10)


        #button1
        button=tb.Button(mp3, bootstyle="success outline",
                         text="Check",
                         command=check
                         )
        button.pack(padx=10, pady=10)

        #button use last used path

        button_save=tb.Button(mp3, bootstyle="success outline",
                         text="Last Path",
                
                         command=save
                         )
        button_save.pack(padx=10, pady=10)

        #label
        label=tb.Label(mp3, text="")
        label.pack(pady=10)

        label2=tb.Label(mp3, text="")
        label2.pack(pady=10)

        #button2
        button2=tb.Button(mp3, bootstyle="success outline",
                 
                         text="Download",
                 
                         command=download_yt
                 
                        )
        button2.pack(pady=10, padx=10)



        mp3.mainloop()

    elif(x == 'mp4'):

        root_main.withdraw()

        #WINDOW ZA YT--MP4
        mp4 = tb.Toplevel()

        mp4.title("YT--MP4")
        mp4.iconbitmap('')
        mp4.geometry('500x450')

        #style
        style_mp4 = tb.Style()
        style_mp4.configure('info.Outline.TButton', font=("Helvetica", 18))

        #funkcije

        def distroj():
            mp4.destroy()
            root_main.update()
            root_main.deiconify()


        def check2():
            label_mp4.config(text=f"Typed URL: {entry_mp4.get()}")
            label2_mp4.config(text=f"Typed path to file: {entry_path_mp4.get()}")

        global count2
        def save2():
            count2 = 0
            count2 += 1
            path=""
            empty=""
            f=open("save_mp4.txt", "r")
            if(f.read() == empty):
                print("file is empty")
                f.close()
                pass
            else:
               fl=open("save_mp4.txt", "r")
               path = fl.read() 
               fl.close()
               print(path)
               print(count2)
               return path, count2
       
    
        def download_yt2():
            
            path, count2 = save2() #assigning fansfn
            #yt download
            link=entry_mp4.get()
            yt = YouTube(link)

            print("Title: ", yt.title)
            print("Views: ", yt.views)

            #convertanje u mp4
            video = yt.streams.get_highest_resolution()

            #put do filea
            #print("Insert destination")
            if(count2 >= 1):
                if(path != ""):
                    destination=path
                else:
                    destination=entry_path_mp4.get()
            else:
                 destination=entry_path_mp4.get()


            #download
            video.download(destination)

            #saving file
            #base, ext = os.path.splitext(out_file)
            #new_file = base + '.mp3'
            #os.rename(out_file, new_file)

            #save in file
            file=open("save_mp4.txt", "w")
            path = destination
            file.write(path)
            file.close()

        #header
        label_title=tb.Button(mp4, bootstyle="info",                           
                            text="YT -- MP4 DOWNLOADER",
                            style="info.Outline.TButton",
                            command=distroj
                            )

        label_title.pack(pady=10)


         #header1
        label3=tb.Label(mp4, text="Insert URL: ")
        label3.pack(pady=0)

        #entry
        entry_mp4=tb.Entry(mp4, bootstyle="info",
                       width=50,
                       #text="Inssert URL: "
                       #font=("Helvetica", 18),
                       #foreground="red",
                       #width=5,
                       )
        entry_mp4.pack(pady=10)

        #header2
        label4=tb.Label(mp4, text="Insert path: ")
        label4.pack(pady=0)

        #entry path
        entry_path_mp4=tb.Entry(mp4, bootstyle="info",
                            width=50,
                            #text="Insert path"
                            #font=("Helvetica", 18),
                            #foreground="red",
                            #width=5,
                            )
        entry_path_mp4.pack(pady=10)


        #button1
        button=tb.Button(mp4, bootstyle="success outline",
                         text="Check",
                         command=check2
                         )
        button.pack(padx=10, pady=10)

        #button use last used path

        button_save=tb.Button(mp4, bootstyle="success outline",
                         text="Last Path",
                
                         command=save2
                         )
        button_save.pack(padx=10, pady=10)

        #label
        label_mp4=tb.Label(mp4, text="")
        label_mp4.pack(pady=10)

        label2_mp4=tb.Label(mp4, text="")
        label2_mp4.pack(pady=10)

        #button2
        button2=tb.Button(mp4, bootstyle="success outline",
                 
                         text="Download",
                 
                         command=download_yt2
                 
                        )
        button2.pack(pady=10, padx=10)


        mp4.mainloop()
 

#dodavanje backgrounda za main

#bg = PhotoImage(file="waves1.png")

##canvas
#canvas_main = Canvas(root_main, width=500, height=450)
#canvas_main.pack(fill="both", expand=True)

#canvas_main.create_image(0, 0, image=bg, anchor="nw")


#style
style_menu = tb.Style()
style_menu.configure('info.Outline.TMenubutton', font=("Helvetica", 18))

#TITLE
label_main_title = tb.Label(root_main, text="MULTIPRAKTIK",
                           bootstyle="success",
                           font="Helvetica, 22"
                           )  
label_main_title.pack(pady=20)

#menu
menu_g = tb.Menubutton(root_main,
                       style = "info.Outline.TMenubutton",
                       
                       text="MENU")
menu_g.pack(pady=50)

#meni u menuuu
in_menu = tb.Menu(menu_g)

#dodavanje itema u in_menu
item_var = StringVar()
for x in ['mp3', 'mp4']:
    in_menu.add_radiobutton(label = x,
                            variable=item_var,
                            command=lambda x=x: choise(x)
                            
                            )


#asociranje
menu_g['menu'] = in_menu

my_label = tb.Label(root_main, text="")
my_label.pack(pady=30)


root_main.mainloop()
