import json
import oandapyV20
from oandapyV20 import API
import oandapyV20.endpoints.pricing as pricing
import oandapyV20.endpoints.instruments as instruments

# OANDA API V20の口座IDとAPIトークン
accountID = "111-222-3333333-444"
access_token="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"

def test1():
    params ={"instruments": "EUR_USD,EUR_JPY"}

    # OANDAのデモ口座へのAPI接続
    api = API(access_token=access_token, environment="practice")

    r = pricing.PricingInfo(accountID=accountID, params=params)
    rv = api.request(r)

    print(rv['prices'][0]['bids'][0]['price'])

def test2():
    params = {"count": 10, "granularity": "D"}

    api = API(access_token=access_token, environment="practice")

    r = instruments.InstrumentsCandles(instrument="USD_JPY", params=params)

    rv = api.request(r)
    print(rv)

    p0 = rv['candles'][0]['mid']['c']
    p1 = rv['candles'][1]['mid']['c']
    p2 = rv['candles'][2]['mid']['c']
    p3 = rv['candles'][3]['mid']['c']
    p4 = rv['candles'][4]['mid']['c']
    p5 = rv['candles'][5]['mid']['c']
    p6 = rv['candles'][6]['mid']['c']
    p7 = rv['candles'][7]['mid']['c']
    p8 = rv['candles'][8]['mid']['c']
    p9 = rv['candles'][9]['mid']['c']

    print (p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)

    if p0 < p1:
        print ('↑')
    else:
        print ('↓')



if __name__ == '__main__':
    test1()
    test2()
