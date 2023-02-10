import dash
from dash import dcc
from dash import html
from dash import Input,Output
import plotly.graph_objects as go
import pandas as pd
import pickle

url = ('https://github.com/DariaPrzytula/Property-Prices-in-Gdansk/blob/main/dane_mieszkania_gdansk.xlsx?raw=true')
df = pd.read_excel(url)

with open('model.pickle', 'rb') as file:
    model = pickle.load(file)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.Div([
        html.H2('Housing Price in Gdansk Prediction Using Machine Learning'),
        html.H5('Random Forest Model (scikit-learn library)')
    ],  style={'textAlign': 'center'}),

    html.Hr(),

    html.Div([

    html.Label('Select the size of the apartment:'),
        dcc.Slider(
            id='slider-1',
            min=0,
            max=300,
            step=0.1,
            marks={i: str(i) for i in range(0, 301, 20)},
            tooltip={'placement': 'bottom'}
        ),

        html.Hr(),

        html.Label('Select the year of construction of the apartment:'),
        dcc.Slider(
            id='slider-2',
            min=1850,
            max=2030,
            step=1,
            marks={i: str(i) for i in range(1850, 2031, 10)},
            tooltip={'placement': 'bottom'}
        ),

        html.Hr(),

        html.Label('Select the number of rooms:'),
        html.Div([
            dcc.Dropdown(
                id='dropdown-1',
                options=[{'label': i, 'value': i} for i in range(1,21,1)]
            )
        ], style={'width': '20%', 'textAlign': 'left'}
        ),

        html.Hr(),

        html.Label('Select the floor:'),
        html.Div([
            dcc.Dropdown(
                id='dropdown-2',
                options=[{'label': i, 'value': i} for i in range(0,21,1)]
            )
        ], style={'width': '20%', 'textAlign': 'left'}
        ),

        html.Hr(),

        html.Label('Select the district:'),
        html.Div([
            dcc.Dropdown(
                id='dropdown-3',
                options=[{'label': i, 'value': i} for i in ['Aniołki', 'Brzeźno', 'Brętowo', 'Chełm', 'Górki Zachodnie',
                                                             'Jasień', 'Jelitkowo', 'Kokoszki', 'Letnica', 'Matarnia', 'Młyńska',
                                                            'Nowy Port', 'Oliwa', 'Olszynka', 'Orunia', 'Osowa', 'Piecki-Migowo',
                                                             'Przeróbka', 'Przymorze', 'Rudniki', 'Siedlce',
                                                             'Stogi', 'Strzyża', 'Suchanino', 'Ujeścisko-Łostowice',
                                                             'VII Dwór', 'Wrzeszcz', 'Wyspa Sobieszewska',
                                                             'Zaspa', 'Śródmieście', 'Żabianka']]
            )
        ], style={'width': '20%', 'textAlign': 'left'}
        ),

        html.Hr(),

    ###############

        html.Div([
            html.H4('Your selected parameters:'),
            html.Div(id='div-1'),
            html.Div(id='div-2'),
            html.Hr()
        ], style={'margin': '0 auto', 'textAlign': 'center'})

    ],style={'width': '80%', 'textAlign': 'left', 'margin': '0 auto', 'fontSize': 22,
              'background-color': 'white', 'padding': '30px'})

], style={'background-color': '#61BAAE'})

########
@app.callback(
    Output('div-1', 'children'),
    [Input('slider-1', 'value'),
     Input('slider-2', 'value'),
     Input('dropdown-1', 'value'),
     Input('dropdown-2', 'value'),
     Input('dropdown-3', 'value')
     ]
)

def display_parameters(val1, val2, val3, val4, val5):
    if val1 and val2 and val3 and val4 and val5 :

        return html.Div([
            html.H6(f'Metric area: {val1}'),
            html.H6(f'Year: {val2}'),
            html.H6(f'Rooms: {val3}'),
            html.H6(f'Floor: {val4}'),
            html.H6(f'District: {val5}'),

        ], style={'textAlign': 'left'})
    else:
        return html.Div([
            html.H6('Select all parameters!')
        ])


#####

@app.callback(
    Output('div-2', 'children'),
    [Input('slider-1', 'value'),
     Input('slider-2', 'value'),
     Input('dropdown-1', 'value'),
     Input('dropdown-2', 'value'),
     Input('dropdown-3', 'value')
     ]
)

def predict_value(val1, val2, val3, val4, val5):
    if val1 and val2 and val3 and val4 and val5:

        val5_1, val5_2, val5_3, val5_4, val5_5, val5_6, val5_7, val5_8, val5_9, val5_10, val5_11, val5_12, val5_13, val5_14, val5_15, val5_16, val5_17, val5_18, val5_19, val5_20, val5_21, val5_22, val5_23, val5_24, val5_25, val5_26, val5_27, val5_28, val5_29, val5_30 =  0, 0, 0, 0, 0,0, 0, 0, 0, 0,0, 0, 0, 0, 0,0, 0, 0, 0, 0,0, 0, 0, 0, 0,0, 0, 0, 0, 0

        if val5 == 'Brzeźno':
            val5_1 = 1
        elif val5 == 'Brętowo':
            val5_2 = 1
        elif val5 == 'Chełm':
            val5_3 = 1
        elif val5 == 'Górki Zachodnie':
            val5_4 = 1
        elif val5 == 'Jasień':
            val5_5 = 1
        elif val5 == 'Jelitkowo':
            val5_6 = 1
        elif val5 == 'Kokoszki':
            val5_7 = 1
        elif val5 == 'Letnica':
            val5_8 = 1
        elif val5 == 'Matarnia':
            val5_9 = 1
        elif val5 == 'Młyńska':
            val5_10 = 1
        elif val5 == 'Nowy Port':
            val5_11 = 1
        elif val5 == 'Oliwa':
            val5_12 = 1
        elif val5 == 'Olszynka':
            val5_13= 1
        elif val5 == 'Orunia':
            val5_14 = 1
        elif val5 == 'Osowa':
            val5_15 = 1
        elif val5 == 'Piecki-Migowo':
            val5_16 = 1
        elif val5 == 'Przeróbka':
            val5_17 = 1
        elif val5 == 'Przymorze':
            val5_18 = 1
        elif val5 == 'Rudniki':
            val5_19 = 1
        elif val5 == 'Siedlce':
            val5_20 = 1
        elif val5 == 'Stogi':
            val5_21 = 1
        elif val5 == 'Strzyża':
            val5_22 = 1
        elif val5 == 'Suchanino':
            val5_23 = 1
        elif val5 == 'Ujeścisko-Łostowice':
            val5_24 = 1
        elif val5 == 'VII Dwór':
            val5_25 = 1
        elif val5 == 'Wrzeszcz':
            val5_26 = 1
        elif val5 == 'Wyspa Sobieszewska':
            val5_27 = 1
        elif val5 == 'Zaspa':
            val5_28 = 1
        elif val5 == 'Śródmieście':
            val5_29 = 1
        elif val5 == 'Żabianka':
            val5_30 = 1
        else:
            val5 = 0

        df_sample = pd.DataFrame(
            data=[
                [val1, val2, val3, val4, val5_1, val5_2, val5_3, val5_4, val5_5, val5_6, val5_7, val5_8, val5_9,
                 val5_10, val5_11, val5_12, val5_13, val5_14, val5_15, val5_16, val5_17, val5_18, val5_19,
                 val5_20, val5_21, val5_22, val5_23, val5_24, val5_25, val5_26, val5_27, val5_28, val5_29, val5_30]
            ],
            columns=['Metric area','Year','Rooms','Floor','District_Brzeźno','District_Brętowo',
                     'District_Chełm','District_Górki Zachodnie','District_Jasień','District_Jelitkowo',
                     'District_Kokoszki','District_Letnica','District_Matarnia','District_Młyńska',
                     'District_Nowy Port','District_Oliwa','District_Olszynka','District_Orunia','District_Osowa',
                     'District_Piecki-Migowo','District_Przeróbka','District_Przymorze','District_Rudniki',
                     'District_Siedlce','District_Stogi','District_Strzyża','District_Suchanino','District_Ujeścisko-Łostowice',
                     'District_VII Dwór','District_Wrzeszcz','District_Wyspa Sobieszewska','District_Zaspa',
                     'District_Śródmieście','District_Żabianka']
        )
        print(df_sample)

        price = model.predict(df_sample)[0]
        price = int(round(price, 0))

        return html.Div([
            html.H4(f'Sugerowana cena {price} zł')
        ], style={'background-color': '#AF90C2', 'width': '60%', 'margin': '0 auto'})




if __name__ == '__main__':
    app.run_server(debug=True)


