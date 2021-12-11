#!/usr/bin/python
# HPCC Login--->     ssh -XY bhoyt003@cluster.hpcc.ucr.edu
#module load miniconda3
#conda activate GEN220

#Assign execution permissions
chmod +x project.py
#chmod +x Primerscript.py
#Run the script by using its filename

#Running python scripts
#./project.py
#./Primerscript.py

#Load Blast on HPCC cluster
#module load ncbi-blast/2.9.0+
#makeblastdb -dbtype nucl -in ./databases/Pc2113T1_genome.mRNA.fasta
#makeblastdb -dbtype nucl -in ./databases/Pc2109T1_genome.mRNA.fasta
#makeblastdb -dbtype nucl -in ./databases/Capsici_mRNA_sequences.fasta
#makeblastdb -dbtype nucl -in ./databases/Fragariae_sequences.fasta
#makeblastdb -dbtype nucl -in ./databases/Infestans_mRNA_sequence.fasta
#makeblastdb -dbtype nucl -in ./databases/Parasitica_mRNA_sequence.fasta
#makeblastdb -dbtype nucl -in ./databases/Ramorum_genome_sequence.fasta
#makeblastdb -dbtype nucl -in ./databases/Sojae_mRNA_sequence.fasta
###list files in current directory, should be in /Final
#ls
#Blasting PCPrimers.Fasta file to databases- without a loop because I couldn't figure out how to get the loop to work at first, then I had a little
#blastn -word_size 10 -query PCPrimers.fasta -db databases/Pc2109T1_genome.mRNA.fasta -evalue 0.01 -outfmt 7 -out BLASTN.PC2109T1.txt
#blastn -word_size 10 -query PCPrimers.fasta -db databases/Pc2113T1_genome.mRNA.fasta -evalue 0.01 -outfmt 7 -out BLASTN_Pc2113T1.txt
#blastn -word_size 10 -query PCPrimers.fasta -db databases/Infestans_mRNA_sequence.fasta -evalue 0.01 -outfmt 7 -out BLASTN_Infestans.txt
#blastn -word_size 10 -query PCPrimers.fasta -db databases/Ramorum_genome_sequence.fasta -evalue 0.01 -outfmt 7 -out BLASTN_Ramorum.txt
#blastn -word_size 10 -query PCPrimers.fasta -db databases/Sojae_mRNA_sequence.fasta -evalue 0.01 -outfmt 7 -out BLASTN_Sojae.txt
#blastn -word_size 10 -query PCPrimers.fasta -db databases/Fragariae_sequences.fasta -evalue 0.01 -outfmt 7 -out BLASTN_Fragariae.txt


###Tried to load a linux BLAST folder with makeblastdb.exe for linux but this wasn't working properly, then decided I should use the HPCC cluster and load up NCBI and found your examples, much easier. 
#ncbi-blast-2.12.0+/bin/makeblastdb -in Pc2113.all.maker.transcripts.fasta -dbtype nucl
#ncbi-blast-2.12.0+/bin/makeblastdb -in Pc2109.all.maker.transcripts.fasta -dbtype nucl
#ncbi-blast-2.12.0+/bin/makeblastdb -in Capsici_mRNA_sequences.fasta -dbtype nucl
#ncbi-blast-2.12.0+/bin/makeblastdb -in Fragariae_sequences.fasta -dbtype nucl
#ncbi-blast-2.12.0+/bin/makeblastdb -in Infestans_mRNA_sequence.fasta -dbtype nucl
#ncbi-blast-2.12.0+/bin/makeblastdb -in Parasitica_mRNA_sequence.fasta -dbtype nucl
#ncbi-blast-2.12.0+/bin/makeblastdb -in Ramorum_genome_sequence.fasta -dbtype nucl
#ncbi-blast-2.12.0+/bin/makeblastdb -in Sojae_mRNA_sequence.fasta -dbtype nucl

