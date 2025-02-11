from google.analytics.data_v1beta import BetaMetricsServiceAsyncClient
from google.oauth2 import service_account
import asyncio

# Replace with the path to your credentials JSON file
credentials_file = "path/to/your/credentials.json"

# Replace with your Google Analytics property ID
property_id = "your_property_id"

# Create a service client
credentials = service_account.Credentials.from_file(credentials_file)
client = BetaMetricsServiceAsyncClient(credentials=credentials)

# Create a request
request = BetaMetricsServiceAsyncClient.RunReportRequest(
    property="properties/" + property_id,
    dimensions=[
        BetaMetricsServiceAsyncClient.Dimension(name="date"),
        BetaMetricsServiceAsyncClient.Dimension(name="country"),
    ],
    metrics=[
        BetaMetricsServiceAsyncClient.Metric(name="activeUsers"),
    ],
    date_ranges=[
        BetaMetricsServiceAsyncClient.DateRange(start_date="2023-01-01", end_date="2023-01-31"),
    ],
)



async def make_request():
    response = await client.run_report(request=request)
    return response

# Run the request
response = make_request()

# Print the results
for row in response.rows:
    print(row.dimension_values[0].value, row.dimension_values[1].value, row.metric_values[0].value)
