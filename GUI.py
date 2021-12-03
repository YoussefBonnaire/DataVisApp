from tkinter import *

import matplotlib
from pandastable import Table

import Reader

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import Viewer


# LARGE_FONT = ("Verdana", 24)
# background = '#000731'
# frame_background = '#010523'
# text_colour = '#aaa0c7'
# entry_colour = '#394381'
# button_colour = '#111b55'


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
        self.view_by = StringVar()
        self.Drop_Down = StringVar()
        self.body()

        # Main
        master.title('The Data Analyser')
        master.configure(background=self.background)

        # for multi-page use

        # container = Frame(self)
        # container.pack(side="top", fill="both", expand=True)
        # container.grid_rowconfigure(0, weight=2)
        # container.grid_rowconfigure(1, weight=1)
        # container.grid_rowconfigure(2, weight=1)
        # container.grid_rowconfigure(3, weight=10)
        # container.grid_rowconfigure(4, weight=2)
        # container.grid_columnconfigure(tuple(range(60)), weight=1)

        # for F in (StartPage, Document_viewer, Avid_reader, Also_likes):
        #     frame = F(container, self)
        #
        #     self.frames[F] = frame
        #
        #     frame.grid(row=0, column=0, sticky="nsew")
        #
        # self.show_frame(StartPage)

    def body(self):
        # Configure grid
        self.master.rowconfigure(0, weight=2)
        self.master.rowconfigure(1, weight=1)
        self.master.rowconfigure(2, weight=1)
        self.master.rowconfigure(3, weight=8)
        self.master.rowconfigure(4, weight=1)
        self.master.rowconfigure(5, weight=2)
        self.master.columnconfigure(tuple(range(60)), weight=1)

        # Frame
        left_seperation = Label(self.master, anchor='center', bg=self.frame_background)
        bottom_bar = Label(self.master, anchor='center', bg=self.frame_background)

        # Labels
        title_lab = Label(self.master, text='Welcome to the Data Analyser', anchor='center', font=100,
                          width=24, bg=self.frame_background, fg=self.text_colour)

        doc_id_lab = Label(self.master, text='Document id:', bg=self.background, fg=self.text_colour,
                           font='100 12 bold')

        view_lab = Label(self.master, text='display by:', bg=self.background, fg=self.text_colour)

        # Entry boxes
        document_id = Entry(self.master, width=45, bg=self.entry_colour, textvariable=self.document)

        # Dropdown
        view_choice = {'Country', 'Continent', 'Browser', 'All'}
        self.Drop_Down.set('Country')  # set the default option
        view_menu = OptionMenu(self.master, self.Drop_Down, *view_choice)
        view_menu.config(bg=self.button_colour, activebackground=self.frame_background, fg=self.text_colour,
                         activeforeground=self.text_colour, width=7)
        view_menu['menu'].config(bg=self.entry_colour, fg=self.text_colour, borderwidth=0, activeborderwidth=0,
                                 activeforeground=self.text_colour, activebackground=self.frame_background)
        view_menu["highlightthickness"] = 0

        # Buttons
        display = Button(self.master, text='Display', width=7, bg=self.button_colour,
                         activebackground=self.frame_background, fg=self.text_colour,
                         activeforeground=self.text_colour)
        display.bind('<Button-1>', self.view_display)

        reader = Button(self.master, text='Show top 10 most avid reader', bg=self.button_colour,
                        activebackground=self.frame_background, fg=self.text_colour,
                        activeforeground=self.text_colour)
        reader.bind('<Button-1>', self.reader_display)

        exit_button = Button(self.master, text='Exit')
        exit_button.bind('<Button-1>', self.closeGUI)

        # Positioning
        title_lab.grid(row=0, column=0, columnspan=101, sticky="news")
        doc_id_lab.grid(row=1, column=0, sticky="NE")
        document_id.grid(row=1, column=1, sticky="NE")
        display.grid(row=1, column=2, sticky="NE")
        view_lab.grid(row=1, column=3, sticky="NE")
        view_menu.grid(row=1, column=4, sticky="NE")

        reader.grid(row=2, column=1, columnspan=3, sticky="N")

        left_seperation.grid(row=1, column=5, rowspan=4, sticky="news")
        bottom_bar.grid(row=5, column=0, columnspan=101, sticky="news")
        exit_button.grid(row=0, column=100, sticky="nw")

    # def show_frame(self, cont):
    #     frame = self.frames[cont]
    #     frame.tkraise()

    def view_display(self, event):
        if self.Drop_Down.get() == 'Country':
            self.country_click()
        if self.Drop_Down.get() == 'Continent':
            self.continent_click()
        if self.Drop_Down.get() == 'Browser':
            self.browser_click()
        if self.Drop_Down.get() == 'All':
            self.all_click()

    def reader_display(self, event):
        top10 = Reader.top10()
        # top10_list = Label(self.master, text=top10.to_string(), anchor='center', font=100,
        #                    width=24, bg=self.frame_background, fg=self.text_colour)
        # top10_list.grid(row=3, column=0, columnspan=5)
        f = Frame(self.master)
        f.grid(row=3, column=0, columnspan=5)
        self.table = pt = Table(f, dataframe=top10,
                                showtoolbar=True, showstatusbar=True)
        pt.show()

    def country_click(self):
        doc = self.document.get()
        country_group, _ = Viewer.Get_countries(doc)

        fr_plot = Frame(self.master)
        fr_plot.grid(row=3, column=0, columnspan=5, sticky='news')
        fig = Figure()
        ax1 = fig.add_subplot(111)
        canvas = FigureCanvasTkAgg(fig, fr_plot)
        if type(country_group) is not str:
            country_group.plot(kind='bar', ax=ax1)
            ax1.set_ylabel('Number of viewers')
            ax1.set_xlabel('Countries')
            ax1.set_title('Views by country')
            toolbar = NavigationToolbar2Tk(canvas, self.master, pack_toolbar=False)
            toolbar.update()
            toolbar.grid(row=4, column=0, columnspan=5, sticky='news')
            canvas._tkcanvas.grid(row=3, column=0, columnspan=5, sticky='news')
        else:
            no_views = Label(self.master, text=country_group, anchor='center', font=100,
                             width=24, bg=self.frame_background, fg=self.text_colour)
            no_views.grid(row=3, column=0, columnspan=5)

    def continent_click(self):
        doc = self.document.get()
        _, countries = Viewer.Get_countries(doc)
        continent_groups = Viewer.Get_continents(countries)

        fr_plot = Frame(self.master)
        fr_plot.grid(row=3, column=0, columnspan=5, sticky='news')
        fig = Figure()
        ax1 = fig.add_subplot(111)
        canvas = FigureCanvasTkAgg(fig, fr_plot)
        if type(continent_groups) is not str:
            continent_groups.plot(kind='bar', ax=ax1)
            ax1.set_ylabel('Number of viewers')
            ax1.set_xlabel('Continents')
            ax1.set_title('Views by Continents')
            toolbar = NavigationToolbar2Tk(canvas, self.master, pack_toolbar=False)
            toolbar.update()
            toolbar.grid(row=4, column=0, columnspan=5, sticky='news')
            canvas._tkcanvas.grid(row=3, column=0, columnspan=5, sticky='news')
        else:
            no_views = Label(self.master, text=continent_groups, anchor='center', font=100,
                             width=24, bg=self.frame_background, fg=self.text_colour)
            no_views.grid(row=3, column=0, columnspan=5)

    def browser_click(self):
        doc = self.document.get()
        browser_group = Viewer.Get_browser(doc)

        fr_plot = Frame(self.master)
        fr_plot.grid(row=3, column=0, columnspan=5, sticky='news')
        fig = Figure()
        ax1 = fig.add_subplot(111)
        canvas = FigureCanvasTkAgg(fig, fr_plot)
        if type(browser_group) is not str:
            browser_group.plot(kind='bar', ax=ax1)
            ax1.set_ylabel('Number of viewers')
            ax1.set_xlabel('Browsers')
            ax1.set_title('Views by Browsers')
            toolbar = NavigationToolbar2Tk(canvas, self.master, pack_toolbar=False)
            toolbar.update()
            toolbar.grid(row=4, column=0, columnspan=5, sticky='news')
            canvas._tkcanvas.grid(row=3, column=0, columnspan=5, sticky='news')
        else:
            no_views = Label(self.master, text=browser_group, anchor='center', font=100,
                             width=24, bg=self.frame_background, fg=self.text_colour)
            no_views.grid(row=3, column=0, columnspan=5)

    def all_click(self):
        doc = self.document.get()
        country_groups, countries = Viewer.Get_countries(doc)
        continent_groups = Viewer.Get_continents(countries)
        browser_group = Viewer.Get_browser(doc)

        # unfinished = Label(self.master, text='Functionality not finished', anchor='center', font=100,
        # unfinished.grid(row=3, column=0, columnspan=5)
        #                    width=24, bg=self.frame_background, fg=self.text_colour)

        fr_plot = Frame(self.master)
        fr_plot.grid(row=3, column=0, columnspan=5, sticky='news')
        fig = Figure()
        ax1 = fig.add_subplot(131)
        ax2 = fig.add_subplot(132)
        ax3 = fig.add_subplot(133)
        if type(country_groups) is not str:
            country_groups.plot(kind='bar', ax=ax1)
            ax1.set_ylabel('Number of viewers')
            ax1.set_xlabel('Country')
            ax1.set_title('Views by Countries')

            continent_groups.plot(kind='bar', ax=ax2)
            ax2.set_ylabel('Number of viewers')
            ax2.set_xlabel('Continent')
            ax2.set_title('Views by Continents')

            browser_group.plot(kind='bar', ax=ax3)
            ax3.set_ylabel('Number of viewers')
            ax3.set_xlabel('Browsers')
            ax3.set_title('Views by Browsers')

            canvas = FigureCanvasTkAgg(fig, fr_plot)
            toolbar = NavigationToolbar2Tk(canvas, self.master, pack_toolbar=False)
            toolbar.update()
            toolbar.grid(row=4, column=0, columnspan=5, sticky='news')
            canvas._tkcanvas.grid(row=3, column=0, columnspan=5, sticky='news')
        else:
            no_views = Label(self.master, text=continent_groups, anchor='center', font=100,
                             width=24, bg=self.frame_background, fg=self.text_colour)
            no_views.grid(row=3, column=0, columnspan=5)

    def closeGUI(self, event):
        self.master.destroy()


# class StartPage(Frame):
#
#     def __init__(self, parent, controller):
#         Frame.__init__(self, parent)
#         title_lab = Label(self, text="Welcome to the Data Analyser", font=LARGE_FONT)
#         title_lab.grid(row=0, column=0, columnspan=101, sticky="news")
#
#         doc_button = Button(self, text="Click for document views",
#                             command=lambda: controller.show_frame(Document_viewer))
#         doc_button.grid(row=1, column=0, sticky='news')
#
#         reader_button = Button(self, text="Click for Avid reader list",
#                                command=lambda: controller.show_frame(Avid_reader))
#         reader_button.grid(row=1, column=1, sticky='news')
#
#         alsolikes_button = Button(self, text="Click for also likes functionality",
#                                   command=lambda: controller.show_frame(Also_likes))
#         alsolikes_button.grid(row=1, column=2, sticky='news')
#
#         bottom_bar = Label(self.master, anchor='center', bg=self.frame_background)


root = Tk()
obj = MyInterface(root)
root.mainloop()
