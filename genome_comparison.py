from __future__ import annotations
from typing import Any, List

from collections import Counter
import numpy as np
import argparse
import os

class Genome:
    """a class to represent a genome"""
    DNA_MAP = { # Convert DNA to numbers
        "A": 0,
        "C": 1,
        "G": 2,
        "T": 3
    }
    REVERSE_DNA_MAP = { # Convert numbers back to DNA
        v: k for k, v in DNA_MAP.items()
    }

    def __init__(self, name: str, sequence: List[str]):
        """initialise with a name and sequence of nucleotides"""
        self.name = name
        # Convert nucleotides to numbers and store as a numpy array for faster processing
        self.sequence = np.array([self.DNA_MAP[nuc.upper()] for nuc in sequence])

    @classmethod
    def from_file(cls, filename: str) -> Genome:
        """create a genome from a file"""
        with open(filename, "r") as f:
            # Remove whitespace
            sequence = f.read().replace(" ", "").replace("\n", "").replace("\t", "")
        # Use the filename as the genome name
        name = os.path.splitext(os.path.basename(filename))[0]
        # Make sure the sequence is valid
        assert all(nuc.upper() in cls.DNA_MAP for nuc in sequence), f"Invalid DNA sequence ({filename})"
        # Create the genome
        return cls(name, sequence)
    
    def __repr__(self) -> str:
        # Print the same and the first 10 nucleotides
        return f"{self.name} ({' '.join([self.REVERSE_DNA_MAP[s] for s in self.sequence[:10]])} ...)"

    def __len__(self) -> int:
        return len(self.sequence)

    def stats(self) -> str:
        """computer stats about the genome"""
        stats = f"{self}:\n{len(self)} nucleotides\n"
        # Count the number of each nucleotide
        counter = Counter(self.sequence)
        for nuc, count in counter.items():
            # Calculate the percentage of each nucleotide
            stats += f"{self.REVERSE_DNA_MAP[nuc]}: {count / len(self) * 100:.1f}%\n"
        return stats

def longest_common_sequence(arr1: List[Any], arr2: List[Any]) -> List[Any]:
    """computes the longest contiguous sequence in both arrays"""
    # Ensure that arr1 is not longer than arr2 for simplicity
    if len(arr1) > len(arr2):
        tmp = arr1
        arr1 = arr2
        arr2 = tmp
    
    # Create a list of differences between corresponding elements of arr1 and arr2
    diff_arr = [arr1[i] - arr2[i] for i in range(len(arr1))]
    
    # Initialize variables to track maximum subarray found so far
    max_sum = curr_sum = diff_arr[0] # initialize maximum sum and current sum to the first element of diff_arr
    start_index = end_index = max_start_index = 0 # initialize indices to 0
    
    # Iterate over the differences between corresponding elements of arr1 and arr2
    for i, num in enumerate(diff_arr[1:], start=1):
        # If the current number is greater than the sum of the current subarray and the current number
        if num > curr_sum + num:
            curr_sum = num # start a new subarray
            start_index = i
        else:
            curr_sum += num # extend the current subarray
            
        # Update the maximum subarray found so far if the current subarray is greater
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_start_index = start_index
            end_index = i
    
    # Return the subarray of arr1 that corresponds to the maximum subarray found
    return arr1[max_start_index:end_index+1]

if __name__ == "__main__":
    # parse the two input files
    parser = argparse.ArgumentParser(description="Create genomes from text files.")
    parser.add_argument("sequence1", help="the first sequence file")
    parser.add_argument("sequence2", help="the second sequence file")
    args = parser.parse_args()

    # create the genomes
    genome1 = Genome.from_file(args.sequence1)
    genome2 = Genome.from_file(args.sequence2)

    # compute stats
    print(genome1.stats())
    print(genome2.stats())
    print("The length of the longest common sequence in both genomes is", len(longest_common_sequence(genome1.sequence, genome2.sequence)))