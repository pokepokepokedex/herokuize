import pandas as pd
#import dash
#import dash_core_components as dcc
#import dash_html_components as html
import plotly.graph_objs as go
import plotly.offline as pyo
from flask import Flask, render_template, request


server = Flask(__name__)
app = dash.Dash(__name__, server=server)

df = pd.read_csv("pokemon3.csv")

against = []
against.append('name')
against.append('type1')

for name in list(df.columns[1:19]):
    against.append(name)

df_against = df[against]

stats = ['name', 'type1', 'hp', 'defense', 'sp_attack', 'sp_defense', 'speed']
df_stats = df[stats]

all_hp = [df_stats['hp'].mean()]
all_psy = [df_stats[df_stats['type1']=='psychic']['hp'].mean()]
poke = [int(df[df['name']=='Mewtwo']['hp'].values)]

all_def = [df_stats['defense'].mean()]
all_psy1 = [df_stats[df_stats['type1']=='psychic']['defense'].mean()]
poke1 = [int(df[df['name']=='Mewtwo']['defense'].values)]

x1 = ['HP', 'Defense', 'Special Attack', 'Special Defense', 'Speed']

y1 = [df_stats['hp'].mean(), df_stats['defense'].mean(), df_stats['sp_attack'].mean(), df_stats['sp_defense'].mean(),
      df_stats['speed'].mean()]
y2 = [df_stats[df_stats['type1']=='psychic']['hp'].mean(), df_stats[df_stats['type1']=='psychic']['defense'].mean(),
      df_stats[df_stats['type1']=='psychic']['sp_attack'].mean(),df_stats[df_stats['type1']=='psychic']['sp_defense'].mean(),
      df_stats[df_stats['type1']=='psychic']['speed'].mean()]
y3 = [int(df[df['name']=='Mewtwo']['hp'].values), int(df[df['name']=='Mewtwo']['defense'].values),
      int(df[df['name']=='Mewtwo']['sp_attack'].values),int(df[df['name']=='Mewtwo']['sp_defense'].values),
      int(df[df['name']=='Mewtwo']['speed'].values)]

trace1 = go.Bar(x=x1,y=y1,marker=dict(color=['black', 'black', 'black', 'black', 'black']), name='Average of all Pokemon')
trace2 = go.Bar(x=x1,y=y2,marker=dict(color=['violet','violet','violet','violet','violet']), name='Avergae of all Psychic')
trace3 = go.Bar(x=x1,y=y3,marker=dict(color=['purple','purple','purple','purple','purple']), name='Mewtwo')

app.layout = html.Div([html.Div([dcc.Graph(id='bars',
             figure = {'data': [go.Bar(x=df_against[df_against['name']=='Mew'].values[0][2:],y=df_against.columns[2:],
                     orientation = 'h')],
                       'layout': go.Layout(title='Bars', autosize=False,
                                            width=1000, height=500,
                                            yaxis=go.layout.YAxis(automargin=True),
                                            margin=go.layout.Margin(
                                            l=100,r=100,b=100,t=100,pad=10
                                            ))}),html.H1("Check this out!!")]),
                dcc.Graph(id='bars2',
                             figure = {'data': [trace1, trace2, trace3],
                                       'layout': go.Layout(title='Mewtwo vs Others', autosize=False,
                                                            width=800, height=500,
                                                            yaxis=go.layout.YAxis(automargin=True),
                                                            margin=go.layout.Margin(
                                                            l=50,r=50,b=100,t=100,pad=4))})])

#@server.route('/happy')
def index():
    data = [trace1,trace2,trace3]
    layout = go.Layout(title='Mewtwo vs Others', autosize=False,
                         width=800, height=500,
                         yaxis=go.layout.YAxis(automargin=True),
                         margin=go.layout.Margin(
                         l=50,r=50,b=100,t=100,pad=4))
    fig = go.Figure(data=data,layout=layout)
    return pyo.plot(fig)


#if __name__ == '__main__':
#    app.run_server()
