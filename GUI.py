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
        self.database = StringVar(master, value='issuu_cw2.json')
        self.document_also = StringVar()
        self.user_also = StringVar()
        self.database_also = StringVar(master, value='issuu_cw2.json')
        self.background = '#000731'
        self.frame_background = '#010523'
        self.text_colour = '#aaa0c7'
        self.entry_colour = '#394381'
        self.button_colour = '#111b55'
        self.view_by = StringVar()
        self.Drop_Down = StringVar()
        self.left_canvas = Canvas(self.master)
        self.right_canvas = Canvas(self.master)
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
        self.master.rowconfigure(0, weight=3)
        self.master.rowconfigure(1, weight=1)
        self.master.rowconfigure(2, weight=1)
        self.master.rowconfigure(3, weight=1)
        self.master.rowconfigure(4, weight=10)
        self.master.rowconfigure(5, weight=1)
        self.master.rowconfigure(6, weight=2)
        self.master.columnconfigure(tuple(range(13)), weight=1)

        # Frame
        separation = Label(self.master, anchor='center', bg=self.frame_background)
        bottom_bar = Label(self.master, anchor='center', bg=self.frame_background)

        # Labels
        title_lab = Label(self.master, text='Welcome to the Data Analyser', anchor='center', font=100,
                          width=29, bg=self.frame_background, fg=self.text_colour)
        left_subtitle_lab = Label(self.master, text='Views & Top 10', anchor='center', font=100,
                                  width=29, bg=self.frame_background, fg=self.text_colour)
        right_subtitle_lab = Label(self.master, text='Also Likes', anchor='center', font=100,
                                   width=29, bg=self.frame_background, fg=self.text_colour)

        doc_id_lab = Label(self.master, text='Document id:', bg=self.background, fg=self.text_colour,
                           font='100 12 bold', width=13)

        database_file_lab = Label(self.master, text='Database file name:', bg=self.background, fg=self.text_colour,
                                  font='100 12 bold', width=20)

        doc_id_lab_also = Label(self.master, text='Document id:', bg=self.background, fg=self.text_colour,
                                font='100 12 bold', width=13)
        user_id_lab_also = Label(self.master, text='User id:', bg=self.background, fg=self.text_colour,
                                 font='100 12 bold', width=9)

        database_file_lab_also = Label(self.master, text='Database file name:', bg=self.background, fg=self.text_colour,
                                       font='100 12 bold', width=20)

        view_lab = Label(self.master, text='Display by:', bg=self.background, fg=self.text_colour)

        # Entry boxes
        document_id = Entry(self.master, bg=self.entry_colour, textvariable=self.document)
        database_file = Entry(self.master, bg=self.entry_colour, textvariable=self.database)

        document_id_also = Entry(self.master, bg=self.entry_colour, textvariable=self.document_also)
        user_id_also = Entry(self.master, bg=self.entry_colour, textvariable=self.user_also)
        database_file_also = Entry(self.master, bg=self.entry_colour, textvariable=self.database_also)

        # Dropdown
        view_choice = {'Country', 'Continent', 'Browser', 'All'}
        self.Drop_Down.set('Country')  # set the default option
        view_menu = OptionMenu(self.master, self.Drop_Down, *view_choice)
        view_menu.config(bg=self.button_colour, activebackground=self.frame_background, fg=self.text_colour,
                         activeforeground=self.text_colour, width=10)
        view_menu['menu'].config(bg=self.entry_colour, fg=self.text_colour, borderwidth=0, activeborderwidth=0,
                                 activeforeground=self.text_colour, activebackground=self.frame_background)
        view_menu["highlightthickness"] = 0

        # Buttons
        display = Button(self.master, text='Display', width=8, bg=self.button_colour,
                         activebackground=self.frame_background, fg=self.text_colour,
                         activeforeground=self.text_colour)
        display.bind('<Button-1>', self.view_display)

        reader = Button(self.master, text='Show Top 10 Readers', bg=self.button_colour,
                        activebackground=self.frame_background, fg=self.text_colour,
                        activeforeground=self.text_colour, width=28)
        reader.bind('<Button-1>', self.reader_display)

        graph_doc = Button(self.master, text='Display Document View', width=21, bg=self.button_colour,
                           activebackground=self.frame_background, fg=self.text_colour,
                           activeforeground=self.text_colour)
        graph_user = Button(self.master, text='Display User View', width=21, bg=self.button_colour,
                            activebackground=self.frame_background, fg=self.text_colour,
                            activeforeground=self.text_colour)

        display.bind('<Button-1>', self.view_display)

        exit_button = Button(self.master, text='Exit')
        exit_button.bind('<Button-1>', self.closeGUI)

        # Positioning
        title_lab.grid(row=0, column=0, columnspan=13, sticky="news")
        left_subtitle_lab.grid(row=1, column=0, columnspan=6, sticky="news")
        right_subtitle_lab.grid(row=1, column=7, columnspan=6, sticky="news")

        database_file_lab.grid(row=2, column=0, sticky="news", pady=10, padx=2)
        database_file.grid(row=2, column=1, sticky="news", pady=10, padx=2)
        reader.grid(row=2, column=2, columnspan=3, sticky="news", pady=10, padx=2)

        doc_id_lab.grid(row=3, column=0, sticky="news")
        document_id.grid(row=3, column=1, sticky="news", pady=10, padx=2)
        display.grid(row=3, column=2, sticky="news", pady=10, padx=2)
        view_lab.grid(row=3, column=3, sticky="news", pady=10, padx=2)
        view_menu.grid(row=3, column=4, sticky="news", pady=10, padx=2)

        self.left_canvas.grid(row=4, column=0, columnspan=5, rowspan=2, sticky='news')

        database_file_lab_also.grid(row=2, column=7, sticky="news", pady=10, padx=2)
        database_file_also.grid(row=2, column=8, columnspan=6, sticky="news", pady=10, padx=2)

        doc_id_lab_also.grid(row=3, column=7, sticky="news")
        document_id_also.grid(row=3, column=8, sticky="news", pady=10, padx=2)
        graph_doc.grid(row=3, column=9, sticky="news", pady=10, padx=2)

        user_id_lab_also.grid(row=3, column=10, sticky="news", pady=10, padx=2)
        user_id_also.grid(row=3, column=11, sticky="news", pady=10, padx=2)
        graph_user.grid(row=3, column=12, sticky="news", pady=10, padx=2)

        self.right_canvas.grid(row=4, column=6, columnspan=7, rowspan=2, sticky='news')

        separation.grid(row=1, column=5, rowspan=5, columnspan=2, sticky="news")
        bottom_bar.grid(row=6, column=0, columnspan=13, sticky="news")
        exit_button.grid(row=0, column=12, sticky="ne")

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
        f = Frame(self.master)
        f.grid(row=4, column=0, columnspan=5, rowspan=2, sticky='news')
        self.left_canvas = pt = Table(f, dataframe=top10,
                                      showtoolbar=True, showstatusbar=True)
        pt.show()

    def country_click(self):
        doc = self.document.get()
        database = self.database.get()
        country_group, _ = Viewer.Get_countries(doc, database)

        fig = Figure()
        ax1 = fig.add_subplot(111)
        if type(country_group) is not str:
            country_group.plot(kind='bar', ax=ax1)
            ax1.set_ylabel('Number of viewers')
            ax1.set_xlabel('Countries')
            ax1.set_title('Views by country')

            self.draw_canvas(fig, self.master)
        else:
            no_views = Label(self.master, text=country_group, anchor='center', font=100,
                             width=24, bg=self.frame_background, fg=self.text_colour)
            no_views.grid(row=4, column=0, columnspan=5, rowspan=2, sticky='news')

    def continent_click(self):
        doc = self.document.get()
        database = self.database.get()
        _, countries = Viewer.Get_countries(doc, database)
        continent_groups = Viewer.Get_continents(countries)

        fig = Figure()
        ax1 = fig.add_subplot(111)
        if type(continent_groups) is not str:
            continent_groups.plot(kind='bar', ax=ax1)
            ax1.set_ylabel('Number of viewers')
            ax1.set_xlabel('Continents')
            ax1.set_title('Views by Continents')

            self.draw_canvas(fig, self.master)
        else:
            no_views = Label(self.master, text=continent_groups, anchor='center', font=100,
                             width=24, bg=self.frame_background, fg=self.text_colour)
            no_views.grid(row=4, column=0, columnspan=5, rowspan=2, sticky='news')

    def browser_click(self):
        doc = self.document.get()
        database = self.database.get()
        browser_group = Viewer.Get_browser(doc, database)

        fig = Figure()
        ax1 = fig.add_subplot(111)
        if type(browser_group) is not str:
            browser_group.plot(kind='bar', ax=ax1)
            ax1.set_ylabel('Number of viewers')
            ax1.set_xlabel('Browsers')
            ax1.set_title('Views by Browsers')

            self.draw_canvas(fig, self.master)
        else:
            no_views = Label(self.master, text=browser_group, anchor='center', font=100,
                             width=24, bg=self.frame_background, fg=self.text_colour)
            no_views.grid(row=4, column=0, columnspan=5, rowspan=2, sticky='news')

    def all_click(self):
        doc = self.document.get()
        country_groups, countries = Viewer.Get_countries(doc)
        continent_groups = Viewer.Get_continents(countries)
        browser_group = Viewer.Get_browser(doc)

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
            ax2.set_xlabel('Continent')
            ax2.set_title('Views by Continents')

            browser_group.plot(kind='bar', ax=ax3)
            ax3.set_xlabel('Browsers')
            ax3.set_title('Views by Browsers')

            self.draw_canvas(fig, self.master)
        else:
            no_views = Label(self.master, text=country_groups, anchor='center', font=100,
                             width=24, bg=self.frame_background, fg=self.text_colour)
            no_views.grid(row=4, column=0, columnspan=5, rowspan=2, sticky='news')

    def draw_canvas(self, fig, plot):
        self.left_canvas = FigureCanvasTkAgg(fig, plot)
        self.left_canvas.draw()
        self.left_canvas.get_tk_widget().grid(row=3, column=0, columnspan=5, sticky='news', ipadx=0, ipady=0)
        toolbar = NavigationToolbar2Tk(self.left_canvas, self.master, pack_toolbar=False)
        toolbar.update()
        toolbar.grid(row=4, column=0, columnspan=5, sticky='news')

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
