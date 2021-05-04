# uses python3
# uses UN refugee data to make a stacked bar chart
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
	# chooses which columns we need
	df = pd.read_excel('UN_Refugees_Admissions.xlsx', 
		engine='openpyxl', 
		sheet_name='chart',
		usecols=['year', 'CAN', 'AUS', 'US', 'THAI', 'THAI_CAMP'])

	# prints column names so we know that it is reading the sheet correctly
	print("Column headings:")
	print(df.columns)
	
	# converts data to csv and saves it
	print('Excel Sheet to CSV:\n', df.to_csv(index=False))
	df.to_csv('~/Desktop/syracuse/UN_refugees_total.csv', index=False)
	
	
def plot_data():
### cleans csv
### plots total refugees by year into line chart
### builds datawrapper line chart

	# runs above function
	read_file()
	to_plot = pd.read_csv('~/Desktop/syracuse/UN_refugees_total.csv', sep=',')
	
	# cuts off last three lines which are text
	# to_plot = to_plot.iloc[:-3]
	print(to_plot)
	# makes sure the Total column has only numeric values in it
	to_plot["CAN"] = pd.to_numeric(to_plot["CAN"])
	to_plot["AUS"] = pd.to_numeric(to_plot["AUS"])
	to_plot["US"] = pd.to_numeric(to_plot["US"])
	to_plot["THAI"] = pd.to_numeric(to_plot["THAI"])
	to_plot["THAI_CAMP"] = pd.to_numeric(to_plot["THAI_CAMP"])
	
	# plots line chart
	to_plot.plot(x='year', kind = 'barh')
	plt.show()

	# adds basic info to chart
	dw = Datawrapper(access_token = "E7v0xklNnXGQMw7fkWLYfIjs8TsX0oVInrvMK8vD9WjxwvIJDAY24HHV89i6C3lU")
	UN_refugee_chart = dw.create_chart(title = "UN refugee arrival data to various countries", 
	chart_type = 'd3-bars-stacked', data = to_plot)
	dw.update_description(UN_refugee_chart['id'], 
		intro = 'Since 2013, far more refugees have moved to live in refugee camps in Thailand than have been resettled in North America.',
		source_name = 'UN refugee data', 
		source_url = 'https://data2.unhcr.org/en/', 
		byline = 'The Daily Orange')

	# adds visual properties
	properties = {
 		'visualize' : {
    		'thick': True,
    		'custom-colors': {
    		'CAN': '#c71e1d',
    		'GBR': '#c4c4c4',
    		'US': '#09bb9f',
    		'THAI': '#ffca76',
    		'THAI_CAMP': '#15607a',
    		},
    		"show-color-key": True
		}
	}
	dw.update_metadata(UN_refugee_chart['id'], properties)
	
	# publishes chart to datawrapper, displays in chrome
	dw.publish_chart(UN_refugee_chart['id'])
	url = 'https://datawrapper.dwcdn.net/'+UN_refugee_chart['id']+'/1'
	chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
	webbrowser.get(chrome_path).open(url)

plot_data()