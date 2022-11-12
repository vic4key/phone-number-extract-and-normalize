from main import *

def test():
	''' Test function
	'''

	# Note: phone numbers that 11 digits are removed in VN several years ago
	# so we don't need to test them

	# SĐT 10 số

	list_test_10_digits =\
	[
		# None
		'981234567',
		'98 123 4567',
		'98.123.4567',
		'98-123-4567',
		# 098
		'0981234567',
		'098 123 4567',
		'098.123.4567',
		'098-123-4567',
		# 84
		'84981234567',
		'84 98 123 4567',
		'84 98.123.4567',
		'84 98-123-4567',
		# 84 098
		'840981234567',
		'84 098 123 4567',
		'84 098.123.4567',
		'84 098-123-4567',
		# (84)
		'(84)981234567',
		'(84) 98 123 4567',
		'(84) 98.123.4567',
		'(84) 98-123-4567',
		# (84) 098
		'(84)0981234567',
		'(84) 098 123 4567',
		'(84) 098.123.4567',
		'(84) 098-123-4567',
		# +84
		'+84981234567',
		'+84 98 123 4567',
		'+84 98.123.4567',
		'+84 98-123-4567',
		# +84 098
		'+840981234567',
		'+84 098 123 4567',
		'+84 098.123.4567',
		'+84 098-123-4567',
		# (+84)
		'(+84)981234567',
		'(+84) 98 123 4567',
		'(+84) 98.123.4567',
		'(+84) 98-123-4567',
		# (+84) 098
		'(+84)0981234567',
		'(+84) 098 123 4567',
		'(+84) 098.123.4567',
		'(+84) 098-123-4567',
	]

	list_test_10_digits_text_multi_lines =\
		"\n".join(list_test_10_digits)

	# SĐT 10 số in text multi-lines

	for text in list_test_10_digits:
		phone_number = normalize_phone_number(text)
		assert phone_number == "0981234567", text

	print("ALL TEST CASES ARE PASSED (LIST 10-DIGITS PHONE NUMBERS)")

	phone_numbers = extract_phone_numbers(list_test_10_digits_text_multi_lines)
	for phone_number in phone_numbers:
		assert phone_number == "0981234567", phone_number

	print("ALL TEST CASES ARE PASSED (LIST 10-DIGITS PHONE NUMBERS IN TEXT MULTI-LINES)")

if __name__ == "__main__": test()