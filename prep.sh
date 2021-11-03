#!/bin/bash

set_return() { return $1; }
FLASK_APP=flask_app.py flask run > /dev/null &
FLASK_PID=$!

locust -f locust_test.py --csv=prefix1 --headless -t20s --host http://localhost:5000 > /dev/null
locust -f locust_test.py --csv=prefix2 --headless -t20s --host http://localhost:5000 > /dev/null

kill $FLASK_PID
set_return 0
