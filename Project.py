#!/usr/bin/env python3

import re
import os
import gzip
import shutil
import tarfile


##Setting URL links to URL1, 2,3 etc

#URL1='https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/020/800/215/GCA_020800215.1_PR-102_v3_p/GCA_020800215.1_PR-102_v3_p_genomic.fna.gz'
#URL2='https://genome.jgi.doe.gov/portal/Physo3/download/Physo3_GeneCatalog_transcripts_20110401.nt.fasta.gz'

#error downloading Sojae(URL2) transcript file, uploaded manually to my HPCC folder on Jupyterlabs

#URL3='https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/009/729/435/GCA_009729435.1_ASM972943v1/GCA_009729435.1_ASM972943v1_genomic.fna.gz'
#URL4='https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/016/618/375/GCA_016618375.1_Pcap_4.1/GCA_016618375.1_Pcap_4.1_rna_from_genomic.fna.gz'
#URL5='https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/142/945/GCF_000142945.1_ASM14294v1/GCF_000142945.1_ASM14294v1_rna.fna.gz'
#URL6='https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/247/585/GCF_000247585.1_PP_INRA-310_V2/GCF_000247585.1_PP_INRA-310_V2_rna.fna.gz'


##setting URL to path basename
#Ramorum=os.path.basename(URL1)
#Sojae=os.path.basename(URL2)
#Fragariae=os.path.basename(URL3)
#Capsici=os.path.basename(URL4)
#Infestans=os.path.basename(URL5)
#Parasitica=os.path.basename(URL6)

##Uploaded P. cinnamomi genomes Pc2109 and Pc2113 to Jupyter.hpcc.ucr.edu/user/bhoyt003/Final because there was trouble downloading files from google docs with curl commmand since access is only between several Manosalva Lab member @ucr.edu emails.

##downloading files with curl command, doesnt download if it already exists, error in URL2/Sojae sequences, so uploaded manually to HPCC folder in jupyterlabs

#if not os.path.exists(Ramorum):
    #os.system("curl -O {}".format(URL1))
#if not os.path.exists(Sojae):
    #os.system("curl -O {}".format(URL2))
#if not os.path.exists(Fragariae):
    #os.system("curl -O {}".format(URL3))
#if not os.path.exists(Capsici):
   # os.system("curl -O {}".format(URL4))   
#if not os.path.exists(Infestans):
#    os.system("curl -O {}".format(URL5))
#if not os.path.exists(Parasitica):
   # os.system("curl -O {}".format(URL6))

##Unzip .gz files/rename, some of my available sequences did not have transcript fasta files, used genome sequences in this. Labeled with "mRNA" if it is a transcript fasta file or just "sequence" if it is not a transcript fasta file

#with gzip.open('Ramorum_sequence.gz', 'rb') as f_in:
#    with open('Ramorum_genome_sequence.fasta', 'wb') as f_out:
#        shutil.copyfileobj(f_in, f_out)
#with gzip.open('Infestans_sequence.gz', 'rb') as f_in:
#    with open('Infestans_mRNA_sequence.fasta', 'wb') as f_out:
#        shutil.copyfileobj(f_in, f_out)
#with gzip.open('Sojae_mRNA_sequence.gz', 'rb') as f_in:
#    with open('Sojae_mRNA_sequence.fasta', 'wb') as f_out:
#        shutil.copyfileobj(f_in, f_out)
#with gzip.open('Fragariae_sequences.gz', 'rb') as f_in:
#    with open('Fragariae_sequences.fasta', 'wb') as f_out:
#        shutil.copyfileobj(f_in, f_out)
#with gzip.open('Capsici_sequences.gz', 'rb') as f_in:
#    with open('Capsici_mRNA_sequences.fasta', 'wb') as f_out:
#        shutil.copyfileobj(f_in, f_out)
#with gzip.open('Parasitica_sequence.gz', 'rb') as f_in:
#    with open('Parasitica_mRNA_sequence.fasta', 'wb') as f_out:
#        shutil.copyfileobj(f_in, f_out) 
#with gzip.open('Pc2109T1_genome.mRNA.fasta.gz', 'rb') as f_in:
#    with open('Pc2109T1_genome.mRNA.fasta', 'wb') as f_out:
#        shutil.copyfileobj(f_in, f_out)
#with gzip.open('Pc2113T1_genome.mRNA.fasta.gz', 'rb') as f_in:
#    with open('Pc2113T1_genome.mRNA.fasta', 'wb') as f_out:
#        shutil.copyfileobj(f_in, f_out)

#Tried to load NCBI blast bin folder with makeblastdb.exe but this was the wrong direction and loaded in NCBI using HPCC instead to make databases
#tf = tarfile.open("ncbi-blast-2.12.0+-x64-linux.tar.gz")
#tf.extractall()
