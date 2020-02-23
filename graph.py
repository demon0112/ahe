
import io
import random
from flask import Response
from flask import Flask
from flask import render_template
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
import json
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
app=Flask(__name__)

@app.route('/plot_min.png')
def plot_png_min():
    fig = create_figure_min()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure_min():
    fig = Figure()
    df_s = pd.read_csv('solar_power_data.csv')
    df_l= pd.read_csv('load_power_data.csv')
    axis = fig.add_subplot(1, 1, 1)
    x_s= df_s['ts']
    y_s= df_s['solarpower']
    x_l= df_l['ts']
    y_l= df_l['loadpower']
    axis.plot(x_s,y_s)
    axis.plot(x_l,y_l)
    return fig
@app.route('/plot_hour.png')
def plot_png_hour():
    fig = create_figure_hour()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure_hour():
    fig = Figure()
    df_s= pd.read_csv('solar_power_data.csv',parse_dates=['ts'], index_col=['ts'])
    df_l= pd.read_csv('load_power_data.csv',parse_dates=['ts'], index_col=['ts'])
    df_sr=df_s.resample('60Min',  base=30).mean()
    df_lr=df_l.resample('60Min',  base=30).mean()
    axis = fig.add_subplot(1, 1, 1)
    x_s= df_sr.index
    y_s= df_sr['solarpower']
    x_l= df_lr.index
    y_l= df_lr['loadpower']
    axis.plot(x_s,y_s)
    axis.plot(x_l,y_l)
    return fig


if __name__=="__main__":
    app.run()