#DNA_sequence = raw_input('DNAsequence:')
#print DNA_sequence


"This test will return the position of incorrect nucleotide(s)' in a DNA sequence"

valid_nucleotides = ['T', 'A', 'G', 'C']

def Seq_position (DNA_sequence):
	inc_position = []
	for position in range(len(DNA_sequence)):
		nucleotide = DNA_sequence[position]
		if nucleotide not in valid_nucleotides:
			inc_position.append(position)
	print inc_position

Seq_position('ACTGAD') == 5