import boto3
import logging
def lambda_handler(event, context):
 try:
  client = boto3.client('sagemaker')
  client.start_notebook_instance(NotebookInstanceName='yashaswi-notebook')
  client = boto3.client('sns')
  snsArn = '<arn of sns topic>'
  message = "Execution trigger has been successful"
  response = client.publish(
        TopicArn = snsArn,
        Message = message ,
        Subject='Lambda function execution status'
    )
  return response
 except Exception as e:
  client = boto3.client('sns')
  snsArn = '<arn of sns topic>'
  message = "Execution trigger has been failed"
  response = client.publish(
        TopicArn = snsArn,
        Message = message ,
        Subject='Lambda function execution status'
    )
  return response
