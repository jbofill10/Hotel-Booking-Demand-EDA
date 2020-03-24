import plotly.express as px

def babies_2017(df):
    babies_resort_df = df[df.hotel == 'Resort Hotel']

    babies_city_df = df[df.hotel == 'City Hotel']

    babies_resort_per_country = babies_resort_df.groupby(['country'])['babies'].sum()

    babies_city_per_country = babies_city_df.groupby(['country'])['babies'].sum()

    fig = px.choropleth(babies_resort_per_country,
                        locations=babies_resort_per_country.index,
                        color=babies_resort_per_country.values,
                        color_continuous_scale="ylorrd")
    fig.show()

    fig = px.choropleth(babies_city_per_country,
                        locations=babies_city_per_country.index,
                        color=babies_city_per_country.values,
                        color_continuous_scale="purpor")

    fig.show()