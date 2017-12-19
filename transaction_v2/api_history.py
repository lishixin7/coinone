import api, json, pprint

URL = "https://api.coinone.co.kr/v2/transaction/history/"


def get_result(currency):
	PAYLOAD = api.PAYLOAD
	PAYLOAD["currency"] = currency
	content = api.get_response(URL, PAYLOAD)
	content = json.loads(content)

	return content


if __name__ == "__main__":
	pprint.pprint(get_result("btc"))
