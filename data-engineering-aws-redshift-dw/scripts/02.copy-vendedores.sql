copy vendedores
from 's3://egalimentos-sales/data/vendedores.csv'
CREDENTIALS 'aws_access_key_id=<YOUR_AWS_ACCESS_KEY_ID>;aws_secret_access_key=<YOUR_AWS_SECRET_ACCESS_KEY>'
region 'sa-east-1'
delimiter ';'
IGNOREHEADER 1
DATEFORMAT 'DD/MM/YYYY';