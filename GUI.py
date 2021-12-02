from tkinter import *

import Viewer


class MyInterface:
    LABEL_TEXT = ['This is the Interface package.',
                  'This is the class for GUI,']

    def __init__(self, master):
        # Declaration of Variables
        self.master = master
        self.document = StringVar()
        self.background = '#000731'
        self.frame_background = '#010523'
        self.text_colour = '#aaa0c7'
        self.entry_colour = '#394381'
        self.button_colour = '#111b55'
        self.afgc = '#'
        self.view_by = StringVar()
        self.Drop_Down = StringVar()
        self.body()

        # Main
        master.title('The Data Analyser')
        master.configure(background=self.background)
        master.geometry('1200x700')

    def body(self):
        # Label
        top_bar = Frame(bg=self.frame_background, width="1366", height="56").place(x=0, y=0)
        top_lab = Label(self.master, text='Welcome to the Data Analyser', anchor=W, font=100,
                        width=24, bg=self.frame_background, fg=self.text_colour).place(x=450, y=15)

        bor1 = Frame(bg=self.frame_background, width="3", height="700").place(x=600, y=56)

        bottom_bar = Frame(bg=self.frame_background, width="1366", height="20").place(x=0, y=680)

        doc_id_lab = Label(self.master, text='Document id:', bg=self.background, fg=self.text_colour,
                           font='100 12 bold').place(
            x=100, y=80)

        view_lab = Label(self.master, text='View by:', bg=self.background, fg=self.text_colour)

        # Entry boxes
        document_id = Entry(self.master, width=25, bg=self.entry_colour, textvariable=self.document).place(
            x=210, y=80)

        # Dropdown
        view_choice = {'Country', 'Continent', 'Browser'}
        self.Drop_Down.set('Country')  # set the default option
        view_menu = OptionMenu(self.master, self.Drop_Down, *view_choice)
        view_menu.config(bg=self.entry_colour, activebackground=self.frame_background, fg=self.text_colour,
                         activeforeground=self.text_colour)
        view_menu['menu'].config(bg=self.entry_colour, fg=self.text_colour, borderwidth=0, activeborderwidth=0,
                                 activeforeground=self.text_colour, activebackground=self.frame_background)
        view_menu["highlightthickness"] = 0
        view_menu.place(x=500, y=75)

        # Buttons
        ###### MAKE DYNAMIC
        View = Button(self.master, text='Search', width=7, bg=self.button_colour,
                      fg=self.text_colour)
        if self.Drop_Down.get() == 'Country':
            View.bind('<Button-1>', self.country_click)
        if self.Drop_Down.get() == 'Continent':
            View.bind('<Button-1>', self.continent_click)
        if self.Drop_Down.get() == 'Browser':
            View.bind('<Button-1>', self.browser_click)
        View.place(x=400, y=75)

        exit_button = Button(self.master, text='Exit')
        exit_button.place(x=1000, y=0)
        exit_button.bind('<Button-1>', self.closeGUI)

    def country_click(self):
        doc = self.document.get()
        plot_countries, _ = Viewer.Display_countries(doc)

        return None

    def continent_click(self):
        return None

    def browser_click(self):
        return None

    def closeGUI(self, event):
        self.master.destroy()


root = Tk()
obj = MyInterface(root)
root.mainloop()
