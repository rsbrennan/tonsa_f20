import pandas as pd
import numpy as np
import gzip
import csv
import re
from collections import OrderedDict

#sig_col = sig_col[1:]
# assign GO terms
filepath = '/data/atonsa/Atonsa_gen_trans_agp_gff/blast2go_gff_export_20170613_0815.gff.gz'

####
## all loci
####

#make empty array
num_lines = sum(1 for line in open('/users/r/b/rbrennan/tonsa_f20/analysis/pca_loadings_goenrich.txt'))-1

go_df = np.empty(shape=(num_lines,2), dtype = object)

i=0 # start counter

with open('/users/r/b/rbrennan/tonsa_f20/analysis/pca_loadings_goenrich.txt') as master_file:
        head1 = next(master_file)
        for idx, line in enumerate(master_file):
            tmp_gene = line.split("\t")[0]
            out_go = []
            # match GO terms
            match = []
            with gzip.open(filepath, mode="rt") as file:
                for gene_line in file:
                    if len(re.findall(tmp_gene, gene_line)) > 0:
                        gene_spl = gene_line.split("\n")[0].split("\t")
                        go_spl = [i for i in gene_spl[8].split(";") if i.startswith('Ontology_id')]
                        if len(go_spl) > 0:
                            if len(go_spl[0].split()) > 1:
                                go_tmp = go_spl[0].split()[1]
                            if len(out_go) == 0:
                                out_go = go_tmp
                            if len(out_go) > 0:
                                out_go = go_tmp + "," + go_tmp
            go_df[idx,0] = tmp_gene
            if len(out_go) > 0:
                go_df[idx,1] = out_go.replace('"',"").replace(',',";")
            if len(out_go) == 0:
                go_df[idx,1] = "NA"
            i=i+1
            if i % 500 == 0: print(i)

np.savetxt('/users/r/b/rbrennan/tonsa_f20/analysis/pcLoadings_GOterms.out', go_df,fmt='%5s', delimiter='\t')

