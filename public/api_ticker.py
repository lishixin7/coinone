import requests,json
def get_result(currency):
	"""
	:param currency: btc, bch, eth, etc, xrp, qtum, iota, ltc, btg
	:return:
	"""
	res=requests.get("https://api.coinone.co.kr/ticker/?currency="+currency)
	return json.loads(res.text)

if __name__=="__main__":
	import pprint
	pprint.pprint(get_result("qtum"))