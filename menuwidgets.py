from tkinter import *
from PIL import ImageTk, Image
from tkinter.ttk import *
from time import strftime
import webbrowser

# creating tkinter window 
root = Tk() 
root.title('RANCHI TOURISM')
root.geometry("400x200")
root.configure(bg='blue')

# Creating Menubar 
menubar = Menu(root)

# Functions
def Jagannath():
    canv = Canvas(root, width=1000, height=400, bg='blue')
    canv.grid(row=2, column=3)
    canv.place(relx=0.5, rely=0.5, anchor=CENTER)
    img = ImageTk.PhotoImage(Image.open("jagannathimg.jpg"))  # PIL solution
    canv.create_image(200, 10, anchor=NW, image=img)
    canv.create_text(410, 280, text= "The first thing that strikes you about Jagannath Temple is its resemblance to the temple in Puri.\n Located about 10 km from the main city, this 17th-century shrine is one of the most popular places in the city and is thus visited by innumerable tourists.\n The best time to visit the temple is undoubtedly during the Ratha Yatra which is held every year in the months of June-July.\n As the temple is built on a hill, you will have to climb several stairs to reach there.\n After seeking blessings, don’t forget to spend a few minutes enjoying the splendid views of the city from the top.\nTimings: 5:00 am to 12:00 pm, 3:00 pm to 6:00 pm", fill = "yellow")
    new = 1
    url = "https://www.google.com/search?sxsrf=ALeKk00_4SrFXmIs8UI7IJ5236CdN-STVQ%3A1603810101846&source=hp&ei=NTOYX9SYMc_vz7sP_IW2iAU&q=jagannath+temple+ranchi&oq=jagannath+temple+ranchi&gs_lcp=Cgdnd3Mtd2l6EAMyDgguEMcBEK8BEMkDEJMCMgIIADICCAAyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB5QiQFYwBpgjxxoAXAAeACAAZsMiAG_IJIBBTctMi4xmAEAoAEBqgEHZ3dzLXdpeg&sclient=gws-wiz&ved=0ahUKEwiUh5-bgtXsAhXP93MBHfyCDVEQ4dUDCAc&uact=5"
    def openweb():
        webbrowser.open(url,new=new)
    button1 = Button(canv, text = "CLICK FOR MORE INFO", command = openweb)
    button1.configure(width= 100)
    button1_window = canv.create_window(100, 350, anchor=NW, window=button1)
    Button1.place(x=50,y=350)
def Pahari():
    canv = Canvas(root, width=1000, height=400, bg='blue')
    canv.grid(row=2, column=3)
    canv.place(relx=0.5, rely=0.5, anchor=CENTER)
    img = ImageTk.PhotoImage(Image.open("Paharimandir.jpg"))  # PIL solution
    canv.create_image(200, 10, anchor=NW, image=img)
    canv.create_text(410, 280, text= "Situated atop Ranchi Hill at an altitude of 2140 ft.,\n Pahari Mandir offers the most overwhelming views of the city. \n It sees a huge crowd of Shiva devotees round the year, especially during the season of Shravan, which is typically observed between July and August.\n The temple is also revered among devotees as it’s believed to have the powers to fulfil their wishes.\n To reach the temple, one needs to climb close to 400 steps.", fill = "yellow")
    new = 1
    url = "https://www.google.com/search?sxsrf=ALeKk03JxVRwzM3p2boIQzCynGyk8tfIuQ%3A1603994648548&source=hp&ei=GASbX6iGH9SCyAOho5uwAg&q=pahari+mandir+ranchi&oq=pahari+mandir+ranchi&gs_lcp=Cgdnd3Mtd2l6EAMyEwguEMcBEK8BEMkDEBQQhwIQkwIyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMggILhDHARCvATICCABQ2QFY0iNg2SZoAHAAeACAAe8ViAHqNpIBBTgtMS4ymAEAoAEBqgEHZ3dzLXdpeg&sclient=gws-wiz&ved=0ahUKEwio8vvZsdrsAhVUAXIKHaHRBiYQ4dUDCAc&uact=5"
    def openweb():
        webbrowser.open(url,new=new)
    button2 = Button(canv, text = "CLICK FOR MORE INFO", command = openweb)
    button2.configure(width= 100)
    button2_window = canv.create_window(100, 350, anchor=NW, window=button2)
    Button2.place(x=50,y=350)
def Tagore():
    canv = Canvas(root, width=1000, height=400, bg='blue')
    canv.grid(row=2, column=3)
    canv.place(relx=0.5, rely=0.5, anchor=CENTER)
    img = ImageTk.PhotoImage(Image.open("Tagore.jpg"))  # PIL solution
    canv.create_image(200, 10, anchor=NW, image=img)
    canv.create_text(410, 280, text= "Tagore Hill is the scenic locality of morabadi. The view of sunrise and sunset from the hill top is one of the most beautiful things to see.\n But before Tagore Hill became a hangout place it was the ashram ofRabindra Nath’s elder brother Jyotindra Nath and even before that it was a rest house.", fill = "yellow")
    new = 1
    url = "https://en.wikipedia.org/wiki/Tagore_Hill"
    def openweb():
        webbrowser.open(url,new=new)
    button3 = Button(canv, text = "CLICK FOR MORE INFO", command = openweb)
    button3.configure(width= 100)
    button3_window = canv.create_window(100, 350, anchor=NW, window=button3)
    Button3.place(x=50,y=350)
def Sun():
    canv = Canvas(root, width=1000, height=400, bg='blue')
    canv.grid(row=2, column=3)
    canv.place(relx=0.5, rely=0.5, anchor=CENTER)
    img = ImageTk.PhotoImage(Image.open("sun.jpg"))  # PIL solution
    canv.create_image(200, 10, anchor=NW, image=img)
    canv.create_text(450, 280, text= "Sun temple, Ranchi Overview The Sun Temple has an extremely captivating architecture and has the shape of a giant vehicle with 18 wheels driven by seven horses.\n The temple complex also has a holy pond which is highly revered among Hindus.\n The Sun Temple is located amidst lush greenery and serene surroundings and absolutely worth a visit.", fill = "yellow")
    new = 1
    url = "https://en.wikipedia.org/wiki/Sun_Temple"
    def openweb():
        webbrowser.open(url,new=new)
    button4 = Button(canv, text = "CLICK FOR MORE INFO", command = openweb)
    button4.configure(width= 100)
    button4_window = canv.create_window(100, 350, anchor=NW, window=button4)
    Button4.place(x=50,y=350)
def Nakshatra():
    canv = Canvas(root, width=1000, height=400, bg='blue')
    canv.grid(row=2, column=3)
    canv.place(relx=0.5, rely=0.5, anchor=CENTER)
    img = ImageTk.PhotoImage(Image.open("Nakshatra.jpg"))  # PIL solution
    canv.create_image(200, 10, anchor=NW, image=img)
    canv.create_text(370, 280, text= "An urban park located near Raj Bhawan, Nakshatra Van is definitely a crowd-puller. \n As the name suggests, the park is based on the concept of Nakshatras or stars. \n It is believed that each Zodiac sign corresponds to a tree that has medicinal, aesthetic, social and economic value. \n Divided into various sections based on these nakshatras or zodiac signs, they offer a unique experience to those visiting.", fill = "yellow")
    new = 1
    url = "https://en.wikipedia.org/wiki/Nakshatra_Van"
    def openweb():
        webbrowser.open(url,new=new)
    button5 = Button(canv, text = "CLICK FOR MORE INFO", command = openweb)
    button5.configure(width= 100)
    button5_window = canv.create_window(100, 350, anchor=NW, window=button5)
    Button5.place(x=50,y=350)
def RanchiHill():
    canv = Canvas(root, width=1000, height=400, bg='blue')
    canv.grid(row=2, column=3)
    canv.place(relx=0.5, rely=0.5, anchor=CENTER)
    img = ImageTk.PhotoImage(Image.open("ranchihill.jpg"))  # PIL solution
    canv.create_image(200, 10, anchor=NW, image=img)
    canv.create_text(410, 280, text= "Ranchi Hill is one of the popular tourist attractions in Ranchi, located at a height of 2140 feet above sea level. \n The site attracts visitors every year, from various parts of the country. \n The hill top offers a panoramic view of the town and the surroundings, where a temple devoted to Lord Shiva is also situated.", fill = "yellow")
    new = 1
    url = "https://en.wikipedia.org/wiki/Ranchi"
    def openweb():
        webbrowser.open(url,new=new)
    button6 = Button(canv, text = "CLICK FOR MORE INFO", command = openweb)
    button6.configure(width= 100)
    button6_window = canv.create_window(100, 350, anchor=NW, window=button6)
    Button6.place(x=50,y=350)
def BaragainHill():
    canv = Canvas(root, width=1000, height=450, bg='blue')
    canv.grid(row=2, column=3)
    canv.place(relx=0.5, rely=0.5, anchor=CENTER)
    img = ImageTk.PhotoImage(Image.open("baragainhill.jpg"))  # PIL solution
    canv.create_image(200, 10, anchor=NW, image=img)
    canv.create_text(410, 320, text= "Bargain is basically pronounce as Baragain. \n It is situated approx 6kms away from Ranchi town. It has a mixed demography of muslim minority, Sarna and Hindus. \n It is semi-urban hence it has influence of city and village as well.", fill = "yellow")
    new = 1
    url = "https://en.wikipedia.org/wiki/Hill"
    def openweb():
        webbrowser.open(url,new=new)
    button7 = Button(canv, text = "CLICK FOR MORE INFO", command = openweb)
    button7.configure(width= 100)
    button7_window = canv.create_window(100, 370, anchor=NW, window=button7)
    Button7.place(x=50,y=350)

# Adding HILL STATION Menu and commands 
file = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='HILL STATION', menu = file) 
file.add_command(label ='1. TAGORE HILL', command = Tagore) 
file.add_command(label ='2. RANCHI HILL', command = RanchiHill) 
file.add_command(label ='3. BARAGAIN HILL PAHADI MOHALLA', command = BaragainHill) 
file.add_separator()
more_menu = Menu(file)
file.add_cascade(label ='MORE', menu = more_menu)
more_menu.add_separator()
more_menu.add_command(label ='1. NETAHAT HILLS', command = None) 
more_menu.add_command(label ='2. GHATSHILA HILLS', command = None)
more_menu.add_separator()
file.add_command(label ='EXIT', command = None)



# Adding TEMPLES Menu and commands 
edit = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='TEMPLES', menu = edit) 
edit.add_command(label ='1. PAHADI MANDIR', command = Pahari) 
edit.add_command(label ='2. JAGANNATH TEMPLE', command = Jagannath) 
edit.add_command(label ='3. SURYA TEMPLE', command = None) 
edit.add_command(label ='4. SUN TEMPLE', command = Sun) 
edit.add_separator() 
edit.add_command(label ='Exit', command = None)  

# Adding GARDENS Menu 
help_ = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='GARDENS', menu = help_) 
help_.add_command(label ='1. NAKSHATRA VAN', command = Nakshatra) 
help_.add_command(label ='2. BIODIVERSITY PARK', command = None) 
help_.add_separator() 
help_.add_command(label ='Exit', command = None)

#Adding ABOUT Menu
about=Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='ABOUT', menu = about)


# display Menu 
root.config(menu = menubar) 
mainloop() 
