import matplotlib.pyplot as plt
import pandas as pd
import ydata_profiling


def build_a_simple_graph(data):
    data["price"] = data["price"]
    data["volume"] = data["volume"] / 1000000
    data["marketcap"] = data["marketcap"] / 10000000
    data.set_index('date', inplace=True)

    data.plot(figsize=(15, 6))

    plt.title('Bitcoin-metrics chart')
    plt.xlabel('Date')
    plt.ylabel('Value')

    plt.xticks(data.index[::31], [date.strftime('%b %Y') for date in data.index[::31]])

    plt.legend(["Price in USD", "Volume in USD x0.000001", "Marketcap in USD x0.0000001"], loc='upper left')
    plt.tight_layout()
    plt.savefig('bitcoin_chart.png')
    plt.show()


def build_a_graph(data):
    data["price"] = data["price"]
    data["volume"] = data["volume"] / 1000000
    data["daily_active_addresses"] = data["daily_active_addresses"] / 10
    data.set_index('date', inplace=True)

    data.plot(figsize=(15, 6))

    plt.title('Bitcoin-metrics chart')
    plt.xlabel('Date')
    plt.ylabel('Value')

    plt.xticks(data.index[::30], [date.strftime('%b %Y') for date in data.index[::30]])

    plt.legend(["Price in USD", "Volume in USD x0.000001", "Daily active addresses x0.1"], loc='upper left')
    plt.tight_layout()
    plt.savefig('bitcoin_chart_extended.svg')
    plt.show()

def correlations(data):

    profile = ydata_profiling.ProfileReport(data, title="Bitcoin-metrics")
    profile.to_file('correlations.html')


if __name__ == '__main__':
    data = pd.read_json('bitcoin_data_extended.json')
    # build_a_graph(data)
    correlations(data)

