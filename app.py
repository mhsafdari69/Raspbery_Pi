from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)
import os
import RPi.GPIO as GPIO


# @app.route("/")
# def hallo(): os.system('echo "20" > /sys/class/gpio/export; echo "out" >
# /sys/class/gpio/gpio20/direction; echo "0" > /sys/class/gpio/gpio20/value')


# class User:
#     def __init__(self, identi, username, password):
#         self.id = identi
#         self.username = username
#         self.password = password
#
#     def __repr__(self):
#         return self.username


app = Flask(__name__)
# users = []
# mahta = users.append(User(1025, username='mahta', password='breath'))
# users.append(User(1024, username='mahbod', password='123231312'))
# app.secret_key = 'somesecretkeythatonlyishouldknow'


# @app.before_request
# def before_request():
#     g.user = None
#
#     if 'user_id' in session:
#         user = [x for x in users if x.id == session['user_id']][0]
#         g.user = user


# @app.route('/login', methods=['GET', 'POST'])
# @app.route('/', methods=['GET', 'POST'])
# # def login():
#     if request.method == 'POST':
#         session.pop('user_id', None)
#         username = request.form['username']
#         pas = request.form['pass']
#         for x in users:
#             if x.username == username and x.password == pas:
#                 session['user_id'] = x.id
#                 return redirect(url_for('profile'))
#     return render_template('login.html')


@app.route('/', methods=['GET', 'POST'])
def profile():
    # if not g.user:
    # return redirect(url_for('login'))
    if request.method == 'POST':
        checkbox = request.form.getlist('checkbox')
        print("++++++ mahbod ++++++", checkbox)
        try:
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(20, GPIO.OUT)
            GPIO.setup(26, GPIO.OUT)
            GPIO.setup(21, GPIO.OUT)
            print(len(checkbox))
            if len(checkbox) == 0:
                GPIO.output(21, False)
                GPIO.output(20, False)
                GPIO.output(26, False)
                return render_template('profile.html')
            else:
                if '1' in checkbox:
                    try:
                        GPIO.output(21, True)
                        print("switch_1 on")
                    except:
                        pass
                else:
                    try:
                        GPIO.output(21, False)
                        print("switch_1 off")
                    except:
                        pass
                # -------------------------------------
                if '2' in checkbox:
                    try:
                        GPIO.output(20, True)
                        print("switch_2 on")
                    except:
                        pass
                else:
                    try:
                        GPIO.output(20, False)
                        print("switch_2 off")
                    except:
                        pass
                # ------------------------------------
                if '3' in checkbox:
                    try:
                        GPIO.output(26, True)
                        print("switch_3 on")
                    except:
                        pass
                else:
                    try:
                        GPIO.output(26, False)
                        print("switch_3 off")
                    except:
                        pass

                return render_template('profile.html')
        except:
            return redirect(url_for('not_work'))
    else:
        return render_template('profile.html')


@app.route('/not_work')
def not_work():
    return render_template('not_work.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
