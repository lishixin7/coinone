import api, json, pprint

URL = 'https://api.coinone.co.kr/v2/order/order_info/'


def get_result(order_id, currency):
	PAYLOAD = api.PAYLOAD
	PAYLOAD["currency"] = currency
	PAYLOAD["order_id"] = order_id
	content = api.get_response(URL, PAYLOAD)
	content = json.loads(content)

	return content


if __name__ == "__main__":
	pprint.pprint(get_result("32FF744B-D501-423A-8BA1-05BB6BE7814A", "btc"))
