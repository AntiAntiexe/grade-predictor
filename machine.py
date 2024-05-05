from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




y = [0.3,0.3,0.5,0.75,0.5,0.75,0.55,0.3,0.95,0.75,0.45,0.6,0.7,0.55,0.8,0.7,0.7,0.5,0.25,0.5,0.75,0.75,0.8,0.6,0.4,0.4,0.55,0.75,0.55,0.55,0.6,0.85,0.8,0.6,0.75,0.3,0.9,0.75,0.55,0.65,0.55,0.6,0.9,0.55,0.45,0.3,0.55,1,0.7,0.35,0.65,0.65,0.5,0.55,0.65,0.5,0.75,0.75,0.45,0.8,0.55,0.55,0.45,0.45,0.5,0.75,0.6,0.3,0.4,0.8,0.75,0.5,0.25,0.7,0.55,0.5,0.5,0.55,0.5,0.25,0.6,0.55,0.3,0.75,0.5,0.4,0.3,0.7,0.5,0.35,0.4,0.9,0.3,0.5,0.7,0.5,0.75,0.5,0.7,0.4,0.25,0.85,0.7,0.3,0.9,0.55,0.4,0.9,0.65,0.8,0.95,0.5,0.65,0.95,0.45,0.8,0.7,0.65,0.4,0.65,0.75,0.75,0.65,0.65,0.4,0.6,0.55,0.45,0,0.9,0,0,0.6,0.55,0,0,0,0,0.6,0.75,0,0.45,0.55,0.65,0,0.55,0,0.55,0,0.5,0,0.7,0.5,0,0.6,0.4,0.65,0.5,0.75,0.6,0,0.35,0,0.5,0.35,0.6,0.5,0.8,0,0.7,0,0.8,0.5,0,0.45,0.45,0.55,0.3,0.45,0.55,0.4,0.6,0.85,0.4,0.6,0.55,0.55,0.75,0.45,0.5,0.65,0.45,0.4,0.5,0.7,0.75,0.8,0.5,0.9,0.5,0.8,0.5,0.5,0.3,0.55,0.45,0.35,0.65,0.5,0.35,0.4,0.65,0.7,0.4,0.5,0.75,0.2,0.4,0.4,0.5,0.3,0,0.85,0.65,0.7,0.35,0.75,0.6,0.45,0.6,0.7,0.55,0.45,0.65,0.3,0.5,0.65,0.6,0.55,0,0.6,0.6,0,0.6,0,0.9,0.65,0.4,0.25,0.75,0.4,0.5,0.4,0.4,0.6,0.4,0.65,0.55,0.7,0,0.9,0.4,0.6,0.45,0,0.85,0.5,0.55,0.5,0,0.45,0.7,0.55,0.7,0.5,0.6,0.45,0.45,0.4,0.5,0.4,0.5,0.6,0.5,0.55,0.55,0.95,0.6,0.7,0.75,0.55,0.75,0.65,0.9,0.7,0.55,0,0.4,0.7,0.8,0.55,0.5,0.7,0.9,0.65,0.6,0.9,0.4,0.6,0.5,0,0.65,0.55,0.55,0.65,0.55,0,0.45,0.5,0.55,0.65,0.45,0.55,0.75,0.75,0.55,0.8,0.5,0.45,0.7,0.4,0.7,0,0,0,0.75,0.65,0,0.85,0.5,0.55,0,0.75,0,0.5,0.7,0.8,0.45,0.75,0.65,0.4,0.65,0.4,0.4,0.55,0.45,0.65,0.55,0.5,0.8,0.65,0.6,0.5,0.75,0.6,0.5,0.65,0,0.5,0.55,0.45,0.6,0.55,0.25,0.95,0.5,0.75,0.5,0.75,0.5,0.7,0.35,0.5,0,0.25,0.5,0.3,0,0.4,0,0.45,0.8,0.35,0.5,0.45]

x = [0.315789474,0.263157895,0.421052632,0.736842105,0.526315789,0.789473684,0.631578947,0.263157895,0.947368421,
         0.789473684,0.421052632,0.631578947,0.736842105,0.526315789,0.842105263,0.736842105,0.736842105,0.526315789,
         0.263157895,0.526315789,0.736842105,0.789473684,0.789473684,0.684210526,0.473684211,0.473684211,0.631578947,
         0.842105263,0.578947368,0.631578947,0.578947368,0.842105263,0.842105263,0.526315789,0.736842105,0.368421053,
         0.842105263,0.842105263,0.631578947,0.684210526,0.526315789,0.631578947,0.947368421,0.421052632,0.526315789,
         0.421052632,0.631578947,1,0.789473684,0.368421053,0.684210526,0.684210526,0.578947368,0.526315789,0.684210526,
         0.473684211,0.789473684,0.789473684,0.526315789,0.842105263,0.578947368,0.421052632,0.526315789,0.473684211,
         0.526315789,0.789473684,0.684210526,0.368421053,0.473684211,0.842105263,0.789473684,0.526315789,0.315789474,
         0.631578947,0.631578947,0.473684211,0.578947368,0.578947368,0.421052632,0.263157895,0.631578947,0.526315789,
         0.315789474,0.789473684,0.526315789,0.473684211,0.368421053,0.736842105,0.526315789,0.315789474,0.368421053,
         0.894736842,0.315789474,0.526315789,0.684210526,0.526315789,0.789473684,0.473684211,0.736842105,0.473684211,
         0.368421053,0.894736842,0.684210526,0.315789474,0.947368421,0.578947368,0.421052632,0.947368421,0.684210526,
         0.789473684,1,0.526315789,0.684210526,1,0.473684211,0.789473684,0.684210526,0.736842105,0.368421053,0.684210526,
         0.789473684,0.736842105,0.684210526,0.578947368,0.368421053,0.684210526,0.526315789,0.421052632,0.210526316,
         0.947368421,0,0,0.684210526,0.578947368,0,0,0,0,0.631578947,0.842105263,0.473684211,0.473684211,0.578947368,
         0.736842105,0,0.578947368,0.368421053,0.578947368,0.315789474,0.473684211,0.263157895,0.684210526,0.526315789,0,
         0.578947368,0.421052632,0.631578947,0.421052632,0.789473684,0.631578947,0.315789474,0.473684211,0,0.526315789,
         0.421052632,0.578947368,0.526315789,0.789473684,0.368421053,0.736842105,0.263157895,0.789473684,0.578947368,0.368421053,
         0.578947368,0.473684211,0.684210526,0.263157895,0.421052632,0.526315789,0.421052632,0.684210526,0.894736842,0.473684211,
         0.684210526,0.631578947,0.631578947,0.789473684,0.368421053,0.473684211,0.631578947,0.421052632,0.421052632,
         0.473684211,0.736842105,0.789473684,0.789473684,0.473684211,0.947368421,0.473684211,0.842105263,0.526315789,
         0.473684211,0.315789474,0.526315789,0.473684211,0.368421053,0.631578947,0.473684211,0.368421053,0.421052632,
         0.631578947,0.684210526,0.368421053,0.526315789,0.789473684,0.315789474,0.315789474,0.368421053,0.526315789,
         0.315789474,0.263157895,0.842105263,0.684210526,0.684210526,0.421052632,0.789473684,0.578947368,0.421052632,
         0.526315789,0.684210526,0.578947368,0.473684211,0.684210526,0.368421053,0.473684211,0.684210526,0.631578947,
         0.578947368,0.368421053,0.631578947,0.578947368,0,0.631578947,0,0.947368421,0.631578947,0.421052632,0.263157895,
         0.789473684,0.421052632,0.526315789,0.473684211,0.473684211,0.631578947,0.473684211,0.631578947,0.578947368,
         0.736842105,0.473684211,0.947368421,0.421052632,0.631578947,0.473684211,0.526315789,0.894736842,0.473684211,
         0.526315789,0.473684211,0,0.473684211,0.736842105,0.578947368,0.736842105,0.526315789,0.631578947,0.473684211,
         0.473684211,0.421052632,0.578947368,0.421052632,0.473684211,0.631578947,0.473684211,0.473684211,0.526315789,
         0.947368421,0.631578947,0.736842105,0.684210526,0.578947368,0.789473684,0.631578947,0.947368421,0.684210526,
         0.631578947,0.473684211,0.421052632,0.684210526,0.789473684,0.526315789,0.578947368,0.631578947,0.894736842,
         0.736842105,0.631578947,0.947368421,0.473684211,0.631578947,0.526315789,0.473684211,0.631578947,0.578947368,
         0.526315789,0.684210526,0.578947368,0.421052632,0.526315789,0.578947368,0.578947368,0.684210526,0.473684211,
         0.578947368,0.736842105,0.789473684,0.631578947,0.789473684,0.526315789,0.473684211,0.736842105,0.421052632,
         0.736842105,0,0.421052632,0.473684211,0.789473684,0.684210526,0.421052632,0.789473684,0.526315789,0.631578947,
         0.526315789,0.789473684,0.421052632,0.526315789,0.684210526,0.789473684,0.526315789,0.789473684,0.684210526,
         0.368421053,0.684210526,0.368421053,0.421052632,0.578947368,0.473684211,0.684210526,0.631578947,0.526315789,
         0.842105263,0.684210526,0.631578947,0.578947368,0.789473684,0.578947368,0.526315789,0.684210526,0.315789474,
         0.526315789,0.631578947,0.368421053,0.631578947,0.578947368,0.263157895,0.947368421,0.421052632,0.736842105,
         0.473684211,0.789473684,0.526315789,0.736842105,0.315789474,0.578947368,0.263157895,0.263157895,0.473684211,
         0.263157895,0.263157895,0.473684211,0.263157895,0.473684211,0.842105263,0.421052632,0.631578947,0.473684211]
#x = [0.125,0.125,0.25,0.75,0.1875,0.75,0.5625,0.1875,0.8125,0.6875,0.4375,0.4375,0.6875,0.4375,0.6875,0.6875,0.625,0.3125,0.1875,0.3125,0.625,0.5625,0.75,0.625,0.4375,0.1875,0.5625,0.75,0.5,0.4375,0.375,0.875,0.875,0.3125,0.5625,0.3125,0.75,0.75,0.5625,0.6875,0.25,0.5625,1,0.3125,0.4375,0.3125,0.5,1,0.75,0.25,0.5625,0.5,0.5,0.3125,0.4375,0.3125,0.6875,0.6875,0.375,0.75,0.4375,0.4375,0.3125,0.4375,0.4375,0.8125,0.625,0.25,0.3125,0.8125,0.625,0.4375,0.3125,0.5625,0.5,0.375,0.5,0.5,0.3125,0.125,0.4375,0.5,0.25,0.75,0.375,0.25,0.3125,0.625,0.5,0.3125,0.25,0.8125,0.25,0.5,0.5,0.25,0.5,0.3125,0.5,0.25,0.25,0.8125,0.4375,0.25,0.8125,0.4375,0.25,0.8125,0.4375,0.6875,0.9375,0.25,0.4375,0.9375,0.375,0.75,0.5,0.625,0.375,0.6875,0.8125,0.8125,0.625,0.6875,0.3125,0.625,0.25,0.25,0.25,0.9375,0.5625,0.3125,0.4375,0.5625,0.375,0.5,0.4375,0.0625,0.6875,0.8125,0.25,0.375,0.375,0.6875,0.125,0.3125,0.1875,0.4375,0.25,0.3125,0.1875,0.5625,0.4375,0.125,0.5,0.5,0.8125,0.375,0.875,0.4375,0.25,0.125,0.25,0.4375,0.125,0.5625,0.4375,0.6875,0.1875,0.6875,0.1875,0.625,0.625,0.3125,0.4375,0.4375,0.625,0.1875,0.4375,0.4375,0.375,0.5625,0.8125,0.375,0.5625,0.5625,0.5,0.75,0.3125,0.3125,0.5,0.3125,0.25,0.3125,0.625,0.6875,0.875,0.375,0.9375,0.375,0.8125,0.3125,0.375,0.25,0.4375,0.4375,0.25,0.5,0.375,0.25,0.3125,0.5625,0.5625,0.1875,0.3125,0.6875,0.1875,0.1875,0.25,0.375,0.1875,0.1875,0.8125,0.5625,0.625,0.375,0.8125,0.5625,0.4375,0.5625,0.625,0.5,0.5,0.6875,0.375,0.5,0.6875,0.625,0.625,0.25,0.5625,0.4375,0.1875,0.625,0.25,0.9375,0.5625,0.1875,0,0.625,0.1875,0.25,0.1875,0.3125,0.3125,0.25,0.6875,0.5,0.75,0.4375,0.875,0.3125,0.625,0.4375,0.375,0.875,0.375,0.5625,0.4375,0.1875,0.375,0.75,0.5,0.75,0.4375,0.5625,0.4375,0.375,0.375,0.4375,0.3125,0.5,0.5625,0.3125,0.4375,0.5625,0.9375,0.625,0.75,0.75,0.5625,0.75,0.5625,0.9375,0.6875,0.6875,0.4375,0.4375,0.6875,0.8125,0.5625,0.5,0.75,0.875,0.75,0.6875,0.875,0.3125,0.75,0.5625,0.375,0.6875,0.625,0.625,0.75,0.625,0.3125,0.375,0.5,0.5,0.625,0.5,0.5,0.5625,0.8125,0.375,0.6875,0.5,0.4375,0.6875,0.375,0.5625,0.25,0.3125,0.4375,0.8125,0.6875,0.25,0.8125,0.375,0.5,0.4375,0.8125,0.375,0.5,0.625,0.8125,0.4375,0.625,0.5,0.3125,0.625,0.3125,0.3125,0.625,0.4375,0.5625,0.5625,0.4375,0.9375,0.625,0.625,0.5,0.8125,0.5625,0.4375,0.625,0.25,0.5,0.6875,0.25,0.6875,0.625,0.1875,1,0.3125,0.75,0.3125,0.75,0.4375,0.75,0.25,0.5,0.1875,0.1875,0.4375,0.1875,0.25,0.25,0.1875,0.375,0.6875,0.4375,0.5,0.3125]




slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
   return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x,y)
plt.plot(x,mymodel)
plt.show()

predict = myfunc(0.9)



print(predict)