"""Google Sheets"""

import pygsheets
from pygsheets.exceptions import SpreadsheetNotFound


class GoogleSheet:
	"""Google Sheet Module"""

	service = pygsheets.authorize(service_account_file='../key.json')

	def create_sheet(self, title):
		"""Creates Google sheet"""
		return self.service.create(title)

	def get_sheet_by_id(self, sheet_id):
		"""Gets sheet by Id"""
		return self.service.sheet.get(sheet_id)

	def get_sheet_by_title(self, title):
		"""Gets sheet by Id"""
		return self.service.open(title)

	def process_add_to_sheet_logic(self, form_id):
		"""Process add to sheet logic"""
		form_sheet_title = f'Response - {form_id}'
		try:
			sheet = self.get_sheet_by_title(form_sheet_title)
		except Exception as E:
			print(E)
			sheet = self.create_sheet(form_sheet_title)
		