import requests

api_client = requests.Session()

response = api_client.post(
    f"/v1/installments/{{installment.external_id}}/postpone",
    json={"postpone_until": {"postpone_until": "postpone_until.strftime(YYYY_MM_DD_FORMAT)"}},
)


print(response.status_code)
print(response.json())

