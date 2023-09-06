import pandas as pd
import plotly.express as px


data = {
    'Provinsi': ['Aceh', 'Sumatera Utara', 'Sumatera Barat', 'Riau', 'Jambi'],
    'Latitude': [4.6951, 3.5952, 0.7824, 0.4602, -1.4852],
    'Longitude': [96.7494, 98.6722, 100.2168, 101.8741, 103.7562],
    'Suhu': [28.5, 29.0, 28.2, 29.8, 30.1]
}

df = pd.DataFrame(data)

fig = px.scatter_geo(
    df,
    lat='Latitude',
    lon='Longitude',
    hover_name='Provinsi',
    size='Suhu',
    projection='natural earth',
    title='Temperatur Provinsi di Indonesia'
)

fig.update_geos(
    resolution=50,
    showcoastlines=True, coastlinecolor="Black",
    showland=True, landcolor="rgb(245, 245, 220)",
    showocean=True, oceancolor="rgb(0, 128, 255)",
    showlakes=True, lakecolor="rgb(0, 0, 255)",
    showrivers=True, rivercolor="rgb(0, 0, 255)"
)

fig.update_layout(
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_scale=50,
    ),
)

fig.show()