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

Version 1 has the process of downloading youtube videos with the option of either mp3 or mp4
I will contiune or at least come up with features like having a download directory because 
when you download a youtube video it goes where the program is.

What it has:
A GUI that has a simple design.

Can download from any youtube video as long you have the url

MP4: Downloads video

MP3: Downloads audio and converts to MP3 format

Both: Downloads both video and audio formats

Exit Button: To exit the program

Progess download bar: It downloads pretty fast at least on what I did my tests for videos that were either short or 5 minutes.

The run program bat file suppose to be like this run the program without having to open the python file.
It also has the install_requirements bat which can install the necessary imports though you can either do the pip install yourself or
use the requirements.txt to install everything yourself. 
