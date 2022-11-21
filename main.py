import phonenumbers
import re

# @refer to PyVutils.Utils.RegEx
'''
Eg. text   = "16x09.bin\nimage_07x02.bin"
    regex  = r"([\d]+)x([\d]+)"
    result = [('16', '09'), ('07', '02')]
'''
def RegEx(text, regex, flags = re.MULTILINE | re.IGNORECASE):
    result = re.findall(regex, text, flags)
    if len(result) == 1 and not type(result[0]) is tuple: result = [(result[0],)]
    return result

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

	groups = RegEx(text, R"([+-\. \(\)\d]+)")
	for group in groups:
		tmp = ""
		group_type = type(group)
		if group_type is tuple: tmp = " ".join(group)
		elif group_type is str: tmp = group
		else: assert False, "unknown extraction group"
		tmp = tmp.strip().replace(' ', '') # .replace('.', '').replace('-', '').replace('(', '').replace(')', '').replace(')', '')
		if len(tmp) < 9: continue # 098.123.4567 # at least 9 digits - 2 for area code and 7 for international numbers
		tmp = normalize_phone_number(tmp)
		result.append(tmp)

	return result
