# The Nostradamus
The Nostradamus is an "accurate" grade predictor. Based of a data set of over 1,000 grades. The Nostradamus can calculate a person's third grade based on their 1st and 2nd. 

It uses CustomTkinter to create a modern Ui. I opted for the use of CTk instead of Tkinter, even though Tk has more infrastructure built already. But CTk is slowly developing and I think it was the right choice to make. 

When someone first reads this project then they just assume that I average the two results. However, this app actually uses a linear regression model from scipy stats. This module imports specific linear regression statistics. These statistics can create the default linear equation, y = mx + c. Using this equation, you can predict certain values, such as input the x value to calculate the y value and vice versa. 

Finally, I used matplotlib to display the graph on the application. Displaying the graph will help the user to visualize the data.

For further improvements I will probably change the way that I have normalized the data. Thorugh my research in neural networks, I have found that the normalization formula that I chose:

![image](https://github.com/AntiAntiexe/grade-predictor/assets/117411246/a5c5368b-b89f-4891-ab74-ddafc01edb1a)

Is not accurate enough for the purpose of predicting grades so to imporve this I have decided to use the softmax function. 

![image](https://github.com/AntiAntiexe/grade-predictor/assets/117411246/58dcd82a-fc2b-49bd-b9f3-cddba2e2dd0d)

This function is far more accurate at normalizing data between 0 and 1. This is because of the use of exponents. And as of the latest Numpy version. Calculating with exponents is quite simple.

## Getting Started
Follow these steps to start using this app:
- You can simply download the folder.
- Make sure you have the modules needed:
  > customTkinter,
  > CTk Message Box,
  > Scipy,
  > Matplotlib and
  > Math
- Finally, run the nostradamus.py file and enjoy!
