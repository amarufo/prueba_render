# app.py
import os
import dash
from layout import layout

app = dash.Dash(__name__)
app.title = "Dashboard Histograma"

app.layout = layout

app = app.server

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))
    app.run(host="0.0.0.0", port=port)



