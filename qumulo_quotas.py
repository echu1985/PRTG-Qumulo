import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
##Comment Disable Warning Lib if your https is not self signed

from paesslerag_prtg_sensor_api.sensor.result import CustomSensorResult
from paesslerag_prtg_sensor_api.sensor.units import ValueUnit



# Change Endpoint name and token from Bearer
endpoint = "https://##REPLACE-ENDPOINTNAME##/v1/files/quotas/status/"
token = "session-v1:"##REPLACE-TOKEN##"

headers = {
	"Content-Type": "application/json",
	"Authorization": f"Bearer {token}"
}

result = requests.get(url=endpoint, headers=headers, verify=False)
quotas = json.loads(result.text)["quotas"]

csr = CustomSensorResult(text="QUOTAS-QUMULO")
for quota in quotas:

	csr.add_primary_channel(name=quota["path"],
                        value=round((int(quota["capacity_usage"]) * 100) / int(quota["limit"]),0),
                        unit=ValueUnit.PERCENT,
                        is_float=True,
                        is_limit_mode=True,
 #                       limit_max_warn=90,
 #                       limit_max_error=95,
                        limit_error_msg="Percentage too high")


print(csr.json_result)
