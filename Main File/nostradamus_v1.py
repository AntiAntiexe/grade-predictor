# imports
import customtkinter
from customtkinter import *
from scipy import stats
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math
from CTkMessagebox import CTkMessagebox

# Defining the app and setting the geometry including appearance colour.
app = CTk()
app.title("The Nostradamus")
app.geometry("2560x1600")
set_appearance_mode("dark")


'''
Function takes two first creates the linear rule relating the two x data sets x and xx with the y data set.
It uses this linear rule to then calculate the y value if the x value is (G1 or G2).
G1 = entry.get()
G2 = entry2.get()

Then it averages the two predicted results and displays it on the UI
Based of the result it will display the GWSC grade value as well.
'''


def predict():
    # Final (Third Grade) data set which is the grade which is being predicted
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
    # First grade data stored as a list
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
    # Second Grade data stored in a list
    xx = [0.315789474, 0.263157895, 0.421052632, 0.736842105, 0.526315789, 0.789473684, 0.631578947, 0.263157895, 0.947368421,
          0.789473684, 0.421052632, 0.631578947, 0.736842105, 0.526315789, 0.842105263, 0.736842105, 0.736842105, 0.526315789,
          0.263157895, 0.526315789, 0.736842105, 0.789473684, 0.789473684, 0.684210526, 0.473684211, 0.473684211, 0.631578947,
          0.842105263, 0.578947368, 0.631578947, 0.578947368, 0.842105263, 0.842105263, 0.526315789, 0.736842105, 0.368421053,
          0.842105263, 0.842105263, 0.631578947, 0.684210526, 0.526315789, 0.631578947, 0.947368421, 0.421052632, 0.526315789,
          0.421052632, 0.631578947, 1, 0.789473684, 0.368421053, 0.684210526, 0.684210526, 0.578947368, 0.526315789, 0.684210526,
          0.473684211, 0.789473684, 0.789473684, 0.526315789, 0.842105263, 0.578947368, 0.421052632, 0.526315789, 0.473684211,
          0.526315789, 0.789473684, 0.684210526, 0.368421053, 0.473684211, 0.842105263, 0.789473684, 0.526315789, 0.315789474,
          0.631578947, 0.631578947, 0.473684211, 0.578947368, 0.578947368, 0.421052632, 0.263157895, 0.631578947, 0.526315789,
          0.315789474, 0.789473684, 0.526315789, 0.473684211, 0.368421053, 0.736842105, 0.526315789, 0.315789474, 0.368421053,
          0.894736842, 0.315789474, 0.526315789, 0.684210526, 0.526315789, 0.789473684, 0.473684211, 0.736842105, 0.473684211,
          0.368421053, 0.894736842, 0.684210526, 0.315789474, 0.947368421, 0.578947368, 0.421052632, 0.947368421, 0.684210526,
          0.789473684, 1, 0.526315789, 0.684210526, 1, 0.473684211, 0.789473684, 0.684210526, 0.736842105, 0.368421053, 0.684210526,
          0.789473684, 0.736842105, 0.684210526, 0.578947368, 0.368421053, 0.684210526, 0.526315789, 0.421052632, 0.210526316,
          0.947368421, 0, 0, 0.684210526, 0.578947368, 0, 0, 0, 0, 0.631578947, 0.842105263, 0.473684211, 0.473684211, 0.578947368,
          0.736842105, 0, 0.578947368, 0.368421053, 0.578947368, 0.315789474, 0.473684211, 0.263157895, 0.684210526, 0.526315789, 0,
          0.578947368, 0.421052632, 0.631578947, 0.421052632, 0.789473684, 0.631578947, 0.315789474, 0.473684211, 0, 0.526315789,
          0.421052632, 0.578947368, 0.526315789, 0.789473684, 0.368421053, 0.736842105, 0.263157895, 0.789473684, 0.578947368, 0.368421053,
          0.578947368, 0.473684211, 0.684210526, 0.263157895, 0.421052632, 0.526315789, 0.421052632, 0.684210526, 0.894736842, 0.473684211,
          0.684210526, 0.631578947, 0.631578947, 0.789473684, 0.368421053, 0.473684211, 0.631578947, 0.421052632, 0.421052632,
          0.473684211, 0.736842105, 0.789473684, 0.789473684, 0.473684211, 0.947368421, 0.473684211, 0.842105263, 0.526315789,
          0.473684211, 0.315789474, 0.526315789, 0.473684211, 0.368421053, 0.631578947, 0.473684211, 0.368421053, 0.421052632,
          0.631578947, 0.684210526, 0.368421053, 0.526315789, 0.789473684, 0.315789474, 0.315789474, 0.368421053, 0.526315789,
          0.315789474, 0.263157895, 0.842105263, 0.684210526, 0.684210526, 0.421052632, 0.789473684, 0.578947368, 0.421052632,
          0.526315789, 0.684210526, 0.578947368, 0.473684211, 0.684210526, 0.368421053, 0.473684211, 0.684210526, 0.631578947,
          0.578947368, 0.368421053, 0.631578947, 0.578947368, 0, 0.631578947, 0, 0.947368421, 0.631578947, 0.421052632, 0.263157895,
          0.789473684, 0.421052632, 0.526315789, 0.473684211, 0.473684211, 0.631578947, 0.473684211, 0.631578947, 0.578947368,
          0.736842105, 0.473684211, 0.947368421, 0.421052632, 0.631578947, 0.473684211, 0.526315789, 0.894736842, 0.473684211,
          0.526315789, 0.473684211, 0, 0.473684211, 0.736842105, 0.578947368, 0.736842105, 0.526315789, 0.631578947, 0.473684211,
          0.473684211, 0.421052632, 0.578947368, 0.421052632, 0.473684211, 0.631578947, 0.473684211, 0.473684211, 0.526315789,
          0.947368421, 0.631578947, 0.736842105, 0.684210526, 0.578947368, 0.789473684, 0.631578947, 0.947368421, 0.684210526,
          0.631578947, 0.473684211, 0.421052632, 0.684210526, 0.789473684, 0.526315789, 0.578947368, 0.631578947, 0.894736842,
          0.736842105, 0.631578947, 0.947368421, 0.473684211, 0.631578947, 0.526315789, 0.473684211, 0.631578947, 0.578947368,
          0.526315789, 0.684210526, 0.578947368, 0.421052632, 0.526315789, 0.578947368, 0.578947368, 0.684210526, 0.473684211,
          0.578947368, 0.736842105, 0.789473684, 0.631578947, 0.789473684, 0.526315789, 0.473684211, 0.736842105, 0.421052632,
          0.736842105, 0, 0.421052632, 0.473684211, 0.789473684, 0.684210526, 0.421052632, 0.789473684, 0.526315789, 0.631578947,
          0.526315789, 0.789473684, 0.421052632, 0.526315789, 0.684210526, 0.789473684, 0.526315789, 0.789473684, 0.684210526,
          0.368421053, 0.684210526, 0.368421053, 0.421052632, 0.578947368, 0.473684211, 0.684210526, 0.631578947, 0.526315789,
          0.842105263, 0.684210526, 0.631578947, 0.578947368, 0.789473684, 0.578947368, 0.526315789, 0.684210526, 0.315789474,
          0.526315789, 0.631578947, 0.368421053, 0.631578947, 0.578947368, 0.263157895, 0.947368421, 0.421052632, 0.736842105,
          0.473684211, 0.789473684, 0.526315789, 0.736842105, 0.315789474, 0.578947368, 0.263157895, 0.263157895, 0.473684211,
          0.263157895, 0.263157895, 0.473684211, 0.263157895, 0.473684211, 0.842105263, 0.421052632, 0.631578947, 0.473684211]

    if entry.get().isnumeric() != True or entry2.get().isnumeric() != True:
        CTkMessagebox(title="That's an Error!", message="Please enter only a number")
    elif int(entry.get()) > 100 or int(entry2.get()) > 100:
        CTkMessagebox(title="That's an Error!", message="Please enter only a number between 0 and 100.")
    elif int(entry.get()) < 0 or int(entry2.get()) < 0:
        CTkMessagebox(title="That's an Error!", message="Please enter only a number between 0 and 100.")
    else:
        slope2, intercept2, r2, p2, std_err2 = stats.linregress(xx, y)
        slope, intercept, r, p, std_err = stats.linregress(x, y)
        # Create a linear equation in the form of y=mx+c from the first x data set

        def linear_rule1(x):
            return slope * x + intercept

        # Create a linear equation in the form of y=mx+c from the second xx data set
        def linear_rule2(x):
            return slope2 * x + intercept2

        predict2 = linear_rule2((float(entry2.get())) / 100)
        predict = linear_rule1((float(entry.get())) / 100)

        print('Grade 2:', predict2)
        print('Grade 1:', predict)

        y_value = (predict+predict2)/2

        predicted = math.trunc(y_value * 100)
        '''
                Define the different errors that could occur during the program
                    - enters a number less than 0
                    - enters a number greater than 100
        '''
        if predicted >= 91:
            print('You received', str(predicted) + '%' + ',', 'which is an Outstanding')
            color = '#00ff00'
            result = 'Oustanding'
        elif predicted < 91 and predicted >= 82:
            print('You received', str(predicted) + '%' + ',', ' which is an Excellent')
            color = '#00ffff'
            result = 'Excellent'
        elif predicted < 82 and predicted >= 73:
            print('You received', str(predicted) + '%' + ',', ' which is a Very Good')
            color = '#c27ba0'
            result = 'Very Good'
        elif predicted < 73 and predicted >= 64:
            print('You received', str(predicted) + '%' + ',', ' which is a Good')
            color = '#8e7cc3'
            result = 'Good'
        elif predicted < 64 and predicted >= 55:
            print('You received', str(predicted) + '%' + ',', ' which is a Competent')
            color = '#ffffff'
            result = 'Competent'
        elif predicted < 55 and predicted >= 46:
            print('You received', str(predicted) + '%' + ',', ' which is a Satisfactory')
            color = '#ffff00'
            result = 'Satisfactory'
        elif predicted < 46 and predicted >= 35:
            print('You received', str(predicted) + '%' + ',', ' which is a Below Standard')
            color = '#ff9900'
            result = 'Below Standard'
        else:
            print('You received', str(predicted) + '%' + ',', ' which is a Not Demonstrated')
            color = '#ff0000'
            result = 'Not Demonstrated'

        # Configure the labels to display the final grade
        label3.configure(text=str(predicted) + '%', text_color=color)
        label4.configure(text=result, text_color=color)

        '''
        Create a linear rule in the form of x = (y-c)/m 
        as well as averaging the intercepts and slopes for both of the data sets
        '''
        def linear_rule_fory(y):
            return (y-intercept-((intercept+intercept2)/2))/((slope+slope2)/2)

        x_value = linear_rule_fory(y_value)

        mymodel = list(map(linear_rule1, x))

        # Prepare the graph by scattering the data and plotting the line.
        fig_1 = Figure(figsize=(6.2, 3.4))
        ax_1 = fig_1.add_subplot()
        ax_1.scatter(x, y)
        ax_1.plot(x, mymodel, color='green')
        ax_1.plot(x_value, y_value, marker='D', color='red')

        # Display the graph on the app.
        canvas = FigureCanvasTkAgg(fig_1, master=frame)
        canvas.draw()
        canvas.get_tk_widget().place(relx=.5, rely=.43)


# Create the User interface using custom tkinter

# Frames
frame = CTkFrame(master=app, fg_color='#323231', border_color='#323231', border_width=2, width=2560, height=1600,)
frame.place(relx=.5, rely=.5, anchor=CENTER)

frame2 = CTkFrame(master=app, fg_color='#323231', bg_color='#323231', border_color='#323231', border_width=2, width=260, height=181,)
frame2.place = frame2.place(relx=.32, rely=.75, anchor=CENTER)

# fonts
my_font = customtkinter.CTkFont(family="sans serif", size=75, weight="bold", )

my_font2 = customtkinter.CTkFont(family="sans serif", size=25, weight="normal",)

# Entry boxes
entry = CTkEntry(master=frame, placeholder_text="Input first grade", width=185, fg_color='#0fa4af', border_color='#0d737a', text_color="black", placeholder_text_color='#323231', font=(my_font2, 20))
entry.place(relx=0.328, rely=0.6, anchor=E)
entry2 = CTkEntry(master=frame, placeholder_text="Input second grade", width=185, fg_color='#0fa4af', border_color='#0d737a', text_color="black", placeholder_text_color='#323231', font=(my_font2, 20))
entry2.place(relx=0.328, rely=0.63, anchor=E)


# Button to control the entry data
btn = CTkButton(master=frame, text="Submit", command=predict, fg_color="#0fa4af", border_color='#0d737a', border_width=2, hover_color='#024950', text_color="#323231", height=40, font=(my_font2, 25))
btn.place(relx=0.284, rely=0.7, anchor='s')

# Labels
label = CTkLabel(master=frame, text="The", font=my_font)
label.place(relx=0.28, rely=0.3, anchor=CENTER)

label1 = CTkLabel(master=frame, text="Nostradamus.", font=my_font, text_color='#0fa4af')
label1.place(relx=0.35, rely=0.35, anchor=CENTER)


label2 = CTkLabel(master=frame, text="The Nostradamus is an accurate grade predictor. This grade predictor uses a data base of 1,188 grades collected from a reliable source developed for machine learning applications. This can be used by inputting your two recent grades which will predict your third grade. It will also display the graph used to predict your grade with your grade highlighted!", wraplength=550, justify='left', font=my_font2, width=20, height=25)
label2.place(relx=0.36, rely=0.49, anchor=CENTER)

label3 = CTkLabel(master=frame2, text="0%", font=my_font, text_color='#0fa4af')
label3.place(relx=0.6, rely=0.3, anchor=CENTER)

label4 = CTkLabel(master=frame2, text="Your Result", font=my_font2)
label4.place(relx=0.6, rely=0.6, anchor=CENTER)

# All code must be written before the mainloop.
app.mainloop()



