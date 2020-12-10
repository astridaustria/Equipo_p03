# Comandos de la Práctica 02
## Equipo 00
### Acosta García Daniel Enrique
### Hérnandez Leyva Mirén Jessamyn
### Muñoz Barón Luis Miguel 
...

##Parte 1

| Plataforma/ compañía     | Longitud de reads (pb) | # reads x run   | Tiempo      | Costo x 10^6 bases | Error (%) | Química                                                                  |
|--------------------------|------------------------|-----------------|-------------|--------------------|-----------|--------------------------------------------------------------------------|
| Sanger/life technologies | 800                    | 1               | 2 hrs       | $2400              | 0.1       | Dideoxy terminator                                                       |
| Illumina                 | 50 - 250               | <3 mil millones | 1 - 10 días | ~$0.10             | 2         | Síntesis detectada por fluorescencia paso a paso                         |
| Roche 454                | 700                    | 1 millón        | 1 día       | $10                | 0.1       | Pirosecuenciación por síntesis detectada por acción de la luciferasa     |
| PACBio                   | 2900                   | <75,000         | <2 hrs      | $2                 | 1         | Sïntesis de una sola molécula de gran tamaño detectada por fluorescencia |
| Ion Torrent              | 200                    | <5 millón       | <2 hrs      | $1                 | 2         | Detección de cambios de pH tras la adición de diferentes nucleótidos     |Tabla anexa al repositorio



Deschamps, S., Llaca, V.,& May, G.. (2012). Genotyping-by-Sequencing in Plants. Biology. 1. 460-83. 10.3390/biology1030460.

FH Munster University of Applied Sciences. (s.f.). Analysis of next-generation sequencing data. 8/12/2020, de FH Munster Sitio web: https://www.fh-muenster.de/eti/downloads/labore/db/bioinf/BFG_Chapter09_NGS_v04.pdf


##Parte 2


1.- zcat ERR486827_1.fastq.gz | awk 'BEGIN{P=1}{if(P==1||P==2){gsub(/^[@]/,">");print}; if(P==4)P=0; P++}' ERR486827_1.fastq.gz > Mgenitalium_1_fasta

zcat ERR486829_2.fastq.gz | awk 'BEGIN{P=1}{if(P==1||P==2){gsub(/^[@]/,">");print}; if(P==4)P=0; P++}'> Mgenitalium_2_fasta



2.- grep -c "^>" Mgenitalium_1.fasta 
398824

grep -c "^>" Mgenitalium_2.fasta 
384747




