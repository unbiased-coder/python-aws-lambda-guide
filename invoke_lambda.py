import boto3_helper

session = boto3_helper.init_aws_session()
lambda_client = session.client('lambda')

lambda_payload = '{"first_name" : "Unbiased", "last_name"  : "Coder"}'

res = lambda_client.invoke(FunctionName='unbiased_coder_lambda', InvocationType='RequestResponse', Payload=lambda_payload)

print('Lambda return: ', end='')
while True:
    try:
        content = res['Payload'].next()
        print(content)
    except StopIteration:
        break
