cdef extern from "vienna_utils.h":
    cdef float partition_distance(char *, char *)
    cdef char * tRNA_sequence()
    cdef float partition_distance_from_tRNA_sequence(char * seq)
    cdef int get_bp_distance(char * seq1, char * seq2)
    cdef int get_bp_distance_from_tRNA(char * seq)
    cdef char * fold_string(char * seq)


def fold(seq):
    return fold_string(seq)

def get_distance(seq1, seq2):
    return get_bp_distance(seq1, seq2)

def get_tRNA_sequence():
    return tRNA_sequence()

def get_distance_from_tRNA_sequence(seq):
    return get_bp_distance_from_tRNA(seq)
