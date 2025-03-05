import abc


class StockPriceDatasetAdapter(metaclass=abc.ABCMeta):
    """
    Interface to access any datasource of stock price data
    """
    DEFAULT_TIKER = "PFE"

    @property
    @abc.abstractmethod
    def training_set(self, ticker= None):
        """
        Property to get the training set of stock prices for a given ticker
        :param ticker:
        :return:
        """
        ...
    @property
    @abc.abstractmethod
    def validation_set(self, ticker=None):
        """
        Property to get the validation set of stock prices for a given ticker
        :param ticker:
        :return:
        """
        ...