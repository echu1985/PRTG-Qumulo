# PRTG-Qumulo
Python scripts for monitoring Qumulo Quotas.

Replace URL from your ENDPOINT and Access Token

# Change Endpoint name and token from Bearer

Example:

endpoint = "https://qumulo.domain.com/v1/files/quotas/status/"

token = "session-v1:7LfFVZKlo48wOIS3h+W7Py5YffZTR61PQuM9d3TavcABAAAAeJwL7O9MYQCCj9JdYPqcDQMDG5BmZILQskDwAzA0a+Q=="

1 - Save script in your Custom Sensor folder in prtg.
C:\Program Files (x86)\PRTG Network Monitor\Custom Sensors\python\

2- Add sensor 

![image](https://github.com/echu1985/PRTG-Qumulo/assets/47377572/90dcf22e-379f-4b2c-8cda-13052be83be5)

3 - Select your Script.
![image](https://github.com/echu1985/PRTG-Qumulo/assets/47377572/317a12e0-b3fc-4c60-9889-db5576d2d860)


![image](https://github.com/echu1985/PRTG-Qumulo/assets/47377572/d50d1eba-a87c-4afb-98a9-a7dffd391f81)


Output JSON format:

{"prtg": {"text": "QUOTAS-QUMULO", "result": [{"Channel": "/Datos1/", "Value": 92.0, "DecimalMode": "All", "Float": 1, "Unit": "Percent", "SpeedSize": "One", "VolumeSize": "One", "SpeedTime": "Second", "Mode": "Absolute", "LimitErrorMsg": "Percentage too high", "LimitMode": 1}, {"Channel": "/Pacs_Largo_Plazo_S/", "Value": 91.0, "DecimalMode": "All", "Float": 1, "Unit": "Percent", "SpeedSize": "One", "VolumeSize": "One", "SpeedTime": "Second", "Mode": "Absolute", "LimitErrorMsg": "Percentage too high", "LimitMode": 1}, {"Channel": "/Datos6/", "Value": 91.0, "DecimalMode": "All", "Float": 1, "Unit": "Percent", "SpeedSize": "One", "VolumeSize": "One", "SpeedTime": "Second", "Mode": "Absolute", "LimitErrorMsg": "Percentage too high", "LimitMode": 1}, {"Channel": "/Datos5/", "Value": 90.0, "DecimalMode": "All", "Float": 1, "Unit": "Percent", "SpeedSize": "One", "VolumeSize": "One", "SpeedTime": "Second", "Mode": "Absolute", "LimitErrorMsg": "Percentage too high", "LimitMode": 1}, {"Channel": "/Datos3/", "Value": 93.0, "DecimalMode": "All", "Float": 1, "Unit": "Percent", "SpeedSize": "One", "VolumeSize": "One", "SpeedTime": "Second", "Mode": "Absolute", "LimitErrorMsg": "Percentage too high", "LimitMode": 1}, {"Channel": "/IMGDEX_DATA4/DENSITO/", "Value": 82.0, "DecimalMode": "All", "Float": 1, "Unit": "Percent", "SpeedSize": "One", "VolumeSize": "One", "SpeedTime": "Second", "Mode": "Absolute", "LimitErrorMsg": "Percentage too high", "LimitMode": 1}, {"Channel": "/IMGDEX_DATA4/HCD/", "Value": 79.0, "DecimalMode": "All", "Float": 1, "Unit": "Percent", "SpeedSize": "One", "VolumeSize": "One", "SpeedTime": "Second", "Mode": "Absolute", "LimitErrorMsg": "Percentage too high", "LimitMode": 1}, {"Channel": "/IMGDEX_DATA4/Consentiments/", "Value": 87.0, "DecimalMode": "All", "Float": 1, "Unit": "Percent", "SpeedSize": "One", "VolumeSize": "One", "SpeedTime": "Second", "Mode": "Absolute", "LimitErrorMsg": "Percentage too high", "LimitMode": 1}, {"Channel": "/IMGDEX_DATA4/Informes/", "Value": 72.0, "DecimalMode": "All", "Float": 1, "Unit": "Percent", "SpeedSize": "One", "VolumeSize": "One", "SpeedTime": "Second", "Mode": "Absolute", "LimitErrorMsg": "Percentage too high", "LimitMode": 1}, {"Channel": "/images/import/", "Value": 5.0, "DecimalMode": "All", "Float": 1, "Unit": "Percent", "SpeedSize": "One", "VolumeSize": "One", "SpeedTime": "Second", "Mode": "Absolute", "LimitErrorMsg": "Percentage too high", "LimitMode": 1}, {"Channel": "/Datos4/", "Value": 91.0, "DecimalMode": "All", "Float": 1, "Unit": "Percent", "SpeedSize": "One", "VolumeSize": "One", "SpeedTime": "Second", "Mode": "Absolute", "LimitErrorMsg": "Percentage too high", "LimitMode": 1}, {"Channel": "/Datos0/", "Value": 93.0, "DecimalMode": "All", "Float": 1, "Unit": "Percent", "SpeedSize": "One", "VolumeSize": "One", "SpeedTime": "Second", "Mode": "Absolute", "LimitErrorMsg": "Percentage too high", "LimitMode": 1}, {"Channel": "/analiticas2009/", "Value": 86.0, "DecimalMode": "All", "Float": 1, "Unit": "Percent", "SpeedSize": "One", "VolumeSize": "One", "SpeedTime": "Second", "Mode": "Absolute", "LimitErrorMsg": "Percentage too high", "LimitMode": 1}, {"Channel": "/devops/", "Value": 66.0, "DecimalMode": "All", "Float": 1, "Unit": "Percent", "SpeedSize": "One", "VolumeSize": "One", "SpeedTime": "Second", "Mode": "Absolute", "LimitErrorMsg": "Percentage too high", "LimitMode": 1}, {"Channel": "/sistemas/", "Value": 2.0, "DecimalMode": "All", "Float": 1, "Unit": "Percent", "SpeedSize": "One", "VolumeSize": "One", "SpeedTime": "Second", "Mode": "Absolute", "LimitErrorMsg": "Percentage too high", "LimitMode": 1}, {"Channel": "/repositorio2/data/", "Value": 75.0, "DecimalMode": "All", "Float": 1, "Unit": "Percent", "SpeedSize": "One", "VolumeSize": "One", "SpeedTime": "Second", "Mode": "Absolute", "LimitErrorMsg": "Percentage too high", "LimitMode": 1}]}}
