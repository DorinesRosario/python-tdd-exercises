#command to run it: py.test -vv "filename"


########### NEW TEST ############


"This test will return the position of incorrect nucleotide(s)' in a DNA sequence"

valid_nucleotides = ['T', 'A', 'G', 'C']

def Seq_position (DNA_sequence):
	inc_position = []
	for position in range(len(DNA_sequence)):
		nucleotide = DNA_sequence[position]
		if nucleotide not in valid_nucleotides:
			inc_position.append(position)
	return inc_position


def test_Seq_position ():
	assert Seq_position('ACTGAD') == [5]



# __________________________________________________________________________

def reverse_list(l):
	l.reverse()
	return l


def test_reverse_list():
	assert reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]


# 2------------------------------------------------------------------------------

def reverse_string(s):
	return s[::-1]


def test_reverse_string():
	assert reverse_string("foobar") == "raboof"


# 3------------------------------------------------------------------------------

def is_english_vowel(c):
	vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'E', 'I', 'O', 'U', 'Y', 'A']
	if c in vowels:
		return True
	else:
		return False
	
def test_is_english_vowel():
	assert is_english_vowel('a')
	assert is_english_vowel('e')
	assert is_english_vowel('i')
	assert is_english_vowel('o')
	assert is_english_vowel('u')
	assert is_english_vowel('y')
	assert is_english_vowel('A')
	assert is_english_vowel('E')
	assert is_english_vowel('I')
	assert is_english_vowel('O')
	assert is_english_vowel('U')
	assert is_english_vowel('Y')
	assert not is_english_vowel('k')
	assert not is_english_vowel('z')
	assert not is_english_vowel('?')

	
# 4------------------------------------------------------------------------------

def count_num_vowels(s):
	z=0
	for i in s:
		if i in ('a', 'e', 'i', 'o', 'u', 'y', 'E', 'I', 'O', 'U', 'Y', 'A'):
			z=z+1
	return z
	

def test_count_num_vowels():
	sentence = "hey ho let's go"
	assert count_num_vowels(sentence) == 5
	sentence = "HEY ho let's GO"
	assert count_num_vowels(sentence) == 5
	paragraph = """She told me her name was Billie Jean,
					as she caused a scene
					Then every head turned with eyes
					that dreamed of being the on
					Who will dance on the floor in the round"""
	assert count_num_vowels(paragraph) == 53
	
# 5------------------------------------------------------------------------------

import pandas as pd
import collections
def histogram(l):
	data = []
	collections.Counter(data)
	z = ''
	for x in l:
		z=z+'#'*x+'\n'
	z=z[:-1]

	return z


def test_histogram():
	assert histogram([2, 5, 1]) == '##\n#####\n#'


# 6------------------------------------------------------------------------------

def get_word_lengths(s):
	list = []
	for z in s.split(' '):
		list.append(len(z))

	return list


def test_get_word_lengths():
	text = "Three tomatoes are walking down the street"
	assert get_word_lengths(text) == [5, 8, 3, 7, 4, 3, 6]


# 7------------------------------------------------------------------------------

def find_longest_word(s):
	list = [len(z) for z in s.split(' ')]
	for z in s.split(' '):
		if len(z) == max(list):
			return z
	return None


def test_find_longest_word():
	text = "Three tomatoes are walking down the street"
	assert find_longest_word(text) == "tomatoes"
	text = "foo foo1 foo2 foo3"
	assert find_longest_word(text) == "foo1"


# 8------------------------------------------------------------------------------

def validate_dna(s):
	for z in range(len(s)):
		if s[z] in ('a','t','c','g','A','T','C','G'):
			z = z + 1
			while z ==len(s)-1:
				return True
		else:
			return False


def test_validate_dna():
	assert validate_dna('CCGGAAGAGCTTACTTAGccggaagagcttacttag')
	assert not validate_dna('xCCGGAAGAGCTTACTTAGccggaagagcttacttag')
	assert not validate_dna('CCxGGAAGAGCTTACTTAGccggaagagcttacttag')


# 9------------------------------------------------------------------------------
	
def base_pair(c):
	if c in ('A','a'):
		return 't'
	elif c in ('T','t'):
		return 'a'
	elif c in ('c','C'):
		return 'g'
	elif c in ('g','G'):
		return 'c'
	else:
		return 'unknown'
	


def test_base_pair():
	assert base_pair('a') == 't'
	assert base_pair('t') == 'a'
	assert base_pair('c') == 'g'
	assert base_pair('g') == 'c'
	assert base_pair('A') == 't'
	assert base_pair('T') == 'a'
	assert base_pair('C') == 'g'
	assert base_pair('G') == 'c'
	assert base_pair('x') == 'unknown'
	assert base_pair('foo') == 'unknown'


# 10------------------------------------------------------------------------------

def transcribe_dna_to_rna(s):
	z =''
	for n in range(len(s)):
		if s[n]=='a':
			z+='A'
		elif s[n]=='t':
			z+='U'
		elif s[n]=='c':
			z+='C'
		elif s[n]=='g':
			z+='G'
		elif s[n]=='T':
			z+='U'
		else:
			z+=s[n]
	return z


def test_transcribe_dna_to_rna():
	dna = 'CCGGAAGAGCTTACTTAGccggaagagcttacttag'
	assert transcribe_dna_to_rna(dna) == 'CCGGAAGAGCUUACUUAGCCGGAAGAGCUUACUUAG'


# 11------------------------------------------------------------------------------

def get_complement(s):
	
	z=''
	for n in range(len(s)):
		if s[n]=='a':
			z+='T'
		elif s[n]=='t':
			z+='A'
		elif s[n]=='c':
			z+='G'
		elif s[n]=='g':
			z+='C'
		elif s[n]=='A':
			z+='T'
		elif s[n]=='T':
			z+='A'
		elif s[n]=='G':
			z+='C'
		elif s[n]=='C':
			z+='G'

	return z


def test_get_complement():
	assert get_complement('CCGGAAGAGCTTACTTAG') == 'GGCCTTCTCGAATGAATC'
	assert get_complement('ccggaagagcttacttag') == 'GGCCTTCTCGAATGAATC'


# 12------------------------------------------------------------------------------

def get_reverse_complement(s):
	z=""
	for n in range(len(s)):
		if s[n]=='a':
			z+='T'
		elif s[n]=='t':
			z+='A'
		elif s[n]=='c':
			z+='G'
		elif s[n]=='g':
			z+='C'
		elif s[n]=='A':
			z+='T'
		elif s[n]=='T':
			z+='A'
		elif s[n]=='G':
			z+='C'
		elif s[n]=='C':
			z+='G'

	return z[::-1]


def test_get_reverse_complement():
	assert get_reverse_complement('CCGGAAGAGCTTACTTAG') == 'CTAAGTAAGCTCTTCCGG'
	assert get_reverse_complement('ccggaagagcttacttag') == 'CTAAGTAAGCTCTTCCGG'


# 13------------------------------------------------------------------------------

def remove_substring(substring, string):
	"""
	Returns string with all occurrences of substring removed.
	"""
	return None


def test_remove_substring():
	assert remove_substring('GAA', 'CCGGAAGAGCTTACTTAG') == 'CCGGAGCTTACTTAG'
	assert remove_substring('CCG', 'CCGGAAGAGCTTACTTAG') == 'GAAGAGCTTACTTAG'
	assert remove_substring('TAG', 'CCGGAAGAGCTTACTTAG') == 'CCGGAAGAGCTTACT'
	assert remove_substring('GAA', 'GAAGAAGAA') == ''


# 14------------------------------------------------------------------------------

def get_position_indices(triplet, dna):
	"""
	Returns list of position indices for a specific triplet (3-mer)
	in a DNA sequence. We start counting from 0
	and jump by 3 characters from one position to the next.
	"""
	return None


def test_get_position_indices():
	assert get_position_indices('GAA', 'CCGGAAGAGCTTACTTAG') == [1]
	assert get_position_indices('GAA', 'CCGGAAGAGCTTACTTAGGAAGAA') == [1, 6, 7]


# 15------------------------------------------------------------------------------

def get_3mer_usage_chart(s):
	"""
	This routine implements a 'sliding window'
	and extracts all possible consecutive 3-mers.
	It counts how often they appear and returns
	a list of tuples with (name, occurrence).
	The list is alphabetically sorted by the name
	of the 3-mer.
	"""
	return None


def test_get_3mer_usage_chart():
	s = 'CCGGAAGAGCTTACTTAGGAAGAA'
	result = []
	result.append(('AAG', 2))
	result.append(('ACT', 1))
	result.append(('AGA', 2))
	result.append(('AGC', 1))
	result.append(('AGG', 1))
	result.append(('CCG', 1))
	result.append(('CGG', 1))
	result.append(('CTT', 2))
	result.append(('GAA', 3))
	result.append(('GAG', 1))
	result.append(('GCT', 1))
	result.append(('GGA', 2))
	result.append(('TAC', 1))
	result.append(('TAG', 1))
	result.append(('TTA', 2))
	assert get_3mer_usage_chart(s) == result


# 16------------------------------------------------------------------------------

def read_column(file_name, column_number):
	"""
	Reads column column_number from file file_name
	and returns the values as floats in a list.
	"""
	return None


def test_read_column():

	import tempfile
	import os

	text = """1   0.1  0.001
2   0.2  0.002
3   0.3  0.003
4   0.4  0.004
5   0.5  0.005
6   0.6  0.006"""

	# we save this text to a temporary file
	file_name = tempfile.mkstemp()[1]
	with open(file_name, 'w') as f:
		f.write(text)

	# and now we pass the file name to the function which will read the column
	assert read_column(file_name, 2) == [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]

	# we remove the temporary file
	os.unlink(file_name)


# 17------------------------------------------------------------------------------

def character_statistics(file_name):
	"""
	Reads text from file file_name, then
	lowercases the text, and then returns
	a tuple (x, y), where x is the most abundant
	and y is the least abundant but present character found.
	Use the isalpha() method to figure out
	whether the character is in the alphabet.
	"""
	return None


def test_character_statistics():

	import tempfile
	import os

	text = """
To be, or not to be: that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles,
And by opposing end them? To die: to sleep;
No more; and by a sleep to say we end
The heart-ache and the thousand natural shocks
That flesh is heir to, 'tis a consummation
Devoutly to be wish'd. To die, to sleep;
To sleep: perchance to dream: ay, there's the rub;
For in that sleep of death what dreams may come
When we have shuffled off this mortal coil,
Must give us pause: there's the respect
That makes calamity of so long life;
For who would bear the whips and scorns of time,
The oppressor's wrong, the proud man's contumely,
The pangs of despised love, the law's delay,
The insolence of office and the spurns
That patient merit of the unworthy takes,
When he himself might his quietus make
With a bare bodkin? who would fardels bear,
To grunt and sweat under a weary life,
But that the dread of something after death,
The undiscover'd country from whose bourn
No traveller returns, puzzzles the will
And makes us rather bear those ills we have
Than fly to others that we know not of?
Thus conscience does make cowards of us all;
And thus the native hue of resolution
Is sicklied o'er with the pale cast of thought,
And enterprises of great pith and moment
With this regard their currents turn awry,
And lose the name of action.--Soft you now!
The fair Ophelia! Nymph, in thy orisons
Be all my sins remember'd."""

	# we save this text to a temporary file
	file_name = tempfile.mkstemp()[1]
	with open(file_name, 'w') as f:
		f.write(text)

	# and now we pass the file name to the function which will get the stats
	(most_abundant, least_abundant) = character_statistics(file_name)
	assert (most_abundant, least_abundant) == ('e', 'q')

	# we remove the temporary file
	os.unlink(file_name)


# 18------------------------------------------------------------------------------

def pythagorean_triples(n):
	"""
	Returns list of all unique pythagorean triples
	(a, b, c) where a < b < c <= n.
	"""
	l = []
	# loop over all a < b < c <= n
	for c in range(1, n + 1):
		for b in range(1, c):
			for a in range(1, b):
				if a*a + b*b == c*c:
					l.append((a, b, c))
	return l


# 19------------------------------------------------------------------------------

def test_pythagorean_triples():
	pass  # so far we do not test anything, check also test coverage
