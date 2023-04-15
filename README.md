# Genome Analysis
This script performs a comparative analysis of the nucleotides of two DNA sequences.
## Functionality
The script:
- counts the number of nucleotides for each genome
- computes the percentages of each nucleotide in the genotype
- calculates the longest common shared sequence
## Usage
You will first need to install numpy: `pip install numpy`
```
usage: main.py [-h] sequence1 sequence2

Create genomes from text files.

positional arguments:
  sequence1   the first sequence file
  sequence2   the second sequence file

options:
  -h, --help  show this help message and exit
```
### Example
```
python genome_comparison.py example_species1.fna example_species2.fna
```
This gives the following output
```
example_species1 (C C A T C A C T T T ...):
2119 nucleotides
C: 18.4%
A: 31.2%
T: 32.5%
G: 17.9%

example_species2 (A G T C C A T T T G ...):
299761 nucleotides
A: 27.5%
G: 20.1%
T: 29.6%
C: 22.9%

The length of the longest common sequence in both genomes is 722
```