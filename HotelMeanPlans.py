import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.style as style


def hotel_meals_visualization(df):

    style.use('seaborn-poster')
    style.use('ggplot')

    resort_meal_plans = df[df.hotel == 'Resort Hotel']
    city_meal_plans = df[df.hotel == 'City Hotel']

    resort_meal_plans = resort_meal_plans.groupby(['hotel'])['meal'].value_counts()
    city_meal_plans = city_meal_plans.groupby(['hotel'])['meal'].value_counts()

    # Add undefined row since there were no entries for it in city hotels
    city_meal_plans.loc[('City Hotel', 'Undefined')] = 0

    fig, axs = plt.subplots(ncols=2)

    fig.suptitle('Meal Plans Chosen at Different Hotel Types', fontsize=22, y=.98)

    sns.barplot(x=list(range(5)), y=resort_meal_plans, ax=axs[0])

    axs[0].set_xticklabels(['BB', 'HB', 'FB', 'SC', 'Undefined'])
    axs[0].set_xlabel('Meal Plans Chosen at Resort Hotels', fontsize=18, color='black')
    axs[0].set_ylabel('Count of Meal Plans Chosen', fontsize=17, color='black')

    sns.barplot(x=[0, 3, 1, 2, 4], y=city_meal_plans, ax=axs[1])

    axs[1].set_xticklabels(['BB', 'HB', 'FB', 'SC', 'Undefined'])
    axs[1].set_xlabel('Meal Plans Chosen at City Hotels', fontsize=18, color='black')
    axs[1].set_ylabel('Count of Meal Plans Chosen', fontsize=17, color='black')

    # Annotate graphs with values since a low number like 44 looks like 0
    for x in axs:
        for p in x.patches:
            x.annotate("%d" % p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()),
                       ha='center', va='center', fontsize=13, color='black', xytext=(0, 13),
                       textcoords='offset points')

    plt.subplots_adjust(wspace=.4)
    # plt.savefig('Data Visualization/MealsChosenAtHotels.png')
    plt.show()