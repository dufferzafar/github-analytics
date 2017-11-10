from bokeh.models import HoverTool
from bokeh.palettes import Spectral5
from bokeh.plotting import figure
from bokeh.io import show

import pandas as pd
odf = pd.read_json(open("outputs/user-year-country-count.json"))

hover = HoverTool(tooltips=[
    ("year", "$x{(0000)}"),
    ("users", "$y{(0.00 a)}"),
])

p = figure(plot_height=500, y_axis_label="No. of Users",
           x_axis_label="Year", title="No. of users in countries")
p.add_tools(hover)

countries = ["us", "in", "cn", "gb", "de"]
colors = Spectral5

for i, country in enumerate(countries):
    odf4 = odf.loc[odf.country_code == country]
    odf4 = odf4.sort_values("year")

    x = odf4['year']
    y = odf4['count']

    color = colors[i % len(colors)]

    p.line(x, y, color=color, legend=country)
    p.circle(x, y, fill_color="white", size=8, color=color)


p.legend.location = "top_left"

show(p)
