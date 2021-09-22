import threading
import time

from ibapi.client import EClient
from ibapi.common import BarData
from ibapi.contract import Contract
from ibapi.wrapper import EWrapper
from prettyprinter import cpprint


class IBapi(EWrapper, EClient):

    def __init__(self):
        EClient.__init__(self, self)
        self.data = []  #Initialize variable to store candle

    def historicalData(self, reqId: int, bar: BarData) -> None:
        print('RequestID:', reqId, bar)
        self.data.append([bar.date, bar.open, bar.high, bar.close, bar.low, bar.volume, bar.barCount, bar.average])
        # print("HistoricalData. ", reqId, " Date:", bar.date, "Open:", bar.open, "High:", bar.high, "Low:", bar.low, "Close:", bar.close, "Volume:", bar.volume, "Count:", bar.barCount, "WAP:", bar.average)


def run_loop():
    app.run()


app = IBapi()
app.connect('127.0.0.1', 7497, 123)

#Start the socket in a thread
api_thread = threading.Thread(target=run_loop, daemon=True)
api_thread.start()

time.sleep(1)  #Sleep interval to allow time for connection to server

####################################################################

#Create contract object
eurusd_contract = Contract()
eurusd_contract.symbol = 'EUR'
eurusd_contract.secType = 'CASH'
eurusd_contract.exchange = 'IDEALPRO'
eurusd_contract.currency = 'USD'

#Request historical candles
#   - Requesting Historical Bar Data - https://interactivebrokers.github.io/tws-api/historical_bars.html
#   - Reference: https://rdrr.io/cran/IBrokers/man/reqHistoricalData.html
app.reqHistoricalData(reqId=1,
                      contract=eurusd_contract,
                      endDateTime='',
                      durationStr='2 D',
                      barSizeSetting='1 hour',
                      whatToShow='BID',
                      useRTH=0,
                      formatDate=2,
                      keepUpToDate=False,
                      chartOptions=[])

# NOTE: IB will send over the most recent candle, even if it has not closed.
#       In most cases, an incomplete candle is not useful and should be discarded.

time.sleep(3)  #sleep to allow enough time for data to be returned

####################################################################

#Working with Pandas DataFrames
import pandas

# Load data as a DataFrame giving the columns header names
column_headers = ['DateTime', 'Open', 'High', 'Low', 'Close', 'Volume', 'Count', 'WAP']
df = pandas.DataFrame(app.data, columns=column_headers)

# Convert DateTime column to datetime
df['DateTime'] = pandas.to_datetime(df['DateTime'], unit='s')

# Calculate 20 Point Moving Average
df['20SMA'] = df['Close'].rolling(20).mean()

# Save to CSV file
df.to_csv('EURUSD_Hourly.csv')

print(df)

####################################################################

app.disconnect()
