import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
from dash import html
from app import app
import dash
import ds  # Asume que ds contiene la función entrenar_y_evaluar y distribucion_pases_por_equipo

# Cargar los datos una vez (si es adecuado)
df = pd.read_csv('datos_bundesliga.csv')

@app.callback(
    Output('output-neural-network', 'children'),
    [Input('trigger-neural-network', 'n_clicks')]
)
def update_output(n_clicks):
    if n_clicks:
        losses = ds.entrenar_y_evaluar()
        return html.Ul([html.Li(f'Epoch {i+1}: {loss}') for i, loss in enumerate(losses)])
    return "Haz clic en el botón para entrenar la red neuronal."

@app.callback(
    Output('grafica-pases-por-equipo', 'figure'),
    [Input('trigger-update', 'n_clicks')]
)
def grafica_pases_por_equipo(n_clicks):
    pases_por_equipo = ds.distribucion_pases_por_equipo(df)
    fig = px.bar(pases_por_equipo, x=pases_por_equipo.index, y='Pases')
    fig.update_traces(
        hoverinfo='all',
        marker=dict(color='blue'),  # Estilo normal
        hovertemplate="<b>%{y} pases</b><extra></extra>",  # Personaliza el texto de hover
        selected=dict(marker=dict(color='crimson')),  # Cambia color en hover
        unselected=dict(marker=dict(opacity=0.5))  # Estilo cuando no está en hover
    )
    return fig


@app.callback(
    Output('grafica-pases-por-fase', 'figure'),
    [Input('trigger-neural-graph', 'n_clicks')]
)
def update_grafica_pases_por_fase(n_clicks):
    
    datos_grafica = ds.pases_por_fase_del_partido(df)
    fig = px.bar(datos_grafica, barmode='group')
    return fig
    


@app.callback(
    Output('grafica-posicion-inicio-pases', 'figure'),
    [Input('trigger-graph', 'n_clicks')]
)
def update_grafica_posicion_inicio_pases(n_clicks):
    
    fig = px.box(df, x='Posicion_Inicio', y='Pases', points="all")
    return fig
    


@app.callback(
    Output('grafica-cantidad-pases-jugada', 'figure'),
    [Input('trigger', 'n_clicks')]
)
def update_grafica_cantidad_pases_jugada(n_clicks):
    
    # Convertir minutos y segundos a un solo valor numérico (por ejemplo, minuto + segundo/60)
    df['Momento'] = df['Minuto'] + df['Segundo'] / 60.0
    fig = px.scatter(df, x='Momento', y='Pases', color='Equipo', hover_data=['Fase_del_Partido'])
    return fig
   