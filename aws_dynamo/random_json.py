import random
import time
import json

def main():
    with open('data.json', 'w') as json_file:
        data = []
        for i in range(1, 20):
            d = {
                'deviceid': i,
                'devicename': 'device' + str(i),
                'data': {
                    'sensor_value': random.randrange(10, 120),
                    'timestamp': time.time()
                }
            }
            data.append(d)
            time.sleep(0.5)
        json.dump(data, json_file)


if __name__ == '__main__':
    main()
