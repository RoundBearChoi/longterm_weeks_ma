import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import cryptocompare
from datetime import datetime


def plot_moving_average(weeks):
    print('Hi..')
    print('Calculating ' + str(weeks) + '-week moving average..')

    # Fetch daily price data for Bitcoin
    days_limit = 1600

    data1 = cryptocompare.get_historical_price_day(
        'BTC', currency='USD', limit=days_limit, toTs=datetime.now())
    data2 = cryptocompare.get_historical_price_day(
        'BTC', currency='USD', limit=days_limit, toTs=datetime.now() - pd.DateOffset(days=days_limit))

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
    plt.style.use('ggplot')
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(df['moving_avg'], label=f'{weeks}-Week Moving Average', linewidth=1)
    ax.plot(df['close'], label='Bitcoin Price', linewidth=1)
    ax.set_ylabel('Price (USD)')
    ax.legend()
    ax.grid(False)

    # Add commas to y-axis
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

    plt.show()


if __name__ == '__main__':
    # Call the function with the number of weeks you want
    plot_moving_average(140)
