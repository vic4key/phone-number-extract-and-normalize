import phonenumbers

def normalize_phone_number(text: str) -> str:
	''' Normalize a phone number to standard international format.
	Eg. 0981234567
	'''
	result = ""
	try:
		tmp = phonenumbers.parse(text, "VN")
		result = f"0{tmp.national_number}"
	except Exception as e: pass
	return result

def extract_phone_numbers(text: str) -> list:
	''' Extract phone numbers from text then normalize them to standard international format.
	Eg. ["0981234567"]
	'''
	result = []
	# your code here
	return result
