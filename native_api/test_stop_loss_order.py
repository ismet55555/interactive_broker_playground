"""
Grouping original stop loss order with original order
If you decide to delete your original order, your stop order gets deleted automatically

Main order: Parent order
Stop loss / Take profit: Child order

Assigning order number of the parent order as a `parentId` in the child order

Incrementing and assigning `orderId` to both orders is needed to avoid duplicate orders
"""

from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import *

import threading
import time

class IBapi(EWrapper, EClient):
	
	def __init__(self):
		EClient.__init__(self, self)
	
	def nextValidId(self, orderId: int):
		super().nextValidId(orderId)
		self.nextorderId = orderId
		print('The next valid order id is: ', self.nextorderId)

	def orderStatus(self, orderId, status, filled, remaining, avgFullPrice, permId, parentId, lastFillPrice, clientId, whyHeld, mktCapPrice):
		print('orderStatus - orderid:', orderId, 'status:', status, 'filled', filled, 'remaining', remaining, 'lastFillPrice', lastFillPrice)
	
	def openOrder(self, orderId, contract, order, orderState):
		print('openOrder id:', orderId, contract.symbol, contract.secType, '@', contract.exchange, ':', order.action, order.orderType, order.totalQuantity, orderState.status)

	def execDetails(self, reqId, contract, execution):
		print('Order Executed: ', reqId, contract.symbol, contract.secType, contract.currency, execution.execId, execution.orderId, execution.shares, execution.lastLiquidity)

####################################################################

def thread_run_loop():
	app.run()

app = IBapi()
app.connect('127.0.0.1', 7497, 123)

app.nextorderId = None

# Start the socket in a thread
api_thread = threading.Thread(target=thread_run_loop, daemon=True)
api_thread.start()

# Check if the API is connected via orderid
# Waiting for API to send over the nextorderid
#   - Replaces straight time.sleep()
while True:
	if isinstance(app.nextorderId, int):
		print('connected')
		print()
		break
	else:
		print('waiting for connection')
		time.sleep(1)

####################################################################

# Function to create FX Order contract
def FX_order(symbol):
	contract = Contract()
	contract.symbol = symbol[:3]
	contract.secType = 'CASH'
	contract.exchange = 'IDEALPRO'
	contract.currency = symbol[3:]
	return contract

# Create order object
order = Order()
order.action = 'BUY'
order.totalQuantity = 100000
order.orderType = 'LMT'
order.lmtPrice = '1.10'
order.orderId = app.nextorderId

# Ensure the first order does not get processed until the rest of the bracket orders are transmitted
order.transmit = False

# Increment order number for next order
app.nextorderId += 1

#Create stop loss order object
stop_order = Order()
stop_order.action = 'SELL'
stop_order.totalQuantity = 100000
stop_order.orderType = 'STP'
stop_order.auxPrice = '1.09'
stop_order.orderId = app.nextorderId
stop_order.parentId = order.orderId

# Process the entire bracket order (parent and child)
order.transmit = True

# Place the orders
app.placeOrder(order.orderId, FX_order('EURUSD'), order)
app.placeOrder(stop_order.orderId, FX_order('EURUSD'), stop_order)

####################################################################

app.disconnect()