# Random Stock Generator

To generate random stock data, all you have to do is:

```bash
$ python data_generator.py
```

This will create a file with 100,000 data points of companies called `stock-data.json`. Every data point will be structured like:

```typescript
type Datum = {
    name: string;
    ticker: string;
    date: 'YYYY-MM-DD'
    price: number;
    dcf: number;
}
```

And this data will be presented as an `Array<Datum>` 

> **Disclaimer:** Don't delete the `nasdaq.csv` that is where we pull company data from.