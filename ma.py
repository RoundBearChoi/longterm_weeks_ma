import pandas as pd
import matplotlib.pyplot as plt
import cryptocompare
from datetime import datetime


def plot_moving_average(weeks):
    print('Hi..')
    print('Calculating ' + str(weeks) + '-week moving average..')

    # Fetch daily price data for Bitcoin
    data1 = cryptocompare.get_historical_price_day(
        'BTC', currency='USD', limit=2000, toTs=datetime.now())
    data2 = cryptocompare.get_historical_price_day(
        'BTC', currency='USD', limit=2000, toTs=datetime.now() - pd.DateOffset(days=2000))

    # Convert lists to DataFrames
    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)

    # Concatenate the DataFrames
    df = pd.concat([df2, df1])
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df.set_index('time', inplace=True, drop=False)

    # Calculate moving average
    df['moving_avg'] = df['close'].rolling(window=7 * weeks).mean()

    # Plot
    plt.figure(figsize=(14, 7))
    plt.plot(df['close'], label='Bitcoin Price')
    plt.plot(df['moving_avg'], label=f'{weeks}-Week Moving Average')
    plt.title('Bitcoin Price and Moving Average')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.show()


# Call the function with the number of weeks you want
plot_moving_average(140)
