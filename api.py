import base64, json, hashlib, hmac, requests, time

with open("../key.json") as f:
	keys = json.load(f)
	ACCESS_TOKEN = keys["AccessToken"]
	SECRET_KEY = keys["SecretKey"]

PAYLOAD = {
	"access_token": ACCESS_TOKEN,
}


def get_encoded_payload(payload):
	payload[u'nonce'] = int(time.time() * 1000)

	dumped_json = json.dumps(payload)
	encoded_json = base64.b64encode(bytes(dumped_json, 'utf-8'))
	return encoded_json


def get_signature(encoded_payload, secret_key):
	signature = hmac.new(bytes(secret_key, 'utf-8'), bytes(encoded_payload), hashlib.sha512)
	return signature.hexdigest()


def get_response(url, payload):
	encoded_payload = get_encoded_payload(payload)
	headers = {
		'Content-type': 'application/json',
		'X-COINONE-PAYLOAD': encoded_payload,
		'X-COINONE-SIGNATURE': get_signature(encoded_payload, SECRET_KEY)
	}
	res = requests.post(url, data=encoded_payload, headers=headers)
	return res.text
