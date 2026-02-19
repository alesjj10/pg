from cviceni6_2 import download_rates
import sys


def convert(amount_czk, rates):
    result = {}
    rates = download_rates('http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt')

    for currency, rate in rates.items():
        result[currency] = amount_czk / rate
    return result


if __name__ == "__main__":



    conversions = convert(amount_czk)

    for currency, conversion in conversions.items():
        print(currency, conversion)