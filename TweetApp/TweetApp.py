import tkinter as tk
from tkinter.scrolledtext import ScrolledText

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

        self.text_form = ScrolledText(self,
                                 height = 5,
                                 width = 20,
                                 font = ('メイリオ', '11'))
        self.text_form.pack(side="left")

    def tweet(self):
        text = self.text_form.get('1.0', tk.END)
        print(text)
        self.text_form.delete('1.0', tk.END)

root = tk.Tk()
app = Application(root)
app.mainloop()
