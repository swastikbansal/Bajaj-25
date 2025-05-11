import requests
import json

sql_query = """ 
SELECT
  e1.EMP_ID,
  e1.FIRST_NAME,
  e1.LAST_NAME,
  D.DEPARTMENT_NAME,
  COUNT(e2.EMP_ID) AS YOUNGER_EMPLOYEES_COUNT
FROM EMPLOYEE AS e1
JOIN DEPARTMENT AS D
  ON e1.DEPARTMENT = D.DEPARTMENT_ID
LEFT JOIN EMPLOYEE AS e2
  ON e2.DEPARTMENT = e1.DEPARTMENT
  AND e2.DOB > e1.DOB
GROUP BY
  e1.EMP_ID,
  e1.FIRST_NAME,
  e1.LAST_NAME,
  D.DEPARTMENT_NAME
ORDER BY
  e1.EMP_ID DESC;
"""

url = "https://bfhldevapigw.healthrx.co.in/hiring/testWebhook/PYTHON"

headers = {"Authorization": "eyJhbGciOiJIUzI1NiJ9.eyJyZWdObyI6IlJFRzEwMzAiLCJuYW1lIjoiU3dhc3RpayBCYW5zYWwiLCJlbWFpbCI6InN3YXN0aWtiYW5zYWwyMjA0NjFAYWNyb3BvbGlzLmluIiwic3ViIjoid2ViaG9vay11c2VyIiwiaWF0IjoxNzQ2OTYzMDU5LCJleHAiOjE3NDY5NjM5NTl9.Es8eWOd2yqcPK7QD8f1jt9mu8quCTAFsitPyrzo58-o",
           "Content-Type": "application/json"}

data = {
    "finalQuery": sql_query
}

payload = requests.post(url, headers=headers, json=data)

print(payload.text,payload)