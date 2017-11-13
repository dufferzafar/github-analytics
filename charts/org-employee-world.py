from bokeh.io import show
from bokeh.palettes import magma
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
from math import pi

import pandas as pd
odf = pd.read_csv(open("outputs/orgs-employee-count.csv"))
# odf = odf.loc[odf.year != 2017]
# odf['year'] = pd.to_datetime(odf['year'], format="%Y")

# odf.head(50).country_code.unique()
odf = odf.rename(columns=lambda x: x.strip())
odf = odf.sort_values("employees", ascending=False)
# odf3.country_code.unique()

# x_axis = list(odf.corporate)
# x_axis = list(map(lambda x: x.strip(), x_axis))

# y_axis = odf.employees

p = figure(
    x_range=odf.corporate.unique(),
    plot_height=800,
    plot_width=1000
)

colors = magma(30)
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
p.yaxis.axis_label_text_font_size = "14pt"
p.xaxis.axis_label_text_font_size = "14pt"
p.axis.major_label_text_font_size = "15pt"

show(p)
