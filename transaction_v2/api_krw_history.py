import api, json, pprint

URL = "https://api.coinone.co.kr/v2/transaction/krw/history/"


def get_result():
	PAYLOAD = api.PAYLOAD
	content = api.get_response(URL, PAYLOAD)
	content = json.loads(content)

	return content


if __name__ == "__main__":
	pprint.pprint(get_result())
