import json
import urllib.request


class Currency:
    URL = "https://free.currencyconverterapi.com/api/v5/" \
          "convert?q={}_{}&compact=y"

    def get_rates(self, f, s):
        response = json.load(urllib.request.urlopen(self.URL.format(f, s)))
        return response[f'{f}_{s}']['val']
