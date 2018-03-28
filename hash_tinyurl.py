from hashlib import blake2b

#tinyurl creator

base_url = 'http://xurl.com/'


def create_mikeurl(starting_url):
	
	while True:
		
		try:
			
			if len(starting_url) > 10:  # check to make sure the url is actually longer than the mikeurl will be
			
				large_url = starting_url
				
			else:
				
				print('\nThe starting url is pretty short, not going to do anything to it\n')
				return starting_url
		
			large_url = bytearray(large_url, 'UTF-8')
			large_url = int.from_bytes(large_url, byteorder='big', signed=False)
			large_url = str(hash(large_url))
			
			# turn it back into a bytearray to use blake2b to turn the long string into a short string
			
			large_url = bytearray(large_url, 'UTF-8')
			
			tiny_url = base_url + str(blake2b(key=large_url, digest_size=2).hexdigest())
	
			return tiny_url
		
		except ValueError:
			
			print("Could not convert data to a bytes array.")
			break
			
		except:
			
			print("Something went wrong")
			break
		
		# http://www.facebook.com/whateverthisis/_everyotherhtmlfile
		# http://mikeurl.com/f51e5eb9522bc1e6
	
	
starting_url = 'http://www.facebook.com'
print('Starting url: {}'.format(starting_url) + '\nNew, shorter url {}'.format(create_mikeurl(starting_url)))