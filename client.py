################################################################################
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500


def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    """ ------------- Update this function ------------- """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price)/2
    return stock, bid_price, ask_price, price


def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    """ ------------- Update this function ------------- """
    #if price_b == 0, then price_a/price_b would be problematic - nothing divided by 0 goes well! A quick filter to divvy up values of price_b between 0 and non-zero values is all that is necessary to prevent any issues.
    if (price_b == 0):
        return
    return (price_a/price_b)


# Main
if __name__ == "__main__":
    # Below is a relatively sloppy solution - I am still learning a lot when it comes to python, and a constantly filling/emptying list seemed like the most apt solution
    TempStorage=[]
    # Query the price once every N seconds.
    for _ in iter(range(N)):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        """ ----------- Update to get the ratio --------------- """
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))
            #Fill TempStorage so that I can call getRatio with the correct values
            TempStorage.append(price)
        print("Ratio %s" % getRatio(TempStorage[0], TempStorage[1]))
        #It is essential to clear the list otherwise the same value will be repeated ad infinitum, which is unideal as that does not occur in reality.
        TempStorage.clear()
