# report.py
#
# Exercise 2.4
# pcost.py

import csv
from pprint import pprint


def read_portfolio(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            portfolio_items = dict(zip(headers, row))
            portfolio.append(portfolio_items)

    return portfolio


def read_prices(filename):
    '''
    Reading the prices of stocks in a portfolio file and store it in a dictionary
    '''

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        price = {}
        for row in rows:
            try:
                price[row[0]] = float(row[1])
            except IndexError:
                pass

    return price


'''
for portfolio_item in portfolio:
    stock_name = portfolio_item["name"]
    stock_previous_price = float(portfolio_item["price"])
    stock_current_price = prices[stock_name]
    portfolio_item["current value"] = round(stock_current_price *
                                            int(portfolio_item["shares"]), 2)
    portfolio_item["gain/loss"] = round(float(portfolio_item["shares"]) *
                                        (stock_current_price-stock_previous_price), 2)
'''


def make_report(portfolio, prices):
    """Make a table with stock name, shares, current share proce and change in price."""
    report = []
    for portfolio_item in portfolio:
        change = round(prices[portfolio_item["name"]] -
                       float(portfolio_item["price"]), 2)
        report.append(
            (portfolio_item["name"], portfolio_item["shares"], prices[portfolio_item["name"]], change))
    return report


def print_report(report):
    '''
    Print the portfolio report in a formatted way.
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(
        f"{headers[0]:>10s}{headers[1]:>10s}{headers[2]:>10s}{headers[3]:>10s}")
    print('---------- ---------- ---------- -----------')
    for name, shares, price, change in report:
        prices_with_sigh = "$"+str(price)
        print(f"{name:>10s}{shares:>10s}{prices_with_sigh:>10s}{change:>10.02f}")


def portfolio_report(porfolio_filename, prices_filename):
    portfolio = read_portfolio(porfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)


portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
portfolio_report('Data/portfolio2.csv', 'Data/prices.csv')

files = ['Data/portfolio.csv', 'Data/portfolio2.csv']
for name in files:
    print(f'{name:-^43s}')
    portfolio_report(name, 'Data/prices.csv')
    print()
