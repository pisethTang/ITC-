import matplotlib.pyplot as plt
import numpy as np
import bubble



plt.style.use('fivethirtyeight')

# Function to check if the array is sorted
def isSorted(A: list[int]) -> bool:
    if len(A) == 0: return True
    for i in range(1, len(A)):
        if A[i-1] > A[i]: return False
    return True

# Testing function to ensure sorting algorithm works correctly
def test_sort_ok(sorting_algo, name: str):
    print(f"Testing: {name}")
    final_answer = True
    for i in range(100):
        print(".", end="", flush=True)
        a = bubble.random_array(i)
        a, c, s = sorting_algo(a)
        answer = isSorted(a)
        if not answer:
            print(f"Uh oh...problem with {name}")
            print(f"Not sorted: {a}")
            exit()
        final_answer = final_answer and answer
    print()
    print(final_answer)

# Calculate the mean comparisons and swaps for a given array size and number of samples
def experiences(sorting_algo, size, num_samples):
    sum_c = 0
    sum_s = 0
    for _ in range(0, num_samples):
        a = bubble.random_array(size)
        a, exp_c, exp_s = sorting_algo(a)
        sum_c += exp_c
        sum_s += exp_s
    return sum_c / num_samples, sum_s / num_samples

# Function to test and collect data for each sorting algorithm
def test(sorting_algo, name, num_samples, max_length, step_size):
    print(f"Collecting sorting times for {name}")
    lengths = []
    comps = []
    moves = []
    for size in range(0, max_length, step_size):
        c, s = experiences(sorting_algo, size, num_samples)
        lengths.append(size)
        comps.append(c)
        moves.append(s)
        print(f"{name} data for array of size {size}: Comparisons = {c}, Moves = {s}")
    return lengths, comps, moves

# Define the array sizes to test
max_length = 5000 
array_sizes = []

# Number of samples for each size
SAMPLES = 10
STEPS = 100

# Collecting data for each sorting algorithm
# bsn_lengths, bsn_comps, bsn_moves = test(bubble.bubble_sort_with_mésure, "Bubble (naïve)", array_sizes, SAMPLES)
# bso_lengths, bso_comps, bso_moves = test(bubble.bubble_sort_optimised, "Bubble (optimised)", array_sizes, SAMPLES)
# bsso_lengths, bsso_comps, bsso_moves = test(bubble.bubble_sort_super_optimized, "Bubble (super optimized)", array_sizes, SAMPLES)
bsn_lengths, bsn_comps, bsn_moves = test(bubble.bubble_sort_with_mésure, "Bubble (naïve)", max_length, SAMPLES, STEPS)
bso_lengths, bso_comps, bso_moves = test(bubble.bubble_sort_optimised, "Bubble (optimised)", max_length, SAMPLES, STEPS,)
bsso_lengths, bsso_comps, bsso_moves = test(bubble.bubble_sort_super_optimized, "Bubble (super optimized)", max_length, SAMPLES, STEPS)
# Function references for visual comparison

print()
print(bsn_comps)
print(bso_comps)
print(bsso_comps)

# f_n = array_sizes
# f_n_squared = array_sizes ** 2


# Plot settings
# plt.figure(figsize=(14, 7))


# Plot Comparisons
# print(plt.subplot(1, 2, 1)) # 1 row, 2 columns
# fig, ax = plt.subplot(1, 2)
# plt.plot(array_sizes, bsn_comps, color='#ff0000', linestyle='-', label='Bubble (naive)', linewidth=2, markersize=8)
# plt.plot(array_sizes, bso_comps, color='#00ff00', linestyle='--', label='Bubble (optimised)', linewidth=2, markersize=8)
# plt.plot(array_sizes, bsso_comps, color='#0000ff', linestyle=':', label='Bubble (super optimized)', linewidth=2, markersize=8)
# plt.plot(array_sizes, f_n, color='#ff00ff', linestyle='-', label='f(n) = n', linewidth=2)
# plt.plot(array_sizes, f_n_squared, color='#00ffff', linestyle='--', label='f(n) = n^2', linewidth=2)




# plt.tight_layout()
# plt.show()

# Plot Comparisons
# plt.subplot(1, 2, 1)
# plt.plot(bsn_lengths, bsn_comps, 'bo-', label='Bubble (naive)', linewidth=2, markersize=8)
# plt.plot(bso_lengths, bso_comps, 'go--', label='Bubble (optimised)', linewidth=2, markersize=8)
# plt.plot(bsso_lengths, bsso_comps, 'yo:', label='Bubble (super optimized)', linewidth=2, markersize=8)
# plt.plot(array_sizes, f_n, 'r-', label='f(n) = n', linewidth=2)
# plt.plot(array_sizes, f_n_squared, 'm--', label='f(n) = n^2', linewidth=2)

# Adjust axis limits based on data range
# plt.ylim(0, max(f_n_squared) * 1.1)
# plt.xlabel('Array Size')
# plt.xticks(np.arange(0, 6500, 500))

# plt.ylabel('Mean Comparisons')
# max_y = max(max(bsn_comps), max(bso_comps), max(bsso_comps))
# plt.yticks(np.arange(0, max_y, 1e3))

# plt.title('Average Comparisons')
# plt.grid(True)
# plt.legend()

# Plot Swaps (Moves)
# plt.subplot(1, 2, 2)
# plt.plot(array_sizes, bsn_moves, 'bo-', label='Bubble (naive)', linewidth=2, markersize=8)
# plt.plot(array_sizes, bso_moves, 'go--', label='Bubble (optimised)', linewidth=2, markersize=8)
# plt.plot(array_sizes, bsso_moves, 'yo:', label='Bubble (super optimized)', linewidth=2, markersize=8)
# plt.plot(array_sizes, f_n, 'r-', label='f(n) = n', linewidth=2)
# plt.plot(array_sizes, f_n_squared, 'm--', label='f(n) = n^2', linewidth=2)

# # Adjust axis limits based on data range
# plt.ylim(0, max(f_n_squared) * 1.1)
# plt.xlabel('Array Size')
# plt.ylabel('Mean Swaps')
# plt.title('Average Swaps (Moves)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()