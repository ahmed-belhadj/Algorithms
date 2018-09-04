#!/usr/bin/python

import argparse


def find_max_profit(prices):
    profits = []
    for i, price in enumerate(prices):
        for i2 in range(i, len(prices)):
            try:
                profits.append(prices[i2+1]-price)
            except IndexError:
                pass
    return max(profits)


if __name__ == '__main__':
    # This is just some code to input accepting inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
