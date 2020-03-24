import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.style as style
import HotelMeanPlans as h_t

import BookingsWorldWide as bookings

from booking_timespans import CityHotelBookingTimeSpan as city_timespan
from booking_timespans import ResortHotelBookingTimeSpan as resort_timespan
from weird_trends import Babies as babies
from machine_learning import LogisticRegression as lg


def main():
    df = pd.read_csv('Data/hotel_bookings.csv')

    style.use('seaborn-poster')
    style.use('ggplot')

    h_t.hotel_meals_visualization(df)
    city_timespan.city_timespan_visualizations(df[df.hotel == 'City Hotel'])
    babies.babies_2017(df)
    lg.log_reg(df)


    bookings.booking_visualization(df)

    resort_timespan.resort_timespan_visualizations(df[df.hotel == 'Resort Hotel'])

    sns.barplot(x=list(range(2)), y=df['hotel'].value_counts())

    plt.xticks(range(2), ['Resort Hotel', 'City Hotel'])
    plt.title('Popularity of hotel bookings', fontsize=18)
    plt.xlabel('Type of hotel', fontsize=18)
    plt.ylabel('Count of Hotel Type Chosen', fontsize=18)

    #plt.savefig('Data Visualization/HotelType.png')
    plt.show()

    sns.barplot(x=list(range(5)), y=df['meal'].value_counts())

    plt.xticks(range(5), ['BB', 'HB', 'FB', 'SC', 'Undefined'])
    plt.title('Meal Plans Chosen with Hotel Bookings', fontsize=18)
    plt.xlabel('Meal kind', fontsize=18)
    plt.ylabel('Meal count', fontsize=18)

    # plt.savefig('Data Visualization/MealTypes.png')
    plt.show()


if __name__ == '__main__':
    main()
