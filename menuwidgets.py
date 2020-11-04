
from tkinter import *
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
    lable = Label(root,text='The first thing that strikes you about Jagannath Temple is its resemblance to the temple in Puri.\n Located about 10 km from the main city, this 17th-century shrine is one of the most popular places in the city and is thus visited by innumerable tourists.\n The best time to visit the temple is undoubtedly during the Ratha Yatra which is held every year in the months of June-July.\n As the temple is built on a hill, you will have to climb several stairs to reach there.\n After seeking blessings, don’t forget to spend a few minutes enjoying the splendid views of the city from the top.\nTimings: 5:00 am to 12:00 pm, 3:00 pm to 6:00 pm')
    lable.pack()
    new = 1
    url = "https://www.google.com/search?sxsrf=ALeKk00_4SrFXmIs8UI7IJ5236CdN-STVQ%3A1603810101846&source=hp&ei=NTOYX9SYMc_vz7sP_IW2iAU&q=jagannath+temple+ranchi&oq=jagannath+temple+ranchi&gs_lcp=Cgdnd3Mtd2l6EAMyDgguEMcBEK8BEMkDEJMCMgIIADICCAAyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB5QiQFYwBpgjxxoAXAAeACAAZsMiAG_IJIBBTctMi4xmAEAoAEBqgEHZ3dzLXdpeg&sclient=gws-wiz&ved=0ahUKEwiUh5-bgtXsAhXP93MBHfyCDVEQ4dUDCAc&uact=5"
    def openweb():
        webbrowser.open(url,new=new)
    Btn = Button(root, text = "CLICK HERE FOR MORE INFORMATON",command=openweb)
    Btn.pack()
def Pahari():
    lable = Label(root,text='Situated atop Ranchi Hill at an altitude of 2140 ft.,\n Pahari Mandir offers the most overwhelming views of the city. \n It sees a huge crowd of Shiva devotees round the year, especially during the season of Shravan, which is typically observed between July and August.\n The temple is also revered among devotees as it’s believed to have the powers to fulfil their wishes.\n To reach the temple, one needs to climb close to 400 steps.')
    lable.pack()
    new = 1
    url = "https://www.google.com/search?sxsrf=ALeKk03JxVRwzM3p2boIQzCynGyk8tfIuQ%3A1603994648548&source=hp&ei=GASbX6iGH9SCyAOho5uwAg&q=pahari+mandir+ranchi&oq=pahari+mandir+ranchi&gs_lcp=Cgdnd3Mtd2l6EAMyEwguEMcBEK8BEMkDEBQQhwIQkwIyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMggILhDHARCvATICCABQ2QFY0iNg2SZoAHAAeACAAe8ViAHqNpIBBTgtMS4ymAEAoAEBqgEHZ3dzLXdpeg&sclient=gws-wiz&ved=0ahUKEwio8vvZsdrsAhVUAXIKHaHRBiYQ4dUDCAc&uact=5"
    def openweb():
        webbrowser.open(url,new=new)
    Btn = Button(root, text = "CLICK HERE FOR MORE INFORMATON",command=openweb)
    Btn.pack()
def Tagore():
    lable = Label(root,text='Tagore Hill owes its name to the great poet Rabindranath Tagore, who is believed to have spent a lot of time here.\n Also known as Moradabad Hill, this spot is perfect to enjoy and admire the beautiful views of the city and the clear blue skies.\n The hill is also very popular among adventure seekers who can try rock climbing and trekking here.\n At the base of the hill is the Ramakrishna Mission Ashrama, the centre of Agrarian Vocational Institute and Divyayan.')
    lable.pack()
    new = 1
    url = "https://www.google.com/search?sxsrf=ALeKk01jEJR-HBXM2rhMa4OquJ290Fgqkw%3A1603994954877&source=hp&ei=SgWbX6OoM9v59QP157K4Dg&q=tagore+hill+ranchi&gs_ssp=eJzj4tLP1TfIMk4xi7c0YLRSNagwtkwzSTU0sTSztDRJTDawtDKoSDIxTDQzTEtNMTA2MLM0T_QSKklMzy9KVcjIzMlRKErMS87IBACttRSf&oq=tagore+hill+ra&gs_lcp=Cgdnd3Mtd2l6EAMYADIOCC4QxwEQrwEQyQMQkwIyAggAMgIIADICCAAyAggAMgIIADIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeOhAILhDHARCvARDJAxBDEJMCOgcIABCxAxBDOgUIABCxAzoECAAQQzoKCC4QxwEQrwEQQzoCCC46BQguELEDOggILhDHARCvAVDCDVi2TWDbYmgDcAB4AYABqAyIAeRLkgEHNi0yLjUuMZgBAKABAaoBB2d3cy13aXo&sclient=gws-wiz"
    def openweb():
        webbrowser.open(url,new=new)
    Btn = Button(root, text = "CLICK HERE FOR MORE INFORMATON",command=openweb)
    Btn.pack()
def Sun():
    lable = Label(root,text='The first glimpse of the Sun Temple in Ranchi is absolutely captivating. \nSituated on a hilltop, the temple is constructed in the typical Sun temple architecture depicting a giant chariot with 18 wheels, pulled by seven horses.\n Other than the Sun God, the shrine holds idols of many other Hindu Gods and Goddesses and also has a pond within its complex which is considered sacred.\n The temple is visited by a number of tourists every day and makes for one of the most popular places to see in Ranchi.')
    lable.pack()
    new = 1
    url = "https://www.google.com/search?sxsrf=ALeKk03AmJzJUguxjgcVA_StAJXZ2YHIDQ%3A1603994970111&ei=WgWbX_SwBpeGyAPy2IuYAw&q=sun+temple+ranchi&oq=sun+temple+ranchi&gs_lcp=Cgdnd3Mtd2l6EAMyEAguEMcBEK8BEMkDEEMQkwIyCAgAELEDEJECMgIIADIQCC4QsQMQxwEQrwEQFBCHAjIICC4QxwEQrwEyAggAMgIIADICCAAyAggAMgQIABBDUIWPCFiEsghgibUIaABwAXgAgAGkDYgBpA2SAQM4LTGYAQCgAQGqAQdnd3Mtd2l6wAEB&sclient=gws-wiz&ved=0ahUKEwj0xajzstrsAhUXA3IKHXLsAjMQ4dUDCA0&uact=5"
    def openweb():
        webbrowser.open(url,new=new)
    Btn = Button(root, text = "CLICK HERE FOR MORE INFORMATON",command=openweb)
    Btn.pack()
def Nakshatra():
    lable = Label(root,text='Nakshatra Van is an urban park situated in front of the Governor House (Raj Bhawan) in Ranchi.\n Created on the unique concept of Nakshatras, the park is divided into various sections, each of which represents a Zodiac sign and celestial bodies.\n Hindu astrologers also believe that each constellation corresponds to a tree that has medicinal, aesthetic, social and economic value. Exploring the park according to your star sign is an experience unlike any other so you certainly don’t want to miss on it. The musical fountain and the scenic pathways surrounding it add to the beauty of the park. Evenings are typically the best time to visit!')
    lable.pack()
    new = 1
    url = "https://www.google.com/search?sxsrf=ALeKk00egPeRuIh_pJi7PcqhPSq9dFnwyA%3A1603995398398&ei=BgebX5L6F62S4-EPzueD2AU&q=nakshatra+van+ranchi&oq=nakshatra+van+ranchi&gs_lcp=Cgdnd3Mtd2l6EAMyCwguEMcBEK8BEJMCMgYIABAHEB4yBggAEAcQHjIECAAQHjIGCAAQBRAeOgQIABBHOggIABAIEAcQHjoCCAA6CAgAEAcQBRAeOgYIABAIEB5Q9jpYy2dgmGpoAXACeACAAagCiAGODZIBAzItN5gBAKABAaoBB2d3cy13aXrIAQjAAQE&sclient=gws-wiz&ved=0ahUKEwiSlcW_tNrsAhUtyTgGHc7zAFsQ4dUDCA0&uact=5"
    def openweb():
        webbrowser.open(url,new=new)
    Btn = Button(root, text = "CLICK HERE FOR MORE INFORMATON",command=openweb)
    Btn.pack()
def RanchiHill():
    lable = Label(root,text='Ranchi Hill is one of the favorite tourist attractions in Ranchi. At the summit of the Ranchi Hill there is a temple devoted to Lord Shiva. 3 The hill of Ranchi attracts visitors from different parts of the country to have a panoramic view of the place. At the base of the Ranchi hill there is a lake, which is known as the Ranchi Lake. This lake has enhanced the beauty of the place. The place is visited by many people every year. People, who visit the city on business purposes, also include Ranchi Hill in their schedule. The Ranchi hill in Ranchi can be easily accessed from all corners of the city. People coming from other parts of the country can reach this popular destination via Ranchi Airport and railway station. The place is also considered to be one of the prime locations for trekking and rock climbing. For this reason, many adventure lovers are also attracted to the Ranchi Hill. Local people also use the place as a picnic spot.The temple of Lord Shiva at the top of the hill is regarded as one of the holy places of the state. People from different corners of the country gather at the temple to offer their homage to the deity. During the festival of Sravan Mela, the place is flooded by Hindu devotees.')
    lable.pack()
    new = 1
    url = "https://www.google.com/search?sxsrf=ALeKk0201VPL33zso2_tHRns0IpokS5HJg%3A1603996471622&source=hp&ei=NwubX_boI5bb9QOYqIOoCA&q=ranchi+hill&oq=ranchi+hill&gs_lcp=Cgdnd3Mtd2l6EAMyBwguECcQkwIyBQgAEMkDMgIIADIICC4QxwEQrwEyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB46CgguEMcBEKMCECc6BAgjECc6BAguEEM6CgguEMcBEK8BEEM6BAgAEEM6BwgAEMkDEEM6BwguELEDEEM6CgguELEDEBQQhwI6BwgjELECECc6BwgAEMkDEAo6AgguOgQIABAKOgoILhCxAxDJAxAKOgcILhCxAxAKOgcIABCxAxAKOgoIABCxAxCDARBDOgUILhCxAzoHCAAQsQMQQzoNCC4QsQMQxwEQrwEQQzoFCAAQsQM6CwguEMcBEK8BEMkDOhAILhDHARCvARDJAxAUEIcCOgcIABAUEIcCUOQDWOovYKgyaAJwAHgAgAGhA4gBkR6SAQcyLTcuNS4xmAEAoAEBqgEHZ3dzLXdpeg&sclient=gws-wiz&ved=0ahUKEwi24KO_uNrsAhWWbX0KHRjUAIUQ4dUDCAc&uact=5"
    def openweb():
        webbrowser.open(url,new=new)
    Btn = Button(root, text = "CLICK HERE FOR MORE INFORMATON",command=openweb)
    Btn.pack()
def BaragainHill():
    lable = Label(root,text='Bargain is basically pronounce as Baragain. It is situated approx 6kms away from Ranchi town. It has a mixed demography of muslim minority, Sarna and Hindus. It is semi-urban hence it has influence of city and village as well. This is a developing area. After 2km towards East joined to NH-33 which leads to Ramgarh, Hazaribagh, Barhi, Patna etc.There is a hill/mountain better known as Chandmari as this is a military firing zone. Also there is a number of old and new hospitals like Mahabir Medica, Seventh-Day Adventist, RIMS and others. Thus it is known as doctors area.')
    lable.pack()
    new = 1
    url = "https://www.google.com/search?sxsrf=ALeKk01g14R06D_0KTrMHa1CUUAfoqCfrg%3A1603996479362&ei=PwubX7_KFZqprtoPhJ2nyAc&q=bargain+hill+ranchi&oq=bargain+hill+ranchi&gs_lcp=Cgdnd3Mtd2l6EAM6BAgjECc6DQguEMcBEK8BEMkDEEM6BAgAEEM6AggAOgcILhDJAxBDOgUILhCRAjoLCC4QxwEQrwEQkQI6BAguEEM6CgguEMcBEK8BEEM6DQguELEDEMcBEKMCEEM6CgguEMcBEK8BECc6BQgAEJECOggILhCxAxCDAToICAAQsQMQgwE6BwgAEMkDEEM6BwguELEDEEM6BQguELEDOgUIABCxAzoQCC4QxwEQrwEQyQMQQxCTAjoLCC4QxwEQrwEQkwI6BwgAELEDEAo6AgguOg8IABCxAxDJAxAKEEYQ_wE6BAgAEAo6CwgAEMkDEBYQChAeOgYIABAWEB46CQgAEMkDEBYQHjoHCCEQChCgAToECCEQFToFCCEQoAFQlLUOWNvXDmCy2w5oAHABeACAAekDiAGmLZIBBzItOS45LjGYAQCgAQGqAQdnd3Mtd2l6wAEB&sclient=gws-wiz&ved=0ahUKEwj_5f3CuNrsAhWalEsFHYTOCXkQ4dUDCA0&uact=5"
    def openweb():
        webbrowser.open(url,new=new)
    Btn = Button(root, text = "CLICK HERE FOR MORE INFORMATON",command=openweb)
    Btn.pack()

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
