# bioinf_sparc
A re-implementation of the Sparc algorithm.

To compile:
g++ -std=c++11 -o Sparc Sparc.cpp

To run:
Sparc -g x -k y -b path_to_backbone.fasta -r path_to_reads.fastq  -m path_to_mappings.paf 
