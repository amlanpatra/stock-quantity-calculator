def FuturesBrokerageCalc(price, sl, quantity=50):
    buy = price
    sell = price
    turnover = (buy+sell)*quantity
    brokerage = 40
    stt = round(((sell*quantity)*(0.025))/100, 2)
    exchange_txn_charge = round((turnover*0.00345)/100, 2)
    gst = round((brokerage+exchange_txn_charge)*0.18, 2)
    sebi = round((10/10000000)*turnover, 2)
    stamp = round((0.003*(buy*quantity)/100), 2) if (buy *
                                                     quantity) < 10000000 else 300

    total_brokerages = round(brokerage +
                             stt+exchange_txn_charge+gst+sebi+stamp, 2)

    breakeven = round((abs(total_brokerages))/quantity, 2)
    risk = total_brokerages + (sl * quantity)

    arr = [total_brokerages, breakeven, risk]
    return arr


# arr = FuturesBrokerageCalc(37500, 23)
# print("Risk : {}".format(str(arr[2])))
# print("breakeven : {}".format(str(arr[1])))
# print("Brokerage is : {}".format(str(arr[0])))
