# layout.py
import numpy as np
import pandas as pd
import plotly.express as px
from dash import html, dcc

# Generar datos inventados
df = pd.DataFrame({"valor": np.random.default_rng(42).normal(loc=50, scale=10, size=500)})

def build_histogram():
    return px.histogram(df, x="valor", nbins=30, title="Distribución de Valores")

layout = html.Div([
    html.H1("Histograma de Datos Inventados"),
    dcc.Graph(id="histograma", figure=build_histogram())
])