import streamlit as st
import google.analytics.data_v1beta as data_v1beta
from google.oauth2 import service_account

# Replace with the path to your credentials JSON file
credentials_file = "credentials.json"

# Replace with your Google Analytics property ID
property_id = "475812416"

# Create a service client
credentials = service_account.Credentials.from_service_account_file(credentials_file)
client = data_v1beta.BetaAnalyticsDataClient(credentials=credentials)

# Create a request
request = data_v1beta.RunReportRequest(
    property="properties/" + property_id,
    dimensions=[
        data_v1beta.Dimension(
            name="city"
        ),
        data_v1beta.Dimension(
            name="country"
        )
    ]
)



async def make_request():
    response = await client.run_report(request=request)
    return response

# Run the request
response = make_request()

# Print the results
st.write(response)
for row in response.rows:
    st.write(row.dimension_values[0].value, row.dimension_values[1].value, row.metric_values[0].value)
