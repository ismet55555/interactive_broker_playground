# interactive_broker_playground
Just testing things out with interactive broker API


## Installation and Setup

### Interactive Broker TWS

- Download, install, run, and log-in
    - https://www.interactivebrokers.com/en/index.php?f=16042

- Change Settings
    - File > Global Configuration > API > Settings
    - Check: `Enable ActiveX and Socket Clients`
    - Uncheck: `Read-Only API`
    - Ensure: `Socket port: 7497`
    - Check: `Allow connections form localhost only` *(Uncheck if connecting from remote computer)*


### Python Tools
1. `python3 -m venv env`
2. `source env/bin/activate`
3. `pip install -r requirements.txt`


## Notes

- Connection
    - `Python API -> TWS/Gateway Client -> Interactive Broker Servers`

- Python Script Communication
    - Outgoing: `Python Script -> EClient -> TWS/Gateway Client`
    - Incoming: `Python Script <- EWrapper <- TWS/Gateway Client`

- [Available Tick Types](https://interactivebrokers.github.io/tws-api/tick_types.html)
- [Market Data Types](https://interactivebrokers.github.io/tws-api/market_data_type.html)

## Links

- Native Python API
    - [Tutorial](https://algotrading101.com/learn/interactive-brokers-python-api-native-guide/)

- `ib_insync` Python Library
    - [GitHub Repo](https://github.com/erdewit/ib_insync)
    - [Tutorial](https://algotrading101.com/learn/ib_insync-interactive-brokers-api-guide/)
    - Details:
        - Utilizes asynchronous methods to communicate with the native API to increase efficiency.
        - Utilizes the asyncio library to provide an asynchronous single thread to interact with the API
        - Simplifies the process of receiving data from the API.

- `IbPy` Python Library
    - [GitHub Repo](https://github.com/blampe/IbPy)