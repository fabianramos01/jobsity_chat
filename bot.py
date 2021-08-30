import csv
import re
from json import dumps, loads

import websocket
import _thread

from requests import get

from decouple import config

def get_stock_data(stock_code):
    data = get(f'https://stooq.com/q/l/?s={stock_code}&f=sd2t2ohlcv&h&e=csv')
    decode_content = data.content.decode('utf-8')
    if decode_content == 'Ticker missing':
        return 'Error: Ticker missing'
    else:
        reader_list = csv.DictReader(decode_content.splitlines())
        result = next(reader_list)
        if result['Close'] != 'N/D':
            return f'{result["Symbol"]} quote is ${result["Close"]} per share'
        else:
            return 'Error: Wrong stock code'

def on_message(wsocket, message):
    data = loads(message)
    if pattern_stock.match(data['message']):
        # stock_code = 'aapl.us'
        stock_code = data['message'].replace('/stock=', '')
        data = {
            'message': get_stock_data(stock_code),
            'owner': 'bot'
        }
        wsocket.send(dumps(data))

def on_error(wsocket, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print('----- Connection closed -----')

def on_open(wsocket):
    def run(*args):
        print('----- Connection open -----')
        print('The bot is running')
    _thread.start_new_thread(run, ())

if __name__ == '__main__':
    pattern_stock = re.compile(r'^/stock=.*')
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp(f'ws://{config("CHAT_HOST")}/chat/jobsity/',
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)
    ws.run_forever()