import argparse
# from memory_profiler import memory_usage
import sched
import psutil
import time
import requests
import json


def collect_args():
    """
    Function to collect arguments for memory usage script.
    The argparse module makes it easy to write user-friendly command-line interfaces.
    """
    parser = argparse.ArgumentParser(description='Script for checking memory usage')
    parser.add_argument('--url',
                        type=str,
                        default='78.27.202.55:8080/flask',
                        help='target URL')
    parser.add_argument('--message',
                        type=str,
                        default='RAM usage is reach the limit !',
                        help='message to send',
                        required=False)
    parser.add_argument('--time', type=int,
                        default=20,
                        choices=range(60, 360, 60),
                        help='Time interval to check memory usage, in seconds. step 60 sec')
    args = parser.parse_args()
    # print('args.url = ', args.url)  # call argument URL
    return args


def main(local_handler):
    try:
        # got current RAM memory usage of system (in percents)
        memory_usage = psutil.virtual_memory().percent

        if memory_usage > 60:  # checking if memory used more than 70%
            headers = {'Content-Type': 'application/json'}
            url = args.url+'/memory_alarm'
            payload = json.dumps({'value': args.message})
            
            r = requests.post(url=url, data=payload, headers=headers)
        #     print('after post', r.status_code)
        # print('memory_usage', memory_usage)
        local_handler.enter(args.time, 1, main, (local_handler,))
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    args = collect_args()
    print('start here')
    my_scheduler = sched.scheduler(time.time, time.sleep)
    my_scheduler.enter(args.time, 1, main, (my_scheduler,))
    my_scheduler.run()
