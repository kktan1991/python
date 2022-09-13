# import packages
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

start_date = "2021-12-31"
end_date = "2022-09-11"

data = web.DataReader(name="TSLA", data_source='yahoo',
                      start=start_date, end=end_date)
print(data)

close = data['Close']
ax = close.plot(title='Telsa')
ax.set_xlabel('Date')
ax.set_ylabel('Close')
ax.grid()
plt.show()
