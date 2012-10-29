import subprocess

def command_fold(seq):
    #subprocess.call(['RNAfold'])
    fold = subprocess.Popen(['RNAfold'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    output = fold.communicate(seq)
    structure = output[0].split('\n')
    return structure[1][0:len(seq)]

#look at using check_output

def command_distanct(seq1, seq2):
    pass

def get_tRNA_sequence():
    pass

def command_get_distance_from_tRNA(seq):
    pass
