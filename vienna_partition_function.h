#ifndef VIENNA_PARTITION_FUNCTION_H
#define VIENNA_PARTITION_FUNCTION_H
const char* tRNA_sequence();
float partition_distance_from_tRNA_sequence(const char * seq);
float partition_distance(const char *, const char *);
int get_bp_distance(const char * seq1, const char * seq2);
int get_bp_distance_from_tRNA(const char * seq);
const char * fold_string(const char * seq);
#endif
