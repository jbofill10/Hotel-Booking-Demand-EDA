# Hotel-Booking-Demand-EDA
Exploring a hotel booking data set in hopes to find some interesting trends and possibly predict some things. 


# Data Visualization

## Hotel Types
I decided to look at the first column to see which hotel types are chosen the most. In this data set, there are only two kinds: Resort Hotels and City Hotels

![alt text](https://github.com/jbofill10/Hotel-Booking-Demand-EDA/blob/master/Data%20Visualization/HotelType.png)

It seems that this data set contains more resort hotel bookings over city hotel bookings. My intution tells me that I think there will be a trend in the meal plan chosen along with the hotel type. I can imagine that maybe BB is more common amongst Resort Hotels just because I would assume people at Resorts would leave do to "vacationy" activies throughout the day.

## Booking Throughout 2017

### Resort Hotels
![alt text](https://github.com/jbofill10/Hotel-Booking-Demand-EDA/blob/master/Data%20Visualization/bookings2017.png)
Not sure if the three months missing are just due to the data set not having them, or is it a case that the hotel wasn't available/open/booked. Nevertheless, I could see that being problematic for future plans that I had to predicite bookings. Other than that, I was surprised that the bookings throughout the year were about the same, expect for December. I expected the earlier months in the year to have less bookings.

### City Hotels
![alt text](https://github.com/jbofill10/Hotel-Booking-Demand-EDA/blob/master/Data%20Visualization/city_bookings2017.png)
It's interesting to me that Resort Hotels has a steadier booking trend than city hotels. I understand the spike during the summer is probably due to tourism, but I would that the same would apply to resort hotels. I guess rich people vacation whenver they want (satire)

## Meal plans chosen

![alt text](https://github.com/jbofill10/Hotel-Booking-Demand-EDA/blob/master/Data%20Visualization/MealTypes.png)

So BB is chosen by far the most of all meal type, which is no surprise. Other than kind of applying the same thought process that I spoke of in the hotel types visualization to all the different meal types , I don't think there is anymore more to say here. 

![alt text](https://github.com/jbofill10/Hotel-Booking-Demand-EDA/blob/master/Data%20Visualization/MealsChosenAtHotels.png) 

I was surprised to see that so many people in city hotels chose BB. Also interesting to see that SC was fairly popular in city hotels as well.

## What Countries are Booking the most Hotels
I create a chart to see what counties were the bookings coming from the most.
![alt text](https://github.com/jbofill10/Hotel-Booking-Demand-EDA/blob/master/Data%20Visualization/BookingsAroundTheWorld.png)
Clearly, it seems that a majority of the bookings are coming from Europe. My guess is that the data set comes from Portugal (since it is just a hotel booking data set and doesn't say where it's from). The chart is a plotly chart, and since I am not using Jupyter nb I cannot embed the interactive chart like I would've hoped for.

## What Countries has the Most Families with Babies that Book Hotels  
I don't know why I was curious about this, so I categorized these discoveries under "weird_trends" in my project directory.

## Resort Hotels
![alt_text](https://github.com/jbofill10/Hotel-Booking-Demand-EDA/blob/master/Data%20Visualization/BabiesResort.png)

### City Hotels
![alt_text](https://github.com/jbofill10/Hotel-Booking-Demand-EDA/blob/master/Data%20Visualization/BabyCity.png)

# Logistic Regression
My first attempt at creating a predictive ML model for the prediction of whether a booking cancelation would occur or not.

I basically applied **One Hot Coding** to all the different columns which I thought would play influence on cancelations and then fitted it to the model.

The results were somewhat disappointing, as I scored:  

<p align="center">
  <img src="https://github.com/jbofill10/Hotel-Booking-Demand-EDA/blob/master/Data%20Visualization/ModelScores.png">
</p>

The confusion matrix has 1355 false positives and 3013 false negatives. I thought hard about what could be causing this, but I am not sure. One column, reservation_status, causes a huge data leak and causes my score to be 100% -- so I removed that from the dataframe completely. 
