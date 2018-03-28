class ReverseWordsInAString(object):
	
	def reverse_words(s):
		"""
		:type s: str
		:rtype: str
		"""
		s = s.split(' ')
		new_string = ''
		for words in reversed(s):
			new_string = new_string + words + ' '
		
		new_string = new_string.strip()
		return new_string
	
	print(reverse_words('here is a test'))