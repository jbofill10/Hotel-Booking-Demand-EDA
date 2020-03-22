import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.style as style
import HotelMeals as h_t
import BookingsWorldWide as bookings

from tqdm import tqdm


def main():
    df = pd.read_csv('Data/hotel_bookings.csv')

    style.use('seaborn-poster')
    style.use('ggplot')

    h_t.hotel_meals_visualization(df)
    bookings.booking_visualization(df)

    sns.barplot(x=list(range(2)), y=df['hotel'].value_counts(), dodge=False)

    plt.xticks(range(2), ['Resort Hotel', 'City Hotel'])
    plt.title('Popularity of hotel bookings', fontsize=18)
    plt.xlabel('Type of hotel', fontsize=18)
    plt.ylabel('Count of Hotel Type Chosen', fontsize=18)

    plt.savefig('Data Visualization/HotelType.png')
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
