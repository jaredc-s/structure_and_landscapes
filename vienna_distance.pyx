cdef extern from "vienna_partition_function.h":
    cdef float partition_distance(char *, char *)
    cdef char * tRNA_sequence()

def get_distance(seq1, seq2):
    return partition_distance(seq1, seq2)

def get_tRNA_sequence():
    return tRNA_sequence()
