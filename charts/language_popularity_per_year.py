from bokeh.io import show
from bokeh.palettes import magma
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
from math import ceil

import pandas as pd

odf = pd.read_json(open("outputs/top_lang_year.json"))
odf['sum_MB'] = odf['sum_MB'].apply(lambda x: ceil(x / 1024))
odf.rename(columns={'sum_MB': 'sum_GB'}, inplace=True)

excluded = ["html", "css", "makefile"]
odf = odf.loc[~ (odf.language.isin(excluded))]
data_2015 = odf.loc[odf.year == 2015].sort_values("sum_GB").tail(15)
data_2016 = odf.loc[odf.year == 2016].sort_values("sum_GB").tail(15)
data_2017 = odf.loc[odf.year == 2017].sort_values("sum_GB").tail(15)

# print(data_2015)
p = figure(
    x_axis_label="Code Size (GB)",
    y_range=data_2015.language.unique(),
    plot_height=800,
    plot_width=800
)

p.yaxis.axis_label_text_font_size = "14pt"
p.xaxis.axis_label_text_font_size = "14pt"
p.axis.major_label_text_font_size = "15pt"

colors = magma(30)
colors = list(reversed((colors)[4:]))

p.hbar(
    source=data_2015,
    right='sum_GB', y='language',
    height=0.8,
    line_color='white',
    fill_color=factor_cmap('language', palette=colors,
                           factors=data_2015.language.unique())
)
show(p)
