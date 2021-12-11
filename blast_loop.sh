#!/usr/bin/bash
module load ncbi-blast/2.9.0+
path=databases

for file in ${path}/*.fasta;
do
	F=$(basename $file)	
	F2=${F%.fasta*}
    blastn -word_size 10 -query PCPrimers.fasta -db ${file} -evalue 0.01 -outfmt 7 -out BLASTN.${F2}.txt
	grep "hits" BLASTN.${F2}.txt | sort | uniq -c > BLAST.${F2}.clean.txt
done

#blastn -word_size 10 -query PCPrimers.fasta -db databases/Pc2109T1_genome.mRNA.fasta -evalue 0.01 -outfmt 7 -out BLASTN.PC2109T1.txt

# change *.fasta to *.txt to loop through all txt files
# 	cut -f1 BLASTN.${F2}.txt | sort | uniq -c > BLAST.${F2}.clean.txt
