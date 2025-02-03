import logging
import boto3
from aws_lambda_powertools.utilities.data_classes import APIGatewayProxyRequest, APIGatewayProxyResponse
from aws_lambda_powertools.utilities.data_classes import event_source

# Initialize DynamoDB client
dynamodb = boto3.client('dynamodb')

def handler(event, context):
    try:
        # Define parameters for updating DynamoDB item
        table_name = "cloud-resume-challenge"
        key = {
            "ID": {"S": "visitors"}
        }
        update_expression = "ADD visitors :inc"
        expression_attribute_values = {
            ":inc": {"N": "1"}
        }

        # Update item in DynamoDB
        response = dynamodb.update_item(
            TableName=table_name,
            Key=key,
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values
        )

    except Exception as e:
        logging.error(f"Got error calling update_item: {e}")
        raise

    # Return a successful response with CORS headers
    return APIGatewayProxyResponse(
        status_code=200,
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Headers": "*",
        },
        body="",
    )


# For local testing or actual Lambda function execution
if __name__ == "__main__":
    # Simulate an API Gateway ProxyRequest for testing
    event = {}  # You can replace this with a mock event for local testing
    context = {}  # Replace with your context object if needed
    handler(event, context)
