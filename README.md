# interactive_broker_playground

In this repository we are simply playing around with the Interactive Brokers API

# Repo Setup

This repository is divided into two sections.

1. Native API Scripts (`native_api`)

   - This library is developed and maintained by Interactive Brokers
   - It is downloaded via the Interactive Brokers website and installed manually
   - Documentation: https://interactivebrokers.github.io/tws-api/index.html

2. `ib_insync`
   - This library is a wrapper on the native interactive broker API
   - It makes working with the native library easier and asynchronous
   - GitHub Repo: https://github.com/erdewit/ib_insync

# Installation and Setup

### Interactive Broker Trader Workstation (TWS)

In order to use any code that interacts with the interactive broker servers, a local client has to be installed.
This local client can either be the TWS or the Interactive Broker Gateway.

- TWS: Download, install, run, and log-in

  - https://www.interactivebrokers.com/en/index.php?f=16042

- TWS: Change Settings
  - File > Global Configuration > API > Settings
  - Check: `Enable ActiveX and Socket Clients`
  - Uncheck: `Read-Only API`
  - Ensure: `Socket port: 7497`
  - Check: `Allow connections form localhost only` _(Uncheck if connecting from remote computer)_

# Market/Data Analysis Tools

Interactive brokers API is great for getting data and managing orders, however for any data or market analysis another tools needed. The following tools enable any technical analysis.

### Stockstats

A open-source technical analysis tool for python.

- GitHub Repo: https://github.com/jealous/stockstats
- `pip install stockstats`

### TA-Lib Market Analysis Tool

TA-Lib is an open-source technical analysis toolkit. See [home page](https://ta-lib.org/).
While the original library is not available in Python, a wrapper is available to allow Python users access.

- GitHub Repo: https://github.com/mrjbq7/ta-lib
- Follow instructions how to download compressed file and build from source
- `pip install ta-lib`

### Bta-Lib Market Analysis Tool

- GitHub Repo: https://github.com/mementum/bta-lib
- Website: https://btalib.backtrader.com/
- `pip install bta-lib`

# NOTES

- Connection

  - `Python API -> TWS/Gateway Client -> Interactive Broker Servers`

- Python Script Communication

  - Outgoing: `Python Script -> EClient -> TWS/Gateway Client`
  - Incoming: `Python Script <- EWrapper <- TWS/Gateway Client`

- P1L0veTorontoUrenan823

# Links

- Native Python API

  - [Tutorial](https://algotrading101.com/learn/interactive-brokers-python-api-native-guide/)
  - [Available Tick Types](https://interactivebrokers.github.io/tws-api/tick_types.html)
  - [Market Data Types](https://interactivebrokers.github.io/tws-api/market_data_type.html)

  - Historical Data

    - [Requesting Historical Bar Data](https://interactivebrokers.github.io/tws-api/historical_bars.html)
    - [Historical Data Limitations](https://interactivebrokers.github.io/tws-api/historical_limitations.html)
    - Examples:
      - [Get Historical Data - Github Gist](https://gist.github.com/robcarver17/f50aeebc2ecd084f818706d9f05c1eb4#file-temp-py)
      - [CLI to Download Historical Data - GitHub Gist](https://gist.github.com/wrighter/dd201adb09518b3c1d862255238d2534)
      - [Receiving Market Data and Historical Candlesticks](https://tradersacademy.online/trading-topics/trader-workstation-tws/receiving-market-data-and-historical-candlesticks)

  - Orders

    - [Available Orders](https://interactivebrokers.github.io/tws-api/available_orders.html)
    - [Order Managment](https://interactivebrokers.github.io/tws-api/order_management.html)

  - Message Codes
    - [Message Codes](https://interactivebrokers.github.io/tws-api/message_codes.html)

- `ib_insync` Python Library

  - [Tutorial](https://algotrading101.com/learn/ib_insync-interactive-brokers-api-guide/)
  - Details:
    - Utilizes asynchronous methods to communicate with the native API to increase efficiency.
    - Utilizes the asyncio library to provide an asynchronous single thread to interact with the API
    - Simplifies the process of receiving data from the API.

- `IbPy` Python Library
  - Another library and a wrapper of the Interactive Broker API
  - [GitHub Repo](https://github.com/blampe/IbPy)
