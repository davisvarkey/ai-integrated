import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Loading the dataset
uber = pd.read_csv("Uber Request Data.csv")

# Checking for duplicate records if present
print(uber.shape[0])  # 6745
print(uber['Request.id'].nunique())  # 6745
# Hence duplicate records are not present

# Changing Request and Drop Timestamp column to a fixed format
uber['Request.timestamp'] = pd.to_datetime(uber['Request.timestamp'], errors='coerce')
uber['Drop.timestamp'] = pd.to_datetime(uber['Drop.timestamp'], errors='coerce')

# Extracting the hour of the day from the requested time and storing in new column
uber['Request.Time.Hour'] = uber['Request.timestamp'].dt.hour

# Creating time slots based on request time hour
bins = [0, 4, 9, 16, 22, 24]
labels = ['Late Night', 'Early Morning', 'Mid Day', 'Late Evening', 'Late Night']
uber['Time.Slot'] = pd.cut(uber['Request.Time.Hour'], bins=bins, labels=labels, right=False)

# Visualizing the frequency of request and the different status based on the time slots derived
# Using the entire dataset consisting of trips from city to airport and from airport to city
sns.countplot(x='Time.Slot', hue='Status', data=uber)
plt.title('Status of Request v/s Time Slot on all trips made')
plt.xlabel('Time Slot')
plt.ylabel('Count of request')
plt.show()

# Analyzing further how the frequency of request and status varies with Pickup Point
# For trips from city to airport
uber_city_pickup = uber[uber['Pickup.point'] == "City"]
sns.countplot(x='Time.Slot', hue='Status', data=uber_city_pickup)
plt.title('Status of Request v/s Time Slot (For City to Airport trips)')
plt.xlabel('Time Slot')
plt.ylabel('Count of request')
plt.show()

# For trips from airport to city
uber_airport_pickup = uber[uber['Pickup.point'] == "Airport"]
sns.countplot(x='Time.Slot', hue='Status', data=uber_airport_pickup)
plt.title('Status of Request v/s Time Slot (For Airport to City trips)')
plt.xlabel('Time Slot')
plt.ylabel('Count of request')
plt.show()

# Visualizing on the entire dataset how request for pickup varies as per Time Slot
sns.countplot(x='Time.Slot', hue='Pickup.point', data=uber)
plt.title('Request of cabs as per time slots on all trips')
plt.xlabel('Time Slots')
plt.ylabel('Count of request')
plt.show()


