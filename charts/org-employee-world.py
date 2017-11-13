from bokeh.io import show
from bokeh.layouts import column, row
from bokeh.palettes import magma, viridis
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
from math import pi

import pandas as pd
# odf = pd.read_csv(open("outputs/orgs-employee-count.csv"), delimiter=' *, *', engine='python')
odf = pd.read_csv(open("outputs/orgs-employee-count-indian.csv"), delimiter=' *, *', engine='python')

# Remove spaces etc. from column names
# odf = odf.rename(columns=lambda x: x.strip())

odf = odf.sort_values("employees", ascending=False)

plot_height = 600
plot_width = 900

p = figure(
    title="Number of Employees",
    x_range=odf.corporate.unique(),
    tools="",
    toolbar_location=None,
    plot_height=plot_height,
    plot_width=plot_width
)

# colors = magma(30)
# colors = (colors)[6:]

colors = viridis(30)
colors = (colors)[6:]

p.vbar(
    source=odf,
    x='corporate', top='employees',
    width=1,
    line_color='white',
    fill_color=factor_cmap('corporate', palette=colors,
                           factors=odf.corporate.unique())
)

p.xaxis.major_label_orientation = pi / 3
p.x_range.range_padding = 0.01
p.y_range.range_padding = 0.01
# p.xgrid.grid_line_color = None

p.yaxis.axis_label_text_font_size = "14pt"
p.xaxis.axis_label_text_font_size = "14pt"
p.axis.major_label_text_font_size = "15pt"

odf = odf.sort_values("followers_per_employee", ascending=False)
s = figure(
    title="Number of Followers per Employee",
    x_range=odf.corporate.unique(),
    tools="",
    toolbar_location=None,
    plot_height=plot_height,
    plot_width=plot_width
)

s.vbar(
    source=odf,
    x='corporate', top='followers_per_employee',
    width=1,
    line_color='white',
    fill_color=factor_cmap('corporate', palette=colors,
                           factors=odf.corporate.unique())
)

s.xaxis.major_label_orientation = pi / 3
s.x_range.range_padding = 0.01
s.y_range.range_padding = 0.01
# s.xgrid.grid_line_color = None
s.yaxis.axis_label_text_font_size = "14pt"
s.xaxis.axis_label_text_font_size = "14pt"
s.axis.major_label_text_font_size = "15pt"

odf = odf.sort_values("stars_per_employee", ascending=False)
t = figure(
    title="Number of Stars per Employee",
    x_range=odf.corporate.unique(),
    tools="",
    toolbar_location=None,
    plot_height=plot_height,
    plot_width=plot_width
)

t.vbar(
    source=odf,
    x='corporate', top='stars_per_employee',
    width=1,
    line_color='white',
    fill_color=factor_cmap('corporate', palette=colors,
                           factors=odf.corporate.unique())
)

t.xaxis.major_label_orientation = pi / 3
t.x_range.range_padding = 0.01
t.y_range.range_padding = 0.01
# t.xgrid.grid_line_color = None
t.yaxis.axis_label_text_font_size = "14pt"
t.xaxis.axis_label_text_font_size = "14pt"
t.axis.major_label_text_font_size = "15pt"

show(column(row(p), row(s), row(t)))
