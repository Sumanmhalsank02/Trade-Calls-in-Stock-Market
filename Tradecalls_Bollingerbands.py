#Using TATAPOWER dataframe close price to calc the following
# Trade Calls using Bollinger Bands


# Importing the dependencies
import pandas as pd
import matplotlib.pyplot as plt


# Load the dataset 
data1 = pd.read_csv(r'C:\Users\URL......\TATAPOWER.csv')
data1.drop(data1[data1['Series'] !='EQ'].index , inplace =True)  # Removing rows wehere Series value is not equal to EQ
data1['Date'] = pd.to_datetime(data1['Date'])   # Changing date to the standard date format


# Bollinger bands for the stock
window = 14    # Duration of 14 days
no_of_std = 2    # 2 standard deviation away from the average


# Calculate rolling mean and standard deviation using number of days set above
rolling_mean = data1['Close Price'].rolling(window).mean()  # This is the average
rolling_std = data1['Close Price'].rolling(window).std()   # The satndasr deviation


# Made a new dataframe to store values of the bollinger bands
# This is completely optional
Bands_for_TATAPOWER = pd.DataFrame()


# Converting the dataframe to a csv file
Bands_for_TATAPOWER.to_csv("./Bollinger for TATAPOWER.csv", sep=',',index=False)


# Create three columns to hold values of mean and upper and lower Bollinger bands
Bands_for_TATAPOWER['Date'] = data1['Date']  # standard Date format
Bands_for_TATAPOWER['Close Price'] = data1['Close Price']  # The column close price

Bands_for_TATAPOWER['Rolling Mean'] = rolling_mean
Bands_for_TATAPOWER['Bollinger High'] = rolling_mean + (rolling_std * no_of_std)  # Upper band
Bands_for_TATAPOWER['Bollinger Low'] = rolling_mean - (rolling_std * no_of_std)   # Lower band


# Used a dictionary to rename the columns 
dict  = {'DateTata' : Bands_for_TATAPOWER['Date'] ,
         'Close Price' :Bands_for_TATAPOWER['Close Price'],
         'Rolling Mean' : Bands_for_TATAPOWER['Rolling Mean'],
          'Bollinger High' : Bands_for_TATAPOWER['Bollinger High'],
          'Bollinger Low' : Bands_for_TATAPOWER['Bollinger Low']}

# With the new column names, update the dataframe
Bands_for_TATAPOWER = pd.DataFrame(dict)


# Plot the Close Price, Upper and Lower Bands
Bands_for_TATAPOWER[['Close Price','Bollinger High','Bollinger Low']].plot()
plt.grid(True)
plt.title('Trade Calls using Bollinger Bands for TATAPOWER')
plt.legend()
plt.show()


'''# Plot the Rolling Mean, Upper and Lower Bands
Bands_for_TATAPOWER[['Rolling Mean','Bollinger High','Bollinger Low']].plot()
plt.grid(True)
plt.title('Trade Calls using Bollinger Bands for TATAPOWER')
plt.legend()
plt.show()'''


# Check rolling_mean and rolling_std values by printing it
# Have FUN!!✌