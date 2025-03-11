#from tkinter import *
#import ttkbootstrap as tb
#from datetime import date
#from ttkbootstrap.dialogs import Querybox
#from pytube import YouTube
#from sys import argv
#import os

#root = tb.Window(themename="solar")

#root.title("TTK Bootstrap")
#root.iconbitmap('')
#root.geometry('500x450')

##funkcije
#def check():
#    label.config(text=f"Typed URL: {entry.get()}")
#    label2.config(text=f"Typed path to file: {entry_path.get()}")

#global count
#def save():
#    count = 0
#    count += 1
#    path=""
#    empty=""
#    f=open("save.txt", "r")
#    if(f.read() == empty):
#        print("file is empty")
#        f.close()
#        pass
#    else:
#       fl=open("save.txt", "r")
#       path = fl.read() 
#       fl.close()
#       return path,count
       
    
#def download_yt():
#    path, count = save() #assigning fansfn
#    #yt download
#    link=entry.get()
#    yt = YouTube(link)

#    print("Title: ", yt.title)
#    print("Views: ", yt.views)

#    #convertanje u mp3
#    video = yt.streams.filter(only_audio=True).first()

#    #put do filea
#    #print("Insert destination")
#    if(count >= 1):
#        if(path != ""):
#            destination=path
#        else:
#            destination=entry_path.get()
#    else:
#         destination=entry_path.get()


#    #download
#    out_file = video.download(output_path=destination)

#    #saving file
#    base, ext = os.path.splitext(out_file)
#    new_file = base + '.mp3'
#    os.rename(out_file, new_file)

#    #save in file
#    file=open("save.txt", "w")
#    path = destination
#    file.write(path)
#    file.close()

##header
#label_title=tb.Label(root, bootstyle="info",
#                    #foreground="danger",
#                    text="YT -- MP3 DOWNLOADER",
#                    font=("Helvetica", 18),
                   
#                    )

#label_title.pack(pady=10)


# #header1
#label3=tb.Label(root, text="Insert URL: ")
#label3.pack(pady=0)

##entry
#entry=tb.Entry(root, bootstyle="info",
#               width=50,
#               #text="Inssert URL: "
#               #font=("Helvetica", 18),
#               #foreground="red",
#               #width=5,
#               )
#entry.pack(pady=10)

##header2
#label4=tb.Label(root, text="Insert path: ")
#label4.pack(pady=0)

##entry path
#entry_path=tb.Entry(root, bootstyle="info",
#                    width=50,
#                    #text="Insert path"
#                    #font=("Helvetica", 18),
#                    #foreground="red",
#                    #width=5,
#                    )
#entry_path.pack(pady=10)


##button1
#button=tb.Button(root, bootstyle="success outline",
#                 text="Check",
#                 command=check
#                 )
#button.pack(padx=10, pady=10)

##button use last used path

#button_save=tb.Button(root, bootstyle="success outline",
#                 text="Last Path",
                
#                 command=save
#                 )
#button_save.pack(padx=10, pady=10)

##label
#label=tb.Label(root, text="")
#label.pack(pady=10)

#label2=tb.Label(root, text="")
#label2.pack(pady=10)

##button2
#button2=tb.Button(root, bootstyle="success outline",
                 
#                 text="Download",
                 
#                 command=download_yt
                 
#                )
#button2.pack(pady=10, padx=10)



#root.mainloop()


