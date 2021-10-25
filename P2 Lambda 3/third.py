import time
import boto3


DATABASE = 'parcialpunto2'
TABLE = 'news'
S3_OUTPUT = 's3://punto2parcial2/LambdaParticion/'
S3_BUCKET = 'punto2parcial2'

def handler(event, context):
    query = 'MSCK REPAIR TABLE `news`;'
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