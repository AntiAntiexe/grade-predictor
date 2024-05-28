# imports
from CTkMessagebox import *
from scipy import stats
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.lines import Line2D
import math


class LinearRegr:

    '''
        Once LinearRegr is called in nostradamus_v2. __init__ defines all the variables needed for the processes:
        - the values from the entry boxes
        - the labels which have to change to display the grade
        - the frame which the labels have to configure on to display the grade
        - and finally the app class, so it can use the variables from nostradamus_v2.App class
    '''

    def __init__(self, app, val1, val2, frame_toconfig, label_toconfig1, label_toconfig2):
        self.app = app
        self.val1 = val1
        self.val2 = val2
        self.frame_toconfig = frame_toconfig
        self.label_toconfig1 = label_toconfig1
        self.label_toconfig2 = label_toconfig2

        self.y = [0.3, 0.3, 0.5, 0.75, 0.5, 0.75, 0.55, 0.3, 0.95, 0.75, 0.45, 0.6, 0.7, 0.55, 0.8, 0.7, 0.7, 0.5, 0.25,
                  0.5,
                  0.75, 0.75, 0.8, 0.6, 0.4, 0.4, 0.55, 0.75, 0.55, 0.55, 0.6, 0.85, 0.8, 0.6, 0.75, 0.3, 0.9, 0.75,
                  0.55,
                  0.65,
                  0.55, 0.6, 0.9, 0.55, 0.45, 0.3, 0.55, 1, 0.7, 0.35, 0.65, 0.65, 0.5, 0.55, 0.65, 0.5, 0.75, 0.75,
                  0.45,
                  0.8,
                  0.55, 0.55, 0.45, 0.45, 0.5, 0.75, 0.6, 0.3, 0.4, 0.8, 0.75, 0.5, 0.25, 0.7, 0.55, 0.5, 0.5, 0.55,
                  0.5,
                  0.25,
                  0.6, 0.55, 0.3, 0.75, 0.5, 0.4, 0.3, 0.7, 0.5, 0.35, 0.4, 0.9, 0.3, 0.5, 0.7, 0.5, 0.75, 0.5, 0.7,
                  0.4,
                  0.25,
                  0.85, 0.7, 0.3, 0.9, 0.55, 0.4, 0.9, 0.65, 0.8, 0.95, 0.5, 0.65, 0.95, 0.45, 0.8, 0.7, 0.65, 0.4,
                  0.65,
                  0.75,
                  0.75, 0.65, 0.65, 0.4, 0.6, 0.55, 0.45, 0, 0.9, 0, 0, 0.6, 0.55, 0, 0, 0, 0, 0.6, 0.75, 0, 0.45, 0.55,
                  0.65, 0,
                  0.55, 0, 0.55, 0, 0.5, 0, 0.7, 0.5, 0, 0.6, 0.4, 0.65, 0.5, 0.75, 0.6, 0, 0.35, 0, 0.5, 0.35, 0.6,
                  0.5,
                  0.8, 0,
                  0.7, 0, 0.8, 0.5, 0, 0.45, 0.45, 0.55, 0.3, 0.45, 0.55, 0.4, 0.6, 0.85, 0.4, 0.6, 0.55, 0.55, 0.75,
                  0.45,
                  0.5,
                  0.65, 0.45, 0.4, 0.5, 0.7, 0.75, 0.8, 0.5, 0.9, 0.5, 0.8, 0.5, 0.5, 0.3, 0.55, 0.45, 0.35, 0.65, 0.5,
                  0.35,
                  0.4, 0.65, 0.7, 0.4, 0.5, 0.75, 0.2, 0.4, 0.4, 0.5, 0.3, 0, 0.85, 0.65, 0.7, 0.35, 0.75, 0.6, 0.45,
                  0.6,
                  0.7,
                  0.55, 0.45, 0.65, 0.3, 0.5, 0.65, 0.6, 0.55, 0, 0.6, 0.6, 0, 0.6, 0, 0.9, 0.65, 0.4, 0.25, 0.75, 0.4,
                  0.5,
                  0.4,
                  0.4, 0.6, 0.4, 0.65, 0.55, 0.7, 0, 0.9, 0.4, 0.6, 0.45, 0, 0.85, 0.5, 0.55, 0.5, 0, 0.45, 0.7, 0.55,
                  0.7,
                  0.5,
                  0.6, 0.45, 0.45, 0.4, 0.5, 0.4, 0.5, 0.6, 0.5, 0.55, 0.55, 0.95, 0.6, 0.7, 0.75, 0.55, 0.75, 0.65,
                  0.9,
                  0.7,
                  0.55, 0, 0.4, 0.7, 0.8, 0.55, 0.5, 0.7, 0.9, 0.65, 0.6, 0.9, 0.4, 0.6, 0.5, 0, 0.65, 0.55, 0.55, 0.65,
                  0.55, 0,
                  0.45, 0.5, 0.55, 0.65, 0.45, 0.55, 0.75, 0.75, 0.55, 0.8, 0.5, 0.45, 0.7, 0.4, 0.7, 0, 0, 0, 0.75,
                  0.65, 0,
                  0.85, 0.5, 0.55, 0, 0.75, 0, 0.5, 0.7, 0.8, 0.45, 0.75, 0.65, 0.4, 0.65, 0.4, 0.4, 0.55, 0.45, 0.65,
                  0.55,
                  0.5,
                  0.8, 0.65, 0.6, 0.5, 0.75, 0.6, 0.5, 0.65, 0, 0.5, 0.55, 0.45, 0.6, 0.55, 0.25, 0.95, 0.5, 0.75, 0.5,
                  0.75,
                  0.5, 0.7, 0.35, 0.5, 0, 0.25, 0.5, 0.3, 0, 0.4, 0, 0.45, 0.8, 0.35, 0.5, 0.45]
        # First grade data stored as a list
        self.x = [0.125, 0.125, 0.25, 0.75, 0.1875, 0.75, 0.5625, 0.1875, 0.8125, 0.6875, 0.4375, 0.4375, 0.6875,
                  0.4375,
                  0.6875,
                  0.6875, 0.625, 0.3125, 0.1875, 0.3125, 0.625, 0.5625, 0.75, 0.625, 0.4375, 0.1875, 0.5625, 0.75, 0.5,
                  0.4375,
                  0.375, 0.875, 0.875, 0.3125, 0.5625, 0.3125, 0.75, 0.75, 0.5625, 0.6875, 0.25, 0.5625, 1, 0.3125,
                  0.4375,
                  0.3125, 0.5, 1, 0.75, 0.25, 0.5625, 0.5, 0.5, 0.3125, 0.4375, 0.3125, 0.6875, 0.6875, 0.375, 0.75,
                  0.4375,
                  0.4375, 0.3125, 0.4375, 0.4375, 0.8125, 0.625, 0.25, 0.3125, 0.8125, 0.625, 0.4375, 0.3125, 0.5625,
                  0.5,
                  0.375,
                  0.5, 0.5, 0.3125, 0.125, 0.4375, 0.5, 0.25, 0.75, 0.375, 0.25, 0.3125, 0.625, 0.5, 0.3125, 0.25,
                  0.8125,
                  0.25,
                  0.5, 0.5, 0.25, 0.5, 0.3125, 0.5, 0.25, 0.25, 0.8125, 0.4375, 0.25, 0.8125, 0.4375, 0.25, 0.8125,
                  0.4375,
                  0.6875, 0.9375, 0.25, 0.4375, 0.9375, 0.375, 0.75, 0.5, 0.625, 0.375, 0.6875, 0.8125, 0.8125, 0.625,
                  0.6875,
                  0.3125, 0.625, 0.25, 0.25, 0.25, 0.9375, 0.5625, 0.3125, 0.4375, 0.5625, 0.375, 0.5, 0.4375, 0.0625,
                  0.6875,
                  0.8125, 0.25, 0.375, 0.375, 0.6875, 0.125, 0.3125, 0.1875, 0.4375, 0.25, 0.3125, 0.1875, 0.5625,
                  0.4375,
                  0.125,
                  0.5, 0.5, 0.8125, 0.375, 0.875, 0.4375, 0.25, 0.125, 0.25, 0.4375, 0.125, 0.5625, 0.4375, 0.6875,
                  0.1875,
                  0.6875, 0.1875, 0.625, 0.625, 0.3125, 0.4375, 0.4375, 0.625, 0.1875, 0.4375, 0.4375, 0.375, 0.5625,
                  0.8125,
                  0.375, 0.5625, 0.5625, 0.5, 0.75, 0.3125, 0.3125, 0.5, 0.3125, 0.25, 0.3125, 0.625, 0.6875, 0.875,
                  0.375,
                  0.9375, 0.375, 0.8125, 0.3125, 0.375, 0.25, 0.4375, 0.4375, 0.25, 0.5, 0.375, 0.25, 0.3125, 0.5625,
                  0.5625,
                  0.1875, 0.3125, 0.6875, 0.1875, 0.1875, 0.25, 0.375, 0.1875, 0.1875, 0.8125, 0.5625, 0.625, 0.375,
                  0.8125,
                  0.5625, 0.4375, 0.5625, 0.625, 0.5, 0.5, 0.6875, 0.375, 0.5, 0.6875, 0.625, 0.625, 0.25, 0.5625,
                  0.4375,
                  0.1875, 0.625, 0.25, 0.9375, 0.5625, 0.1875, 0, 0.625, 0.1875, 0.25, 0.1875, 0.3125, 0.3125, 0.25,
                  0.6875,
                  0.5,
                  0.75, 0.4375, 0.875, 0.3125, 0.625, 0.4375, 0.375, 0.875, 0.375, 0.5625, 0.4375, 0.1875, 0.375, 0.75,
                  0.5,
                  0.75, 0.4375, 0.5625, 0.4375, 0.375, 0.375, 0.4375, 0.3125, 0.5, 0.5625, 0.3125, 0.4375, 0.5625,
                  0.9375,
                  0.625,
                  0.75, 0.75, 0.5625, 0.75, 0.5625, 0.9375, 0.6875, 0.6875, 0.4375, 0.4375, 0.6875, 0.8125, 0.5625, 0.5,
                  0.75,
                  0.875, 0.75, 0.6875, 0.875, 0.3125, 0.75, 0.5625, 0.375, 0.6875, 0.625, 0.625, 0.75, 0.625, 0.3125,
                  0.375,
                  0.5,
                  0.5, 0.625, 0.5, 0.5, 0.5625, 0.8125, 0.375, 0.6875, 0.5, 0.4375, 0.6875, 0.375, 0.5625, 0.25, 0.3125,
                  0.4375,
                  0.8125, 0.6875, 0.25, 0.8125, 0.375, 0.5, 0.4375, 0.8125, 0.375, 0.5, 0.625, 0.8125, 0.4375, 0.625,
                  0.5,
                  0.3125, 0.625, 0.3125, 0.3125, 0.625, 0.4375, 0.5625, 0.5625, 0.4375, 0.9375, 0.625, 0.625, 0.5,
                  0.8125,
                  0.5625, 0.4375, 0.625, 0.25, 0.5, 0.6875, 0.25, 0.6875, 0.625, 0.1875, 1, 0.3125, 0.75, 0.3125, 0.75,
                  0.4375,
                  0.75, 0.25, 0.5, 0.1875, 0.1875, 0.4375, 0.1875, 0.25, 0.25, 0.1875, 0.375, 0.6875, 0.4375, 0.5,
                  0.3125]
        # Second Grade data stored in a list
        self.xx = [0.315789474, 0.263157895, 0.421052632, 0.736842105, 0.526315789, 0.789473684, 0.631578947,
                   0.263157895,
                   0.947368421,
                   0.789473684, 0.421052632, 0.631578947, 0.736842105, 0.526315789, 0.842105263, 0.736842105,
                   0.736842105,
                   0.526315789,
                   0.263157895, 0.526315789, 0.736842105, 0.789473684, 0.789473684, 0.684210526, 0.473684211,
                   0.473684211,
                   0.631578947,
                   0.842105263, 0.578947368, 0.631578947, 0.578947368, 0.842105263, 0.842105263, 0.526315789,
                   0.736842105,
                   0.368421053,
                   0.842105263, 0.842105263, 0.631578947, 0.684210526, 0.526315789, 0.631578947, 0.947368421,
                   0.421052632,
                   0.526315789,
                   0.421052632, 0.631578947, 1, 0.789473684, 0.368421053, 0.684210526, 0.684210526, 0.578947368,
                   0.526315789,
                   0.684210526,
                   0.473684211, 0.789473684, 0.789473684, 0.526315789, 0.842105263, 0.578947368, 0.421052632,
                   0.526315789,
                   0.473684211,
                   0.526315789, 0.789473684, 0.684210526, 0.368421053, 0.473684211, 0.842105263, 0.789473684,
                   0.526315789,
                   0.315789474,
                   0.631578947, 0.631578947, 0.473684211, 0.578947368, 0.578947368, 0.421052632, 0.263157895,
                   0.631578947,
                   0.526315789,
                   0.315789474, 0.789473684, 0.526315789, 0.473684211, 0.368421053, 0.736842105, 0.526315789,
                   0.315789474,
                   0.368421053,
                   0.894736842, 0.315789474, 0.526315789, 0.684210526, 0.526315789, 0.789473684, 0.473684211,
                   0.736842105,
                   0.473684211,
                   0.368421053, 0.894736842, 0.684210526, 0.315789474, 0.947368421, 0.578947368, 0.421052632,
                   0.947368421,
                   0.684210526,
                   0.789473684, 1, 0.526315789, 0.684210526, 1, 0.473684211, 0.789473684, 0.684210526, 0.736842105,
                   0.368421053, 0.684210526,
                   0.789473684, 0.736842105, 0.684210526, 0.578947368, 0.368421053, 0.684210526, 0.526315789,
                   0.421052632,
                   0.210526316,
                   0.947368421, 0, 0, 0.684210526, 0.578947368, 0, 0, 0, 0, 0.631578947, 0.842105263, 0.473684211,
                   0.473684211, 0.578947368,
                   0.736842105, 0, 0.578947368, 0.368421053, 0.578947368, 0.315789474, 0.473684211, 0.263157895,
                   0.684210526,
                   0.526315789, 0,
                   0.578947368, 0.421052632, 0.631578947, 0.421052632, 0.789473684, 0.631578947, 0.315789474,
                   0.473684211, 0,
                   0.526315789,
                   0.421052632, 0.578947368, 0.526315789, 0.789473684, 0.368421053, 0.736842105, 0.263157895,
                   0.789473684,
                   0.578947368, 0.368421053,
                   0.578947368, 0.473684211, 0.684210526, 0.263157895, 0.421052632, 0.526315789, 0.421052632,
                   0.684210526,
                   0.894736842, 0.473684211,
                   0.684210526, 0.631578947, 0.631578947, 0.789473684, 0.368421053, 0.473684211, 0.631578947,
                   0.421052632,
                   0.421052632,
                   0.473684211, 0.736842105, 0.789473684, 0.789473684, 0.473684211, 0.947368421, 0.473684211,
                   0.842105263,
                   0.526315789,
                   0.473684211, 0.315789474, 0.526315789, 0.473684211, 0.368421053, 0.631578947, 0.473684211,
                   0.368421053,
                   0.421052632,
                   0.631578947, 0.684210526, 0.368421053, 0.526315789, 0.789473684, 0.315789474, 0.315789474,
                   0.368421053,
                   0.526315789,
                   0.315789474, 0.263157895, 0.842105263, 0.684210526, 0.684210526, 0.421052632, 0.789473684,
                   0.578947368,
                   0.421052632,
                   0.526315789, 0.684210526, 0.578947368, 0.473684211, 0.684210526, 0.368421053, 0.473684211,
                   0.684210526,
                   0.631578947,
                   0.578947368, 0.368421053, 0.631578947, 0.578947368, 0, 0.631578947, 0, 0.947368421, 0.631578947,
                   0.421052632, 0.263157895,
                   0.789473684, 0.421052632, 0.526315789, 0.473684211, 0.473684211, 0.631578947, 0.473684211,
                   0.631578947,
                   0.578947368,
                   0.736842105, 0.473684211, 0.947368421, 0.421052632, 0.631578947, 0.473684211, 0.526315789,
                   0.894736842,
                   0.473684211,
                   0.526315789, 0.473684211, 0, 0.473684211, 0.736842105, 0.578947368, 0.736842105, 0.526315789,
                   0.631578947,
                   0.473684211,
                   0.473684211, 0.421052632, 0.578947368, 0.421052632, 0.473684211, 0.631578947, 0.473684211,
                   0.473684211,
                   0.526315789,
                   0.947368421, 0.631578947, 0.736842105, 0.684210526, 0.578947368, 0.789473684, 0.631578947,
                   0.947368421,
                   0.684210526,
                   0.631578947, 0.473684211, 0.421052632, 0.684210526, 0.789473684, 0.526315789, 0.578947368,
                   0.631578947,
                   0.894736842,
                   0.736842105, 0.631578947, 0.947368421, 0.473684211, 0.631578947, 0.526315789, 0.473684211,
                   0.631578947,
                   0.578947368,
                   0.526315789, 0.684210526, 0.578947368, 0.421052632, 0.526315789, 0.578947368, 0.578947368,
                   0.684210526,
                   0.473684211,
                   0.578947368, 0.736842105, 0.789473684, 0.631578947, 0.789473684, 0.526315789, 0.473684211,
                   0.736842105,
                   0.421052632,
                   0.736842105, 0, 0.421052632, 0.473684211, 0.789473684, 0.684210526, 0.421052632, 0.789473684,
                   0.526315789,
                   0.631578947,
                   0.526315789, 0.789473684, 0.421052632, 0.526315789, 0.684210526, 0.789473684, 0.526315789,
                   0.789473684,
                   0.684210526,
                   0.368421053, 0.684210526, 0.368421053, 0.421052632, 0.578947368, 0.473684211, 0.684210526,
                   0.631578947,
                   0.526315789,
                   0.842105263, 0.684210526, 0.631578947, 0.578947368, 0.789473684, 0.578947368, 0.526315789,
                   0.684210526,
                   0.315789474,
                   0.526315789, 0.631578947, 0.368421053, 0.631578947, 0.578947368, 0.263157895, 0.947368421,
                   0.421052632,
                   0.736842105,
                   0.473684211, 0.789473684, 0.526315789, 0.736842105, 0.315789474, 0.578947368, 0.263157895,
                   0.263157895,
                   0.473684211,
                   0.263157895, 0.263157895, 0.473684211, 0.263157895, 0.473684211, 0.842105263, 0.421052632,
                   0.631578947,
                   0.473684211]

    '''
    Function takes two values, first creates the linear rule relating the two x data sets x and xx with the y data set.
    It uses this linear rule to then calculate the y value if the x value is (G1 or G2).
    G1 = entry.get()
    G2 = entry2.get()

    Then it averages the two predicted results and displays it on the UI
    Based of the result it will display the GWSC grade value as well.
    '''

    def predict(self):
        '''
                Define the different errors that could occur during the program
                        - user enters a number less than 0
                        - user enters a number greater than 100
                        - user enters a string which contains letters or other symbols
        '''
        if self.val1.get().isnumeric() != True or self.val2.get().isnumeric() != True:
            CTkMessagebox(title="That's an Error!", message="Please enter only a number")
        elif int(self.val1.get()) > 100 or int(self.val2.get()) > 100:
            CTkMessagebox(title="That's an Error!", message="Please enter only a number between 0 and 100.")
        elif int(self.val1.get()) < 0 or int(self.val2.get()) < 0:
            CTkMessagebox(title="That's an Error!", message="Please enter only a number between 0 and 100.")
        else:
            slope2, intercept2, r2, p2, std_err2 = stats.linregress(self.xx, self.y)
            slope, intercept, r, p, std_err = stats.linregress(self.x, self.y)
            # Create a linear equation in the form of y=mx+c from the first x data set

            def linear_rule1(x):
                return slope * x + intercept

            # Create a linear equation in the form of y=mx+c from the second xx data set
            def linear_rule2(x):
                return slope2 * x + intercept2

            self.predict2 = linear_rule2((float(self.val2.get())) / 100)
            self.predict = linear_rule1((float(self.val1.get())) / 100)

            print('Grade 2:', self.predict2)
            print('Grade 1:', self.predict)

            self.y_value = (self.predict + self.predict2)/2

            self.predicted = math.trunc(self.y_value * 100)

            if self.predicted >= 91:
                print('You received', str(self.predicted) + '%' + ',', 'which is an Outstanding')
                color = '#00ff00'
                result = 'Outstanding'
            elif self.predicted < 91 and self.predicted >= 82:
                print('You received', str(self.predicted) + '%' + ',', ' which is an Excellent')
                color = '#00ffff'
                result = 'Excellent'
            elif self.predicted < 82 and self.predicted >= 73:
                print('You received', str(self.predicted) + '%' + ',', ' which is a Very Good')
                color = '#c27ba0'
                result = 'Very Good'
            elif self.predicted < 73 and self.predicted >= 64:
                print('You received', str(self.predicted) + '%' + ',', ' which is a Good')
                color = '#8e7cc3'
                result = 'Good'
            elif self.predicted < 64 and self.predicted >= 55:
                print('You received', str(self.predicted) + '%' + ',', ' which is a Competent')
                color = '#ff9900'
                result = 'Competent'
            elif self.predicted < 55 and self.predicted >= 46:
                print('You received', str(self.predicted) + '%' + ',', ' which is a Satisfactory')
                color = '#ffff00'
                result = 'Satisfactory'
            elif self.predicted < 46 and self.predicted >= 35:
                print('You received', str(self.predicted) + '%' + ',', ' which is a Below Standard')
                color = '#ff9900'
                result = 'Below Standard'
            else:
                print('You received', str(self.predicted) + '%' + ',', ' which is a Not Demonstrated')
                color = '#ff0000'
                result = 'Not Demonstrated'

            # Configure the labels to display the final grade
            self.label_toconfig1.configure(text=str(self.predicted) + '%', text_color=color)
            self.label_toconfig2.configure(text=result, text_color=color)

            '''
            Create a linear rule in the form of x = (y-c)/m 
            as well as averaging the intercepts and slopes for both of the data sets
            '''
            def linear_rule_fory(y):
                return (y-intercept-((intercept+intercept2)/2))/((slope+slope2)/2)

            self.x_value = linear_rule_fory(self.y_value)

            self.mymodel = list(map(linear_rule1, self.x))

            # Prepare the graph by scattering the data and plotting the line.

            fig_1 = Figure(figsize=(6.2, 3.9))
            ax_1 = fig_1.add_subplot()
            ax_1.scatter(self.x, self.y, color='#0fa4af')
            ax_1.plot(self.x, self.mymodel, color='green')
            ax_1.plot(self.x_value, self.y_value, marker='D', color=color, markersize=8)
            ax_1.set_xlabel('Given Grades (as percentiles)', font='sans serif')
            ax_1.set_ylabel('Predicted Grades (as percentiles)', font='sans serif')
            ax_1.set_title('Graph comparing the predicted grades to the given grades')
            legend_elements = [Line2D([0], [0], color='g', lw=4, label='Line'),
                               Line2D([0], [0], marker='o', color='w', label='Scatter',
                                      markerfacecolor='#0fa4af', markersize=12),
                               Line2D([0], [0], marker='D', color='w', label='Your Grade',
                                      markerfacecolor=color, markersize=12)
                               ]

            # Display the graph on the app.
            ax_1.legend(handles=legend_elements, loc='lower right')
            canvas = FigureCanvasTkAgg(fig_1, master=self.frame_toconfig)
            canvas.draw()
            canvas.get_tk_widget().place(relx=.5, rely=.420)
