import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import calendar


def resort_timespan_visualizations(df):
    bookings_2017 = df[df.reservation_status_date >= '2017-01-01']

    bookings_2017['arrival_date_month'] = bookings_2017['arrival_date_month'].apply(
        lambda x: list(calendar.month_name).index(x))

    bookings_2017_df = pd.DataFrame(bookings_2017['arrival_date_month'].value_counts()).sort_index()

    # Add missing months
    bookings_2017_df.loc[9] = 0
    bookings_2017_df.loc[10] = 0
    bookings_2017_df.loc[11] = 0

    # Sort index again
    bookings_2017_df=bookings_2017_df.sort_index()

    sns.barplot(x=list(bookings_2017_df['arrival_date_month'].index), y=list(bookings_2017_df['arrival_date_month'].values))
    plt.xticks(range(0,13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.xlabel("Month", fontsize=18, color='black')
    plt.ylabel("Arrivals", fontsize=18, color='black')
    plt.title("Bookings Throughout 2017", fontsize=22)
    #plt.savefig('./Data Visualization/bookings2017.png')
    plt.show()
