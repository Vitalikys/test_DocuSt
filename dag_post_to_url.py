import json
from datetime import datetime, timedelta

import pendulum # маятник/  Python datetimes made easy.
import requests
from airflow.decorators import dag, task


@dag(
    schedule=timedelta(minutes=5), # https://crontab.guru/
    start_date=pendulum.datetime(2023, 1, 1, tz="Europe/Kiev"),
    catchup=False,
    tags=["post current time", 'Python', 'Test task'],
    doc_md= '* Extension for test task - POST to Flask API *',
    # https://airflow.apache.org/docs/apache-airflow/stable/tutorial/fundamentals.html#default-arguments
    default_args={
        "email": ["airflow@example.com", 'vitalikys@gmail.com'],
        "email_on_failure": True,
        "email_on_retry": False,
        'end_date': datetime(2024, 1, 1),
        "retry_delay": timedelta(minutes=60),
    }
)
def vitalik_api():
    @task()
    def extract() -> str:
        """ Function to get current time for body """
        time_now = datetime.now().strftime("%d-%B-%Y, %H:%M:%S")
        from airflow.models import Variable
        index = Variable.get("index", deserialize_json=False, default_var=':)')
        return time_now + index

    @task()
    def transform(time_now: str) -> str:
        data = 'Dag execution ' + time_now
        payload = json.dumps({"value": data})
        return payload

    @task()
    def post_to_url(payload: str):
        key_day = datetime.now().strftime("%d.%m.%Y-%M")
        url = f"http://78.27.236.114:8080/flask/{key_day}"
        headers = {'Content-Type': 'application/json'}
        requests.post(url, headers=headers, data=payload)

    time_ = extract()
    data_to_payload = transform(time_)
    post_to_url(data_to_payload)


# [START dag_invocation]
vitalik_api()
# [END dag_invocation]
