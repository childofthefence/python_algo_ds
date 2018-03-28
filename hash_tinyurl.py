from hashlib import blake2b

#tinyurl creator

base_url = 'http://mikeurl.com/'


def create_mikeurl(starting_url):
	
	while True:
		
		try:
			
			if len(starting_url) > 35: # check to make sure the url is actually longer than the mikeurl will be
			
				large_url = starting_url
				
			else:
				
				print('\nThe starting url is pretty short, not going to do anything to it\n')
				return starting_url
		
			large_url = bytes(large_url, 'UTF-8')
	
			tiny_url = base_url + str(blake2b(key=large_url, digest_size=8).hexdigest())
	
			return tiny_url
		
		except:
			
			print("Something went wrong")
			continue
		
		# http://www.facebook.com/whateverthisis/_everyotherhtmlfile
		# http://mikeurl.com/f51e5eb9522bc1e6
	
	
starting_url = input('Please enter the url to shorten: ')
print('Starting url: {}'.format(starting_url) + '\nNew, shorter url {}'.format(create_mikeurl(starting_url)))