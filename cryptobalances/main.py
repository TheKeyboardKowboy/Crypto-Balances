import argparse
from services import chain_request
from services import eth_request
from services import doge_request


def main():
    parser = argparse.ArgumentParser(description='Getting balance of wallet of your crypto currency')
    parser.add_argument('currency', nargs='?', type=str, help='Type of currency')
    parser.add_argument('wallet', nargs='?', type=str, help='Identifier of wallet')
    args = parser.parse_args()
    if (args.currency and args.wallet) is not None:
        if args.currency == 'BTC':
            print(chain_request(args.currency, args.wallet))
        elif args.currency == 'LTC':
            print(chain_request(args.currency, args.wallet))
        elif args.currency == 'ETH':
            print(eth_request(args.wallet))
        elif args.currency == 'DOGE':
            print(doge_request(args.wallet))


if __name__ == "__main__":
    main()
