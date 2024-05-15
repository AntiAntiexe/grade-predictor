# The Nostradamus
The Nostradamus is an "accurate" grade predictor. Based of a data set of over 1,000 grades. The Nostradamus can calculate a person's third grade based on their 1st and 2nd. 

It uses CustomTkinter to create a modern Ui. I opted for the use of CTk instead of Tkinter, even though Tk has more infrastructure built already. But CTk is slowly developing and I think it was the right choice to make. 

When someone first reads this project then they just assume that I average the two results. However, this app actually uses a linear regression model from scipy stats. This module imports specific linear regression statistics. These statistics can create the default linear equation, y = mx + c. Using this equation, you can predict certain values, such as input the x value to calculate the y value and vice versa. 

Finally, I used matplotlib to display the graph on the application. Displaying the graph will help the user to visualize the data.

## Getting Started
Follow these steps to start using this app:
- You can simply download the [nostradamus_v1.py](docs/nostradamus_v1.py) file
- Make sure you have the modules needed:
  > customTkinter,
  > CTk Message Box,
  > Scipy,
  > Matplotlib and
  > Math
- Finally, run the file and enjoy!
