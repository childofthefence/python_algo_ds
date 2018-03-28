from hashlib import blake2b

#tinyurl creator

base_url = 'http://xurl.com/'


def create_mikeurl(starting_url):
	
	while True:
		
		try:
			
			if len(starting_url) > 20:  # check to make sure the url is actually longer than the mikeurl will be
			
				large_url = starting_url
				
			else:
				
				print('\nThe starting url is pretty short, not going to do anything to it\n')
				return starting_url
		
			large_url = bytearray(large_url, 'UTF-8')
			large_url = int.from_bytes(large_url, byteorder='big', signed=False)
			large_url = str(hash(large_url))
			large_url = bytearray(large_url, 'UTF-8')
			
			tiny_url = base_url + str(blake2b(key=large_url, digest_size=4).hexdigest())
	
			return tiny_url
		
		except ValueError:
			
			print("Could not convert data to a bytes array.")
			break
			
		except:
			
			print("Something went wrong")
			break
		
		# http://www.facebook.com/whateverthisis/_everyotherhtmlfile
		# http://mikeurl.com/f51e5eb9522bc1e6
	
	
starting_url = 'https://www.google.com/maps/place/20909+Sandstone+Square,+Sterling,+VA+20165/@39.0371926,-77.3980246,17z/data=!3m1!4b1!4m5!3m4!1s0x89b639edde5b47fd:0xda3aba0be5e9cfce!8m2!3d39.0371885!4d-77.3958359'
print('Starting url: {}'.format(starting_url) + '\nNew, shorter url {}'.format(create_mikeurl(starting_url)))