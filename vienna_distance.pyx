cdef extern from "vienna_partition_function.h":
    cdef float partition_distance(char *, char *)
    cdef float parition_distance_from_tRNA(char *seq)
    cdef char * tRNA_target()

def get_distance(seq1, seq2):
    return partition_distance(seq1, seq2)

def get_distance_from_tRNA(seq):
    return parition_distance_from_tRNA(seq)

def get_tRNA_target():
    return tRNA_target()
