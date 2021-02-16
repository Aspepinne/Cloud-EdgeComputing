from flask import Flask, render_template
from dynamodb import get_all_sensors, get_all_by_sensorname

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sensors')
def get_Sensors():
    main_door_1 = get_all_by_sensorname('main_door_1')
    main_door_2 = get_all_by_sensorname('main_door_2')
    return render_template('users.html', main_door_1=main_door_1, main_door_2=main_door_2)


if __name__ == '__main__':
    app.run()
