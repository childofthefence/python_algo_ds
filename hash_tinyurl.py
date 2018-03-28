from hashlib import blake2b

#tinyurl creator

base_url = 'http://mikeurl.com/'


def create_mikeurl(starting_url):
	
	while True:
		
		try:
			
			if len(starting_url) > 35:
			
				large_url = starting_url
				
			else:
				
				return starting_url
		
			large_url = bytes(large_url, 'UTF-8')
	
			tiny_url = base_url + str(blake2b(key=large_url, digest_size=8).hexdigest())
	
			return tiny_url
		
		except:
			
			print("Something went wrong")
			continue
		
		# http://www.facebook.com/whateverthisis/_everyotherhtmlfile
		# http://mikeurl.com/f51e5eb9522bc1e6
	
	
print(create_mikeurl('http://www.facebook.com/whateverthisis/_everyotherhtmlfile'))