#!/bin/bash -l

java -jar ~/bin/VarScan.v2.3.9.jar mpileup2snp ~/tonsa_f20/analysis/merged.pileup --min-coverage 30 --min-reads 2 --min-avg-qual 20 --min-var-freq 0.01 --p-value 0.1 > ~/tonsa_f20/analysis/snp_out

