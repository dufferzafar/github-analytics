from bokeh.models import HoverTool
from bokeh.palettes import Spectral5
from bokeh.plotting import figure
from bokeh.io import show
from bokeh.models import NumeralTickFormatter

import pandas as pd
import datetime as dt
odf = pd.read_json(open("outputs/user-year-month-count.json"))


hover = HoverTool(tooltips=[
    ("users", "$y{(0.00 a)}")
])

years = odf.year.unique().tolist()
years.sort()

count = odf['count']
months = odf['month']
years = odf['year']

colors = Spectral5

date = list(zip(months, years))
date = list(map(lambda x: dt.datetime(year=x[1], month=x[0], day=1), date))

data = list(zip(date, count))

data = sorted(data, key=lambda x: x[0])

date, count = zip(*data)

count = list(count)
for i in range(1, len(count)):
    count[i] += count[i - 1]
# print(date)

p1 = figure(x_axis_type="datetime", y_axis_label="No. of Users",
            x_axis_label="Date", title="Total Users", width=900)

p1.yaxis[0].formatter = NumeralTickFormatter(format="0 a")

p1.line(date, count)

p1.circle(date, count, fill_color="white", size=4)
p1.add_tools(hover)


show(p1)
