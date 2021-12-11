# Gen220_FinalProject_2021
Pc Primer design

Primers for Gene 1 only had 1 hit against both P.cinnamomi databases and not any of the other Phytophthora species databases
Primers for Gene 2 had 2 hits from P. cinnamomi databases for each primer set, and no hits to other Phytophthora species databases
Primer set 3 for Gene 3 had 1 hits from P.cinnamomi databases and none for other Phytophthora species databases, other 2 primer sets has 2 hits on P.cinnamomi databases and 0 hits on other Phytopthora species

Summary: Primers for Gene 1 work, Primer set 3 for gene 3 works.

BlastN.XXXX_sequences.txt are my blast results for each database against my primer sets
BlastN.XXXX_sequences.clean.txt are me cutting the hits and primer id for each database, I had an error with this part and couldn't figure out how to exclude the other stuff I didn't want. This made it a problem to try to generate a summary table, but I am still proud I was able to blast all of them against the databases i made and then cut the hits/primerid.
They are displated as an intiger(the #hits) and the primerID, in files that didn't display it like this, all the non P. cinnamomi genomes, showed that there was no hits and displays "0 hits found" at the top of the .txt file


This is how I created my databases:
Not all of them would fit into github because they are too large, even when i compressed them, but they are safe on my computer and external harddrive.


bhoyt003@pelican:~/Final$ module load ncbi-blast/2.9.0+
bhoyt003@pelican:~/Final$ makeblastdb -dbtype nucl -in Pc2113.all.maker.transcripts.fasta


bhoyt003@pelican:~/Final$ bash Blast.sh
This account is associated with the course gen220.
All data within this user account will be DELETED after the conclusion of this course.


Building a new DB, current time: 12/10/2021 16:37:38
New DB name:   /rhome/bhoyt003/Final/Pc2113T1_genome.mRNA.fasta
New DB title:  Pc2113T1_genome.mRNA.fasta
Sequence type: Nucleotide
Keep MBits: T
Maximum file size: 1000000000B
Adding sequences from FASTA; added 21779 sequences in 2.33065 seconds.


Building a new DB, current time: 12/10/2021 16:37:40
New DB name:   /rhome/bhoyt003/Final/Pc2109T1_genome.mRNA.fasta
New DB title:  Pc2109T1_genome.mRNA.fasta
Sequence type: Nucleotide
Keep MBits: T
Maximum file size: 1000000000B
Adding sequences from FASTA; added 21510 sequences in 2.32029 seconds.


Building a new DB, current time: 12/09/2021 23:25:41
New DB name:   /rhome/bhoyt003/Final/Pc2109.all.maker.transcripts.fasta
New DB title:  Pc2109.all.maker.transcripts.fasta
Sequence type: Nucleotide
Keep MBits: T
Maximum file size: 1000000000B
Adding sequences from FASTA; added 19824 sequences in 3.01817 seconds.


Building a new DB, current time: 12/09/2021 23:25:44
New DB name:   /rhome/bhoyt003/Final/Capsici_mRNA_sequences.fasta
New DB title:  Capsici_mRNA_sequences.fasta
Sequence type: Nucleotide
Keep MBits: T
Maximum file size: 1000000000B
Adding sequences from FASTA; added 28954 sequences in 3.56844 seconds.


Building a new DB, current time: 12/09/2021 23:25:48
New DB name:   /rhome/bhoyt003/Final/Fragariae_sequences.fasta
New DB title:  Fragariae_sequences.fasta
Sequence type: Nucleotide
Keep MBits: T
Maximum file size: 1000000000B
Adding sequences from FASTA; added 124 sequences in 2.90861 seconds.


Building a new DB, current time: 12/09/2021 23:25:51
New DB name:   /rhome/bhoyt003/Final/Infestans_mRNA_sequence.fasta
New DB title:  Infestans_mRNA_sequence.fasta
Sequence type: Nucleotide
Keep MBits: T
Maximum file size: 1000000000B
Adding sequences from FASTA; added 17797 sequences in 2.07907 seconds.


Building a new DB, current time: 12/09/2021 23:25:53
New DB name:   /rhome/bhoyt003/Final/Parasitica_mRNA_sequence.fasta
New DB title:  Parasitica_mRNA_sequence.fasta
Sequence type: Nucleotide
Keep MBits: T
Maximum file size: 1000000000B
Adding sequences from FASTA; added 27944 sequences in 3.53135 seconds.


Building a new DB, current time: 12/09/2021 23:25:56
New DB name:   /rhome/bhoyt003/Final/Ramorum_genome_sequence.fasta
New DB title:  Ramorum_genome_sequence.fasta
Sequence type: Nucleotide
Keep MBits: T
Maximum file size: 1000000000B
Adding sequences from FASTA; added 28 sequences in 2.23986 seconds.


Building a new DB, current time: 12/09/2021 23:25:59
New DB name:   /rhome/bhoyt003/Final/Sojae_mRNA_sequence.fasta
New DB title:  Sojae_mRNA_sequence.fasta
Sequence type: Nucleotide
Keep MBits: T
Maximum file size: 1000000000B
Adding sequences from FASTA; added 26584 sequences in 2.9772 seconds.

bhoyt003@pelican:~/Final$ ls

1.20.21 Log.txt                   Fragariae_sequences.gz               Parasitica_mRNA_sequence.fasta.nsq      Ramorum_genome_sequence.fasta.nhr
Blast.sh                          Infestans_mRNA_sequence.fasta        Parasitica_sequence.gz                  Ramorum_genome_sequence.fasta.nin
Capsici_mRNA_sequences.fasta      Infestans_mRNA_sequence.fasta.nhr    Pc2109.all.maker.transcripts.fasta      Ramorum_genome_sequence.fasta.nsq
Capsici_mRNA_sequences.fasta.nhr  Infestans_mRNA_sequence.fasta.nin    Pc2109.all.maker.transcripts.fasta.nhr  Ramorum_sequence.gz
Capsici_mRNA_sequences.fasta.nin  Infestans_mRNA_sequence.fasta.nsq    Pc2109.all.maker.transcripts.fasta.nin  Sojae_mRNA_sequence.fasta
Capsici_mRNA_sequences.fasta.nsq  Infestans_sequence.gz                Pc2109.all.maker.transcripts.fasta.nsq  Sojae_mRNA_sequence.fasta.nhr
Capsici_sequences.gz              NCBI                                 Pc2113.all.maker.transcripts.fasta      Sojae_mRNA_sequence.fasta.nin
FASTA                             ncbi-blast-2.12.0+                   Pc2113.all.maker.transcripts.fasta.nhr  Sojae_mRNA_sequence.fasta.nsq
Fragariae_sequences.fasta         ncbi-blast-2.12.0+-x64-linux.tar.gz  Pc2113.all.maker.transcripts.fasta.nin  Sojae_mRNA_sequence.gz
Fragariae_sequences.fasta.nhr     Parasitica_mRNA_sequence.fasta       Pc2113.all.maker.transcripts.fasta.nsq  test.py
Fragariae_sequences.fasta.nin     Parasitica_mRNA_sequence.fasta.nhr   project.py
Fragariae_sequences.fasta.nsq     Parasitica_mRNA_sequence.fasta.nin   Ramorum_genome_sequence.fasta




##These proteins are RXLRs, DEGs in Avocado, N.benthamiana, and in zoospores, meaning they are highly expressed in 2 hosts and in zoospore DNA, they are also up regulated in these three categories as well. I chose these because they could be good potential candidates for my research projects. They were pulled from my dataset, then I went and manually found these 3 in my Pc.2113.all.maker.transcripts.fasta and Pc.2109.all.maker.transcripts.fasta by hand because it was only 3 genes --> put them in fasta format in "gene1.fasta, gene2.fasta, gene3.fasta"

##Pc2113T1C00002266g0000100.1  "Unknown protein"  -> gene1.fasta
##Pc2113T1C00002279g0000010.1  "REX2"             -> gene2.fasta
##Pc2113T1C00002938g0000130.1  "Unknown protein"  -> gene3.fasta

The BLAST algorithm uses "words" to nucleate regions of similarity. The default Word size for a protein sequence is 3 residues and for nucleotide sequences it is 11 bp. A blastn search will not work with a Word size of less than 7. A good rule of thumb is that the query length must be at least twice the Word size.

Here is an example of what I had done previously, the BLAST book didn't explain word size but google did above^ 
I had an issue with this because my nucleotides were 20 bp, and that was not twice the default word size "11" so if you set it to 10, then it is twice, to get around this I am using 25 bp primers for this project, and Dr. Manosalva prefers them at 25-28bp 

C:\Users\mrbho\Desktop\BioMarkerBlast>C:\Users\mrbho\Desktop\NCBI\blast-2.11.0+/bin/blastn -word_size 10 -query 86101Primers.fasta -db Pc2113.all.maker.transcripts.fasta -evalue 0.01 > 86101Primer1BLAST.txt

#################################################################################################################################
USE -word_size XX after "blastn" to indicate the minimum size of blast search(fill intergers in for XX, in this case it was 10)
#################################################################################################################################

#load this to use biopython
module load miniconda3
conda activate GEN220


I tried to use the primer3 loadouts to build primers from the terminal but something went wrong and I wasn't able to load the primer3 modules like I wanted to, but I understand the settings that come with it and how to adjust melting temps, min/opt/max bp, the product size, etc.

I used primer3.com GUI interface for this instead after hours of trying to figure out how to do this from the terminal, It would be cool to revisit this and make it work.

