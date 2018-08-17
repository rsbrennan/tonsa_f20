# tonsa_f20 summary


## heterozygosity

Filtering variants by:

  1. All samps have at least 40x coverage
  2. where we call at least three lines variable.
  3. max coverage. Median coverage is 128, remove those > 3*128=385x. But looking across all lines, so across all 8 lines where coverage is > 3078x
  4. This leaves 363,200 variable sites with median coverage of 115x
  5. and 11,026 genes remain (out of 33,313). If we only include genes with at least 10 variants, 7,905 remain

Looking at heterozygosity across each gene. In this case, so heterozygotisy is being averaged acrosss each gene

calculated as 	`Hp <- (2 * sum(numMajor) * sum(numMinor)) / ((sum(numMajor) + sum(numMinor))^2)`

where `sum(numMajor)` and `sum(numMinor))` are the replicate specific sums of the count of the reference and alternate allele. These are counted at all snps in the gene. 

Across the genome, there is no reduction in Hp in the HHHH line. 

| Line    |  mean heterozygosity  |
|:------:| :-----:|
| AAAA_F1_REP1 | 0.302 |
| AAAA_F1_REP2 | 0.303 |
| AAAA_F1_REP3 | 0.304 |
| AAAA_F1_REP4 | 0.302 |
| HHHH_F1_REP1 | 0.302 |
| HHHH_F1_REP2 | 0.302 |
| HHHH_F1_REP3 | 0.304 |
| HHHH_F1_REP4 | 0.303 |

![alt text](https://raw.githubusercontent.com/rsbrennan/tonsa_f20/master/figures/heterozygosity.png)

<img src="https://raw.githubusercontent.com/rsbrennan/tonsa_f20/master/figures/heterozygosity.png" width="500">


The low end of quantiles also do not differ:

![alt text](https://raw.githubusercontent.com/rsbrennan/tonsa_f20/master/figures/het.01_quantile.png)  

![alt text](https://raw.githubusercontent.com/rsbrennan/tonsa_f20/master/figures/het.05_quantile.png)


Next, looking at the lower 0.05 quantile of heterozygosity for each line. So lowest 395 genes

Within AAAA, 138 are present in all.
Within HHHH, 146 are present in all.
87 are consistent across all lines. 



## pi in 1kb windows


![alt text](https://raw.githubusercontent.com/rsbrennan/tonsa_f20/master/figures/1kb.pi.hist.png)




















