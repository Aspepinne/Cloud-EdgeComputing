import json

from flask import Flask, render_template
from dynamodb import get_all_by_sensorname

app = Flask(__name__)


@app.route('/')
def index():
    main_door_1 = get_all_by_sensorname('main_door_1')
    return render_template('index.html', main_door_1=main_door_1)


@app.route('/load')
def load():
    main_door_1 = get_all_by_sensorname('main_door_1')
    main_door_2 = get_all_by_sensorname('main_door_2')
    return render_template('load.html', main_door_1=main_door_1, main_door_2=main_door_2)


@app.route('/someoneoutside')
def someoneoutside():
    return render_template('someoneoutside.html')


@app.route('/nooneoutside')
def nooneoutside():
    return render_template('nooneoutside.html')


@app.route('/sensors')
def get_sensors():
    main_door_1 = get_all_by_sensorname('main_door_1')
    main_door_2 = get_all_by_sensorname('main_door_2')
    return render_template('sensors.html', main_door_1=main_door_1, main_door_2=main_door_2)


@app.route('/check')
def check():
    sensors = get_all_by_sensorname('main_door_1')
    fixed_sensors=[]
    for sensor in sensors:
        sensor['sensorid'] = int(sensor['sensorid'])
        sensor['info']['temp'] = int(sensor['info']['temp'])
        fixed_sensors.append(sensor)
    return json.dumps(fixed_sensors)


if __name__ == '__main__':
    app.run()