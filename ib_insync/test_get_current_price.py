
from ib_insync import *
from pprint import pprint

##############################################################################

ib = IB()
ib.connect(host='127.0.0.1', port=7497, clientId=1)
print(ib.connect)

##############################################################################

# Define the ontract/stock
#   SMART - Automatically route to appropriate exchange
nflx_contract = Stock(symbol='AAPL', exchange='SMART', currency='USD')

# Get more information on our contract
ib.qualifyContracts(nflx_contract)

# Request a tick data stream
quote_ticker = ib.reqMktData(nflx_contract)

ib.sleep(0.5)

# View the current/latest price
print('--------------')
print(quote_ticker.marketPrice())
print(quote_ticker.open)
print(quote_ticker.dict)
