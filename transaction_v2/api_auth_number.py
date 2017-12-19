import api, json, pprint

URL = "https://api.coinone.co.kr/v2/transaction/auth_number/"


def get_result(type):
	PAYLOAD = api.PAYLOAD
	PAYLOAD["type"] = type
	content = api.get_response(URL, PAYLOAD)
	content = json.loads(content)

	return content


if __name__ == "__main__":
	pprint.pprint(get_result("btc"))
