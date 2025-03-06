from abc import ABC, abstractmethod

from stock_price_adaptor import StockPriceDatasetAdapter


class BestStockDatasetAdaptor(StockPriceDatasetAdapter, ABC):
    def __init__(self, ticker:str = None):
        self._ticker = ticker
        self._training_set = None
        self._validation_set = None

    @abstractmethod
    def _connect_and_prepare(self, data_range: tuple):
        """
        Connect to the data source and prepare the data
        :param data_range:
        :return:
        """
        ...

    @property
    def training_set(self, ticker= None):
        return self._training_set
    @property
    def validation_set(self, ticker=None):
        return self._validation_set
    