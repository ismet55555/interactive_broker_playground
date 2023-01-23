
from ib_insync import *

##############################################################################

ib = IB()
ib.connect()

##############################################################################

# Define the ontract/stock
#   SMART - Automatically route to appropriate exchange
contract = Stock(symbol='MSFT', exchange='SMART', currency='USD', primaryExchange='NASDAQ')
# contract = Stock(symbol='EUR', secType='CASH', exchange='IDEALPRO', currency='USD')

# Get more information on our contract
ib.qualifyContracts(contract)

# Request the historical data of contract/stock
historical_data = ib.reqHistoricalData(
    contract=contract,
    endDateTime='',  # Blank so it will pull data up to most recent candle
    barSizeSetting='1 hour',  # Bar sizes anyhere form 1 second to 1 month
    durationStr='2 D',  # How far back data is
    whatToShow='BID',  # Data to show. (MIDPOINT, BID, ASK, TRADES, etc)
    useRTH=False  # Regular trading hours
    )

# Convert to dataframe
historical_data_df = util.df(historical_data)

# Output as Dataframe
print(historical_data_df)