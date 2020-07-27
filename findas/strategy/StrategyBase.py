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

    def simulate_transaction(self):
        if self.df.empty:
            return
        share = INIT_SHARE

        last_state, last_market, market_list = 0, None, []
        for i, r in self.df.iterrows():
            if r.deal == 1:
                if r.deal == last_state:
                    # 继续持有
                    last_market = r.price * share
                else:
                    # 重新买入
                    if last_state == 0:
                        last_market = r.price * share
                    else:
                        share = last_market / r.price
            else:
                if r.deal == last_state:
                    # 继续空仓
                    pass
                else:
                    # 清仓
                    last_market = r.price * share
                    share = 0

            market_list.append({'date': i, 'market': last_market})

            last_state = r.deal

        market_df = pd.DataFrame(data=market_list)
        market_df = market_df.set_index('date')
        self.df = self.df.join(market_df)

