import api, json

URL = 'https://api.coinone.co.kr/v2/account/balance/'


def get_result():
	content = api.get_response(URL, api.PAYLOAD)
	content = json.loads(content)

	return content


if __name__ == "__main__":
	import pprint
	pprint.pprint(get_result())