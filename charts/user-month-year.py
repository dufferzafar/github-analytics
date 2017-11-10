from math import pi
from bokeh.palettes import Spectral11
import pandas as pd

from bokeh.io import show
from bokeh.models import (
    ColumnDataSource,
    HoverTool,
    LinearColorMapper,
    BasicTicker,
    PrintfTickFormatter,
    ColorBar,
)
from bokeh.plotting import figure


data = pd.read_json(open("outputs/user-year-month-count.json"))
print(data)
data['year'] = data['year'].astype(str)
data = data.set_index('year')

data = data.pivot_table(values='count', index=data.index, columns='month', aggfunc='first')

print(data)
# # print(data)
# data.drop('Annual', axis=1, inplace=True)
data.columns.name = 'Month'
print(data)
years = list(data.index)
months = list(data.columns)

# reshape to 1D array or rates with a month and year for each row.
df = pd.DataFrame(data.stack(), columns=['users']).reset_index()
print(df)
# this is the colormap from the original NYTimes plot
colors = ["#75968f", "#a5bab7", "#c9d9d3", "#e2e2e2", "#dfccce", "#ddb7b1", "#cc7878", "#933b41", "#550b1d"]
colors = Spectral11
mapper = LinearColorMapper(palette=colors, low=df.users.min(), high=df.users.max())

source = ColumnDataSource(df)

TOOLS = "hover,save,pan,box_zoom,reset,wheel_zoom"

p = figure(title="Github User Acquisition({0} - {1})".format(years[0], years[-1]),
          x_range=years, y_range=list(reversed(list(map(str, months)))),
          x_axis_location="above", plot_width=900, plot_height=400,
          tools=TOOLS, toolbar_location='below')

p.grid.grid_line_color = None
p.axis.axis_line_color = None
p.axis.major_tick_line_color = None
p.axis.major_label_text_font_size = "5pt"
p.axis.major_label_standoff = 0
p.xaxis.major_label_orientation = pi / 3

p.rect(x="year", y="Month", width=1, height=1,
       source=source,
       fill_color={'field': 'users', 'transform': mapper},
       line_color=None)

color_bar = ColorBar(color_mapper=mapper, major_label_text_font_size="5pt",
                     ticker=BasicTicker(desired_num_ticks=len(colors)),
                     formatter=PrintfTickFormatter(format="%d"),
                     label_standoff=6, border_line_color=None, location=(0, 0))

p.add_layout(color_bar, 'right')

p.select_one(HoverTool).tooltips = [
     ('date', '@Month @year'),
     ('count', '@users'),
]

show(p)      # show the plot