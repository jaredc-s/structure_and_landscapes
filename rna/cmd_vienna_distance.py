import subprocess

def fold(seq):
    #subprocess.call(['RNAfold'])
    fold = subprocess.Popen(['RNAfold', '--noPS'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    output = fold.communicate(seq)
    print output
    structure = output[0].split('\n')
    return structure[1][0:len(seq)]

#look at using check_output

def get_distance(seq1, seq2):
    structure1 = fold(seq1)
    structure2 = fold(seq2)
    distance = subprocess.Popen(['RNAdistance'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    ouput = distance.communicate(structure1+'\n'+structure2)

    return int(ouput[0][2:])

def get_tRNA_sequence():
    return "GGTCTCTTGGCCCAGTTGGTTAAGGCACCGTGCTAATAACGCGGGGATCAGCGGTTCGATCCCGCTAGAGACCA"

def get_distance_from_tRNA_sequence(seq):
    org_struct = fold(seq)
    target_struct = '(((((((.(((((....))........(((((.......)))))(((((........))))).)))))))))).'
    distance = subprocess.Popen(['RNAdistance'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    ouput = distance.communicate(org_struct+'\n'+target_struct)

    return int(ouput[0][2:])

