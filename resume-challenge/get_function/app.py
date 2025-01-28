import json
import requests
from aws_lambda_powertools.utilities.data_classes import APIGatewayProxyRequest, APIGatewayProxyResponse
import logging

# Constants
DEFAULT_HTTP_GET_ADDRESS = "https://checkip.amazonaws.com"
ERR_NON_200_RESPONSE = "Non 200 Response found"

def handler(event, context):
    try:
        # Send HTTP GET request to the default address
        response = requests.get(DEFAULT_HTTP_GET_ADDRESS)

        # Check if the response status code is 200
        if response.status_code != 200:
            raise Exception(ERR_NON_200_RESPONSE)

    except Exception as e:
        logging.error(f"Error: {e}")
        # Return error response
        return APIGatewayProxyResponse(
            status_code=500,
            body=json.dumps({"error": str(e)}),
            headers={
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "*",
                "Access-Control-Allow-Headers": "*",
            },
        )

    # Return a successful response with count in the body
    return APIGatewayProxyResponse(
        status_code=200,
        body=json.dumps({"count": "2"}),
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Headers": "*",
        },
    )

# For local testing or actual Lambda function execution
if __name__ == "__main__":
    # Simulate an event and context for testing
    event = {}  # Replace with a mock event if needed
    context = {}  # Replace with your context object if needed
    print(handler(event, context))
