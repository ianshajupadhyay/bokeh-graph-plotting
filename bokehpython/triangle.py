from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas


df = pandas.read_csv("data.csv")

x =[3,7.5,10]
y= [3,6,9]

output_file("triangle.html")



f = figure()

f.circle(x,y)
show(f)

