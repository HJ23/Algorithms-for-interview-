morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

def find(words):
	ss=set()
	for word in words:
		ss.add("".join(map(lambda x:morse[ord(x)-ord('a')],word)))
	return len(ss)
