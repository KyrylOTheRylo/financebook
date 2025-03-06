import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials

from best_stock_price_dateset_Adaptor import BestStockDatasetAdaptor


class YahooFinancialAdapter(BestStockDatasetAdaptor):

    def __init__(self,
                 ticker=BestStockDatasetAdaptor.DEFAULT_TIKER,
                 frequency="1d",

                 training_set_range=("2020-01-01", "2021-12-31"), validation_set_range=("2022-01-01", "2022-12-31")):
        super().__init__(ticker=ticker)
        self._frequency = frequency
        self._yf = yf
        self._training_set = self._connect_and_prepare(training_set_range)
        self._validation_set = self._connect_and_prepare(validation_set_range)

    def _connect_and_prepare(self, data_range: tuple):
        stock_price_record = None
        records = yf.download(self._ticker, start=data_range[0], end=data_range[1], interval=self._frequency)
        stock_data = records.reset_index()[["Date", "Close"]]
        stock_data.rename(columns={"Date": "time", "Close": "stock price"}, inplace=True)

        return stock_data


def test_yahoo_financial_adapter():
    import matplotlib.pyplot as plt
    yahoo_financial_adapter = YahooFinancialAdapter()
    records = yahoo_financial_adapter.training_set
    data = records["time"].values
    prices = records["stock price"].values.flatten()
    plt.plot(data, prices)
    plt.show()


if __name__ == "__main__":
    test_yahoo_financial_adapter()
