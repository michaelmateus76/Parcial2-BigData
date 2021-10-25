import time
import boto3


DATABASE = 'parcialpunto1'
TABLE = 'stocks'
S3_OUTPUT = 's3://punto1parcial/LambdaParticion/'
S3_BUCKET = 'punto1parcial'

def handler(event, context):
    query = 'MSCK REPAIR TABLE `stocks`;'
    client = boto3.client('athena')

    # Execution
    response = client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={
            'Database': DATABASE
        },
        ResultConfiguration={
            'OutputLocation': S3_OUTPUT,
        }
    )
    return response