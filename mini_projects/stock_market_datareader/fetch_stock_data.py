from email.errors import CloseBoundaryNotFoundDefect
import pandas as pd
from pandas_datareader import DataReader

from datetime import datetime

stocks_list = ["FB",
               "AMZN",
               "NFLX",
               "GOOG"]

start = datetime(datetime.now().year - 1,
                 datetime.now().month,
                 datetime.now().day)

end = datetime.now()

for stock in stocks_list:

    globals()[stock] = DataReader(stock, "yahoo", start, end)


# print(FB.describe())
# print(AMZN)
print(NFLX.info())
