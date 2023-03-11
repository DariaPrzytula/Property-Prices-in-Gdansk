# dodać opisy do wykresów

# Import libraries

import dash
from dash import dcc
from dash import html
from dash import Input,Output
import dash_bootstrap_components as dbc
import pickle
import pandas as pd
import plotly.express as px
import geopandas as gpd

# Import data

df = pd.read_excel("C:\\Users\\kurzy\\Desktop\\Studia podyplomowe\\Property-Prices-in-Gdansk\\dane_uporządkowane.xlsx")

# import model

with open('model.pickle', 'rb') as file:
    model = pickle.load(file)




# dashboard code

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SANDSTONE])


app.layout = html.Div([

    html.Div([

    html.H1('Property prices in Gdańsk',
            style={'textAlign': 'center',
                   'color':'#5b3903', 'fontWeight' : 'bold'
               }
        ),

    html.Br(),

        html.Div([
            html.P(
                'The purpose of the project was to analyze apartment prices by collecting data on apartment sales offers from Trójmiasto.pl using the Data Miner plugin.' 
                'The data collected included information such as price, location, area, number of rooms, year of construction, and floor level.'),
            html.P(
                'The data was then analyzed to identify the key features that impact apartment prices. This analysis led to the development of a predictive model that could estimate the price of an apartment based on specific parameters.'),
            html.P(
                'Overall, this project provided valuable insights into the real estate market and assisted in determining the market value of apartments.')
        ], style={'background-color': 'rgba(245,245,220,0.65)', 'color':'#5b3903', 'fontWeight' : '450',
                  'width': '90%', 'margin': 'auto', 'marginBottom': '20px'}),


        html.Br(),

    html.Div([
        html.H5('Explore the influence of apartment construction year on selected parameters.',
                style={'textAlign': 'center', 'marginBottom': '10px', 'color':'#5b3903', 'fontWeight' : '450'}),
        html.Label("Select the year construction of the apartment:",
                style={'marginBottom': '20px'}),
        dcc.Slider(
            id='year-built-slider',
            min=1900,
            max=2026,
            value=2020,
            marks={str(rok): str(rok) for rok in range(1900, 2026, 10)},
            step=1,
            tooltip={'placement': 'bottom', "always_visible": True}

        )
    ], style={'background-color': 'rgba(245,245,220,0.65)', 'color':'#5b3903', 'fontWeight' : '450',
              "width": "90%", "margin": "auto"}),

    html.Hr(),

    dcc.Tabs(id="tabs", children=[
        dcc.Tab(label='Chart of apartment prices by area', children=[
            dcc.Graph(id='graph-1', style={'backgroundColor': 'inherit', 'margin': 0})
        ], style={'background-color': '#fcfce9'}),
        dcc.Tab(label='Chart of apartment price histogram', children=[
            dcc.Graph(id='graph-2', style={'backgroundColor': 'inherit', 'margin': 0})
        ], style={'background-color': '#f1f1d0'}),
        dcc.Tab(label='Chart of apartment prices distributed by district', children=[
            dcc.Graph(id='graph-3', style={'backgroundColor': 'inherit', 'margin': 0})
        ], style={'background-color': '#dfdfab'}),

    ])


], style={'background-image': 'url(https://images.unsplash.com/photo-1623130622557-8fab31968b8f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Nnx8Z2RhbnNrfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=600&q=60)',
          'background-size': 'cover',
          'background-position': 'top center',
          'background-repeat': 'no-repeat'}),

################ MACHINE LEARNING PART ###################

html.Div([

    html.Div([
        html.H3('Calculate the worth of your apartment'),
    ],  style={'textAlign': 'center', 'color':'#5b3903', 'fontWeight' : 'bold'}),

    html.Hr(),

    html.Div([

    html.Label('Select the size of the apartment:',
               style={'textAlign': 'left', 'color':'#5b3903', 'fontWeight' : '450', 'marginBottom': '20px'}),
        dcc.Slider(
            id='slider-1',
            min=0,
            max=200,
            step=0.1,
            marks={i: str(i) for i in range(0, 201, 20)},
            tooltip={'placement': 'bottom'}
        ),

        html.Hr(),

        html.Label('Select the year construction of the apartment:',
                   style={'textAlign': 'left', 'color':'#5b3903', 'fontWeight' : '450', 'marginBottom': '20px'}),
        dcc.Slider(
            id='slider-2',
            min=1900,
            max=2030,
            step=1,
            marks={i: str(i) for i in range(1900, 2031, 10)},
            tooltip={'placement': 'bottom'}

        ),

        html.Hr(),

        html.Label('Select the number of rooms:',
                   style={'textAlign': 'left', 'color':'#5b3903', 'fontWeight' : '450', 'marginBottom': '20px'}),
        html.Div([
            dcc.Dropdown(
                id='dropdown-1',
                options=[{'label': i, 'value': i} for i in range(1,21,1)],
                style={'backgroundColor': '#dfdfab', 'color':'#5b3903'}
            )
        ], style={'width': '20%', 'textAlign': 'left'}
        ),

        html.Hr(),

        html.Label('Select the floor:',
                   style={'textAlign': 'left', 'color':'#5b3903', 'fontWeight' : '450', 'marginBottom': '20px'}),
        html.Div([
            dcc.Dropdown(
                id='dropdown-2',
                options=[{'label': i, 'value': i} for i in range(0,20,1)],
                style={'backgroundColor': '#dfdfab', 'color':'#5b3903'}
            )
        ], style={'width': '20%', 'textAlign': 'left'}
        ),

        html.Hr(),

        html.Label('Select the district:',
                   style={'textAlign': 'left', 'color':'#5b3903', 'fontWeight' : '450', 'marginBottom': '20px'}),
        html.Div([
            dcc.Dropdown(
                id='dropdown-3',
                options=[{'label': i, 'value': i} for i in ['Aniołki', 'Brzeźno', 'Brętowo', 'Chełm', 'Górki Zachodnie',
                                                             'Jasień', 'Jelitkowo', 'Kokoszki', 'Letnica', 'Matarnia', 'Młyńska',
                                                            'Nowy Port', 'Oliwa', 'Olszynka', 'Orunia', 'Osowa', 'Piecki-Migowo',
                                                             'Przeróbka', 'Przymorze', 'Rudniki', 'Siedlce',
                                                             'Stogi', 'Strzyża', 'Suchanino', 'Ujeścisko-Łostowice',
                                                             'VII Dwór', 'Wrzeszcz', 'Wyspa Sobieszewska',
                                                             'Zaspa', 'Śródmieście', 'Żabianka']],
                style={'backgroundColor': '#dfdfab', 'color':'#5b3903'}
            )
        ], style={'width': '40%', 'textAlign': 'left'}
        ),

        html.Hr(),

        html.Div([
            html.H4('Your selected parameters:'),
            html.Div(id='div-1'),
            html.Div(id='div-2'),
            html.Hr()
        ], style={'margin': '0 auto', 'textAlign': 'left', 'color':'#5b3903', 'fontWeight' : '450'})

    ])

])
], style={'background':'beige'})


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

        val5_1, val5_2, val5_3, val5_4, val5_5, val5_6, val5_7, val5_8, val5_9, val5_10, \
        val5_11, val5_12, val5_13, val5_14, val5_15, val5_16, val5_17, val5_18, val5_19, \
        val5_20, val5_21, val5_22, val5_23, val5_24, val5_25, val5_26, val5_27, val5_28, val5_29, \
        val5_30 =  0, 0, 0, 0, 0,0, 0, 0, 0, 0,0, 0, 0, 0, 0,0, 0, 0, 0, 0,0, 0, 0, 0, 0,0, 0, 0, 0, 0

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
            html.H4(f'The estimated value of your apartment: {price} zł', style= {'color':'#5b3903'})

        ], style={'background-color': '#edebe4', 'width': '60%', 'margin': '0 auto'})


@app.callback(
    Output('graph-1', 'figure'),
    Output('graph-2', 'figure'),
    Output('graph-3', 'figure'),
    Input('year-built-slider', 'value'))
def update_figures(selected_year):
    filtered_df = df[df.Year == selected_year]

    fig1 = px.scatter(filtered_df, x="Metric area", y="Price", color="District", size="Metric area")
    fig1.update_layout(xaxis_title="Metric area",
                       yaxis_title="Price",
                       font=dict(color="color':'#5b3903"),
                       plot_bgcolor="beige"
                       )
    fig1.update_xaxes(showgrid=True, gridcolor='white', zeroline=False)
    fig1.update_yaxes(showgrid=True, gridcolor='white', zeroline=False)

    fig2 = px.histogram(filtered_df, x="Price", nbins=20, range_x=[200000, 5000000])
    fig2.update_layout(bargap=0.2
                       )

    fig3 = px.box(filtered_df, x='District', y='Price')


    return fig1, fig2, fig3

if __name__ == '__main__':
    app.run_server(debug=True)
