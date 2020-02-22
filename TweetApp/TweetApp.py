import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.tweet_button = tk.Button(self)
        self.tweet_button["text"] = "Tweet !"
        self.tweet_button["command"] = self.tweet
        self.tweet_button.pack(side="right")

        self.text_form = tk.Text(self,
                                 height = 5,
                                 width = 20,
                                 font = ('メイリオ', '11'))
        self.text_form.pack(side="left")

    def tweet(self):
        print("Tweet !")

root = tk.Tk()
app = Application(root)
app.mainloop()
