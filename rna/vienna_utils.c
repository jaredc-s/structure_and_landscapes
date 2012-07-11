#include  <stdio.h>
#include <stdlib.h>
#include <string.h>
#include  "utils.h"
#include  "fold.h"
#include  "part_func.h"
#include  "profiledist.h"
#include "vienna_utils.h"


const char* tRNA_sequence()
{
    // >gi|7276232:c443271-443198 Saccharomyces cerevisiae tRNA-Ile
    return "GGTCTCTTGGCCCAGTTGGTTAAGGCACCGTGCTAATAACGCGGGGATCAGCGGTTCGATCCCGCTAGAGACCA";
}

float partition_distance_from_tRNA_sequence(const char * seq)
{
    return partition_distance(tRNA_sequence(), seq);
}

const char * fold_string(const char * seq)
{
    char * struc;
    struc = (char *) space(sizeof(char)*(strlen(seq)+1));
    fold(seq, struc);
    return struc;
}

int get_bp_distance(const char * seq1, const char * seq2)
{

   char *struct1,* struct2;

   struct1 = (char* ) space(sizeof(char)*(strlen(seq1)+1));
   struct2 = (char* ) space(sizeof(char)*(strlen(seq2)+1));

   fold(seq1, struct1);
   fold(seq2, struct2);
   free_arrays();

   return bp_distance(struct1, struct2);
}

int get_bp_distance_from_tRNA(const char * seq)
{
    return get_bp_distance(tRNA_sequence(), seq);
}

float partition_distance(const char *seq1, const char *seq2)
{
   char *struct1,* struct2;
   float profile_dist;
   float *pf1, *pf2;
   FLT_OR_DBL *bppm, *bppm2;

   /* allocate memory for structure and fold */
   struct1 = (char* ) space(sizeof(char)*(strlen(seq1)+1));
   struct2 = (char* ) space(sizeof(char)*(strlen(seq2)+1));


   /* calculate partition function and base pair probabilities */
   pf_fold(seq1, struct1);
   /* get the base pair probability matrix for the previous run of pf_fold() */
   bppm = export_bppm();
   pf1 = Make_bp_profile_bppm(bppm, strlen(seq1));

   pf_fold(seq2, struct2);
   /* get the base pair probability matrix for the previous run of pf_fold() */
   bppm2 = export_bppm();
   pf2 = Make_bp_profile_bppm(bppm2, strlen(seq2));

   free_pf_arrays();  /* free space allocated for pf_fold() */

   profile_dist = profile_edit_distance(pf1, pf2);
   free_profile(pf1); free_profile(pf2);
   return abs(profile_dist);
}
