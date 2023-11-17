from dash import html
from dash import dcc

def create_layout():
    return html.Div([
        html.H1('Análisis de pases en la Bundesliga'),
        html.Button('Entrenar Red Neuronal', id='trigger-neural-network'),
        html.H2('Entrenamiento de la red neuronal'),
        html.Div(id='output-neural-network'),
        html.Div(
                style={'display': 'flex', 'justifyContent': 'space-around'},
                children=[
                    # Contenedor para el primer conjunto de componentes
                    html.Div(
                        children=[
                            html.H2('Análisis de pases por equipo'),
                            dcc.Graph(id='grafica-pases-por-equipo'),
                            html.Button('Pases por equipo', id='trigger-update'),
                        ],
                        style={'width': '40%'}
                    ),

                    # Contenedor para el segundo conjunto de componentes
                    html.Div(
                        children=[
                            html.H2('Análisis de pases por fase del partido'),
                            dcc.Graph(id='grafica-pases-por-fase'),
                            html.Button('Pases por fase', id='trigger-neural-graph'),
                        ],
                        style={'width': '40%'}
                    )
                ]
            ),

        html.H2('Análisis de pases por posición de inicio'),
        dcc.Graph(id='grafica-posicion-inicio-pases'),
        html.Button('Distribución del campo', id='trigger-graph'),
        html.H2('Análisis de pases por jugada'),
        dcc.Graph(id='grafica-cantidad-pases-jugada'),
        html.Button('pases por jugada', id='trigger')
        
    ])
