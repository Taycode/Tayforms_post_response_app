"""Google Sheets"""

import pygsheets
from pygsheets.exceptions import SpreadsheetNotFound


class GoogleSheet:
	"""Google Sheet Module"""

	service = pygsheets.authorize(service_account_file='key.json')

	def create_sheet(self, title):
		"""Creates Google sheet"""
		return self.service.create(title)

	def get_sheet_by_id(self, sheet_id):
		"""Gets sheet by Id"""
		return self.service.sheet.get(sheet_id)

	def get_sheet_by_title(self, title):
		"""Gets sheet by Id"""
		return self.service.open(title)

	def process_add_to_sheet_logic(self, form_id, answers, questions):
		"""Process add to sheet logic"""
		form_sheet_title = f'Response - {form_id}'
		try:
			sheet = self.get_sheet_by_title(form_sheet_title)
			print('sheet exists')
		except SpreadsheetNotFound:
			sheet = self.create_sheet(form_sheet_title)
			print('sheet created', sheet.url)
			worksheet = sheet.sheet1
			worksheet.append_table(values=questions)
			sheet.share('', role='reader', type='anyone')
			print('sheet shared to everyone')

		worksheet = sheet.sheet1
		worksheet.append_table(values=answers)


def write_to_sheet(response, **params):
	"""Writes to sheet"""
	google_sheet = GoogleSheet()
	form_id = response.get('form_id')
	answers = response.get('answers')
	answers_array = [answers[_].get('answer') for _ in answers.keys()]
	questions_array = [answers[_].get('question') for _ in answers.keys()]
	google_sheet.process_add_to_sheet_logic(form_id, answers_array, questions_array)
	print('Write to sheet process completed')
