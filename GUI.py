from tkinter import *

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

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
                        width=24, bg=self.frame_background, fg=self.text_colour).place(x=470, y=15)

        bor1 = Frame(bg=self.frame_background, width="3", height="700").place(x=600, y=56)

        bottom_bar = Frame(bg=self.frame_background, width="1366", height="20").place(x=0, y=680)

        doc_id_lab = Label(self.master, text='Document id:', bg=self.background, fg=self.text_colour,
                           font='100 12 bold').place(
            x=20, y=80)

        view_lab = Label(self.master, text='view by:', bg=self.background, fg=self.text_colour)

        # Entry boxes

        document_id = Entry(self.master, width=45, bg=self.entry_colour, textvariable=self.document).place(
            x=130, y=80)

        # Dropdown
        view_choice = {'Country', 'Continent', 'Browser'}
        self.Drop_Down.set('Country')  # set the default option
        view_menu = OptionMenu(self.master, self.Drop_Down, *view_choice)
        view_menu.config(bg=self.button_colour, activebackground=self.frame_background, fg=self.text_colour,
                         activeforeground=self.text_colour, width=7)
        view_menu['menu'].config(bg=self.entry_colour, fg=self.text_colour, borderwidth=0, activeborderwidth=0,
                                 activeforeground=self.text_colour, activebackground=self.frame_background)
        view_menu["highlightthickness"] = 0
        view_menu.place(x=500, y=74)

        # Buttons
        view = Button(self.master, text='Search', width=7, bg=self.button_colour,
                      activebackground=self.frame_background, fg=self.text_colour,
                      activeforeground=self.text_colour)
        view.bind(self.view_search)
        view.place(x=420, y=75)

        exit_button = Button(self.master, text='Exit')
        exit_button.place(x=1170, y=0)
        exit_button.bind('<Button-1>', self.closeGUI)

    def view_search(self):
        if self.Drop_Down.get() == 'Country':
            self.country_click()
        if self.Drop_Down.get() == 'Continent':
            self.continent_click()
        if self.Drop_Down.get() == 'Browser':
            self.browser_click()

    def country_click(self, event):
        doc = self.document.get()
        country_group = Viewer.Get_countries(doc)
        fig = Figure(figsize=(6, 6))
        try:
            ax = country_group.plot(kind='bar')
            ax.set_ylabel('Number of viewers')
            ax.set_xlabel('Countries')
            ax.set_title('Views by country')

            canvas = FigureCanvasTkAgg(fig, master=self.master)
            canvas.get_tk_widget().pack()
            canvas.draw()
        except IndexError as error:
            raise Exception('No views for this file') from error

    def continent_click(self, event):
        doc = self.document.get()
        countries = Viewer.Get_countries(doc)
        continent_groups = Viewer.Get_continents(countries)
        fig = Figure(figsize=(6, 6))
        try:
            ax = continent_groups.plot(kind='bar')
            ax.set_ylabel('Number of viewers')
            ax.set_xlabel('Continents')
            ax.set_title('Views by Continents')

            canvas = FigureCanvasTkAgg(fig, master=self.master)
            canvas.get_tk_widget().pack()
            canvas.draw()
        except IndexError as error:
            raise Exception('No views for this file') from error

    def browser_click(self, event):
        doc = self.document.get()
        continent_groups = Viewer.Get_browser(doc)
        fig = Figure(figsize=(6, 6))
        try:
            ax = continent_groups.plot(kind='bar')
            ax.set_ylabel('Number of viewers')
            ax.set_xlabel('Continents')
            ax.set_title('Views by Continents')

            canvas = FigureCanvasTkAgg(fig, master=self.master)
            canvas.get_tk_widget().pack()
            canvas.draw()
            return ax
        except IndexError as error:
            raise Exception('No views for this file') from error

    def closeGUI(self, event):
        self.master.destroy()


root = Tk()
obj = MyInterface(root)
root.mainloop()
