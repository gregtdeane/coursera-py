from bs4 import BeautifulSoup
import ssl
import requests
import pandas as pd
from IPython.display import display


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter -') # try with http://www.dr-chuck.com/page1.htm
# url = 'https://finance.yahoo.com/quote/AAPL231013C00050000?p=AAPL231013C00050000'
# url = 'https://finance.yahoo.com/quote/AAPL/options?p=AAPL&guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAEPOwasaxXfS0ENDI0K2zYbI1kT7OPT69ESNZ8btuv6ZHKDwG3hPAhSKdMwxGeFUpUH4Hx1-Qo0NfLcmn1Yv6dyVaJkK9NcHci4r4jX7h6j0euuIrfwkZmFWO0oCMcekg50cvJCCtRCYoHRBtI_d2l94UINVM-BKQ9jkNNAVwRU1'
url = 'https://finance.yahoo.com/quote/TSLA/options?p=TSLA'
# html = urllib.request.urlopen(url,context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')

###########################################################################3
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
print(response.status_code)
soup = BeautifulSoup(response.text, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

tables = soup.find_all('table')
print("Num Tables: "+ str(len(tables)))
# print(tables)


for table in tables:
    table_rows = table.find_all('tr')
    print("############################################################")
    print("############################################################")
    print(table_rows)



# for table in tables:
    # df = pd.read_html(str(table))
    # # print(table.text)
    # display(df[0])

###########################################################################
# dfs = pd.read_html(url,header={'User-Agent': 'Mozilla/5.0'})
# for df in dfs:
#     print(df)

#to do
# Add tables to SQLite database
# Add a column for time to expiration (expiry - current_date)
# write methods to plot volatility of options from database
# Calculate option delta, gamma, other greeks
# Standard deviation of volatility
# Use AI/ML to calculate correlation of greeks with volatility
#