import requests
import time

IFTTT_WEBHOOKS_URL = 'https://maker.ifttt.com/trigger/test_event/with/key/dSQFvOqEuO42HiLjP01HeV'
IFTTT_Key = 'dSQFvOqEuO42HiLjP01HeV'
EVENT_NAME = 'test_event'

def get_latest_bitcoin_price():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    response = requests.get(url)
    response_json = response.json()
    type(response_json)
    print(response_json)
    return response_json['bpi']['USD']['rate']

def send_notification(event, value):
    payload = {'value1': value}
    url = IFTTT_WEBHOOKS_URL.format(event=event, key=IFTTT_Key)
    response = requests.post(url, json=payload)
    print("Notification sent", response.text)

def main():
    price = get_latest_bitcoin_price()
    send_notification(EVENT_NAME, price)
    time.sleep(60*60) # Sleep for 1 hour

if __name__ == '__main__':
    main()