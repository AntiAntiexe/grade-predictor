#imports
from customtkinter import*
from scipy import stats
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math


#Defining the the app and seting the geometry
app = CTk()
app.title("The Nostradamus")
app.geometry("2560x1600")
set_appearance_mode("dark")

#Predict Function using scipy stats
def predict(): #when button is clicked it predicts the third grade based of two values given then averages the result.
    y = [0.3, 0.3, 0.5, 0.75, 0.5, 0.75, 0.55, 0.3, 0.95, 0.75, 0.45, 0.6, 0.7, 0.55, 0.8, 0.7, 0.7, 0.5, 0.25, 0.5,
         0.75, 0.75, 0.8, 0.6, 0.4, 0.4, 0.55, 0.75, 0.55, 0.55, 0.6, 0.85, 0.8, 0.6, 0.75, 0.3, 0.9, 0.75, 0.55, 0.65,
         0.55, 0.6, 0.9, 0.55, 0.45, 0.3, 0.55, 1, 0.7, 0.35, 0.65, 0.65, 0.5, 0.55, 0.65, 0.5, 0.75, 0.75, 0.45, 0.8,
         0.55, 0.55, 0.45, 0.45, 0.5, 0.75, 0.6, 0.3, 0.4, 0.8, 0.75, 0.5, 0.25, 0.7, 0.55, 0.5, 0.5, 0.55, 0.5, 0.25,
         0.6, 0.55, 0.3, 0.75, 0.5, 0.4, 0.3, 0.7, 0.5, 0.35, 0.4, 0.9, 0.3, 0.5, 0.7, 0.5, 0.75, 0.5, 0.7, 0.4, 0.25,
         0.85, 0.7, 0.3, 0.9, 0.55, 0.4, 0.9, 0.65, 0.8, 0.95, 0.5, 0.65, 0.95, 0.45, 0.8, 0.7, 0.65, 0.4, 0.65, 0.75,
         0.75, 0.65, 0.65, 0.4, 0.6, 0.55, 0.45, 0, 0.9, 0, 0, 0.6, 0.55, 0, 0, 0, 0, 0.6, 0.75, 0, 0.45, 0.55, 0.65, 0,
         0.55, 0, 0.55, 0, 0.5, 0, 0.7, 0.5, 0, 0.6, 0.4, 0.65, 0.5, 0.75, 0.6, 0, 0.35, 0, 0.5, 0.35, 0.6, 0.5, 0.8, 0,
         0.7, 0, 0.8, 0.5, 0, 0.45, 0.45, 0.55, 0.3, 0.45, 0.55, 0.4, 0.6, 0.85, 0.4, 0.6, 0.55, 0.55, 0.75, 0.45, 0.5,
         0.65, 0.45, 0.4, 0.5, 0.7, 0.75, 0.8, 0.5, 0.9, 0.5, 0.8, 0.5, 0.5, 0.3, 0.55, 0.45, 0.35, 0.65, 0.5, 0.35,
         0.4, 0.65, 0.7, 0.4, 0.5, 0.75, 0.2, 0.4, 0.4, 0.5, 0.3, 0, 0.85, 0.65, 0.7, 0.35, 0.75, 0.6, 0.45, 0.6, 0.7,
         0.55, 0.45, 0.65, 0.3, 0.5, 0.65, 0.6, 0.55, 0, 0.6, 0.6, 0, 0.6, 0, 0.9, 0.65, 0.4, 0.25, 0.75, 0.4, 0.5, 0.4,
         0.4, 0.6, 0.4, 0.65, 0.55, 0.7, 0, 0.9, 0.4, 0.6, 0.45, 0, 0.85, 0.5, 0.55, 0.5, 0, 0.45, 0.7, 0.55, 0.7, 0.5,
         0.6, 0.45, 0.45, 0.4, 0.5, 0.4, 0.5, 0.6, 0.5, 0.55, 0.55, 0.95, 0.6, 0.7, 0.75, 0.55, 0.75, 0.65, 0.9, 0.7,
         0.55, 0, 0.4, 0.7, 0.8, 0.55, 0.5, 0.7, 0.9, 0.65, 0.6, 0.9, 0.4, 0.6, 0.5, 0, 0.65, 0.55, 0.55, 0.65, 0.55, 0,
         0.45, 0.5, 0.55, 0.65, 0.45, 0.55, 0.75, 0.75, 0.55, 0.8, 0.5, 0.45, 0.7, 0.4, 0.7, 0, 0, 0, 0.75, 0.65, 0,
         0.85, 0.5, 0.55, 0, 0.75, 0, 0.5, 0.7, 0.8, 0.45, 0.75, 0.65, 0.4, 0.65, 0.4, 0.4, 0.55, 0.45, 0.65, 0.55, 0.5,
         0.8, 0.65, 0.6, 0.5, 0.75, 0.6, 0.5, 0.65, 0, 0.5, 0.55, 0.45, 0.6, 0.55, 0.25, 0.95, 0.5, 0.75, 0.5, 0.75,
         0.5, 0.7, 0.35, 0.5, 0, 0.25, 0.5, 0.3, 0, 0.4, 0, 0.45, 0.8, 0.35, 0.5, 0.45]

    x = [0.125, 0.125, 0.25, 0.75, 0.1875, 0.75, 0.5625, 0.1875, 0.8125, 0.6875, 0.4375, 0.4375, 0.6875, 0.4375, 0.6875,
         0.6875, 0.625, 0.3125, 0.1875, 0.3125, 0.625, 0.5625, 0.75, 0.625, 0.4375, 0.1875, 0.5625, 0.75, 0.5, 0.4375,
         0.375, 0.875, 0.875, 0.3125, 0.5625, 0.3125, 0.75, 0.75, 0.5625, 0.6875, 0.25, 0.5625, 1, 0.3125, 0.4375,
         0.3125, 0.5, 1, 0.75, 0.25, 0.5625, 0.5, 0.5, 0.3125, 0.4375, 0.3125, 0.6875, 0.6875, 0.375, 0.75, 0.4375,
         0.4375, 0.3125, 0.4375, 0.4375, 0.8125, 0.625, 0.25, 0.3125, 0.8125, 0.625, 0.4375, 0.3125, 0.5625, 0.5, 0.375,
         0.5, 0.5, 0.3125, 0.125, 0.4375, 0.5, 0.25, 0.75, 0.375, 0.25, 0.3125, 0.625, 0.5, 0.3125, 0.25, 0.8125, 0.25,
         0.5, 0.5, 0.25, 0.5, 0.3125, 0.5, 0.25, 0.25, 0.8125, 0.4375, 0.25, 0.8125, 0.4375, 0.25, 0.8125, 0.4375,
         0.6875, 0.9375, 0.25, 0.4375, 0.9375, 0.375, 0.75, 0.5, 0.625, 0.375, 0.6875, 0.8125, 0.8125, 0.625, 0.6875,
         0.3125, 0.625, 0.25, 0.25, 0.25, 0.9375, 0.5625, 0.3125, 0.4375, 0.5625, 0.375, 0.5, 0.4375, 0.0625, 0.6875,
         0.8125, 0.25, 0.375, 0.375, 0.6875, 0.125, 0.3125, 0.1875, 0.4375, 0.25, 0.3125, 0.1875, 0.5625, 0.4375, 0.125,
         0.5, 0.5, 0.8125, 0.375, 0.875, 0.4375, 0.25, 0.125, 0.25, 0.4375, 0.125, 0.5625, 0.4375, 0.6875, 0.1875,
         0.6875, 0.1875, 0.625, 0.625, 0.3125, 0.4375, 0.4375, 0.625, 0.1875, 0.4375, 0.4375, 0.375, 0.5625, 0.8125,
         0.375, 0.5625, 0.5625, 0.5, 0.75, 0.3125, 0.3125, 0.5, 0.3125, 0.25, 0.3125, 0.625, 0.6875, 0.875, 0.375,
         0.9375, 0.375, 0.8125, 0.3125, 0.375, 0.25, 0.4375, 0.4375, 0.25, 0.5, 0.375, 0.25, 0.3125, 0.5625, 0.5625,
         0.1875, 0.3125, 0.6875, 0.1875, 0.1875, 0.25, 0.375, 0.1875, 0.1875, 0.8125, 0.5625, 0.625, 0.375, 0.8125,
         0.5625, 0.4375, 0.5625, 0.625, 0.5, 0.5, 0.6875, 0.375, 0.5, 0.6875, 0.625, 0.625, 0.25, 0.5625, 0.4375,
         0.1875, 0.625, 0.25, 0.9375, 0.5625, 0.1875, 0, 0.625, 0.1875, 0.25, 0.1875, 0.3125, 0.3125, 0.25, 0.6875, 0.5,
         0.75, 0.4375, 0.875, 0.3125, 0.625, 0.4375, 0.375, 0.875, 0.375, 0.5625, 0.4375, 0.1875, 0.375, 0.75, 0.5,
         0.75, 0.4375, 0.5625, 0.4375, 0.375, 0.375, 0.4375, 0.3125, 0.5, 0.5625, 0.3125, 0.4375, 0.5625, 0.9375, 0.625,
         0.75, 0.75, 0.5625, 0.75, 0.5625, 0.9375, 0.6875, 0.6875, 0.4375, 0.4375, 0.6875, 0.8125, 0.5625, 0.5, 0.75,
         0.875, 0.75, 0.6875, 0.875, 0.3125, 0.75, 0.5625, 0.375, 0.6875, 0.625, 0.625, 0.75, 0.625, 0.3125, 0.375, 0.5,
         0.5, 0.625, 0.5, 0.5, 0.5625, 0.8125, 0.375, 0.6875, 0.5, 0.4375, 0.6875, 0.375, 0.5625, 0.25, 0.3125, 0.4375,
         0.8125, 0.6875, 0.25, 0.8125, 0.375, 0.5, 0.4375, 0.8125, 0.375, 0.5, 0.625, 0.8125, 0.4375, 0.625, 0.5,
         0.3125, 0.625, 0.3125, 0.3125, 0.625, 0.4375, 0.5625, 0.5625, 0.4375, 0.9375, 0.625, 0.625, 0.5, 0.8125,
         0.5625, 0.4375, 0.625, 0.25, 0.5, 0.6875, 0.25, 0.6875, 0.625, 0.1875, 1, 0.3125, 0.75, 0.3125, 0.75, 0.4375,
         0.75, 0.25, 0.5, 0.1875, 0.1875, 0.4375, 0.1875, 0.25, 0.25, 0.1875, 0.375, 0.6875, 0.4375, 0.5, 0.3125]

    xx = [0.315789474, 0.263157895, 0.421052632, 0.736842105, 0.526315789, 0.789473684, 0.631578947, 0.263157895,0.947368421,
          0.789473684, 0.421052632, 0.631578947, 0.736842105, 0.526315789, 0.842105263, 0.736842105, 0.736842105,0.526315789,
          0.263157895, 0.526315789, 0.736842105, 0.789473684, 0.789473684, 0.684210526, 0.473684211, 0.473684211,0.631578947,
          0.842105263, 0.578947368, 0.631578947, 0.578947368, 0.842105263, 0.842105263, 0.526315789, 0.736842105,0.368421053,
          0.842105263, 0.842105263, 0.631578947, 0.684210526, 0.526315789, 0.631578947, 0.947368421, 0.421052632,0.526315789,
          0.421052632, 0.631578947, 1, 0.789473684, 0.368421053, 0.684210526, 0.684210526, 0.578947368, 0.526315789,0.684210526,
          0.473684211, 0.789473684, 0.789473684, 0.526315789, 0.842105263, 0.578947368, 0.421052632, 0.526315789,0.473684211,
          0.526315789, 0.789473684, 0.684210526, 0.368421053, 0.473684211, 0.842105263, 0.789473684, 0.526315789,0.315789474,
          0.631578947, 0.631578947, 0.473684211, 0.578947368, 0.578947368, 0.421052632, 0.263157895, 0.631578947,0.526315789,
          0.315789474, 0.789473684, 0.526315789, 0.473684211, 0.368421053, 0.736842105, 0.526315789, 0.315789474,0.368421053,
          0.894736842, 0.315789474, 0.526315789, 0.684210526, 0.526315789, 0.789473684, 0.473684211, 0.736842105,0.473684211,
          0.368421053, 0.894736842, 0.684210526, 0.315789474, 0.947368421, 0.578947368, 0.421052632, 0.947368421,0.684210526,
          0.789473684, 1, 0.526315789, 0.684210526, 1, 0.473684211, 0.789473684, 0.684210526, 0.736842105, 0.368421053,0.684210526,
          0.789473684, 0.736842105, 0.684210526, 0.578947368, 0.368421053, 0.684210526, 0.526315789, 0.421052632,0.210526316,
          0.947368421, 0, 0, 0.684210526, 0.578947368, 0, 0, 0, 0, 0.631578947, 0.842105263, 0.473684211, 0.473684211,0.578947368,
          0.736842105, 0, 0.578947368, 0.368421053, 0.578947368, 0.315789474, 0.473684211, 0.263157895, 0.684210526,0.526315789, 0,
          0.578947368, 0.421052632, 0.631578947, 0.421052632, 0.789473684, 0.631578947, 0.315789474, 0.473684211, 0,0.526315789,
          0.421052632, 0.578947368, 0.526315789, 0.789473684, 0.368421053, 0.736842105, 0.263157895, 0.789473684,0.578947368, 0.368421053,
          0.578947368, 0.473684211, 0.684210526, 0.263157895, 0.421052632, 0.526315789, 0.421052632, 0.684210526,0.894736842, 0.473684211,
          0.684210526, 0.631578947, 0.631578947, 0.789473684, 0.368421053, 0.473684211, 0.631578947, 0.421052632,0.421052632,
          0.473684211, 0.736842105, 0.789473684, 0.789473684, 0.473684211, 0.947368421, 0.473684211, 0.842105263,0.526315789,
          0.473684211, 0.315789474, 0.526315789, 0.473684211, 0.368421053, 0.631578947, 0.473684211, 0.368421053,0.421052632,
          0.631578947, 0.684210526, 0.368421053, 0.526315789, 0.789473684, 0.315789474, 0.315789474, 0.368421053,0.526315789,
          0.315789474, 0.263157895, 0.842105263, 0.684210526, 0.684210526, 0.421052632, 0.789473684, 0.578947368,0.421052632,
          0.526315789, 0.684210526, 0.578947368, 0.473684211, 0.684210526, 0.368421053, 0.473684211, 0.684210526,0.631578947,
          0.578947368, 0.368421053, 0.631578947, 0.578947368, 0, 0.631578947, 0, 0.947368421, 0.631578947, 0.421052632,0.263157895,
          0.789473684, 0.421052632, 0.526315789, 0.473684211, 0.473684211, 0.631578947, 0.473684211, 0.631578947,0.578947368,
          0.736842105, 0.473684211, 0.947368421, 0.421052632, 0.631578947, 0.473684211, 0.526315789, 0.894736842,0.473684211,
          0.526315789, 0.473684211, 0, 0.473684211, 0.736842105, 0.578947368, 0.736842105, 0.526315789, 0.631578947,0.473684211,
          0.473684211, 0.421052632, 0.578947368, 0.421052632, 0.473684211, 0.631578947, 0.473684211, 0.473684211,0.526315789,
          0.947368421, 0.631578947, 0.736842105, 0.684210526, 0.578947368, 0.789473684, 0.631578947, 0.947368421,0.684210526,
          0.631578947, 0.473684211, 0.421052632, 0.684210526, 0.789473684, 0.526315789, 0.578947368, 0.631578947,0.894736842,
          0.736842105, 0.631578947, 0.947368421, 0.473684211, 0.631578947, 0.526315789, 0.473684211, 0.631578947,0.578947368,
          0.526315789, 0.684210526, 0.578947368, 0.421052632, 0.526315789, 0.578947368, 0.578947368, 0.684210526,0.473684211,
          0.578947368, 0.736842105, 0.789473684, 0.631578947, 0.789473684, 0.526315789, 0.473684211, 0.736842105,0.421052632,
          0.736842105, 0, 0.421052632, 0.473684211, 0.789473684, 0.684210526, 0.421052632, 0.789473684, 0.526315789,0.631578947,
          0.526315789, 0.789473684, 0.421052632, 0.526315789, 0.684210526, 0.789473684, 0.526315789, 0.789473684,0.684210526,
          0.368421053, 0.684210526, 0.368421053, 0.421052632, 0.578947368, 0.473684211, 0.684210526, 0.631578947,0.526315789,
          0.842105263, 0.684210526, 0.631578947, 0.578947368, 0.789473684, 0.578947368, 0.526315789, 0.684210526,0.315789474,
          0.526315789, 0.631578947, 0.368421053, 0.631578947, 0.578947368, 0.263157895, 0.947368421, 0.421052632,0.736842105,
          0.473684211, 0.789473684, 0.526315789, 0.736842105, 0.315789474, 0.578947368, 0.263157895, 0.263157895,0.473684211,
          0.263157895, 0.263157895, 0.473684211, 0.263157895, 0.473684211, 0.842105263, 0.421052632, 0.631578947,0.473684211]
    slope, intercept, r, p, std_err = stats.linregress(xx, y)

    def myfunc(x):
        return slope * x + intercept

    mymodel = list(map(myfunc, xx))

    predict2 = myfunc((float(entry2.get()))/100)

    slope, intercept, r, p, std_err = stats.linregress(x, y)

    mymodel = list(map(myfunc, x))

    predict = myfunc((float(entry.get()))/100)

    print('Grade 2:', predict2)
    print('Grade 1:', predict)

    predicted = math.trunc(((predict+predict2)/2)*100)

    label3.configure(text='Your predicted Grade: \n' + str(predicted)+'%')


    fig_1 = Figure(figsize=(2.5,2.5))
    ax_1 = fig_1.add_subplot()
    ax_1.scatter(x,y)
    ax_1.plot(x, mymodel)

    canvas = FigureCanvasTkAgg(fig_1, master=frame4)
    canvas.draw()
    canvas.get_tk_widget().place(relx=.2, rely= .1)

#Start creating the User interface using custom tkinter

#Frames
frame = CTkFrame(master=app, fg_color="#0fa4af", border_color="#afdde5", border_width=2, width=1000, height=200)
frame.place(relx=0.5, rely=0.15, anchor=CENTER)

frame2 = CTkFrame(master=app, fg_color="#0fa4af", border_color='#afdde5', border_width=2, width=1000, height=200)
frame2.place(relx=0.5, rely=0.45, anchor=CENTER)

frame3 = CTkFrame(master=app, fg_color="#0fa4af", border_color='#afdde5', border_width=2, width=485, height=300)
frame3.place(relx=0.32, rely=0.81, anchor=CENTER)

frame4 = CTkFrame(master=app, fg_color="#0fa4af", border_color='#afdde5', border_width=2, width=485, height=300)
frame4.place(relx=0.68, rely=0.81, anchor=CENTER)

#Entry boxes
entry = CTkEntry(master=frame2, placeholder_text="Type in your first grade", width=250, text_color="#FFCC70")
entry.place(relx=0.35, rely=0.5, anchor=E)
entry2 = CTkEntry(master=frame2, placeholder_text="Type in your Second Grade grade", width=250, text_color="#FFCC70")
entry2.place(relx=0.9, rely=0.5, anchor=E)

#Button to control the entry data
btn = CTkButton(master=frame2, text="Submit", command=predict, fg_color="#964834",border_color='#024950',hover_color='#024950', text_color="#242424")
btn.place(relx=0.5, rely=0.8, anchor='s')



#Label
label = CTkLabel(master=frame, text="The Nostradamus!", font=("Arial", 40,), text_color='#242424')
label.place(relx=0.5, rely=0.15, anchor=CENTER)

label2 = CTkLabel(master=frame, text="The Nostradamus is an accurate grade predictor. \n This grade predicor uses a data base of 1,188 \ngrades collected from a reliabe source developed \nfor machine learning appliations. This can be used by \ninputting your two recent grades which will predict your \nthird grade. It will also display the graph used to predict your grade!", font=("Arial", 15))
label2.place(relx=0.5, rely=0.6, anchor=CENTER)

label3 = CTkLabel(master=frame3, text="Your predicted Grade:", font=("Arial", 20))
label3.place(relx=0.5, rely=0.4, anchor=CENTER)

label4 = CTkLabel(master=frame4, text="Graph", font=("Arial", 20))
label4.place(relx=0.5, rely=0.4, anchor=CENTER)


app.mainloop()

