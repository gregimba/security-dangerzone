from Tkinter import *

try:
    import cpickle as pickle
except:
    import pickle

db = []

def load():
    db = pickle.load(open("db.pkl","wb"))

def dump():
    pickle.dump(db,open("db.pkl","wb"))


class Application(Frame):
    def say_hi(self):
        print "hi there, everyone!"

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.SAVE = Button(self)
        self.SAVE["text"] = "SAVE"
        self.SAVE["fg"] = "black"
        self.SAVE["command"] = self.save

        self.SAVE.pack({"side":"right"})

    def save(self):
    	pickle.dump(db,open("db.pkl","wb"))

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()