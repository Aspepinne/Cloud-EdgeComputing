from dynamodb import get_all_sensors, create_sensor_table, store_Sensors
import json

def main():
    # create_sensor_table()
    # store_Sensors()
    # with open('sensor_data.json', 'r') as f:
    #     data = json.load(f)
    #     store_Sensors(data)
    sensors = get_all_sensors()
    if sensors:
        for sensor in sensors:
            print(sensor['info']['timestamp'])


if __name__ == '__main__':
    main()
