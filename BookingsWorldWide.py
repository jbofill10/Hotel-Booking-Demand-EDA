import plotly.express as px
import pandas as pd


def booking_visualization(df):
    country_count = df['country'].value_counts()

    country_df = pd.DataFrame()
    country_df['country'] = country_count.index
    country_df['country_count'] = country_count.values

    fig = px.choropleth(country_df, locations='country', color='country_count')

    fig.show()
