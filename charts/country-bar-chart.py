from bokeh.io import show
from bokeh.palettes import Spectral11
from bokeh.plotting import figure
from bokeh.transform import factor_cmap

import pandas as pd
odf = pd.read_json(open("outputs/user-year-country-count.json"))
# odf = odf.loc[odf.year != 2017]
# odf['year'] = pd.to_datetime(odf['year'], format="%Y")

# odf.head(50).country_code.unique()
odf2 = odf.loc[odf.year == 2014]
odf2.sort_values("count")

odf3 = odf2.head(10)
# odf3.country_code.unique()


p = figure(
    x_range=(odf3.country_code.unique()),
    plot_height=500
)

p.vbar(
    source=odf3,

    x='country_code', top='count',
    width=1,
    line_color='white',
    fill_color=factor_cmap('country_code', palette=Spectral11,
                           factors=odf3.country_code.unique())
)

show(p)
