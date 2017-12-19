import api, json, pprint

URL = 'https://api.coinone.co.kr/v2/order/cancel/'



def get_result(order_id,price,qty,is_ask,currency):
	PAYLOAD = api.PAYLOAD
	PAYLOAD["order_id"] = order_id
	PAYLOAD["price"] = price
	PAYLOAD["qty"] = qty
	PAYLOAD["is_ask"] = is_ask
	PAYLOAD["currency"] = currency
	content = api.get_response(URL, PAYLOAD)
	content = json.loads(content)

	return content


if __name__ == "__main__":
	pprint.pprint(get_result("orderid",500000,0.1,1,"btc"))
