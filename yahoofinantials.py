from yahoofinancials import YahooFinancials


def get_yahoo_data():
    """
        Method to get exchanges from Euros to Dollars on 5 different days.
        link: https://finance.yahoo.com/currency-converter
    :return:
    """
    currencies = ['EURUSD=X']  # type currencies
    data = YahooFinancials(currencies).get_historical_price_data("2022-08-01", "2022-08-6", "daily")  #getData from YahooAPI
    return data
