import os
import time
import threading
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from multiprocessing import Process
from multiprocessing import Value


name = os.environ["NAME"]
requests_in_process_number = Value('i', 0)

app = Flask(__name__)
server = Process(target = lambda: app.run(host='0.0.0.0', threaded = True))

@app.route('/')
def main():
    global name
    global requests_in_process_number

    threading.Thread(target=process).start()

    return f'service_name: {name}; requests_in_process_number: {requests_in_process_number.value}'

def process():
    global requests_in_process_number
    requests_in_process_number.value += 1
    time.sleep(1)
    requests_in_process_number.value -= 1

def log_current_number_requests():
    if not server.is_alive():
        return
    global requests_in_process_number
    app.logger.warning(f'requests_in_process: {str(requests_in_process_number.value)}')

def start_server():
    global server
    global requests_in_process_number

    if server.is_alive():
        return

    app.logger.warning('Server is starting...')
    
    requests_in_process_number.value = 0

    server = Process(target = lambda: app.run(host='0.0.0.0'))
    server.start()

def stop_server():
    global server
    if not server.is_alive():
        return

    app.logger.error('Server is shutting down...')

    server.terminate()
    server.join()

if __name__ == '__main__':
    server.start()

    scheduler = BackgroundScheduler()
    scheduler.add_job(func = log_current_number_requests, trigger = 'interval', seconds = 10)
    if os.environ["HAS_PROBLEMS"] == 'True':
        scheduler.add_job(func = start_server, trigger = 'interval', seconds = 100)
        scheduler.add_job(func = stop_server, trigger = 'interval', seconds = 200)
    scheduler.start()

    while True:
        pass