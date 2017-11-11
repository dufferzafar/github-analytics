from math import pi
from bokeh.palettes import magma
import pandas as pd

from bokeh.io import show
from bokeh.models import (
    ColumnDataSource,
    HoverTool,
    LinearColorMapper,
    BasicTicker,
    NumeralTickFormatter,
    ColorBar,
)
from bokeh.plotting import figure

colors = magma(21)
colors = list(reversed(colors))[2:]

monthDict = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
             7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}

data = pd.read_json(open("outputs/user-year-month-count.json"))
data = data[data.year != 2007]
data = data.sort_values(['year', 'month'], ascending=[True, False])

data['year'] = data['year'].astype(str)
data['month'] = data['month'].apply(lambda x: monthDict[x])

cols = ['year', 'month', 'count']
data = data[cols]
data.columns = ['year', 'month', 'users']
data = data.set_index('year')

# print(data)
years = list(data.index.unique())
months = list(monthDict.values())
# print(months)

mapper = LinearColorMapper(
    palette=colors, low=data.users.min(), high=data.users.max()
)

source = ColumnDataSource(data)

TOOLS = "hover,save,pan,box_zoom,reset,wheel_zoom"

p = figure(
    # title="Github User Acquisition({0} - {1})".format(years[0], years[-1]),
    x_range=years, y_range=list(reversed(months)),
    y_axis_label="Month", x_axis_label="Year",
    # x_axis_location="above",
    plot_width=550, plot_height=300,
    tools=TOOLS,
    toolbar_location="above"
)

p.grid.grid_line_color = None
p.axis.axis_line_color = None
p.axis.major_tick_line_color = None
p.axis.major_label_text_font_size = "5pt"
p.axis.major_label_standoff = 0
p.xaxis.major_label_orientation = pi / 3

p.rect(
    x="year", y="month", width=1, height=1,
    source=source,
    fill_color={'field': 'users', 'transform': mapper},
    line_color=None
)

color_bar = ColorBar(
    color_mapper=mapper, major_label_text_font_size="5pt",
    ticker=BasicTicker(desired_num_ticks=len(colors)),
    formatter=NumeralTickFormatter(format="(0,0)"),
    label_standoff=8,
    border_line_color=None,
    location=(0, 0)
)

p.add_layout(color_bar, 'right')

p.select_one(HoverTool).tooltips = [
    ('Month', '@month @year'),
    ('Users', '@users'),
]

show(p)      # show the plot
