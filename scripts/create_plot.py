import plotly.express as px
import pandas as pd

def create_plot(csv_file, output_html):
    df = pd.read_csv(csv_file)
    fig = px.line(df, x='Date', y='Close', title='Stock Price Over Time')
    fig.write_html(output_html)

if __name__ == '__main__':
    create_plot('data/data.csv', 'plots/plot.html')
