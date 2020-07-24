import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta


INIT_SHARE = 1000


class StrategyBase(object):
    start = date(2015, 1, 5)
    end = None
    df = pd.DataFrame()

    def __init__(self):
        pass

    def buy_

    def simulate_transaction(self):
        if self.df.empty:
            return
        share = INIT_SHARE

        empty, last_market, market_list = True, None, []
        for i, r in self.df.iterrows():
            if empty and r.deal == -1:
                market_list.append({'date': i, 'market': last_market})
                continue
            if r.deal == -1:
                share = last_market / r.price
                last_market = None
                empty = True
            elif r.deal == 0:
                if not empty:
                    last_market = r.price * share
                else:

            else:
                last_market = r.price * share
                empty = False

            market_list.append({'date': i, 'market': last_market})

