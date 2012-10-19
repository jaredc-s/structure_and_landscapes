import subprocess

def command_fold(seq):
    #subprocess.call(['RNAfold'])
    fold = subprocess.check_output(seq)
    print fold
#look at using check_output

def command_distanct(seq1, seq2):
    pass

def get_tRNA_sequence():
    pass

def command_get_distance_from_tRNA(seq):
    pass
