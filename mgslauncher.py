import tkinter as tk
from PIL import ImageTk, Image
import os

# following method runs the exacutable provided at the exe_path
def run_game(window, exe_path):
    os.system("start " + exe_path)
    window.destroy()

def enable_game(game_button, button_state):
    game_button["state"] = button_state.get()

def options_menu(window,mgs1_button,mgs2_button,mgs3_button,has_mgs1,has_mgs2,has_mgs3):
    popup = tk.Toplevel(window)
    popup.title("choose games and paths to their exe")
    window_width = 400
    window_height = 300
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    popup.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    popup.resizable(False,False)
    popup.config(bg="grey")


    # initialize check buttons
    mgs1_c_button = tk.Checkbutton(popup, text="mgs1", variable=has_mgs1, onvalue="normal", offvalue="disabled", command=lambda: enable_game(mgs1_button,has_mgs1))
    mgs2_c_button = tk.Checkbutton(popup, text="mgs2", variable=has_mgs2, onvalue="normal", offvalue="disabled", command=lambda: enable_game(mgs2_button,has_mgs2))
    mgs3_c_button = tk.Checkbutton(popup, text="mgs3", variable=has_mgs3, onvalue="normal", offvalue="disabled", command=lambda: enable_game(mgs3_button,has_mgs3))

    mgs1_c_button.pack()
    mgs2_c_button.pack()
    mgs3_c_button.pack()

# path variables
dir_path = os.path.dirname(os.path.realpath(__file__))
mgs1_path = r'D:\SteamLibrary\steamapps\common\MGS1\"METAL GEAR SOLID.exe"'     # to be changed
mgs2_path = r'D:\SteamLibrary\steamapps\common\MGS2\"METAL GEAR SOLID2.exe"'    # to be changed
mgs3_path = r'D:\SteamLibrary\steamapps\common\MGS3\"METAL GEAR SOLID3.exe"'    # to be changed

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
mgs1_button = tk.Button(window, image=mgs1_img, borderwidth=0, bg="gold", command=lambda: run_game(window, mgs1_path))
mgs1_button.place(x=23,y=14)

mgs2_img = ImageTk.PhotoImage(Image.open(dir_path + r"\imgs\cover_arts\mgs2.bmp"))
mgs2_button = tk.Button(window, image=mgs2_img, borderwidth=0, bg="gold", command=lambda: run_game(window, mgs2_path))
mgs2_button.place(x=348,y=14)

mgs3_img = ImageTk.PhotoImage(Image.open(dir_path + r"\imgs\cover_arts\mgs3.bmp"))
mgs3_button = tk.Button(window, image=mgs3_img, borderwidth=0, bg="gold", command=lambda: run_game(window, mgs3_path))
mgs3_button.place(x=677,y=14)

# button for exiting the application
close_button = tk.Button(window,text="EXIT", font=("Helvatica", 10, "bold"), bg="brown", foreground="white", borderwidth=0, command=lambda: window.destroy())
close_button.place(x=950,y=400)


# variables for checkboxes
has_mgs1 = tk.StringVar()
has_mgs2 = tk.StringVar()
has_mgs3 = tk.StringVar()

# button for selecting directories for the games
options = tk.Button(window,text="OPTIONS", font=("Helvatica", 10, "bold"), bg="brown", foreground="white", borderwidth=0, 
                    command=lambda: options_menu(window,mgs1_button,mgs2_button,mgs3_button,has_mgs1,has_mgs2,has_mgs3))
options.place(x=878,y=400)

#start the application
window.mainloop()