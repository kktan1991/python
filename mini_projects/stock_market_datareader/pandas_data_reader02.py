# import packages
from lib2to3.pgen2.pgen import DFAState
from typing import Any
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import style

# insert the stock quotes "TSLA", "NFLX"
stocks = [
    "AAPL", "GOOG", "AMZN", "MSFT"
]

start_date = "2022-01-01"
end_date = "2022-09-12"

data = web.DataReader(stocks, "yahoo", start_date, end_date)

close = data['Adj Close']
# print(close)


# adjusting the style
plt.style.use("fivethirtyeight")  # Other styles: "dark_background","ggplot",

ax = close.plot(title=[])
ax.set_title("Stock Performance")
ax.set_xlabel("Date")
ax.set_ylabel("Stock Price ($)")
ax.grid()
plt.legend()
plt.show()
