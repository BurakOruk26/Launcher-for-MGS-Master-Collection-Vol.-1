import tkinter as tk
from tkinter import filedialog as fd
from PIL import ImageTk, Image
import os
import json

# following method runs the exacutable provided at the exe_path
def run_game(window, exe_path):
    if exe_path == "": return           # exit method if no path has been provided

    os.system("start " + exe_path)      # open the game via console command
    window.destroy()                    # destroy the window to close the launcher

# enables or disables any given game button
def enable_game(game_button, button_state):
    game_button["state"] = button_state.get()


def set_game_path(paths, game_path, game_button, has_game, selected_game, savefile):
    game_button["state"] = "normal" # enable the game button
    has_game.set("normal")
    paths[selected_game].set( game_path )
    
    # save paths to json
    path_strings = {
        "mgs1": paths["mgs1"].get(),
        "mgs2": paths["mgs2"].get(),
        "mgs3": paths["mgs3"].get()
    }
    # erase the previous savefile.json contens
    savefile.truncate(0)
    savefile.seek(0)
    # write new contents
    json.dump(path_strings, savefile)


def choose_path(paths, game_button, has_game, selection_popup, selected_game, savefile):
    path=  fd.askopenfilename(filetypes=[("game executable", ".exe")])
    
    # following procedure is done because of Konami has named their exacutables in an amateurish way
    # since the .exe file name involves blank space the path gets corrupted in console command
    # hence, in the following code name of the .exe file has been surrounded by double quotes

    last_slash = path.rfind('/')    # find the last blackslash's index, which means that .exe name will proceed afterwards
    # split it into two parts
    before_last_slash = path[:last_slash+1]
    after_last_slash = path[last_slash+1:]
    # add the needed double quotes before and after the executable name
    path = before_last_slash + '\"' + after_last_slash + '\"'

    set_game_path(paths, path, game_button, has_game, selected_game, savefile)

    selection_popup.destroy()

def options_menu(window, mgs1_info, mgs2_info, mgs3_info, paths, savefile):

    #   fetching the variables from arguments

    mgs1_button = mgs1_info[0]
    mgs2_button = mgs2_info[0]
    mgs3_button = mgs3_info[0]

    has_mgs1 = mgs1_info[1]
    has_mgs2 = mgs2_info[1]
    has_mgs3 = mgs3_info[1]

    mgs1_path = mgs1_info[2]
    mgs2_path = mgs2_info[2]
    mgs3_path = mgs3_info[2]


    # initialize a pop-up screen
    popup = tk.Toplevel(window)
    popup.title("choose games and paths to their exe")
    window_width = 600
    window_height = 85
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    popup.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    popup.resizable(False,False)
    popup.config(bg="#2F4F4F")


    # initialize check buttons
    mgs1_c_button = tk.Checkbutton(popup, bg="#8B2323", variable=has_mgs1, onvalue="normal", offvalue="disabled", 
                                   command=lambda: enable_game(mgs1_button,has_mgs1))
    
    mgs2_c_button = tk.Checkbutton(popup, bg="#3D58AB", variable=has_mgs2, onvalue="normal", offvalue="disabled", 
                                   command=lambda: enable_game(mgs2_button,has_mgs2))
    
    mgs3_c_button = tk.Checkbutton(popup, bg="#458B00", variable=has_mgs3, onvalue="normal", offvalue="disabled", 
                                   command=lambda: enable_game(mgs3_button,has_mgs3))


    # initialize buttons for choosing path
    mgs1_p_button = tk.Button(popup,text="Click to choose path for MGS1: ", bg="#8B2323", fg="white", font=("Helvatica", 8, "bold"),
                              command=lambda: choose_path(paths, mgs1_button, has_mgs1, popup, "mgs1", savefile))
    
    mgs2_p_button = tk.Button(popup,text="Click to choose path for MGS2: ", bg="#3D58AB", fg="white", font=("Helvatica", 8, "bold"),
                              command=lambda: choose_path(paths, mgs2_button, has_mgs2, popup, "mgs2", savefile))
    
    mgs3_p_button = tk.Button(popup,text="Click to choose path for MGS3: ", bg="#458B00", fg="white", font=("Helvatica", 8, "bold"),
                              command=lambda: choose_path(paths, mgs3_button, has_mgs3, popup, "mgs3", savefile))


    # initialize labels for showing current path
    mgs1_p_label = tk.Label(popup, font=("Helvatica", 8, "italic"), fg="red", text=mgs1_path.get())
    mgs2_p_label = tk.Label(popup, font=("Helvatica", 8, "italic"), fg="red", text=mgs2_path.get())
    mgs3_p_label = tk.Label(popup, font=("Helvatica", 8, "italic"), fg="red", text=mgs3_path.get())


    # place the widgets on the pop-up

    mgs1_c_button.place(x=5, y=5)
    mgs2_c_button.place(x=5, y=30)
    mgs3_c_button.place(x=5,y=55)

    mgs1_p_button.place(x=30,y=5)
    mgs2_p_button.place(x=30,y=30)
    mgs3_p_button.place(x=30,y=55)

    mgs1_p_label.place(x=220,y=7)
    mgs2_p_label.place(x=220,y=32)
    mgs3_p_label.place(x=220,y=57)


# window initialization
window = tk.Tk()
window.title("MGS Master Collection Vol. 1")   
window.overrideredirect(True) # to get rid of task bar of the window
window_width = 993
window_height = 427

# following part places the window on the center of the screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

window.resizable(False,False)
window.config(bg="black")  

# variables
dir_path = os.path.dirname(os.path.realpath(__file__))
# variables for checkboxes
has_mgs1 = tk.StringVar()
has_mgs2 = tk.StringVar()
has_mgs3 = tk.StringVar()

# variables for paths
mgs1_path = tk.StringVar()
mgs2_path = tk.StringVar()
mgs3_path = tk.StringVar()


#   read saved paths from paths.json

# open savefile.json
# create savefile.json, if doesn't exist
try: 
    savefile = open( dir_path + "/savefile.json", "r+")
except:
    savefile = open( dir_path + "/savefile.json", "a+", encoding="UTF8" )
    savefile.close()
finally:
    savefile = open( dir_path + "/savefile.json", "r+")

# read the file
try:
    savedpaths = json.load(savefile) 
except:
    savedpaths = {
    "mgs1": "",
    "mgs2": "",
    "mgs3": ""
}

# update checkbuttons according to path info
has_game = [has_mgs1,has_mgs2,has_mgs3]   
for path, has_game in zip(savedpaths, has_game):
    if not savedpaths[path] == "":  has_game.set("normal")
    else:               has_game.set("disable")
    
# set saved paths to variables
mgs1_path.set(savedpaths["mgs1"])
mgs2_path.set(savedpaths["mgs2"])
mgs3_path.set(savedpaths["mgs3"])

paths = {
    "mgs1": mgs1_path,
    "mgs2": mgs2_path,
    "mgs3": mgs3_path
}


# main frame
frame = tk.Frame(window, width=993, height=427)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# background image
background = ImageTk.PhotoImage(Image.open(dir_path + r"\imgs\mgsbg.png"))
label = tk.Label(frame, image = background, borderwidth=0)
label.pack()

# buttons for opening the games
# cover arts of every game has been put into the buttons respectively
mgs1_img = ImageTk.PhotoImage(Image.open(dir_path + r"\imgs\cover_arts\mgs1.bmp"))
mgs1_button = tk.Button(window, image=mgs1_img, borderwidth=0, bg="gold", command=lambda: run_game(window, mgs1_path.get()))
mgs1_button.place(x=23,y=14)

mgs2_img = ImageTk.PhotoImage(Image.open(dir_path + r"\imgs\cover_arts\mgs2.bmp"))
mgs2_button = tk.Button(window, image=mgs2_img, borderwidth=0, bg="gold", command=lambda: run_game(window, mgs2_path.get()))
mgs2_button.place(x=348,y=14)

mgs3_img = ImageTk.PhotoImage(Image.open(dir_path + r"\imgs\cover_arts\mgs3.bmp"))
mgs3_button = tk.Button(window, image=mgs3_img, borderwidth=0, bg="gold", command=lambda: run_game(window, mgs3_path.get()))
mgs3_button.place(x=677,y=14)

# disable the buttons if game paths haven't been initialized
if mgs1_path.get() == "": mgs1_button["state"] = "disabled"
if mgs2_path.get() == "": mgs2_button["state"] = "disabled"
if mgs3_path.get() == "": mgs3_button["state"] = "disabled"


# button for exiting the application
close_button = tk.Button(window,text="EXIT", font=("Helvatica", 10, "bold"), bg="brown", foreground="white", borderwidth=0, 
                         command=lambda: window.destroy())

close_button.place(x=950,y=400)

mgs1_info = [mgs1_button, has_mgs1, mgs1_path]
mgs2_info = [mgs2_button, has_mgs2, mgs2_path]
mgs3_info = [mgs3_button, has_mgs3, mgs3_path]

# button for selecting directories for the games
options = tk.Button(window,text="OPTIONS", font=("Helvatica", 10, "bold"), bg="brown", foreground="white", borderwidth=0, 
                    command=lambda: options_menu(window, mgs1_info, mgs2_info, mgs3_info, paths, savefile))

options.place(x=878,y=400)

#start the application
window.mainloop()