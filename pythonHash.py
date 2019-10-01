import sys
import hashlib

#function that create md5 string in UTF8
def doMD5(strToHash):
    newHash = hashlib.md5()
    
    newHash.update(strToHash.encode('utf-8'))

    return newHash.hexdigest()


try:
	#get string
	strToHash = sys.argv[1]

	# str to lower
	strToHash = strToHash.lower()

	#md5
	newHash = doMD5(strToHash)

	#print new hash
	print (newHash)

	
except NameError:
	print ("There is an error")

except IndexError:
	print ("Please, inform a value to create the hash")
