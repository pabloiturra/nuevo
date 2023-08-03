import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import dash_daq as daq
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from flask import Flask, jsonify
import requests

# Lee el archivo de Excel y carga los datos en el dataframe "rend"
rend = pd.read_excel("C:/Users/Pablo Iturra/Downloads/Recepcioones 2023 (1).xlsx")
# Selecciona solo las columnas 'FecIngreso', 'M3SSC_Recepcion' y 'TipoMvto'
rend = rend[['FecIngreso', 'M3SSC_Recepcion', 'TipoMvto']]
# Convierte la columna 'FecIngreso' a un formato de fecha y hora (datetime)
rend['FecIngreso'] = pd.to_datetime(rend['FecIngreso'], format="%d-%m-%Y %H:%M")
# Convierte la columna 'M3SSC_Recepcion' a un formato numérico
rend['M3SSC_Recepcion'] = pd.to_numeric(rend['M3SSC_Recepcion'], errors='coerce')
# Elimina las filas duplicadas basándose en 'FecIngreso' y ordena los valores de 'FecIngreso'
rend = rend.drop_duplicates(subset=['FecIngreso']).sort_values(by='FecIngreso')

# Datos
data = {
    'Producción': [3165],
    'Ritmo': [189],
    'TFS': ['7:15']
}

# Crear un DataFrame con los datos
resumen1 = pd.DataFrame(data)

# Inicializar la aplicación Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

response = requests.get('http://localhost:8052/get_data')
data = response.json()  # Convierte la respuesta a un objeto Python

# Ahora puedes usar `data` en tu aplicación Dash. Por ejemplo:
Disponibilidad1 = data['Disponibilidad1']
Calidad1 = data['Calidad1']
rendimiento_global1 = data['rendimiento_global1']
Disponibilidad2 = data['Disponibilidad2']
Calidad2 = data['Calidad2']
rendimiento_global2 = data['rendimiento_global2']
Disponibilidad3 = data['Disponibilidad3']
Calidad3 = data['Calidad3']
rendimiento_global3 = data['rendimiento_global3']
Disponibilidad4 = data['Disponibilidad4']
Calidad4 = data['Calidad4']
rendimiento_global4 = data['rendimiento_global4']
rendl1_diario1 = data['rendl1_diario1']
rendl1_diario2 = data['rendl1_diario2']
rendl1_diario3 = data['rendl1_diario3']
rendl1_diario4 = data['rendl1_diario4']
df_grouped1 = data['df_grouped1']
df_grouped2 = data['df_grouped2']
df_grouped3 = data['df_grouped3']
df_grouped4 = data['df_grouped4']

app.layout = html.Div(
    children=[
        dbc.Row(
            [
                dbc.Col(
                    dcc.DatePickerRange(
                        id='my-date-picker-range',
                        start_date=rend['FecIngreso'].min(),  # primera fecha en tu dataframe
                        end_date=rend['FecIngreso'].max(),  # última fecha en tu dataframe
                        display_format='DD/MM/YYYY',
                        style={
                            'border-radius': '25px',  # hace que los bordes sean redondeados
                            'padding': '10px',  # agrega espacio alrededor del DatePickerRange
                        },
                    ),
                    width=12,  # ocupa todo el ancho de la fila
                )
            ]
        ),
        dbc.Row([
            dbc.Col(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    html.Div(
                                        "Línea 1",
                                        className="py-2",
                                        style={
                                            'fontSize': '20px',
                                        },
                                    ),
                                ],
                                style={
                                    'backgroundColor': '#6dae3a',  # Cambia el color de fondo a #6dae3a
                                    'color': 'white',  # Cambia el color de las letras a blanco
                                    'borderTopLeftRadius': '0.25rem',  # Redondea la esquina superior izquierda
                                    'borderTopRightRadius': '0.25rem',  # Redondea la esquina superior derecha
                                },
                            ),
                        ],
                    ),
                    
                    html.Div([
                    html.Iframe(srcDoc=open('highchartmain.html').read(), width='100%', height='290')
                    ],
                    
                    ),
                    dbc.Row([
                        dbc.Col([
                            html.P(f"{Disponibilidad1}%", style={'fontSize': '10px'}),
                            html.Div(style={
                            'height': '15px',
                            'marginRight': '22px',  # Agrega margen a la derecha de la línea para separarla de la siguiente línea
                            'marginLeft': '12px',
                        },
                        ),
                        ],
                        style={
                            'display': 'flex',
                            'alignItems': 'center',
                            'flexDirection': 'column',
                        },
                        ),
                        dbc.Col([
                            html.P(f"{rendimiento_global1}%", style={'fontSize': '10px'}),
                            html.Div(style={
                            'height': '15px',
                            'marginRight': '22px',  # Agrega margen a la derecha de la línea para separarla de la siguiente línea
                            'marginLeft': '12px',
                        },
                        ),
                        ],
                        style={
                            'display': 'flex',
                            'alignItems': 'center',
                            'flexDirection': 'column',
                        },
                        ),
                        dbc.Col([
                            html.P(f"{Calidad1}%", style={'fontSize': '10px'}),
                            html.Div(style={
                            'height': '15px',
                            'marginRight': '22px',  # Agrega margen a la derecha de la línea para separarla de la siguiente línea
                            'marginLeft': '12px',
                        },
                        ),
                        ],
                        style={
                            'display': 'flex',
                            'alignItems': 'center',
                            'flexDirection': 'column',
                        },
                        ),
                    ],
                        className="mb-0",  # Esto aplica una clase de Bootstrap para eliminar el margen inferior
                        style={'paddingBottom': '0'}  # Reducir el padding inferior a 0
                    ),
                    dbc.Row([
                        dbc.Col(
                            html.Div(style={
                            'height': '15px',
                            'background': '#00e272',
                            'borderRadius': '10px',
                            'marginRight': '22px',  # Agrega margen a la derecha de la línea para separarla de la siguiente línea
                            'marginLeft': '12px',
                        },
                        )),
                        dbc.Col(html.Div(style={
                            'height': '15px',
                            'background': '#544fc5',
                            'borderRadius': '10px',
                            'marginRight': '17px',  # Agrega margen a la derecha de la línea para separarla de la siguiente línea
                            'marginLeft': '17px',
                        })),
                        dbc.Col(html.Div(style={
                            'height': '15px',
                            'background': '#2cafff',
                            'borderRadius': '10px',
                            'marginLeft': '22px',
                            'marginRight': '12px',
                        })),
                    ]),
                    dbc.Row([
                        dbc.Col([
                            html.P("Disponibilidad", style={'fontSize': '10px'}),
                            html.Div(style={
                            'height': '15px',
                            'marginRight': '22px',  # Agrega margen a la derecha de la línea para separarla de la siguiente línea
                            'marginLeft': '12px',
                        },
                        ),
                        ],
                        style={
                            'display': 'flex',
                            'alignItems': 'center',
                            'flexDirection': 'column',
                        },
                        ),
                        dbc.Col([
                            html.P("Rendimiento", style={'fontSize': '10px'}),
                            html.Div(style={
                            'height': '15px',
                            'marginRight': '22px',  # Agrega margen a la derecha de la línea para separarla de la siguiente línea
                            'marginLeft': '12px',
                        },
                        ),
                        ],
                        style={
                            'display': 'flex',
                            'alignItems': 'center',
                            'flexDirection': 'column',
                        },
                        ),
                        dbc.Col([
                            html.P("Calidad", style={'fontSize': '10px'}),
                            html.Div(style={
                            'height': '15px',
                            'marginRight': '22px',  # Agrega margen a la derecha de la línea para separarla de la siguiente línea
                            'marginLeft': '12px',
                        },
                        ),
                        ],
                        style={
                            'display': 'flex',
                            'alignItems': 'center',
                            'flexDirection': 'column',
                        },
                        ),
                    ]),
                    html.Div([

                    ],
                    style={
                            'borderBottom': '2px solid grey ',  # Cambia a cualquier color que prefieras
                        },
                        ),
                    html.Br(),
                    html.Div(
                            [
                                dash_table.DataTable(
                                    columns=[
                                        {"name": "Producción", "id": "Producción"},
                                        {"name": "Ritmo", "id": "Ritmo"},
                                        {"name": "TFS", "id": "TFS"},
                                    ],
                                    data=resumen1.to_dict("records"),
                                    style_table={"overflowY": "auto"},
                                    style_header={
                                        "fontWeight": "bold",
                                        'backgroundColor': '#01766e',  # Cambia el color de fondo de la cabecera
                                        'color': 'white'  # Cambia el color del texto de la cabecera a blanco
                                    },
                                    style_cell={"textAlign": "left"},
                                    page_size=2,
                                    style_data_conditional=[
                                        {"if": {"row_index": "odd"}, "backgroundColor": "rgb(248, 248, 248)"}
                                    ]
                                )
                            ],
                            style={"overflowY": "auto"}
                        ),
                ],
                className="border rounded shadow-sm mb-3 d-flex flex-column",
                style={"height": "560px", "marginRight": "10px"},
                id='my-col',
                md=3,
            ),
            dbc.Col(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    html.Div(
                                        "Línea 2",
                                        className="py-2",
                                        style={
                                            'fontSize': '20px',
                                        },
                                    ),
                                ],
                                style={
                                    'backgroundColor': '#6dae3a',  # Cambia el color de fondo a #6dae3a
                                    'color': 'white',  # Cambia el color de las letras a blanco
                                    'borderTopLeftRadius': '0.25rem',  # Redondea la esquina superior izquierda
                                    'borderTopRightRadius': '0.25rem',  # Redondea la esquina superior derecha
                                },
                            ),
                        ],
                    ),
                    
                    html.Div([
                    html.Iframe(srcDoc=open('highchartmain2.html').read(), width='100%', height='290')
                    ],
                    
                    ),
                    dbc.Row([
                        dbc.Col([
                            html.P(f"{Disponibilidad2}%", style={'fontSize': '10px'}),
                            html.Div(style={
                            'height': '15px',
                            'marginRight': '22px',  # Agrega margen a la derecha de la línea para separarla de la siguiente línea
                            'marginLeft': '12px',
                        },
                        ),
                        ],
                        style={
                            'display': 'flex',
                            'alignItems': 'center',
                            'flexDirection': 'column',
                        },
                        ),
                        dbc.Col([
                            html.P(f"{rendimiento_global2}%", style={'fontSize': '10px'}),
                            html.Div(style={
                            'height': '15px',
                            'marginRight': '22px',  # Agrega margen a la derecha de la línea para separarla de la siguiente línea
                            'marginLeft': '12px',
                        },
                        ),
                        ],
                        style={
                            'display': 'flex',
                            'alignItems': 'center',
                            'flexDirection': 'column',
                        },
                        ),
                        dbc.Col([
                            html.P(f"{Calidad2}%", style={'fontSize': '10px'}),
                            html.Div(style={
                            'height': '15px',
                            'marginRight': '22px',  # Agrega margen a la derecha de la línea para separarla de la siguiente línea
                            'marginLeft': '12px',
                        },
                        ),
                        ],
                        style={
                            'display': 'flex',
                            'alignItems': 'center',
                            'flexDirection': 'column',
                        },
                        ),
                    ],
                        className="mb-0",  # Esto aplica una clase de Bootstrap para eliminar el margen inferior
                        style={'paddingBottom': '0'}  # Reducir el padding inferior a 0
                    ),
                    dbc.Row([
                        dbc.Col(
                            html.Div(style={
                            'height': '15px',
                            'background': '#00e272',
                            'borderRadius': '10px',
                            'marginRight': '22px',  # Agrega margen a la derecha de la línea para separarla de la siguiente línea
                            'marginLeft': '12px',
                        },
                        )),
                        dbc.Col(html.Div(style={
                            'height': '15px',
                            'background': '#544fc5',
                            'borderRadius': '10px',
                            'marginRight': '17px',  # Agrega margen a la derecha de la línea para separarla de la siguiente línea
                            'marginLeft': '17px',
                        })),
                        dbc.Col(html.Div(style={
                            'height': '15px',
                            'background': '#2cafff',
                            'borderRadius': '10px',
                            'marginLeft': '22px',
                            'marginRight': '12px',
                        })),
                    ]),
                    dbc.Row([
                        dbc.Col([
                            html.P("Disponibilidad", style={'fontSize': '10px'}),
                            html.Div(style={
                            'height': '15px',
                            'marginRight': '22px',  # Agrega margen a la derecha de la línea para separarla de la siguiente línea
                            'marginLeft': '12px',
                        },
                        ),
                        ],
                        style={
                            'display': 'flex',
                            'alignItems': 'center',
                            'flexDirection': 'column',
                        },
                        ),
                        dbc.Col([
                            html.P("Rendimiento", style={'fontSize': '10px'}),
                            html.Div(style={
                            'height': '15px',
                            'marginRight': '22px',  # Agrega margen a la derecha de la línea para separarla de la siguiente línea
                            'marginLeft': '12px',
                        },
                        ),
                        ],
                        style={
                            'display': 'flex',
                            'alignItems': 'center',
                            'flexDirection': 'column',
                        },
                        ),
                        dbc.Col([
                            html.P("Calidad", style={'fontSize': '10px'}),
                            html.Div(style={
                            'height': '15px',
                            'marginRight': '22px',  # Agrega margen a la derecha de la línea para separarla de la siguiente línea
                            'marginLeft': '12px',
                        },
                        ),
                        ],
                        style={
                            'display': 'flex',
                            'alignItems': 'center',
                            'flexDirection': 'column',
                        },
                        ),
                    ]),
                    html.Div([

                    ],
                    style={
                            'borderBottom': '2px solid grey ',  # Cambia a cualquier color que prefieras
                        },
                        ),
                    html.Br(),
                    html.Div(
                            [
                                dash_table.DataTable(
                                    columns=[
                                        {"name": "Producción", "id": "Producción"},
                                        {"name": "Ritmo", "id": "Ritmo"},
                                        {"name": "TFS", "id": "TFS"},
                                    ],
                                    data=resumen1.to_dict("records"),
                                    style_table={"overflowY": "auto"},
                                    style_header={
                                        "fontWeight": "bold",
                                        'backgroundColor': '#01766e',  # Cambia el color de fondo de la cabecera
                                        'color': 'white'  # Cambia el color del texto de la cabecera a blanco
                                    },
                                    style_cell={"textAlign": "left"},
                                    page_size=2,
                                    style_data_conditional=[
                                        {"if": {"row_index": "odd"}, "backgroundColor": "rgb(248, 248, 248)"}
                                    ]
                                )
                            ],
                            style={"overflowY": "auto"}
                        ),
                ],
                className="border rounded shadow-sm mb-3 d-flex flex-column",
                style={"height": "560px", "marginRight": "10px"},
                id='my-col',
                md=3,
            ),
            dbc.Col(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    html.Div(
                                        "Línea 3",
                                        className="py-2",
                                        style={
                                            'fontSize': '20px',
                                        },
                                    ),
                                ],
                                style={
                                    'backgroundColor': '#6dae3a',  # Cambia el color de fondo a #6dae3a
                                    'color': 'white',  # Cambia el color de las letras a blanco
                                    'borderTopLeftRadius': '0.25rem',  # Redondea la esquina superior izquierda
                                    'borderTopRightRadius': '0.25rem',  # Redondea la esquina superior derecha
                                },
                            ),
                        ],
                    ),
                    
                    html.Div([
                    html.Iframe(srcDoc=open('highchartmain3.html').read(), width='100%', height='290')
                    ],
                    
                    ),
                    dbc.Row([
                        dbc.Col([
                            html.P(f"{Disponibilidad3}%", style={'fontSize': '10px'}),
                            html.Div(style={
                            'height': '15px',
                            'marginRight': '22px',  # Agrega margen a la derecha de la línea para separarla de la siguiente línea
                            'marginLeft': '12px',
                            'marginBottom': '-10px',
                        },
                        ),
                        ],
                        style={
                            'display': 'flex',
                            'alignItems': 'center',
                            'flexDirection': 'column',
                        },
                        ),
                        dbc.Col([
                            html.P(f"{rendimiento_global3}%", style={'fontSize': '10px'}),
                            html.Div(style={
                            'height': '15px',
                            'marginRight': '22px',  # Agrega margen a la derecha de la línea para separarla de la siguiente línea
                            'marginLeft': '12px',
                        },
                        ),
                        ],
                        style={
                            'display': 'flex',
                            'alignItems': 'center',
                            'flexDirection': 'column',
                        },
                        ),
                        dbc.Col([
                            html.P(f"{Calidad3}%", style={'fontSize': '10px'}),
                            html.Div(style={
                            'height': '15px',
                            'marginRight': '22px',  # Agrega margen a la derecha de la línea para separarla de la siguiente línea
                            'marginLeft': '12px',
                        },
                        ),
                        ],
                        style={
                            'display': 'flex',
                            'alignItems': 'center',
                            'flexDirection': 'column',
                        },
                        ),
                    ],
                        className="mb-0",  # Esto aplica una clase de Bootstrap para eliminar el margen inferior
                        style={'paddingBottom': '0'}  # Reducir el padding inferior a 0
                    ),
                    dbc.Row([
                        dbc.Col(
                            html.Div(style={
                            'height': '15px',
                            'background': '#00e272',
                            'borderRadius': '10px',
                            'marginRight': '22px',  # Agrega margen a la derecha de la línea para separarla de la siguiente línea
                            'marginLeft': '12px',
                        },
                        )),
                        dbc.Col(html.Div(style={
                            'height': '15px',
                            'background': '#544fc5',
                            'borderRadius': '10px',
                            'marginRight': '17px',  # Agrega margen a la derecha de la línea para separarla de la siguiente línea
                            'marginLeft': '17px',
                        })),
                        dbc.Col(html.Div(style={
                            'height': '15px',
                            'background': '#2cafff',
                            'borderRadius': '10px',
                            'marginLeft': '22px',
                            'marginRight': '12px',
                        })),
                    ]),
                    dbc.Row([
                        dbc.Col([
                            html.P("Disponibilidad", style={'fontSize': '10px'}),
                            html.Div(style={
                            'height': '15px',
                            'marginRight': '22px',  # Agrega margen a la derecha de la línea para separarla de la siguiente línea
                            'marginLeft': '12px',
                        },
                        ),
                        ],
                        style={
                            'display': 'flex',
                            'alignItems': 'center',
                            'flexDirection': 'column',
                        },
                        ),
                        dbc.Col([
                            html.P("Rendimiento", style={'fontSize': '10px'}),
                            html.Div(style={
                            'height': '15px',
                            'marginRight': '22px',  # Agrega margen a la derecha de la línea para separarla de la siguiente línea
                            'marginLeft': '12px',
                        },
                        ),
                        ],
                        style={
                            'display': 'flex',
                            'alignItems': 'center',
                            'flexDirection': 'column',
                        },
                        ),
                        dbc.Col([
                            html.P("Calidad", style={'fontSize': '10px'}),
                            html.Div(style={
                            'height': '15px',
                            'marginRight': '22px',  # Agrega margen a la derecha de la línea para separarla de la siguiente línea
                            'marginLeft': '12px',
                        },
                        ),
                        ],
                        style={
                            'display': 'flex',
                            'alignItems': 'center',
                            'flexDirection': 'column',
                        },
                        ),
                    ]),
                    html.Div([

                    ],
                    style={
                            'borderBottom': '2px solid grey ',  # Cambia a cualquier color que prefieras
                        },
                        ),
                    html.Br(),
                    html.Div(
                            [
                                dash_table.DataTable(
                                    columns=[
                                        {"name": "Producción", "id": "Producción"},
                                        {"name": "Ritmo", "id": "Ritmo"},
                                        {"name": "TFS", "id": "TFS"},
                                    ],
                                    data=resumen1.to_dict("records"),
                                    style_table={"overflowY": "auto"},
                                    style_header={
                                        "fontWeight": "bold",
                                        'backgroundColor': '#01766e',  # Cambia el color de fondo de la cabecera
                                        'color': 'white'  # Cambia el color del texto de la cabecera a blanco
                                    },
                                    style_cell={"textAlign": "left"},
                                    page_size=2,
                                    style_data_conditional=[
                                        {"if": {"row_index": "odd"}, "backgroundColor": "rgb(248, 248, 248)"}
                                    ]
                                )
                            ],
                            style={"overflowY": "auto"}
                        ),
                ],
                className="border rounded shadow-sm mb-3 d-flex flex-column",
                style={"height": "560px", "marginRight": "10px"},
                id='my-col',
                md=3,
            ),
            dbc.Col(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    html.Div(
                                        "Línea 4",
                                        className="py-2",
                                        style={
                                            'fontSize': '20px',
                                        },
                                    ),
                                ],
                                style={
                                    'backgroundColor': '#6dae3a',  # Cambia el color de fondo a #6dae3a
                                    'color': 'white',  # Cambia el color de las letras a blanco
                                    'borderTopLeftRadius': '0.25rem',  # Redondea la esquina superior izquierda
                                    'borderTopRightRadius': '0.25rem',  # Redondea la esquina superior derecha
                                },
                            ),
                        ],
                    ),
                    
                    html.Div([
                    html.Iframe(srcDoc=open('highchartmain4.html').read(), width='100%', height='290')
                    ],
                    
                    ),
                    dbc.Row([
                        dbc.Col([
                            html.P(f"{Disponibilidad4}%", style={'fontSize': '10px'}),
                            html.Div(style={
                            'height': '15px',
                            'marginRight': '22px',  # Agrega margen a la derecha de la línea para separarla de la siguiente línea
                            'marginLeft': '12px',
                        },
                        ),
                        ],
                        style={
                            'display': 'flex',
                            'alignItems': 'center',
                            'flexDirection': 'column',
                        },
                        ),
                        dbc.Col([
                            html.P(f"{rendimiento_global4}%", style={'fontSize': '10px'}),
                            html.Div(style={
                            'height': '15px',
                            'marginRight': '22px',  # Agrega margen a la derecha de la línea para separarla de la siguiente línea
                            'marginLeft': '12px',
                        },
                        ),
                        ],
                        style={
                            'display': 'flex',
                            'alignItems': 'center',
                            'flexDirection': 'column',
                        },
                        ),
                        dbc.Col([
                            html.P(f"{Calidad4}%", style={'fontSize': '10px'}),
                            html.Div(style={
                            'height': '15px',
                            'marginRight': '22px',  # Agrega margen a la derecha de la línea para separarla de la siguiente línea
                            'marginLeft': '12px',
                        },
                        ),
                        ],
                        style={
                            'display': 'flex',
                            'alignItems': 'center',
                            'flexDirection': 'column',
                        },
                        ),
                    ],
                        className="mb-0",  # Esto aplica una clase de Bootstrap para eliminar el margen inferior
                        style={'paddingBottom': '0'}  # Reducir el padding inferior a 0
                    ),
                    dbc.Row([
                        dbc.Col(
                            html.Div(style={
                            'height': '15px',
                            'background': '#00e272',
                            'borderRadius': '10px',
                            'marginRight': '22px',  # Agrega margen a la derecha de la línea para separarla de la siguiente línea
                            'marginLeft': '12px',
                        },
                        )),
                        dbc.Col(html.Div(style={
                            'height': '15px',
                            'background': '#544fc5',
                            'borderRadius': '10px',
                            'marginRight': '17px',  # Agrega margen a la derecha de la línea para separarla de la siguiente línea
                            'marginLeft': '17px',
                        })),
                        dbc.Col(html.Div(style={
                            'height': '15px',
                            'background': '#2cafff',
                            'borderRadius': '10px',
                            'marginLeft': '22px',
                            'marginRight': '12px',
                        })),
                    ]),
                    dbc.Row([
                        dbc.Col([
                            html.P("Disponibilidad", style={'fontSize': '10px'}),
                            html.Div(style={
                            'height': '15px',
                            'marginRight': '22px',  # Agrega margen a la derecha de la línea para separarla de la siguiente línea
                            'marginLeft': '12px',
                        },
                        ),
                        ],
                        style={
                            'display': 'flex',
                            'alignItems': 'center',
                            'flexDirection': 'column',
                        },
                        ),
                        dbc.Col([
                            html.P("Rendimiento", style={'fontSize': '10px'}),
                            html.Div(style={
                            'height': '15px',
                            'marginRight': '22px',  # Agrega margen a la derecha de la línea para separarla de la siguiente línea
                            'marginLeft': '12px',
                        },
                        ),
                        ],
                        style={
                            'display': 'flex',
                            'alignItems': 'center',
                            'flexDirection': 'column',
                        },
                        ),
                        dbc.Col([
                            html.P("Calidad", style={'fontSize': '10px'}),
                            html.Div(style={
                            'height': '15px',
                            'marginRight': '22px',  # Agrega margen a la derecha de la línea para separarla de la siguiente línea
                            'marginLeft': '12px',
                        },
                        ),
                        ],
                        style={
                            'display': 'flex',
                            'alignItems': 'center',
                            'flexDirection': 'column',
                        },
                        ),
                    ]),
                    html.Div([

                    ],
                    style={
                            'borderBottom': '2px solid grey ',  # Cambia a cualquier color que prefieras
                        },
                        ),
                    html.Br(),
                    html.Div(
                            [
                                dash_table.DataTable(
                                    columns=[
                                        {"name": "Producción", "id": "Producción"},
                                        {"name": "Ritmo", "id": "Ritmo"},
                                        {"name": "TFS", "id": "TFS"},
                                    ],
                                    data=resumen1.to_dict("records"),
                                    style_table={"overflowY": "auto"},
                                    style_header={
                                        "fontWeight": "bold",
                                        'backgroundColor': '#01766e',  # Cambia el color de fondo de la cabecera
                                        'color': 'white'  # Cambia el color del texto de la cabecera a blanco
                                    },
                                    style_cell={"textAlign": "left"},
                                    page_size=2,
                                    style_data_conditional=[
                                        {"if": {"row_index": "odd"}, "backgroundColor": "rgb(248, 248, 248)"}
                                    ]
                                )
                            ],
                            style={"overflowY": "auto"}
                        ),
                ],
                className="border rounded shadow-sm mb-3 d-flex flex-column",
                style={"height": "560px", "marginRight": "10px"},
                id='my-col',
                md=3,
            ),
            
        ],
        ),
    ],
    style={"padding-top": "10px", "padding-right": "80px", "padding-bottom": "10px", "padding-left": "80px"}
)



# Iniciar la aplicación
if __name__ == "__main__":
    app.run_server(debug=True, port=8050)