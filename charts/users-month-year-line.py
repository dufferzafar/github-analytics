from bokeh.models import HoverTool
from bokeh.plotting import figure
from bokeh.io import show, export_png
from bokeh.models import NumeralTickFormatter

import pandas as pd
import datetime as dt

odf = pd.read_json(open("outputs/user-year-month-count.json"))

count = odf['count']
months = odf['month']
years = odf['year']

date = list(zip(months, years))
date = list(map(lambda x: dt.datetime(year=x[1], month=x[0], day=1), date))

data = list(zip(date, count))

# Sort data by timestamp
data = sorted(data, key=lambda x: x[0])

#
date, count = zip(*data)

# Cumulative
count = list(count)
for i in range(1, len(count)):
    count[i] += count[i - 1]

p1 = figure(
    x_axis_type="datetime",
    y_axis_label="No. of Users", x_axis_label="Year",
    # title="Total Users",
    width=1000
)

p1.xaxis.axis_label_text_font_size = "18pt"
p1.yaxis.axis_label_text_font_size = "18pt"

p1.yaxis[0].formatter = NumeralTickFormatter(format="0,0")
p1.yaxis[0].ticker.desired_num_ticks = 10

p1.xaxis[0].ticker.desired_num_ticks = 10

p1.line(date, count)
p1.circle(date, count, fill_color="white", size=4)

hover = HoverTool(tooltips=[
    ("users", "$y{(0.00 a)}")
])

p1.add_tools(hover)

# export_png(p1, filename="users-month-year-line.png")
show(p1)
