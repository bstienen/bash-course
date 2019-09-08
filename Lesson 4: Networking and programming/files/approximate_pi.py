import sys
import argparse
import numpy as np

# Parse arguments
parser = argparse.ArgumentParser(description='Approximate pi by sampling a square.')
parser.add_argument('-n', '--nsamples', type=int, default=1000, help='Number of samples to take')
parser.add_argument('-r', '--repetitions', type=int, default=1, help='Number of repetition experiments. If set to 2 of higher, an error estimate on pi will be provided.')
args = parser.parse_args()

# Create list to store results in
results = np.zeros(args.repetitions)

# Perform experiments
for i in range(args.repetitions):
    # Perform sampling
    samples = np.random.rand(args.nsamples,2)*2-1
    # Calculate distance to origin
    distances = np.sqrt(np.sum(np.power(samples, 2), axis=1))
    # Get number of points within circle
    n_inside = np.sum(distances < 1)
    # Approximate pi
    results[i] = 4*n_inside/args.nsamples

# If no repetitions were performed, return single result
if args.repetitions == 1:
    print(results[0])
    sys.exit()

# Calculate average result and uncertainty
average = np.mean(results)
stdev = np.std(results)
uncertainty_on_average = stdev/np.sqrt(args.repetitions)
# Print result with uncertainty
print("{} +/- {}".format(average, uncertainty_on_average))
