cdef extern from "vienna_partition_function.h":
    cdef float partition_distance(char *, char *)

def get_distance(seq1, seq2):
    return partition_distance(seq1, seq2)
