import json
import random
import datetime

stock_data: dict = {}

def write_stock_data_in_json(f, name, ticker, price_range, date):
    """
    Write stock data in json format to file
    :param f: file
    :param name: stock name
    :param ticker: stock ticker
    :param price_range: price range
    :return: None
    """

    data = {
        "name": name,
        "ticker": ticker,
        "price": random.uniform(price_range[0], price_range[1]),
        "dcf": random.uniform(price_range[0], price_range[1]),
        "date": date
    }
    f.write("\t")
    json.dump(data, f)


def generate_price_range(price):
    """
    Generate price range
    :param price: stock price
    :return: price range
    """
    price_range = [round(price - price * 0.5, 2), round(price + price * 0.5, 2)]
    return price_range


def read_stock_data_from_csv():
    """
    Read stock data from csv file
    :return: stock data
    """
    print('reading stock data from csv file')
    with open("nasdaq.csv", "r") as f:
        i = -2
        for line in f:
            i += 1
            if i == -1: continue

            print('reading line: ', i, ' of 5015', end='\r')

            split_line = line.split(",")
            stock_data[i] = {
                'ticker': split_line[0],
                'name': split_line[1],
                'price_range': generate_price_range(float(split_line[2][1:])),
            }
        
        f.close()

    print('finished reading stock data from csv file\n')




if __name__ == '__main__':
    with open("output/stock_data.json", "w") as f:
        read_stock_data_from_csv()

        company_set = {}
        print('generating stock data')
        f.write("[\n")
        for i in range(55):
            # get unique stock ticker
            stock_index = 8
            while stock_data[stock_index]['name'] in company_set:
                stock_index = random.randint(0, len(stock_data) - 1)
            
            # assign stock informatoin
            stock_information = stock_data[stock_index]

            # add information to company set
            company_set[stock_information['name']] = True
            print('generating ', stock_information['name'], ' data')

            for j in range(1825):
                # generate date
                date = datetime.datetime.now() - datetime.timedelta(days=j)
                date = date.strftime("%Y-%m-%d")

                print('\tgenerating day ', j, ' of 1825', end='\r')
                # write stock data in json format
                write_stock_data_in_json(
                    f,
                    stock_information['name'],
                    stock_information['ticker'],
                    stock_information['price_range'],
                    date
                )

                if i != 54 or j != 1824: f.write(',')
                f.write('\n')

        f.write("]")
        print('finished generating stock data')

    f.close()