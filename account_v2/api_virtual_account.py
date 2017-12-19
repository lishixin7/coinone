import api, json,pprint

URL = 'https://api.coinone.co.kr/v2/account/virtual_account/'


def get_result():
	content = api.get_response(URL, api.PAYLOAD)
	content = json.loads(content)

	return content


if __name__ == "__main__":
	pprint.pprint(get_result())
