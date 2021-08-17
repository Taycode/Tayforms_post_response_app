"""Consumer"""

from kafka import KafkaConsumer
import json
from logics import logics as logic_dict

consumer = KafkaConsumer(
	'form-responses',
	group_id='tayforms',
	bootstrap_servers=['localhost:9092'],
	auto_offset_reset='earliest',
	enable_auto_commit=True,
	value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print('Consumer Started')
for message in consumer:
	print('message received')
	response = message.value
	logics = response.get('logic')
	response_data = response.get('response')

	for _ in logics:
		logic_function = logic_dict[_.get('code')]
		parameters = _.get('parameters')
		logic_function(response_data, params=parameters)
