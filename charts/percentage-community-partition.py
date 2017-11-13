from bokeh.io import show
from bokeh.models import HoverTool
from bokeh.plotting import figure
import pandas as pd

odf = pd.read_json(open("outputs/percent-community-part.json"))

p = figure(
    y_axis_label="No. of Projects",
    x_axis_label="Percentage Community Participation",
    y_axis_type="log",
    title="Total Users",
    width=1500
)

y = list(odf[0])
x = [i for i in range(0, 100)]

p.yaxis.axis_label_text_font_size = "14pt"
p.xaxis.axis_label_text_font_size = "14pt"
p.axis.major_label_text_font_size = "15pt"

hover = HoverTool(tooltips=[
    ("Number of projects", "$y{(0.00 a)}")
])

p.add_tools(hover)

p.line(x, y, line_width=5, line_join='round', line_cap='round')
p.circle(x, y, line_width=2.5, fill_color="white", size=8)
show(p)
