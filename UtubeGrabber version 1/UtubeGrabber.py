"""

Author:  Joseph Belda
Date written: 2/18/25
Assignment:   
Short Desc:

"""



"""
Required installations before running this program:
1. Install the following packages using pip:
   pip install customtkinter
   pip install pytubefix
   pip install pytube

Note: You can install all requirements at once using:
   pip install -r requirements.txt

Make sure you have Python 3.x installed on your system.
You may have to change the Intreperter to have some of the imports/pips to work
You can change it either on the bottom right or clicking on the gear icon Example: Python 3.12.2 64-bit change to 3.10.0 64-bit That is what I had to change to have the imports work
Command palette then find Intreperter.

Required imports for this program:
- tkinter (comes with Python)
- customtkinter
- pytubefix
- pytube
- os (comes with Python)
- io (comes with Python)

"""


#A bunch of imports
import tkinter
import customtkinter
from pytubefix import YouTube 
from io import BytesIO
from pytube import Stream
import os

#Defining modules
def startdownload():
    try:
        ytLink = link.get()
        if not ytLink:
            finish_label.configure(text="Please enter a YouTube URL", text_color="red")
            return
            
        # Clean and validate the URL
        ytLink = ytLink.strip()
        if not ('youtube.com' in ytLink or 'youtu.be' in ytLink):
            finish_label.configure(text="Error: Please enter a valid YouTube URL", text_color="red")
            return
            
        finish_label.configure(text="Downloading...", text_color="white")
        app.update()
        
        # Configure YouTube object
        ytObject = YouTube(ytLink)
        
        # Check download option
        selected_option = format_var.get()
        
        if selected_option == "MP4":
            # Download video (MP4)
            video = ytObject.streams.get_highest_resolution()
            video.download()
            finish_label.configure(text="Video Download Complete!", text_color="green")
            
        elif selected_option == "MP3":
            # Download audio only (MP3)
            audio = ytObject.streams.filter(only_audio=True).first()
            out_file = audio.download()
            # Convert to MP3
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            finish_label.configure(text="Audio Download Complete!", text_color="green")
            
        elif selected_option == "Both":
            # Download both formats
            video = ytObject.streams.get_highest_resolution()
            audio = ytObject.streams.filter(only_audio=True).first()
            
            video.download()
            out_file = audio.download()
            # Convert to MP3
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            
            finish_label.configure(text="Both formats downloaded!", text_color="green")
        
        link.delete(0, tkinter.END)  # Clear the entry field
        
    except Exception as e:
        error_message = str(e)
        finish_label.configure(text=f"Error: {error_message}", text_color="red")
        print(f"Download error: {error_message}")



#app frame
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
app = customtkinter.CTk()
app.geometry("720x480")
app.title("UTubeGrabber")

#UI Elements
title = customtkinter.CTkLabel(app, text="Insert a YouTube link", font=("Arial", 20))
title.pack(padx=10, pady=50)

#link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Format selection
format_var = customtkinter.StringVar(value="MP4")  # default value
format_frame = customtkinter.CTkFrame(app)
format_frame.pack(padx=10, pady=10)

format_label = customtkinter.CTkLabel(format_frame, text="Select Format:")
format_label.pack(side="left", padx=5)

mp4_radio = customtkinter.CTkRadioButton(format_frame, text="MP4", variable=format_var, value="MP4")
mp4_radio.pack(side="left", padx=5)

mp3_radio = customtkinter.CTkRadioButton(format_frame, text="MP3", variable=format_var, value="MP3")
mp3_radio.pack(side="left", padx=5)

both_radio = customtkinter.CTkRadioButton(format_frame, text="Both", variable=format_var, value="Both")
both_radio.pack(side="left", padx=5)

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startdownload)
download.pack(padx=10, pady=10)

exit = customtkinter.CTkButton(app, text="Exit", command=exit)
exit.pack(padx=10, pady=20)

# Add status label
finish_label = customtkinter.CTkLabel(app, text="")
finish_label.pack(padx=10, pady=10)

#running app
app.mainloop()
