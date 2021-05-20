# importing all libraries
from tkinter import *  
from timeit import default_timer as timer

import random
  
# creating window using gui
window = Tk()
window.title("Typing Speed Test")
  
# the size of the window is defined
window.geometry("600x450")
  
x = 0
  
# defining the function for the test
def speed():
    global x
  
    # loop for destroying the window
    # after on test
    print("x==",x)
    if x == 0:
        window.destroy()
        x = x+1
        print("X=",x)
  
    # defining function for results of test
    def calculate_speed():
        if entry.get() == sentences[sentence]:

            # here start time is when the window
            # is opened and end time is when
            # window is destroyed
            end = timer()
            sp=end-start
            t = Label(windows, text= "Time taken to type: "+str(round(sp))+" Secs", font="times 20")
            t.place(x=120, y=320)
  
  
  
            # we deduct the start time from end
            # time and calculate results using
            # timeit function
            print(end-start)
        else:
          
            t = Label(windows, text= "You Typed Incorrectly ", font="times 20")
            t.place(x=120, y=320)
  
  
    sentences = ["Let's learn Python", "quarantine, stay home","All is well that ends well","hackerspirit","Catch the opportunity","Believe in yourself","Home sweet home","Stairway to heaven"]
  
    # Give random words for testing the speed of user
    sentence = random.randint(0, (len(sentences)-1))
  
    # start timer using timeit function
    start = timer()
    windows = Tk()
    windows.geometry("600x400")
    windows.title("Typing Speed Test")
    sen="\""+sentences[sentence]+"\""
  
    # use lable method of tkinter for labling in window
    x2 = Label(windows, text=sen, font=("comic sans MS" ,20))
  
    # place of labling in window
    x2.place(x=200, y=10)
    x3 = Label(windows, text="Type The Above Sentence", font="times 20")
    x3.place(x=150, y=70)
  
    entry = Entry(windows)
    entry.place(x=225, y=120)
  
    # buttons to submit output and check results
    b2 = Button(windows, text="YOUR SPEED",
                command=calculate_speed, width=12, bg='yellow')
    b2.place(x=150, y=160)
  
    b3 = Button(windows, text="TRY AGAIN", 
                command=speed, width=12, bg='red')
    b3.place(x=300, y=160)
    #photon = PhotoImage(file = r"icon.png")
    #photoimage = photon.subsample(9,9)

    #b4 = Button(windows,image=photoimage,compound=CENTER,command=speed,width=200)
    #b4.place(x=170,y=200)

    windows.mainloop()
  
  
x1 = Label(window, text="Lets Check Your Speed..", font="times 20")
x1.place(x=180, y=70)

photo = PhotoImage(file = r"type-speed-open.png")
  
# Resizing image to fit on button
photoimage = photo.subsample(3, 3)
  
b1 = Button(window, text=" START",image=photoimage,compound=CENTER, command=speed, width=300, fg='white')
b1.place(x=140, y=150)
  
# calling window
window.mainloop()