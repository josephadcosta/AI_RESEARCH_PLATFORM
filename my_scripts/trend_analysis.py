import pandas as pd
import plotly.express as px

def trend_graph():

    df = pd.read_csv("data/arxiv_processed.csv")

    trend = df.groupby("year").size()

    fig = px.line(

        x=trend.index,
        y=trend.values,
        title="Research Trend Over Time"

    )

    return fig