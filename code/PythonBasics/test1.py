import tarfile

# Specify the path to your .tgz file
tgz_path = 'code/datasets/mnist_sample.tgz'

# Use the tarfile module to open the file in read mode with gzip compression
with tarfile.open(tgz_path, 'r:gz') as tgz_file:
    # Extract all contents to the current directory
    tgz_file.extractall()

print("Extraction complete.")