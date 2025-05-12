# DNA Sequence Generator in FASTA Format
# Purpose: This program generates a random DNA sequence of a user-specified length, embeds the user's name at a random position without affecting statistics, calculates sequence statistics, and saves the sequence in a FASTA file format.
# Context: Useful for bioinformatics education, testing, and generating mock DNA data for analysis.

import random

# Function to generate a random DNA sequence of a given length
def generate_dna_sequence(length):
    # ORIGINAL:
    # return ''.join(random.choice('ACGT') for _ in range(length))
    # MODIFIED (improved readability by using a list comprehension with join directly for clarity):
    sequence = ''.join([random.choice('ACGT') for _ in range(length)])
    return sequence

# Function to insert the user's name at a random position in the DNA sequence
def insert_name_into_sequence(sequence, name):
    # ORIGINAL:
    # position = random.randint(0, len(sequence))
    # return sequence[:position] + name + sequence[position:]
    # MODIFIED (ensure insertion at a valid index, and added a debug print to show the insertion point):
    position = random.randint(0, len(sequence))
    print(f"Debug: Inserting name at position {position}")  # Added for debugging purposes
    sequence_with_name = sequence[:position] + name + sequence[position:]
    return sequence_with_name

# Function to calculate nucleotide statistics for a DNA sequence
def calculate_statistics(sequence):
    # ORIGINAL:
    # sequence_without_name = ''.join([char for char in sequence if char in 'ACGT'])
    # MODIFIED (improved efficiency by using a filter for nucleotide extraction):
    sequence_without_name = ''.join(filter(lambda char: char in 'ACGT', sequence))

    length = len(sequence_without_name)
    counts = {nucleotide: sequence_without_name.count(nucleotide) for nucleotide in 'ACGT'}
    percentages = {nucleotide: (count / length) * 100 for nucleotide, count in counts.items()}
    cg_ratio = ((counts['C'] + counts['G']) / (counts['A'] + counts['T'])) if (counts['A'] + counts['T']) > 0 else 0
    cg_percentage = percentages['C'] + percentages['G']
    return percentages, cg_percentage, cg_ratio

# Function to save the DNA sequence to a FASTA file
def save_to_fasta_file(sequence_id, description, sequence):
    filename = f"{sequence_id}.fasta"
    # ORIGINAL:
    # with open(filename, 'w') as file:
    # MODIFIED (added error handling to ensure file writing issues are caught):
    try:
        with open(filename, 'w') as file:
            file.write(f">{sequence_id} {description}\n{sequence}\n")
    except IOError as e:
        print(f"Error: Unable to write to file {filename}. {e}")
    return filename

# Main function to interact with the user and execute the program logic
def main():
    # ORIGINAL:
    # sequence_length = int(input("Enter the sequence length: "))
    # MODIFIED (added input validation to handle non-integer inputs):
    while True:
        try:
            sequence_length = int(input("Enter the sequence length: "))
            if sequence_length <= 0:
                raise ValueError("Length must be a positive integer.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid positive integer.")

    sequence_id = input("Enter the sequence ID: ")
    description = input("Provide a description of the sequence: ")
    name = input("Enter your name: ")

    # Generate DNA sequence
    dna_sequence = generate_dna_sequence(sequence_length)
    dna_with_name = insert_name_into_sequence(dna_sequence, name)

    # Save to FASTA file
    filename = save_to_fasta_file(sequence_id, description, dna_with_name)
    print(f"The sequence was saved to the file {filename}")

    # Calculate and display statistics
    percentages, cg_percentage, cg_ratio = calculate_statistics(dna_with_name)
    print("Sequence statistics:")
    for nucleotide, percentage in percentages.items():
        print(f"{nucleotide}: {percentage:.1f}%")
    print(f"%CG: {cg_percentage:.1f}")
    print(f"C:G to A:T ratio: {cg_ratio:.2f}")

if __name__ == "__main__":
    main()
