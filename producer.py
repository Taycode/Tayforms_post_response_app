"""Producer"""

import json
from kafka import KafkaProducer

producer = KafkaProducer(
	bootstrap_servers=['localhost:9092'],
	value_serializer=lambda m: json.dumps(m).encode(),
)

producer.send('form-responses', {
	'logic': [
		{
			'code': 'write_to_sheet',
			'parameters': {}
		},
		{
			'code': 'print_response',
			'parameters': {}
		}
	],
	'response': {
		'form_id': 3,
		'answers': {
			245: {
				'answer': 'abd@def.com',
				'question': 'Your email',
				'question_id': 245
			},
			246: {
				'answer': 'Mr ABC',
				'question': 'Your Name',
				'question_id': 246
			}
		}
	}
})
producer.flush()
print('sent')
