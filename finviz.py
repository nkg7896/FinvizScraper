from lxml import html
import requests

page = requests.get('https://finviz.com/screener.ashx?v=340&s=ta_toplosers')
tree = html.fromstring(page.content)

#This will create a list of buyers:
stocks = tree.xpath('//div[@title="buyer-name"]/text()')
#<div title="buyer-name">Carson Busses</div>
#<tr class="table-light2-row"><td class="snapshot-td">Company</td><td class="snapshot-td"><b>Yuma Energy, Inc.</b></td></tr>
stocks = tree.xpath('//tr[@class="table-light2-row"]/text()')
#'//tr[@class=""]'
#yeah"company-name"/text()'


#This will create a list of prices
#prices = tree.xpath('//span[@class="item-price"]/text()')

print ("Stocks: ", stocks)