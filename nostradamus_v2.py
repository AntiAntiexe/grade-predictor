import customtkinter
from customtkinter import *
from Scripts.linearRegrUtils import LinearRegr, Utils


'''
This is the App class which contains all the UI functions 

It contains the __init__ function and the button function.
'''


class App:

    '''
        Once class app is called, __init__ states and places the different ui elements onto the app.,
    '''

    def __init__(self):
        super().__init__()

        self.app = CTk()
        self.app.title("The Nostradamus")
        self.app.geometry("2560x1600")
        set_appearance_mode("dark")

        # Create the User interface using custom tkinter

        # Frames
        self.frame = CTkFrame(master=self.app, fg_color='#323231', border_color='#323231', border_width=2, width=2560,
                              height=1600, )
        self.frame.place(relx=.5, rely=.5, anchor=CENTER),

        self.frame2 = CTkFrame(master=self.app, fg_color='#323231', bg_color='#323231', border_color='#323231',
                               border_width=2,
                               width=200, height=181, )
        self.frame2.place = self.frame2.place(relx=.36, rely=.75, anchor=CENTER)

        # fonts
        self.my_font = customtkinter.CTkFont(family="sans serif", size=75, weight="bold", )

        self.my_font2 = customtkinter.CTkFont(family="sans serif", size=25, weight="normal", )

        # Entry boxes
        self.entry = CTkEntry(master=self.frame, placeholder_text="Input first grade", width=185, fg_color='#0fa4af',
                              border_color='#0d737a', text_color="black", placeholder_text_color='#323231',
                              font=(self.my_font2, 20))
        self.entry.place(relx=0.328, rely=0.6, anchor=E)
        self.entry2 = CTkEntry(master=self.frame, placeholder_text="Input second grade", width=185, fg_color='#0fa4af',
                               border_color='#0d737a', text_color="black", placeholder_text_color='#323231',
                               font=(self.my_font2, 20))
        self.entry2.place(relx=0.328, rely=0.63, anchor=E)

        # Labels
        self.label = CTkLabel(master=self.frame, text="The", font=self.my_font)
        self.label.place(relx=0.28, rely=0.3, anchor=CENTER)

        self.label1 = CTkLabel(master=self.frame, text="Nostradamus.", font=self.my_font, text_color='#0fa4af')
        self.label1.place(relx=0.35, rely=0.35, anchor=CENTER)

        self.label2 = CTkLabel(master=self.frame,
                               text='The Nostradamus is an "accurate" grade predictor. This can be used by inputting your two recent grades which '
                                    "will predict your third grade. It will also display the graph used to predict "
                                    "your grade with your grade highlighted!",
                               wraplength=550, justify='left', font=self.my_font2, width=20, height=25)
        self.label2.place(relx=0.36, rely=0.46, anchor=CENTER)

        self.label3 = CTkLabel(master=self.frame2, text="0%", font=self.my_font, text_color='#0fa4af')
        self.label3.place(relx=0.5, rely=0.3, anchor=CENTER)

        self.label4 = CTkLabel(master=self.frame2, text="Your Result", font=self.my_font2)
        self.label4.place(relx=0.5, rely=0.6, anchor=CENTER)

        self.linear = LinearRegr(self, self.entry, self.entry2, self.frame, self.label3, self.label4)

        self.util = Utils(self, self.entry, self.entry2)

    '''
           When called it will place the submit button and the reset button on the frame. 
           Once the submit button is clicked it will activate the predict function from class LinearRegr.
           Once the reset button is clicked it will activate the reset function from the utils class
           
           
    '''
    def buttons(self):
        self.btn_reset = CTkButton(master=self.frame, text="Reset", command=self.util.reset, fg_color="#0fa4af",
                                   border_color='#0d737a',
                                   border_width=2, hover_color='#024950', text_color="#323231", height=40,
                                   font=(self.my_font2, 25))
        self.btn_reset.place(relx=.35, rely=.7, anchor='s')



        self.btn_submit = CTkButton(master=self.frame, text="Submit", command=self.linear.predict, fg_color="#0fa4af",
                                   border_color='#0d737a',
                                   border_width=2, hover_color='#024950', text_color="#323231", height=40,
                                   font=(self.my_font2, 25))
        self.btn_submit.place(relx=0.284, rely=0.7, anchor='s')
        self.app.mainloop()

    def reset_button2(self):
        print('hello')


App().buttons()


