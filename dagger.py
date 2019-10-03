from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'Al',
    'depends_on_past': False,
    'start_date': datetime(2019, 10, 1),
    'email': ['kunalnano@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG('tutorial', default_args=default_args, schedule_interval=timedelta(days=1))

# t1, t2, t3 and t4 are examples of tasks created by instantiating operators
t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag)

t2 = BashOperator(
    task_id = 'Array_1_10',
    bash_command='seq 0 10 1',
    dag=dag)

t3 = BashOperator(
    task_id = 'get_text',
    bash_command='txt_sample = wget http://www.gutenberg.org/files/1342/1342-0.txt',
    dag=dag)


t4 = BashOperator(
    task_id='wrd_text',
    bash_command='python /Users/kunalsharma/Library/Mobile Documents/com~apple~CloudDocs/TechField/Assignments/techfield/wordcount_txt.py',
    dag=dag)

t4.set_upstream(t3)
