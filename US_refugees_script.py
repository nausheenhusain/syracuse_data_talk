# uses python3
# uses US refugee data to make a line chart
# for use at syracuse teaching demo

from datawrapper import Datawrapper
import matplotlib.pyplot as plt
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import webbrowser

def read_file():
### reads refugee data into csv

	# reads Excel summary sheet with openpyxl
	# header is row 11
	# chooses which columns we need
	df = pd.read_excel('US-Refugee_Admissions_Report.xlsx', 
		engine='openpyxl', 
		sheet_name='summary', 
		header=10, 
		usecols=['Year', 'Total'])

	# prints column names so we know that it is reading the sheet correctly
	print("Column headings:")
	print(df.columns)
	
	# converts data to csv and saves it
	print('Excel Sheet to CSV:\n', df.to_csv(index=False))
	df.to_csv('~/Desktop/syracuse/US_refugees_total.csv', index=False)
	
	
def plot_data():
### cleans csv
### plots total refugees by year into line chart
### builds datawrapper line chart

	# runs above function
	read_file()
	to_plot = pd.read_csv('US_refugees_total.csv', sep=',')
	
	# cuts off last three lines which are text
	to_plot = to_plot.iloc[:-3]
	print(to_plot)
	# makes sure the Total column has only numeric values in it
	to_plot["Total"] = pd.to_numeric(to_plot["Total"])
	
	# plots line chart
	to_plot.plot(x='Year', y='Total', kind = 'line')
	plt.show()

	# adds basic info to chart
	dw = Datawrapper(access_token = "E7v0xklNnXGQMw7fkWLYfIjs8TsX0oVInrvMK8vD9WjxwvIJDAY24HHV89i6C3lU")
	US_refugee_chart = dw.create_chart(title = "US refugee arrivals over the years", 
	chart_type = 'd3-lines', data = to_plot)
	dw.update_description(US_refugee_chart['id'], 
		source_name = 'US Refugee Admissions', 
		source_url = 'wrapsnet.org', 
		byline = 'The Daily Orange')

	# adds visual properties
	properties = {
 		'visualize' : {
    		'thick': True,
    		'custom-colors': {
    		'Total': '#800080'
    		},
		}
	}
	dw.update_metadata(US_refugee_chart['id'], properties)
	
	# publishes chart to datawrapper, displays in chrome
	dw.publish_chart(US_refugee_chart['id'])
	url = 'https://datawrapper.dwcdn.net/'+US_refugee_chart['id']+'/1'
	chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
	webbrowser.get(chrome_path).open(url)

plot_data()