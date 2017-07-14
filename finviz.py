from lxml import html
import requests

page = requests.get('https://finviz.com/screener.ashx?v=340&s=ta_toplosers')
tree = html.fromstring(page.content)

#Grabs text from html where class="tab-link":

#<a href="http://www.mauiland.com" target="_blank" class="tab-link">Maui Land & Pineapple Company, Inc.</a><br /></b></td></tr>
stocks = tree.xpath('//a[@class="tab-link"]/text()')


print ("Stocks: ", stocks)