import api, json, pprint

URL = 'https://api.coinone.co.kr/v2/order/limit_buy/'


def get_result(price, qty, currency):
	PAYLOAD = api.PAYLOAD
	PAYLOAD["price"] = price
	PAYLOAD["qty"] = qty
	PAYLOAD["currency"] = currency
	content = api.get_response(URL, PAYLOAD)
	content = json.loads(content)

	return content


if __name__ == "__main__":
	pprint.pprint(get_result(500000, 0.1, "btc"))
