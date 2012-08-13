#!/usr/bin/env bash
cd filtered_fastas
for file in *.gz; do gunzip $file; done;
for file in *; do breseq -r ../w3110_ref.gb $file -o ../breseq_output/${file%.*}; done;
cd ../breseq_output
for folder in  *; do cp "${folder}"/output/output.gd ~/Dropbox/mutations/"${folder}".gd; done;
