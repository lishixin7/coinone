import requests, json


def get_result(currency, period):
	"""
	:param currency:btc, bch, eth, etc, xrp, qtum, ltc, iota, btg
	:param period:minute,hour, day
	:return:
	"""
	res = requests.get("https://api.coinone.co.kr/trades/?currency={}&period={}".format(currency, period))
	return json.loads(res.text)


if __name__ == "__main__":
	import pprint
	res=get_result("qtum","hour")
	pprint.pprint(res)
