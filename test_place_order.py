import threading
import time

from ibapi.client import EClient
from ibapi.common import TickerId
from ibapi.contract import Contract
from ibapi.order import Order
from ibapi.wrapper import EWrapper


class IBapi(EWrapper, EClient):

    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: int):
        super().nextValidId(orderId)
        self.nextorderId = orderId
        print('The next valid order id is: ', self.nextorderId)

    def orderStatus(self, orderId, status, filled, remaining, avgFullPrice, permId, parentId, lastFillPrice, clientId,
                    whyHeld, mktCapPrice):
        print('orderStatus - orderid:', orderId, 'status:', status, 'filled', filled, 'remaining', remaining,
              'lastFillPrice', lastFillPrice)

    def openOrder(self, orderId, contract, order, orderState):
        print('openOrder id:', orderId, contract.symbol, contract.secType, '@', contract.exchange, ':', order.action,
              order.orderType, order.totalQuantity, orderState.status)

    def execDetails(self, reqId, contract, execution):
        print('Order Executed: ', reqId, contract.symbol, contract.secType, contract.currency, execution.execId,
              execution.orderId, execution.shares, execution.lastLiquidity)

    # def error(self, reqId: TickerId, errorCode: int, errorString: str):
    # 	super().error(reqId, errorCode, errorString)
    # 	print("Error. Id:", reqId, "Code:", errorCode, "Msg:", errorString)

    def error(self, reqId, errorCode, errorString):
        if errorCode == 202:
            print('Order canceled!') 


def run_loop():
    app.run()


app = IBapi()
app.connect('127.0.0.1', 7497, 123)

app.nextorderId = None

#Start the socket in a thread
api_thread = threading.Thread(target=run_loop, daemon=True)
api_thread.start()

####################################################################

# Check if the API is connected via orderid - Waiting for API to send over the nextorderid
while True:
    if isinstance(app.nextorderId, int):
        print('API is Connected')
        break
    else:
        print('Waiting for API connection ...')
        time.sleep(0.5)

####################################################################


# Function to create FX Order contract
def FX_order(symbol: str) -> Contract:
    contract = Contract()
    contract.symbol = symbol[:3]
    contract.secType = 'CASH'
    contract.exchange = 'IDEALPRO'
    contract.currency = symbol[3:]
    return contract


#Create order object and specify order details
order = Order()
order.action = 'BUY'
order.totalQuantity = 20000
order.orderType = 'LMT'
order.lmtPrice = '1.10'

# Place the order
print('Placing order ...')
app.placeOrder(app.nextorderId, FX_order('EURUSD'), order)
# app.nextorderId += 1  # Increment orderId for next order (if needed)

# Wait some time to process
time.sleep(3)

# Cancel the last order
print('Cancelling order ...')
app.cancelOrder(app.nextorderId)

####################################################################

time.sleep(3)
app.disconnect()
