#!/bin/bash

zcat ERR486827_1.fastq.gz | awk 'BEGIN{P=1}{if(P==1||P==2){gsub(/^[@]/,">");print}; if(P==4)P=0; P++}' ERR486827_1.fastq.gz > Mgenitalium_1_fasta

zcat ERR486829_2.fastq.gz | awk 'BEGIN{P=1}{if(P==1||P==2){gsub(/^[@]/,">");print}; if(P==4)P=0; P++}'> Mgenitalium_2_fasta


