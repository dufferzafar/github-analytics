from bokeh.io import show
from bokeh.core.properties import value
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.transform import dodge
from math import ceil

import pandas as pd

odf = pd.read_json(open("outputs/top_lang_year.json"))
odf['sum_MB'] = odf['sum_MB'].apply(lambda x: ceil(x / 1024))
odf.rename(columns={'sum_MB': 'sum_GB'}, inplace=True)

excluded = ["html", "css", "makefile", "batchfile", "cmake", "jupyter notebook", "apacheconf", "tex", "viml"]

odf = odf.loc[~ (odf.language.isin(excluded))]
data_2015 = odf.loc[odf.year == 2015].sort_values("sum_GB").tail(10).sort_values("language")
data_2016 = odf.loc[odf.year == 2016].sort_values("sum_GB").tail(10).sort_values("language")
data_2017 = odf.loc[odf.year == 2017].sort_values("sum_GB").tail(10).sort_values("language")


languages = data_2015.language.unique()
years = ['2015', '2016', '2017']

cdata = list(zip(languages, list(data_2015.sum_GB), list(data_2016.sum_GB), list(data_2017.sum_GB)))
cdata.sort(key=lambda x: max(x[1:]), reverse=True)

cdata = list(zip(*cdata))
languages = cdata[0]

data = {
    'language': cdata[0],
    '2015': cdata[1],
    '2016': cdata[2],
    '2017': cdata[3],
}

x = [(language, year) for language in languages for year in years]
counts = sum(zip(data['2015'], data['2016'], data['2017']), ())
TOOLS = "hover,save,pan,box_zoom,reset,wheel_zoom"
source = ColumnDataSource(data=data)

p = figure(
    x_range=languages,
    plot_height=500,
    plot_width=1500,
    title="Language Code Size by Year",
    y_axis_label="Code Size (GB)",
    x_axis_label="Language"
)

p.vbar(x=dodge('language', -0.25, range=p.x_range), top='2015', width=0.2, source=source,
       color="#c9d9d3", legend=value('2015'))

p.vbar(x=dodge('language', 0.0, range=p.x_range), top='2016', width=0.2, source=source,
       color="#718dbf", legend=value("2016"))

p.vbar(x=dodge('language', 0.25, range=p.x_range), top='2017', width=0.2, source=source,
       color="#e84d60", legend=value("2017 (upto Aug)"))

hover = HoverTool(tooltips=[
    ("users", "$y{(0.00 a)}")
])

p.y_range.start = 0
p.x_range.range_padding = 0.1
p.xgrid.grid_line_color = None

p.yaxis.axis_label_text_font_size = "14pt"
p.xaxis.axis_label_text_font_size = "14pt"
p.axis.major_label_text_font_size = "15pt"
p.add_tools(hover)

show(p)
