import dash
from dash import dcc, html, callback, Input, Output, State
import dash_table
import pandas as pd
import base64
import io

# Inicializar la aplicación Dash
app = dash.Dash(__name__)
app.title = "Proyecto 2 - Data Science"

# Estilos CSS para mejorar la apariencia
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app.css.append_css({"external_url": external_stylesheets})

# Definir el layout del dashboard
app.layout = html.Div([
    html.Div(id='page-content', children=[
        html.H1("Convertidor de CSV", style={
                'textAlign': 'center', 'color': 'black'}),
        dcc.Upload(
            id='upload-data',
            children=html.Div(
                ['Arrastra o ', html.A('selecciona un archivo CSV')]),
            style={
                'width': '90%', 'height': '60px', 'lineHeight': '60px',
                'borderWidth': '1px', 'borderStyle': 'dashed', 'borderRadius': '5px',
                'textAlign': 'center', 'margin': '10px'
            },
            multiple=False
        ),
        html.Div(id='output-data-upload'),
        html.Button('Continuar', id='submit-button',
                    n_clicks=0, style={'margin': '10px'})
    ])
])

# Callback para procesar el archivo CSV y mostrarlo


@callback(
    Output('output-data-upload', 'children'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename'),
    prevent_initial_call=True,
    suppress_callback_exceptions=True
)
def update_output(contents, filename):
    if contents:
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        try:
            if 'csv' in filename:
                df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
            else:
                return html.Div(['Tipo de archivo no soportado.'])

            return html.Div([
                html.H5(filename),
                dash_table.DataTable(
                    data=df.to_dict('records'),
                    columns=[{'name': i, 'id': i} for i in df.columns],
                    page_size=10
                )
            ])
        except Exception as e:
            print(e)
            return html.Div(['Hubo un error al procesar el archivo.'])

# Callback para cambiar el contenido de la página


@callback(
    Output('page-content', 'children'),
    Input('submit-button', 'n_clicks'),
    prevent_initial_call=True,
    suppress_callback_exceptions=True
)
def change_page_content(n_clicks):
    if n_clicks > 0:
        return html.Div([
            html.H3('Bienvenido a la nueva vista'),
            # ... (cualquier otro contenido que quieras mostrar)
        ])
    else:
        raise dash.exceptions.PreventUpdate


# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
