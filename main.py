# importo las bibliotecas necesarias
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
from flask_cors import CORS

# cargo la data disponible
l1 = pd.read_csv("C:/Users/Pablo Iturra/Downloads/l1.csv")
l2 = pd.read_csv("C:/Users/Pablo Iturra/Downloads/l2.csv")
l3 = pd.read_csv("C:/Users/Pablo Iturra/Downloads/l3 (2).csv")
l4 = pd.read_csv("C:/Users/Pablo Iturra/Downloads/l4.csv")

# Los datos vienen en un formato de fecha no compatible
meses_ingles = {
    'ene': 'Jan', 'feb': 'Feb', 'mar': 'Mar', 'abr': 'Apr',
    'may': 'May', 'jun': 'Jun', 'jul': 'Jul', 'ago': 'Aug',
    'sep': 'Sep', 'sept': 'Sep', 'oct': 'Oct', 'nov': 'Nov', 'dic': 'Dec'
}

# Reemplazar abreviaturas de meses en español por nombres de meses en inglés
l1['fecha'] = l1['fecha'].str.replace(r'(\d+)-([a-z]+)-(\d+)', lambda x: f"{x.group(1)}-{meses_ingles[x.group(2)]}-{x.group(3)}", regex=True)
# Convierte la columna de fechas a formato DateTime
l1['fecha'] = pd.to_datetime(l1['fecha'], format='%d-%b-%y %H:%M:%S')
# Calcula la diferencia en horas entre las fechas usando el método 'diff'
l1['duracion'] = l1['fecha'].diff().dt.total_seconds() / 3600
# Suma las horas en condición 0 y las horas en condición 1
horas_condicion_0 = l1[l1['21027110Q.CIN'] == 0]['duracion'].sum()
horas_condicion_1 = l1[l1['21027110Q.CIN'] == 1]['duracion'].sum()
# Calcula el total de horas en la columna 'duracion'
horas_totales = l1['duracion'].sum()
# Disponibilidad calculada (horas de funcionamiento)/(horas esperadas)
Disponibilidad1 = (round(((horas_condicion_1)/horas_totales)*100,1))

# Reemplazar abreviaturas de meses en español por nombres de meses en inglés
l2['fecha'] = l2['fecha'].str.replace(r'(\d+)-([a-z]+)-(\d+)', lambda x: f"{x.group(1)}-{meses_ingles[x.group(2)]}-{x.group(3)}", regex=True)
# Convierte la columna de fechas a formato DateTime
l2['fecha'] = pd.to_datetime(l2['fecha'], format='%d-%b-%y %H:%M:%S')
# Calcula la diferencia en horas entre las fechas usando el método 'diff'
l2['duracion'] = l2['fecha'].diff().dt.total_seconds() / 3600
# Suma las horas en condición 0 y las horas en condición 1
horas_condicion_02 = l2[l2['21027210Q.CIN'] == 0]['duracion'].sum()
horas_condicion_12 = l2[l2['21027210Q.CIN'] == 1]['duracion'].sum()
# Calcula el total de horas en la columna 'duracion'
horas_totales2 = l2['duracion'].sum()
# Disponibilidad calculada (horas de funcionamiento)/(horas esperadas)
Disponibilidad2 = round(((horas_condicion_12)/horas_totales2)*100,1)

# Reemplazar abreviaturas de meses en español por nombres de meses en inglés
l3['fecha'] = l3['fecha'].str.replace(r'(\d+)-([a-z]+)-(\d+)', lambda x: f"{x.group(1)}-{meses_ingles[x.group(2)]}-{x.group(3)}", regex=True)
# Convierte la columna de fechas a formato DateTime
l3['fecha'] = pd.to_datetime(l3['fecha'], format='%d-%b-%y %H:%M:%S')
# Calcula la diferencia en horas entre las fechas usando el método 'diff'
l3['duracion'] = l3['fecha'].diff().dt.total_seconds() / 3600
# Suma las horas en condición 0 y las horas en condición 1
horas_condicion_03 = l3[l3['21027210Q.CIN'] == 0]['duracion'].sum()
horas_condicion_13 = l3[l3['21027210Q.CIN'] == 1]['duracion'].sum()
# Calcula el total de horas en la columna 'duracion'
horas_totales3 = l3['duracion'].sum()
# Disponibilidad calculada (horas de funcionamiento)/(horas esperadas)
Disponibilidad3 = round(((horas_condicion_13)/horas_totales3)*100,1)

# Reemplazar abreviaturas de meses en español por nombres de meses en inglés
l4['fecha'] = l4['fecha'].str.replace(r'(\d+)-([a-z]+)-(\d+)', lambda x: f"{x.group(1)}-{meses_ingles[x.group(2)]}-{x.group(3)}", regex=True)
# Convierte la columna de fechas a formato DateTime
l4['fecha'] = pd.to_datetime(l4['fecha'], format='%d-%b-%y %H:%M:%S')
# Calcula la diferencia en horas entre las fechas usando el método 'diff'
l4['duracion'] = l4['fecha'].diff().dt.total_seconds() / 3600
# Suma las horas en condición 0 y las horas en condición 1
horas_condicion_04 = l4[l4['CHIPER4_FUNC'] == 0]['duracion'].sum()
horas_condicion_14 = l4[l4['CHIPER4_FUNC'] == 1]['duracion'].sum()
# Calcula el total de horas en la columna 'duracion'
horas_totales4 = l4['duracion'].sum()
# Disponibilidad calculada (horas de funcionamiento)/(horas esperadas)
Disponibilidad4 = (round(((horas_condicion_04)/horas_totales4)*100,1))

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
# Separo por línea 
rendl1 = rend[rend['TipoMvto'].str.contains('línea 1', case=False)]
# Hago un resample por día
rendl1_diario1 = rendl1.resample('D', on='FecIngreso')['M3SSC_Recepcion'].sum().round(0)
# sumo los rendimientos diarios
suma_rendimientos_diarios1 = rendl1_diario1.sum()
# Cantidad total de días
total_dias1 = rendl1_diario1.count()
# Ritmo por hora ideal o esperado
ritmo_esperado1 = 160
# disponibilidad esperada por línea
disp_esperada1 = 0.7
# Rendimiento diario esperado según ritmo y disponibilidad esperados
rendimiento_diario_esperado1 = int(ritmo_esperado1*disp_esperada1*24)
# Cálculo del rendimiento global
rendimiento_global1 = round((suma_rendimientos_diarios1 / (rendimiento_diario_esperado1 * total_dias1))*100,1)


rendl2 = rend[rend['TipoMvto'].str.contains('línea 2', case=False)]
# Hago un resample por día
rendl1_diario2 = rendl2.resample('D', on='FecIngreso')['M3SSC_Recepcion'].sum().round(0)
# sumo los rendimientos diarios
suma_rendimientos_diarios2 = rendl1_diario2.sum()
# Cantidad total de días
total_dias2 = rendl1_diario2.count()
# Ritmo por hora ideal o esperado
ritmo_esperado2 = 219
# disponibilidad esperada por línea
disp_esperada2 = 0.7
# Rendimiento diario esperado según ritmo y disponibilidad esperados
rendimiento_diario_esperado2 = int(ritmo_esperado2*disp_esperada2*24)
# Cálculo del rendimiento global
rendimiento_global2 = round((suma_rendimientos_diarios2 / (rendimiento_diario_esperado2 * total_dias2))*100,1)

rendl3 = rend[rend['TipoMvto'].str.contains('línea 3', case=False)]
# Hago un resample por día
rendl1_diario3 = rendl3.resample('D', on='FecIngreso')['M3SSC_Recepcion'].sum().round(0)
# sumo los rendimientos diarios
suma_rendimientos_diarios3 = rendl1_diario3.sum()
# Cantidad total de días
total_dias3 = rendl1_diario3.count()
# Ritmo por hora ideal o esperado
ritmo_esperado3 = 165
# disponibilidad esperada por línea
disp_esperada3 = 0.7
# Rendimiento diario esperado según ritmo y disponibilidad esperados
rendimiento_diario_esperado3 = int(ritmo_esperado3*disp_esperada3*24)
# Cálculo del rendimiento global
rendimiento_global3 = round((suma_rendimientos_diarios3 / (rendimiento_diario_esperado3 * total_dias3))*100,1)

rendl4 = rend[rend['TipoMvto'].str.contains('línea 4', case=False)]
# Hago un resample por día
rendl1_diario4 = rendl4.resample('D', on='FecIngreso')['M3SSC_Recepcion'].sum().round(0)
# sumo los rendimientos diarios
suma_rendimientos_diarios4 = rendl1_diario4.sum()
# Cantidad total de días
total_dias4 = rendl1_diario4.count()
# Ritmo por hora ideal o esperado
ritmo_esperado4 = 190
# disponibilidad esperada por línea
disp_esperada4 = 0.7
# Rendimiento diario esperado según ritmo y disponibilidad esperados
rendimiento_diario_esperado4 = int(ritmo_esperado4*disp_esperada4*24)
# Cálculo del rendimiento global
rendimiento_global4 = round((suma_rendimientos_diarios4 / (rendimiento_diario_esperado4 * total_dias4))*100,1)

# Asegurarse de que el índice sea de tipo datetime
rendl1_diario1.index = pd.to_datetime(rendl1_diario1.index)
# Convertir el índice a una marca de tiempo en milisegundos
rendl1_diario1.index = rendl1_diario1.index.astype(int) // 10**6
# Reemplazar el DataFrame por una lista de listas
rendl1_diario1 = list(map(list, rendl1_diario1.reset_index().values))

# Asegurarse de que el índice sea de tipo datetime
rendl1_diario2.index = pd.to_datetime(rendl1_diario2.index)
# Convertir el índice a una marca de tiempo en milisegundos
rendl1_diario2.index = rendl1_diario2.index.astype(int) // 10**6
# Reemplazar el DataFrame por una lista de listas
rendl1_diario2 = list(map(list, rendl1_diario2.reset_index().values))

# Asegurarse de que el índice sea de tipo datetime
rendl1_diario3.index = pd.to_datetime(rendl1_diario3.index)
# Convertir el índice a una marca de tiempo en milisegundos
rendl1_diario3.index = rendl1_diario3.index.astype(int) // 10**6
# Reemplazar el DataFrame por una lista de listas
rendl1_diario3 = list(map(list, rendl1_diario3.reset_index().values))

# Asegurarse de que el índice sea de tipo datetime
rendl1_diario4.index = pd.to_datetime(rendl1_diario4.index)
# Convertir el índice a una marca de tiempo en milisegundos
rendl1_diario4.index = rendl1_diario4.index.astype(int) // 10**6
# Reemplazar el DataFrame por una lista de listas
rendl1_diario4 = list(map(list, rendl1_diario4.reset_index().values))



cal1 = pd.read_csv("C:/Users/Pablo Iturra/Downloads/renl1.csv")
Calidad1 = round(cal1['Aceptado '].mean(),1)

cal2 = pd.read_csv("C:/Users/Pablo Iturra/Downloads/renl2.csv")
Calidad2 = round(cal2['Aceptado .1'].mean(),1)

cal3 = pd.read_csv("C:/Users/Pablo Iturra/Downloads/renl3.csv")
Calidad3 = round(cal3['Aceptado .2'].mean(),1)

cal4 = pd.read_csv("C:/Users/Pablo Iturra/Downloads/renl4.csv")
Calidad4 = round(cal4['Aceptado .3'].mean(),1)

# Leer la hoja del archivo Excel asegurándose que 'Duracion' se lea como cadena
df1 = pd.read_excel("C:/Users/Pablo Iturra/Downloads/TFS MADERA 2023.xlsx", sheet_name="PML1", dtype={'Duracion': str})
# Seleccionar sólo las columnas "Duracion" y "Responsable"
df1 = df1[["Duracion", "Responsable"]]
# Separar las horas y los minutos y convertir a horas
df1['Duracion'] = df1['Duracion'].str.split(':').apply(lambda x: int(x[0]) + int(x[1])/60)
# Agrupar por "Responsable" y sumar "Duracion"
df_grouped1 = df1.groupby("Responsable")["Duracion"].sum()
df_grouped1 = df_grouped1.reset_index().to_dict('records')


# Leer la hoja del archivo Excel asegurándose que 'Duracion' se lea como cadena
df2 = pd.read_excel("C:/Users/Pablo Iturra/Downloads/TFS MADERA 2023.xlsx", sheet_name="PML2", dtype={'Duracion': str})
# Seleccionar sólo las columnas "Duracion" y "Responsable"
df2 = df2[["Duracion", "Responsable"]]
# Separar las horas y los minutos y convertir a horas
df2['Duracion'] = df2['Duracion'].str.split(':').apply(lambda x: int(x[0]) + int(x[1])/60)
# Agrupar por "Responsable" y sumar "Duracion"
df_grouped2 = df2.groupby("Responsable")["Duracion"].sum()
df_grouped2 = df_grouped2.reset_index().to_dict('records')

# Leer la hoja del archivo Excel asegurándose que 'Duracion' se lea como cadena
df3 = pd.read_excel("C:/Users/Pablo Iturra/Downloads/TFS MADERA 2023.xlsx", sheet_name="PML3", dtype={'Duracion': str})
# Seleccionar sólo las columnas "Duracion" y "Responsable"
df3 = df3[["Duracion", "Responsable"]]
# Separar las horas y los minutos y convertir a horas
df3['Duracion'] = df3['Duracion'].str.split(':').apply(lambda x: int(x[0]) + int(x[1])/60)
# Agrupar por "Responsable" y sumar "Duracion"
df_grouped3 = df3.groupby("Responsable")["Duracion"].sum()
df_grouped3 = df_grouped3.reset_index().to_dict('records')

# Leer la hoja del archivo Excel asegurándose que 'Duracion' se lea como cadena
df4 = pd.read_excel("C:/Users/Pablo Iturra/Downloads/TFS MADERA 2023.xlsx", sheet_name="PML4", dtype={'Duracion': str})
# Seleccionar sólo las columnas "Duracion" y "Responsable"
df4 = df4[["Duracion", "Responsable"]]
# Separar las horas y los minutos y convertir a horas
df4['Duracion'] = df4['Duracion'].str.split(':').apply(lambda x: int(x[0]) + int(x[1])/60)
# Agrupar por "Responsable" y sumar "Duracion"
df_grouped4 = df4.groupby("Responsable")["Duracion"].sum()
df_grouped4 = df_grouped4.reset_index().to_dict('records')


OEE1 = round(((horas_condicion_1)/horas_totales)*((suma_rendimientos_diarios1 / (rendimiento_diario_esperado1 * total_dias1)))*(Calidad1/100)*100,1)

OEE2 = round(((horas_condicion_12)/horas_totales2)*(suma_rendimientos_diarios2 / (rendimiento_diario_esperado2 * total_dias2))*(Calidad2/100)*100,1)

OEE3 = round(((horas_condicion_13)/horas_totales3)*(suma_rendimientos_diarios3 / (rendimiento_diario_esperado3 * total_dias3))*(Calidad3/100)*100,1)

OEE4 = round(((horas_condicion_04)/horas_totales4)*(suma_rendimientos_diarios4 / (rendimiento_diario_esperado4 * total_dias4))*(Calidad4/100)*100,1)

# Inicializar la aplicación Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server
CORS(server, resources={r"/get_data/*": {"origins": "*"}})
@server.route('/get_data', methods=['GET'])
def get_data():
    return jsonify({
        'Disponibilidad1': Disponibilidad1,
        'Calidad1': Calidad1,
        'rendimiento_global1': rendimiento_global1,
        'Disponibilidad2': Disponibilidad2,
        'Calidad2': Calidad2,
        'rendimiento_global2': rendimiento_global2,
        'Disponibilidad3': Disponibilidad3,
        'Calidad3': Calidad3,
        'rendimiento_global3': rendimiento_global3,
        'Disponibilidad4': Disponibilidad4,
        'Calidad4': Calidad4,
        'rendimiento_global4': rendimiento_global4,
        'rendl1_diario1': rendl1_diario1,
        'rendl1_diario2': rendl1_diario2,
        'rendl1_diario3': rendl1_diario3,
        'rendl1_diario4': rendl1_diario4,
        'df_grouped1': df_grouped1,
        'df_grouped2': df_grouped2,
        'df_grouped3': df_grouped3,
        'df_grouped4': df_grouped4,
        
    })

app.layout = html.Div(
    children=[
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Div(
                                            f"Línea 1",
                                            className="py-1",
                                            style={
                                                'fontSize': '16px',
                                            },
                                        ),
                                    ],
                                    
                                    style={
                                        'color': 'white',  # Cambia el color de las letras a blanco
                                        'borderTopLeftRadius': '0.25rem',  # Redondea la esquina superior izquierda
                                    },
                                ),
                                dbc.Col(
                                    [
                                        html.Div(
                                            [
                                                html.Strong(
                                                    f"OEE: {OEE1}%",
                                                ),
                                            ],
                                            className="py-1",
                                            style={
                                                'fontSize': '16px',
                                            },
                                        ),
                                    ],
                                    
                                    style={
                                        'color': 'white',  # Cambia el color de las letras a blanco
                                        'borderTopRightRadius': '0.25rem',  # Redondea la esquina superior derecha
                                        'textAlign': 'right',
                                    },
                                ),
                            ],
                            style={
                                'backgroundColor': '#6dae3a',  # Cambia el color de fondo a #6dae3a
                                'borderTopRightRadius': '0.25rem',  # Redondea la esquina superior derecha
                                'borderTopLeftRadius': '0.25rem',  # Redondea la esquina superior izquierda
                            },
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    [
                                                        html.Div(
                                                            [
                                                                html.Iframe(
                                                                    srcDoc=open('highchart.html').read(), 
                                                                    width='100%', 
                                                                    height='220',
                                                                    style={"marginLeft": "-30px", "marginTop": "-10px"},
                                                                    )
                                                            ],
                                                        ),
                                                    ],
                                                    md=8,
                                                ),
                                                dbc.Col(
                                                    [
                                                        dbc.Row(
                                                            [
                                                                html.Div(
                                                                    [
                                                                        html.P(
                                                                            "Disponibilidad", 
                                                                            style={'font-size': '10px',
                                                                                'margin-bottom': '0',
                                                                                'margin-top': '1'
                                                                                }
                                                                            ),
                                                                        html.P(
                                                                            f"{Disponibilidad1}%",
                                                                            style={
                                                                                'font-size': '10px',
                                                                                'margin-top': '0',
                                                                                'font-weight': 'bold',
                                                                                'margin-bottom': '0px'
                                                                                },
                                                                            ),
                                                                        html.Div(
                                                                            style={
                                                                                'height': '12px',
                                                                                'width': '35px',
                                                                                'background-color': '#00e272',
                                                                                'border-radius': '5px',
                                                                                'margin-top': '0px'
                                                                                }
                                                                            )
                                                                    ],
                                                                    style={
                                                                        'display': 'inline-block',
                                                                        }
                                                                ),
                                                            ],
                                                            style={
                                                                'margin-top': '5px',
                                                                'margin-bottom': '5px'
                                                                }
                                                        ),
                                                        dbc.Row(
                                                            [
                                                                html.Div(
                                                                    [
                                                                        html.P(
                                                                            "Rendimiento", 
                                                                            style={'font-size': '10px',
                                                                                'margin-bottom': '0',
                                                                                'margin-top': '1'
                                                                                }
                                                                            ),
                                                                        html.P(
                                                                            f"{rendimiento_global1}%",
                                                                            style={
                                                                                'font-size': '10px',
                                                                                'margin-top': '0',
                                                                                'font-weight': 'bold',
                                                                                'margin-bottom': '0'
                                                                                },
                                                                            ),
                                                                        html.Div(
                                                                            style={
                                                                                'height': '12px',
                                                                                'width': '35px', 
                                                                                'background-color': '#544fc5',
                                                                                'border-radius': '5px',
                                                                                'margin-top': '0'
                                                                                }
                                                                            )
                                                                    ],
                                                                    style={
                                                                        'display': 'inline-block'
                                                                        }
                                                                ),
                                                            ],
                                                            style={
                                                                'margin-top': '5px',
                                                                'margin-bottom': '5px'
                                                                }
                                                        ),
                                                        dbc.Row(
                                                            [
                                                                html.Div(
                                                                    [
                                                                        html.P(
                                                                            "Calidad", 
                                                                            style={'font-size': '10px',
                                                                                'margin-bottom': '0',
                                                                                'margin-top': '1'
                                                                                }
                                                                            ),
                                                                        html.P(
                                                                            f"{Calidad1}%",
                                                                            style={
                                                                                'font-size': '10px',
                                                                                'margin-top': '0',
                                                                                'font-weight': 'bold',
                                                                                'margin-bottom': '0'
                                                                                },
                                                                            ),
                                                                        html.Div(
                                                                            style={
                                                                                'height': '12px',
                                                                                'width': '35px', 
                                                                                'background-color': '#2cafff',
                                                                                'border-radius': '5px',
                                                                                'margin-top': '0'
                                                                                }
                                                                            )
                                                                    ],
                                                                    style={
                                                                        'display': 'inline-block'
                                                                        }
                                                                ),
                                                            ],
                                                            style={
                                                                'margin-top': '5px',
                                                                'margin-bottom': '5px'
                                                                }
                                                        ),
                                                    ],
                                                    md=3,
                                                ),
                                                dbc.Col(
                                                    [
                                                        
                                                    ],
                                                    md=1
                                                ),

                                            ],
                                        ),
                                    ],
                                    className="border rounded shadow-sm d-flex flex-column",
                                    style={
                                        "height": "150px", 
                                        "marginRight": "1px", 
                                        'marginBottom': '1px'
                                        },
                                ),
                                dbc.Col(
                                    [
                                        html.Div(
                                            [
                                                html.Iframe(
                                                    srcDoc=open('areachart.html').read(), 
                                                    width='120%', 
                                                    height='300',
                                                    style={"marginLeft": "-30px", "marginTop": "-10px"},
                                                )
                                            ],
                                        )
                                    ],
                                    className="border rounded shadow-sm d-flex flex-column justify-content-start",
                                    style={
                                        "height": "150px", 
                                        "marginLeft": "1px",
                                        'marginBottom': '1px',
                                        },
                                ),
                            ],
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Div(
                                            [
                                                html.Iframe(
                                                    srcDoc=open('barstackchart.html').read(), 
                                                    width='120%', 
                                                    height='200',
                                                    style={"marginLeft": "-30px", "marginTop": "-10px"},
                                                )
                                            ],
                                        ),
                                    ],
                                    className="border rounded shadow-sm d-flex flex-column justify-content-start",
                                    style={
                                        "height": "150px", 
                                        "marginRight": "1px",
                                        'marginBottom': '1px',
                                        'marginTop': '1px',
                                        },
                                ),
                                dbc.Col(
                                    [
                                        html.Div(
                                            [
                                                html.Iframe(
                                                    srcDoc=open('barchart.html').read(), 
                                                    width='120%', 
                                                    height='180',
                                                    style={"marginLeft": "-30px", "marginTop": "-10px"},
                                                )
                                            ],
                                        ),
                                    ],
                                    className="border rounded shadow-sm d-flex flex-column justify-content-start",
                                    style={
                                        "height": "150px", 
                                        "marginLeft": "1px",
                                        'marginBottom': '1px',
                                        'marginTop': '1px',
                                        },
                                ),
                            ],
                        ),
                    ],
                    className="border rounded shadow-sm d-flex flex-column justify-content-start",
                    style={
                        'marginBottom': '5px',
                        'marginRight': '5px',
                        'backgroundColor': '#FFFFFF'
                    },
                ),
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Div(
                                            f"Línea 2",
                                            className="py-1",
                                            style={
                                                'fontSize': '16px',
                                            },
                                        ),
                                    ],
                                    
                                    style={
                                        'backgroundColor': '#6dae3a',  # Cambia el color de fondo a #6dae3a
                                        'color': 'white',  # Cambia el color de las letras a blanco
                                        'borderTopLeftRadius': '0.25rem',  # Redondea la esquina superior izquierda
                                    },
                                ),
                                dbc.Col(
                                    [
                                        html.Div(
                                            [
                                                html.Strong(
                                                    f"OEE: {OEE2}%",
                                                ),
                                            ],
                                            className="py-1",
                                            style={
                                                'fontSize': '16px',
                                            },
                                        ),
                                    ],
                                    
                                    style={
                                        'backgroundColor': '#6dae3a',  # Cambia el color de fondo a #6dae3a
                                        'color': 'white',  # Cambia el color de las letras a blanco
                                        'borderTopRightRadius': '0.25rem',  # Redondea la esquina superior derecha
                                        'textAlign': 'right',
                                    },
                                ),
                            ],
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    [
                                                        html.Div(
                                                            [
                                                                html.Iframe(
                                                                    srcDoc=open('highchart2.html').read(), 
                                                                    width='100%', 
                                                                    height='220',
                                                                    style={"marginLeft": "-30px", "marginTop": "-10px"},
                                                                    )
                                                            ],
                                                        ),
                                                    ],
                                                    md=8
                                                ),
                                                dbc.Col(
                                                    [
                                                        dbc.Row(
                                                            [
                                                                html.Div(
                                                                    [
                                                                        html.P(
                                                                            "Disponibilidad", 
                                                                            style={'font-size': '10px',
                                                                                'margin-bottom': '0',
                                                                                'margin-top': '1'
                                                                                }
                                                                            ),
                                                                        html.P(
                                                                            f"{Disponibilidad2}%",
                                                                            style={
                                                                                'font-size': '10px',
                                                                                'margin-top': '0',
                                                                                'font-weight': 'bold',
                                                                                'margin-bottom': '0px'
                                                                                },
                                                                            ),
                                                                        html.Div(
                                                                            style={
                                                                                'height': '12px',
                                                                                'width': '35px',
                                                                                'background-color': '#00e272',
                                                                                'border-radius': '5px',
                                                                                'margin-top': '0px'
                                                                                }
                                                                            )
                                                                    ],
                                                                    style={
                                                                        'display': 'inline-block',
                                                                        }
                                                                ),
                                                            ],
                                                            style={
                                                                'margin-top': '5px',
                                                                'margin-bottom': '5px'
                                                                }
                                                        ),
                                                        dbc.Row(
                                                            [
                                                                html.Div(
                                                                    [
                                                                        html.P(
                                                                            "Rendimiento", 
                                                                            style={'font-size': '10px',
                                                                                'margin-bottom': '0',
                                                                                'margin-top': '1'
                                                                                }
                                                                            ),
                                                                        html.P(
                                                                            f"{rendimiento_global2}%",
                                                                            style={
                                                                                'font-size': '10px',
                                                                                'margin-top': '0',
                                                                                'font-weight': 'bold',
                                                                                'margin-bottom': '0'
                                                                                },
                                                                            ),
                                                                        html.Div(
                                                                            style={
                                                                                'height': '12px',
                                                                                'width': '35px', 
                                                                                'background-color': '#544fc5',
                                                                                'border-radius': '5px',
                                                                                'margin-top': '0'
                                                                                }
                                                                            )
                                                                    ],
                                                                    style={
                                                                        'display': 'inline-block'
                                                                        }
                                                                ),
                                                            ],
                                                            style={
                                                                'margin-top': '5px',
                                                                'margin-bottom': '5px'
                                                                }
                                                        ),
                                                        dbc.Row(
                                                            [
                                                                html.Div(
                                                                    [
                                                                        html.P(
                                                                            "Calidad", 
                                                                            style={'font-size': '10px',
                                                                                'margin-bottom': '0',
                                                                                'margin-top': '1'
                                                                                }
                                                                            ),
                                                                        html.P(
                                                                            f"{Calidad2}%",
                                                                            style={
                                                                                'font-size': '10px',
                                                                                'margin-top': '0',
                                                                                'font-weight': 'bold',
                                                                                'margin-bottom': '0'
                                                                                },
                                                                            ),
                                                                        html.Div(
                                                                            style={
                                                                                'height': '12px',
                                                                                'width': '35px', 
                                                                                'background-color': '#2cafff',
                                                                                'border-radius': '5px',
                                                                                'margin-top': '0'
                                                                                }
                                                                            )
                                                                    ],
                                                                    style={
                                                                        'display': 'inline-block'
                                                                        }
                                                                ),
                                                            ],
                                                            style={
                                                                'margin-top': '5px',
                                                                'margin-bottom': '5px'
                                                                }
                                                        ),
                                                    ],
                                                    md=3
                                                ),
                                                dbc.Col(
                                                    [
                                                        
                                                    ],
                                                    md=1
                                                ),

                                            ],
                                        ),
                                    ],
                                    className="border rounded shadow-sm d-flex flex-column",
                                    style={
                                        "height": "150px", 
                                        "marginRight": "1px", 
                                        'marginBottom': '1px'
                                        },
                                ),
                                dbc.Col(
                                    [
                                        html.Div(
                                            [
                                                html.Iframe(
                                                    srcDoc=open('areachart2.html').read(), 
                                                    width='120%', 
                                                    height='300',
                                                    style={"marginLeft": "-30px", "marginTop": "-10px"},
                                                )
                                            ],
                                        )
                                    ],
                                    className="border rounded shadow-sm d-flex flex-column justify-content-start",
                                    style={
                                        "height": "150px", 
                                        "marginLeft": "1px",
                                        'marginBottom': '1px',
                                        },
                                ),
                            ],
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Div(
                                            [
                                                html.Iframe(
                                                    srcDoc=open('barstackchart.html').read(), 
                                                    width='120%', 
                                                    height='200',
                                                    style={"marginLeft": "-30px", "marginTop": "-10px"},
                                                )
                                            ],
                                        ),
                                    ],
                                    className="border rounded shadow-sm d-flex flex-column justify-content-start",
                                    style={
                                        "height": "150px", 
                                        "marginRight": "1px",
                                        'marginBottom': '1px',
                                        'marginTop': '1px',
                                        },
                                ),
                                dbc.Col(
                                    [
                                        html.Div(
                                            [
                                                html.Iframe(
                                                    srcDoc=open('barchart2.html').read(), 
                                                    width='120%', 
                                                    height='180',
                                                    style={"marginLeft": "-30px", "marginTop": "-10px"},
                                                )
                                            ],
                                        ),
                                    ],
                                    className="border rounded shadow-sm d-flex flex-column justify-content-start",
                                    style={
                                        "height": "150px", 
                                        "marginLeft": "1px",
                                        'marginBottom': '1px',
                                        'marginTop': '1px',
                                        },
                                ),
                            ],
                        ),
                    ],
                    className="border rounded shadow-sm d-flex flex-column justify-content-start",
                    style={
                        'marginBottom': '5px',
                        'marginLeft': '5px',
                        'backgroundColor': '#FFFFFF'
                    },
                ),
            ],
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Div(
                                            f"Línea 3",
                                            className="py-1",
                                            style={
                                                'fontSize': '16px',
                                            },
                                        ),
                                    ],
                                    
                                    style={
                                        'backgroundColor': '#6dae3a',  # Cambia el color de fondo a #6dae3a
                                        'color': 'white',  # Cambia el color de las letras a blanco
                                        'borderTopLeftRadius': '0.25rem',  # Redondea la esquina superior izquierda
                                    },
                                ),
                                dbc.Col(
                                    [
                                        html.Div(
                                            [
                                                html.Strong(
                                                    f"OEE: {OEE3}%",
                                                ),
                                            ],
                                            className="py-1",
                                            style={
                                                'fontSize': '16px',
                                            },
                                        ),
                                    ],
                                    
                                    style={
                                        'backgroundColor': '#6dae3a',  # Cambia el color de fondo a #6dae3a
                                        'color': 'white',  # Cambia el color de las letras a blanco
                                        'borderTopRightRadius': '0.25rem',  # Redondea la esquina superior derecha
                                        'textAlign': 'right',
                                    },
                                ),
                            ],
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    [
                                                        html.Div(
                                                            [
                                                                html.Iframe(
                                                                    srcDoc=open('highchart3.html').read(), 
                                                                    width='100%', 
                                                                    height='220',
                                                                    style={"marginLeft": "-30px", "marginTop": "-10px"},
                                                                    )
                                                            ],
                                                        ),
                                                    ],
                                                    md=8
                                                ),
                                                dbc.Col(
                                                    [
                                                        dbc.Row(
                                                            [
                                                                html.Div(
                                                                    [
                                                                        html.P(
                                                                            "Disponibilidad", 
                                                                            style={'font-size': '10px',
                                                                                'margin-bottom': '0',
                                                                                'margin-top': '1'
                                                                                }
                                                                            ),
                                                                        html.P(
                                                                            f"{Disponibilidad3}%",
                                                                            style={
                                                                                'font-size': '10px',
                                                                                'margin-top': '0',
                                                                                'font-weight': 'bold',
                                                                                'margin-bottom': '0px'
                                                                                },
                                                                            ),
                                                                        html.Div(
                                                                            style={
                                                                                'height': '12px',
                                                                                'width': '35px',
                                                                                'background-color': '#00e272',
                                                                                'border-radius': '5px',
                                                                                'margin-top': '0px'
                                                                                }
                                                                            )
                                                                    ],
                                                                    style={
                                                                        'display': 'inline-block',
                                                                        }
                                                                ),
                                                            ],
                                                            style={
                                                                'margin-top': '5px',
                                                                'margin-bottom': '5px'
                                                                }
                                                        ),
                                                        dbc.Row(
                                                            [
                                                                html.Div(
                                                                    [
                                                                        html.P(
                                                                            "Rendimiento", 
                                                                            style={'font-size': '10px',
                                                                                'margin-bottom': '0',
                                                                                'margin-top': '1'
                                                                                }
                                                                            ),
                                                                        html.P(
                                                                            f"{rendimiento_global3}%",
                                                                            style={
                                                                                'font-size': '10px',
                                                                                'margin-top': '0',
                                                                                'font-weight': 'bold',
                                                                                'margin-bottom': '0'
                                                                                },
                                                                            ),
                                                                        html.Div(
                                                                            style={
                                                                                'height': '12px',
                                                                                'width': '35px', 
                                                                                'background-color': '#544fc5',
                                                                                'border-radius': '5px',
                                                                                'margin-top': '0'
                                                                                }
                                                                            )
                                                                    ],
                                                                    style={
                                                                        'display': 'inline-block'
                                                                        }
                                                                ),
                                                            ],
                                                            style={
                                                                'margin-top': '5px',
                                                                'margin-bottom': '5px'
                                                                }
                                                        ),
                                                        dbc.Row(
                                                            [
                                                                html.Div(
                                                                    [
                                                                        html.P(
                                                                            "Calidad", 
                                                                            style={'font-size': '10px',
                                                                                'margin-bottom': '0',
                                                                                'margin-top': '1'
                                                                                }
                                                                            ),
                                                                        html.P(
                                                                            f"{Calidad3}%",
                                                                            style={
                                                                                'font-size': '10px',
                                                                                'margin-top': '0',
                                                                                'font-weight': 'bold',
                                                                                'margin-bottom': '0'
                                                                                },
                                                                            ),
                                                                        html.Div(
                                                                            style={
                                                                                'height': '12px',
                                                                                'width': '35px', 
                                                                                'background-color': '#2cafff',
                                                                                'border-radius': '5px',
                                                                                'margin-top': '0'
                                                                                }
                                                                            )
                                                                    ],
                                                                    style={
                                                                        'display': 'inline-block'
                                                                        }
                                                                ),
                                                            ],
                                                            style={
                                                                'margin-top': '5px',
                                                                'margin-bottom': '5px'
                                                                }
                                                        ),
                                                    ],
                                                    md=3
                                                ),
                                                dbc.Col(
                                                    [
                                                        
                                                    ],
                                                    md=1
                                                ),

                                            ],
                                        ),
                                    ],
                                    className="border rounded shadow-sm d-flex flex-column",
                                    style={
                                        "height": "150px", 
                                        "marginRight": "1px", 
                                        'marginBottom': '1px'
                                        },
                                ),
                                dbc.Col(
                                    [
                                        html.Div(
                                            [
                                                html.Iframe(
                                                    srcDoc=open('areachart3.html').read(), 
                                                    width='120%', 
                                                    height='300',
                                                    style={"marginLeft": "-30px", "marginTop": "-10px"},
                                                )
                                            ],
                                        )
                                    ],
                                    className="border rounded shadow-sm d-flex flex-column justify-content-start",
                                    style={
                                        "height": "150px", 
                                        "marginLeft": "1px",
                                        'marginBottom': '1px',
                                        },
                                ),
                            ],
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Div(
                                            [
                                                html.Iframe(
                                                    srcDoc=open('barstackchart.html').read(), 
                                                    width='120%', 
                                                    height='200',
                                                    style={"marginLeft": "-30px", "marginTop": "-10px"},
                                                )
                                            ],
                                        ),
                                    ],
                                    className="border rounded shadow-sm d-flex flex-column justify-content-start",
                                    style={
                                        "height": "150px", 
                                        "marginRight": "1px",
                                        'marginBottom': '1px',
                                        'marginTop': '1px',
                                        },
                                ),
                                dbc.Col(
                                    [
                                        html.Div(
                                            [
                                                html.Iframe(
                                                    srcDoc=open('barchart3.html').read(), 
                                                    width='120%', 
                                                    height='180',
                                                    style={"marginLeft": "-30px", "marginTop": "-10px"},
                                                )
                                            ],
                                        ),
                                    ],
                                    className="border rounded shadow-sm d-flex flex-column justify-content-start",
                                    style={
                                        "height": "150px", 
                                        "marginLeft": "1px",
                                        'marginBottom': '1px',
                                        'marginTop': '1px',
                                        },
                                ),
                            ],
                        ),
                    ],
                    className="border rounded shadow-sm d-flex flex-column justify-content-start",
                    style={
                        'marginTop': '5px',
                        'marginRight': '5px',
                        'backgroundColor': '#FFFFFF'
                    },
                ),
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Div(
                                            f"Línea 4",
                                            className="py-1",
                                            style={
                                                'fontSize': '16px',
                                            },
                                        ),
                                    ],
                                    
                                    style={
                                        'backgroundColor': '#6dae3a',  # Cambia el color de fondo a #6dae3a
                                        'color': 'white',  # Cambia el color de las letras a blanco
                                        'borderTopLeftRadius': '0.25rem',  # Redondea la esquina superior izquierda
                                    },
                                ),
                                dbc.Col(
                                    [
                                        html.Div(
                                            [
                                                html.Strong(
                                                    f"OEE: {OEE4}%",
                                                ),
                                            ],
                                            className="py-1",
                                            style={
                                                'fontSize': '16px',
                                            },
                                        ),
                                    ],
                                    
                                    style={
                                        'backgroundColor': '#6dae3a',  # Cambia el color de fondo a #6dae3a
                                        'color': 'white',  # Cambia el color de las letras a blanco
                                        'borderTopRightRadius': '0.25rem',  # Redondea la esquina superior derecha
                                        'textAlign': 'right',
                                    },
                                ),
                            ],
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    [
                                                        html.Div(
                                                            [
                                                                html.Iframe(
                                                                    srcDoc=open('highchart4.html').read(), 
                                                                    width='100%', 
                                                                    height='220',
                                                                    style={"marginLeft": "-30px", "marginTop": "-10px"},
                                                                    )
                                                            ],
                                                        ),
                                                    ],
                                                    md=8
                                                ),
                                                dbc.Col(
                                                    [
                                                        dbc.Row(
                                                            [
                                                                html.Div(
                                                                    [
                                                                        html.P(
                                                                            "Disponibilidad", 
                                                                            style={'font-size': '10px',
                                                                                'margin-bottom': '0',
                                                                                'margin-top': '1'
                                                                                }
                                                                            ),
                                                                        html.P(
                                                                            f"{Disponibilidad4}%",
                                                                            style={
                                                                                'font-size': '10px',
                                                                                'margin-top': '0',
                                                                                'font-weight': 'bold',
                                                                                'margin-bottom': '0px'
                                                                                },
                                                                            ),
                                                                        html.Div(
                                                                            style={
                                                                                'height': '12px',
                                                                                'width': '35px',
                                                                                'background-color': '#00e272',
                                                                                'border-radius': '5px',
                                                                                'margin-top': '0px'
                                                                                }
                                                                            )
                                                                    ],
                                                                    style={
                                                                        'display': 'inline-block',
                                                                        }
                                                                ),
                                                            ],
                                                            style={
                                                                'margin-top': '5px',
                                                                'margin-bottom': '5px'
                                                                }
                                                        ),
                                                        dbc.Row(
                                                            [
                                                                html.Div(
                                                                    [
                                                                        html.P(
                                                                            "Rendimiento", 
                                                                            style={'font-size': '10px',
                                                                                'margin-bottom': '0',
                                                                                'margin-top': '1'
                                                                                }
                                                                            ),
                                                                        html.P(
                                                                            f"{rendimiento_global4}%",
                                                                            style={
                                                                                'font-size': '10px',
                                                                                'margin-top': '0',
                                                                                'font-weight': 'bold',
                                                                                'margin-bottom': '0'
                                                                                },
                                                                            ),
                                                                        html.Div(
                                                                            style={
                                                                                'height': '12px',
                                                                                'width': '35px', 
                                                                                'background-color': '#544fc5',
                                                                                'border-radius': '5px',
                                                                                'margin-top': '0'
                                                                                }
                                                                            )
                                                                    ],
                                                                    style={
                                                                        'display': 'inline-block'
                                                                        }
                                                                ),
                                                            ],
                                                            style={
                                                                'margin-top': '5px',
                                                                'margin-bottom': '5px'
                                                                }
                                                        ),
                                                        dbc.Row(
                                                            [
                                                                html.Div(
                                                                    [
                                                                        html.P(
                                                                            "Calidad", 
                                                                            style={'font-size': '10px',
                                                                                'margin-bottom': '0',
                                                                                'margin-top': '1'
                                                                                }
                                                                            ),
                                                                        html.P(
                                                                            f"{Calidad4}%",
                                                                            style={
                                                                                'font-size': '10px',
                                                                                'margin-top': '0',
                                                                                'font-weight': 'bold',
                                                                                'margin-bottom': '0'
                                                                                },
                                                                            ),
                                                                        html.Div(
                                                                            style={
                                                                                'height': '12px',
                                                                                'width': '35px', 
                                                                                'background-color': '#2cafff',
                                                                                'border-radius': '5px',
                                                                                'margin-top': '0'
                                                                                }
                                                                            )
                                                                    ],
                                                                    style={
                                                                        'display': 'inline-block'
                                                                        }
                                                                ),
                                                            ],
                                                            style={
                                                                'margin-top': '5px',
                                                                'margin-bottom': '5px'
                                                                }
                                                        ),
                                                    ],
                                                    md=3
                                                ),
                                                dbc.Col(
                                                    [
                                                        
                                                    ],
                                                    md=1
                                                ),

                                            ],
                                        ),
                                    ],
                                    className="border rounded shadow-sm d-flex flex-column",
                                    style={
                                        "height": "150px", 
                                        "marginRight": "1px", 
                                        'marginBottom': '1px'
                                        },
                                ),
                                dbc.Col(
                                    [
                                        html.Div(
                                            [
                                                html.Iframe(
                                                    srcDoc=open('areachart4.html').read(), 
                                                    width='120%', 
                                                    height='300',
                                                    style={"marginLeft": "-30px", "marginTop": "-10px"},
                                                )
                                            ],
                                        )
                                    ],
                                    className="border rounded shadow-sm d-flex flex-column justify-content-start",
                                    style={
                                        "height": "150px", 
                                        "marginLeft": "1px",
                                        'marginBottom': '1px',
                                        },
                                ),
                            ],
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Div(
                                            [
                                                html.Iframe(
                                                    srcDoc=open('barstackchart.html').read(), 
                                                    width='120%', 
                                                    height='200',
                                                    style={"marginLeft": "-30px", "marginTop": "-10px"},
                                                )
                                            ],
                                        ),
                                    ],
                                    className="border rounded shadow-sm d-flex flex-column justify-content-start",
                                    style={
                                        "height": "150px", 
                                        "marginRight": "1px",
                                        'marginBottom': '1px',
                                        'marginTop': '1px',
                                        },
                                ),
                                dbc.Col(
                                    [
                                        html.Div(
                                            [
                                                html.Iframe(
                                                    srcDoc=open('barchart4.html').read(), 
                                                    width='120%', 
                                                    height='180',
                                                    style={"marginLeft": "-30px", "marginTop": "-10px"},
                                                )
                                            ],
                                        ),
                                    ],
                                    className="border rounded shadow-sm d-flex flex-column justify-content-start",
                                    style={
                                        "height": "150px", 
                                        "marginLeft": "1px",
                                        'marginBottom': '1px',
                                        'marginTop': '1px',
                                        },
                                ),
                            ],
                        ),
                    ],
                    className="border rounded shadow-sm d-flex flex-column justify-content-start",
                    style={
                        'marginTop': '5px',
                        'marginLeft': '5px',
                        'backgroundColor': '#FFFFFF'
                    },
                ),
            ],
        ),
    ],
    style={
        "padding-top": "10px", 
        "padding-right": "80px", 
        "padding-bottom": "10px", 
        "padding-left": "80px",
        'backgroundColor': '#393939'
        }
)
