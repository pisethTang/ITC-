import random


# In Python, assignment statements do not create a new object (do not allocate new blocks of memory and return reference of that memory to a variable),
# instead, it creates bindings between a target and object, which simply means that 
# the object's reference is copied into the target variable
# so as a result, both the object and the target variable now point to the same memory location.
# Hence, a shallow copy occurs where modifications made to the memory location will be seen through both variables.
# plt.xkcd()




# Exercise 1
def random_array(n: int):
    return [random.randint(0, 3*n) for _ in range(0, n)]

def generate_sizes(min_size: int, max_size: int, step: int):
    return [i for i in range(min_size, max_size, step)]

# Exercise 2: Bubble sort takes in A and sorts it in ascending order 
# to form A' where A'[i] < A'[i+1] for all i in n := len(A) = len(A')
# def bubble_sort_naïve_with_mésure(t):
    if len(t) <= 1:
        return t, 0, 0
    comps = 0
    moves = 0
    swapped = True
    i = 1
    while swapped:
        swapped = False
        for i in range(1, len(t)):
            comps += 1
            if t[i] < t[i - 1]:
                moves += 3
                t[i - 1], t[i] = t[i], t[i - 1]
                swapped = True
    return t, comps, moves

# Exercise 3: Bubble sort with the total number of swaps and comparisons.
def bubble_sort_with_mésure(a: list) -> tuple:
    n = len(a)
    swaps, comparisons = 0,0
    # a = copy.deepcopy(a)
    if n <= 1: return a, swaps, comparisons # Nothing to sort
    # Outer loop includes i = 1 
    for i in range(n-1, 0, -1): # Comparison: i <= 1 (or is i == 1)?  
        for j in range(0,i):    # Comparison: j >= i (or is j == i)?
            comparisons = comparisons + 1 # If this line is reached, 3 comparisons must have been performed.
            if a[j] > a[j+1]:   # Comparison: as is
                a[j], a[j+1] = a[j+1], a[j] # Swap: only when a[j] > a[j+1]
                swaps = swaps + 1 
    return a, swaps, comparisons
          

# Exercise 5: Optimise the bubble sort algorithm such that the
# i ending comparisons can be eliminated.
# This optimization gets better the more sorted the array is. 
# If the array is already sorted, this algorithm will run at most O(1).
# So given an array with small number of inversions, this algorithm will run very quickly compared to the naïve Bubble sorting algorithm above.
def bubble_sort_optimised(a: list[int]) -> tuple:
    N = len(a)
    # a = copy.deepcopy(a)
    isSwapped = False 
    swaps, comps = 0,0
    if N <= 1: return a, swaps, comps 
    
    for i in range(N-1, 0, -1):
        isSwapped = False 
        for j in range(0, i):
            comps += 1
            if a[j] > a[j+1]: 
                a[j], a[j+1] = a[j+1], a[j]
                isSwapped = True
                swaps += 1
        # After each pass, check if any swap of that pass is made. If not, then the array is already sorted
        # The rationale here is that when scanning the array, we compare adjacent elements, each comparison is checking the order each of each element, and 
        # if all comparisons are false, then the array is already sorted (so Bubble sort has this hidden subroutine which checks the order of the array in the current pass, we decide to take advantage of that by using a simple flag called swap)
        
        # print(f"Pass {N - i}: {a}")
        # input("Any key to continue:")
        # When swap is False, no swaps had been made and so we basically stop the procedure by breaking out of the outer loop and return the sorted array.
        if isSwapped == False: 
            # print(f"Pass {N - i} = 2 as expected.")
            # input("Any key to continue:")
            break
    
    # print(f"comps: {comps}")
    # input("Any key to continue:")
    return a, swaps, comps  

def bubble_sort_super_optimized(a: list) -> tuple:
    # a = copy.deepcopy(a)
    n = len(a)
    swaps = 0
    comparisons = 0
    while n > 1:  # Continue until the array is fully sorted
        new_n = 0  # Track the position of the last swap
        for j in range(1, n):
            comparisons += 1
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                swaps += 1
                new_n = j  # Update the position of the last swap
        n = new_n  # Reduce the effective size of the array to avoid redundant comparisons
    return a, swaps, comparisons


def cocktail_sort(arr):
        n = len(arr)
        comparisons = swaps = 0
        swapped = True
        start = 0
        end = n - 1
        while swapped:
            swapped = False
            # Traverse from left to right
            for i in range(start, end):
                comparisons += 1
                if arr[i] > arr[i + 1]:
                    swaps += 1
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
            # If no elements were swapped, then array is sorted
            if not swapped:
                break
            swapped = False
            end -= 1
            # Traverse from right to left
            for i in range(end - 1, start - 1, -1):
                comparisons += 1
                if arr[i] > arr[i + 1]:
                    swaps += 1
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
            start += 1
        return arr, comparisons, swaps
    
    
def cocktail_sort_optimised(arr):
    """
    Optimized Cocktail Sort: Alternate left-to-right and right-to-left passes.
    Stop if no swaps are made during a pass.
    """
    n = len(arr)
    comparisons = swaps = 0
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False
        # Traverse from left to right
        for i in range(start, end):
            comparisons += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1
                swapped = True
        if not swapped:
            break
        swapped = False
        end -= 1
        # Traverse from right to left
        for i in range(end - 1, start - 1, -1):
            comparisons += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1
                swapped = True
        start += 1
    return arr, swaps, comparisons

def cocktail_sort_super_optimised(arr):
    """
    Super Optimized Cocktail Sort: Optimizes by keeping track of the last swap
    position to avoid unnecessary comparisons.
    """
    n = len(arr)
    comparisons = swaps = 0
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False
        new_end = end
        # Traverse from left to right
        for i in range(start, end):
            comparisons += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1
                swapped = True
                new_end = i
        if not swapped:
            break
        swapped = False
        end = new_end  # Update end position based on the last swap
        new_start = start
        # Traverse from right to left
        for i in range(end - 1, start - 1, -1):
            comparisons += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1
                swapped = True
                new_start = i
        start = new_start + 1  # Update start position based on the last swap
    return arr, swaps, comparisons


 
def run_exp(num_runs: int, size: int):
    # For each size, run it num_runs time on all 3 sorting algorithms.
    
    # Mean_Comps1, Mean_Comps2, Mean_Comps3 = [], [], []
    # Mean_Swaps1, Mean_Swaps2, Mean_Swaps3 = [], [], []
    
    sum_swaps1, sum_comps1 = 0, 0
    sum_swaps2, sum_comps2 = 0, 0
    sum_swaps3, sum_comps3 = 0, 0
    sum_swaps4, sum_comps4 = 0, 0
    sum_swaps5, sum_comps5 = 0, 0
    sum_swaps6, sum_comps6 = 0, 0
    mean_swaps1, mean_swaps2, mean_swaps3 = 0,0,0    
    mean_swaps4, mean_swaps5, mean_swaps6 = 0,0,0    
    mean_comps1, mean_comps2, mean_comps3 = 0,0,0
    mean_comps4, mean_comps5, mean_comps6 = 0,0,0
    for _ in range(num_runs):
      # Create an array of the given size.
      rand_arr1 = random_array(size)
      rand_arr2 = rand_arr1[:]
      rand_arr3 = rand_arr1[:]
      rand_arr4 = rand_arr1[:]
      rand_arr5 = rand_arr1[:]
      rand_arr6 = rand_arr1[:]
      

      rand_arr1, s1, c1 = bubble_sort_with_mésure(rand_arr1)
      rand_arr2, s2, c2 = bubble_sort_optimised(rand_arr2)
      rand_arr3, s3, c3 = bubble_sort_super_optimized(rand_arr3)
      rand_arr4, s4, c4 = cocktail_sort(rand_arr4)
      rand_arr5, s5, c5 = cocktail_sort_optimised(rand_arr5)
      rand_arr6, s6, c6 = cocktail_sort_super_optimised(rand_arr6)
      
    
      sum_swaps1 += s1 
      sum_swaps2 += s2
      sum_swaps3 += s3
      
      sum_swaps4 += s4 
      sum_swaps5 += s5
      sum_swaps6 += s6

      
      sum_comps1 += c1
      sum_comps2 += c2
      sum_comps3 += c3
      
      sum_comps4 += c4
      sum_comps5 += c5
      sum_comps6 += c6
      
        
    mean_swaps1 = sum_swaps1/num_runs
    mean_swaps2 = sum_swaps2/num_runs
    mean_swaps3 = sum_swaps3/num_runs
    mean_swaps4 = sum_swaps4/num_runs
    mean_swaps5 = sum_swaps5/num_runs
    mean_swaps6 = sum_swaps6/num_runs
    # Mean_Swaps1.append(mean_swaps1)
    # Mean_Swaps2.append(mean_swaps2)
    # Mean_Swaps3.append(mean_swaps3)
    
    
    mean_comps1 = sum_comps1/num_runs
    mean_comps2 = sum_comps2/num_runs
    mean_comps3 = sum_comps3/num_runs
    mean_comps4 = sum_comps4/num_runs
    mean_comps5 = sum_comps5/num_runs
    mean_comps6 = sum_comps6/num_runs
    # Mean_Comps1.append(mean_comps1)
    # Mean_Comps2.append(mean_comps2)
    # Mean_Comps3.append(mean_comps3)
    
    return  (mean_swaps1, mean_swaps2, mean_swaps3, mean_swaps4, mean_swaps5, mean_swaps6), (mean_comps1, mean_comps2, mean_comps3, mean_comps4, mean_comps5, mean_comps6)
     
 
def test(Sizes): 
    print("Collecting sorting times for all sorting algorithms.")
    Mean_Comps1, Mean_Comps2, Mean_Comps3, Mean_Comps4, Mean_Comps5,Mean_Comps6 = [], [], [],[],[],[]
    Mean_Swaps1, Mean_Swaps2, Mean_Swaps3, Mean_Swaps4, Mean_Swaps5, Mean_Swaps6 = [], [], [],[],[],[]
    
    for size in Sizes:
        print(f"Running all 6 on a random array of size {size} for {num_runs} times...")
        (ms1,ms2,ms3,ms4,ms5,ms6), (mc1,mc2,mc3,mc4,mc5,mc6) = run_exp(num_runs, size)
        Mean_Comps1.append(mc1)
        Mean_Comps2.append(mc2)
        Mean_Comps3.append(mc3)
        Mean_Comps4.append(mc4)
        Mean_Comps5.append(mc5)
        Mean_Comps6.append(mc6)
        
        
        Mean_Swaps1.append(ms1)
        Mean_Swaps2.append(ms2)
        Mean_Swaps3.append(ms3)
        Mean_Swaps4.append(ms4)
        Mean_Swaps5.append(ms5)
        Mean_Swaps6.append(ms6)
        print(f"Result: {Mean_Comps1}\n{Mean_Comps2}\n{Mean_Comps3}")
        # input()
        
    return Mean_Comps1, Mean_Comps2, Mean_Comps3, Mean_Comps4, Mean_Comps5, Mean_Comps6, Mean_Swaps1, Mean_Swaps2, Mean_Swaps3, Mean_Swaps4, Mean_Swaps5, Mean_Swaps6
    

    

# size = int(input("Size? "))
# e = int(input("Number of experiments? "))
num_runs = 10
min_size = 0
max_size = 2000
num_steps = 100

# s1, c1, s2, c2, s3, c3 = 0,0,0,0,0,0
Sizes = generate_sizes(min_size, max_size + num_steps, num_steps)
Mean_Comps1, Mean_Comps2, Mean_Comps3, Mean_Comps4, Mean_Comps5, Mean_Comps6, Mean_Swaps1, Mean_Swaps2, Mean_Swaps3, Mean_Swaps4, Mean_Swaps5, Mean_Swaps6 = test(Sizes)


# print(Sizes)
# for size in Sizes:    
    # sum_swaps1, sum_comps1 = 0, 0
    # sum_swaps2, sum_comps2 = 0, 0
    # sum_swaps3, sum_comps3 = 0, 0
    
    # mean_swaps1, mean_swaps2, mean_swaps3 = 0,0,0    
    # mean_comps1, mean_comps2, mean_comps3 = 0,0,0

    # for _ in range(num_runs):
    #     rand_arr1 = random_array(size)
    #     rand_arr2 = rand_arr1[:]
    #     rand_arr3 = rand_arr1[:]
        
   
    #     rand_arr1, s1, c1 = bubble_sort_with_mésure(rand_arr1)
    #     rand_arr2, s2, c2 = bubble_sort_optimised(rand_arr2)
    #     rand_arr3, s3, c3 = bubble_sort_super_optimized(rand_arr3)
      
    #     sum_swaps1 += s1 
    #     sum_swaps2 += s2
    #     sum_swaps3 += s3
        
    #     sum_comps1 += c1
    #     sum_comps2 += c2
    #     sum_comps3 += c3
        
    # mean_swaps1 = sum_swaps1/num_runs
    # mean_swaps2 = sum_swaps2/num_runs
    # mean_swaps3 = sum_swaps3/num_runs
    # Mean_Swaps1.append(mean_swaps1)
    # Mean_Swaps2.append(mean_swaps2)
    # Mean_Swaps3.append(mean_swaps3)
    
    
    # mean_comps1 = sum_comps1/num_runs
    # mean_comps2 = sum_comps2/num_runs
    # mean_comps3 = sum_comps3/num_runs
    # Mean_Comps1.append(mean_comps1)
    # Mean_Comps2.append(mean_comps2)
    # Mean_Comps3.append(mean_comps3)

    # percent_opt_better_naïve = (c1-c2)/c1 * 100.0
    # percent_super_opt_better_opt = (c2-c3)/c2 * 100.0
    # percent_super_opt_better_naïve = (c1-c3)/c1 * 100.0
    # print(f"""Basic bubble sorting:\t  {c1} comps and {s1} swaps for arrays of size {size}.
    # Optimised bubble sorting: {c2} comps and {s2} swaps for arrays of size {size} <{percent_opt_better_naïve} % better than naïve>.
    # Super opt bubble sorting: {c3} comps and {s3} swaps for arrays of size {size} <{percent_super_opt_better_opt} % better than optimised and {percent_super_opt_better_naïve} % better than naïve>.
    # """)
    # print(f"""    Bubble:  {mean_comps1} comps and {mean_swaps1} swaps for arrays of size {size}.
    # Optimised bubble: {mean_comps2} comps and {mean_swaps2} swaps for arrays of size {size} 
    # Super opt bubble: {mean_comps3} comps and {mean_swaps3} swaps for arrays of size {size}
    # """)

Algorithms = ["Bubble (naïve)", 
              "Bubble (Optimized)", 
              "Bubble (Super Opt.)",
              "Cocktail (normal)", 
              "Cocktail (Optimized)", 
              "Cocktail (Super Opt.)"
              ]

# Sizes = [size*100 for size in Sizes]

# plt.plot(Sizes, Mean_Comps1, color='#ff0000', linestyle='dotted', marker='o', label=Algorithms[0], linewidth=1, markersize=5)
# plt.plot(Sizes, Mean_Comps2, color='#00ff00', linestyle='--', marker='o', label=Algorithms[1], linewidth=1, markersize=5)
# plt.plot(Sizes, Mean_Comps3, color='#0000ff', linestyle='solid', marker='o', label=Algorithms[2], linewidth=1, markersize=7)
# Generates x 
Squares = [n *n for n in Sizes]
Linear = [n for n in Sizes]
# plt.plot(Sizes, Squares, color='pink', label='n^2')
# plt.plot(Sizes, Linear, color='green', label='n')
# Generates x^2

# Plotting
plt.figure(figsize=(15, 8))

# Plot each algorithm with different line styles, markers, and colors
plt.plot(Sizes, Mean_Comps1, color='#ff5733', linestyle='-', marker='o',
         label='Bubble (Naive)', linewidth=2, markersize=7, alpha=0.8)
plt.plot(Sizes, Mean_Comps2, color='#33ff57', linestyle='--', marker='s',
         label='Bubble (Optimized)', linewidth=2, markersize=7, alpha=0.8)
plt.plot(Sizes, Mean_Comps3, color='#3357ff', linestyle='-.', marker='^',
         label='Bubble (Super Optimized)', linewidth=2, markersize=7, alpha=0.8)
plt.plot(Sizes, Mean_Swaps1, color='#ff33a1', linestyle=':', marker='D',
         label='Swaps (Naive)', linewidth=2, markersize=7, alpha=0.8)
plt.plot(Sizes, Mean_Swaps2, color='#a133ff', linestyle='-', marker='x',
         label='Swaps (Optimized)', linewidth=2, markersize=7, alpha=0.8)
plt.plot(Sizes, Mean_Swaps3, color='#33ffa1', linestyle='--', marker='*',
         label='Swaps (Super Optimized)', linewidth=2, markersize=7, alpha=0.8)

# Theoretical curves for comparison
plt.plot(Sizes, Squares, color='purple', linestyle='-.', marker='D',
         label='n^2', linewidth=2, markersize=6, alpha=0.7)
plt.plot(Sizes, Linear, color='orange', linestyle=':', marker='x',
         label='n', linewidth=2, markersize=6, alpha=0.7)


# Set axis limits and labels
plt.ylim(0, 5e5)
plt.xlim(0, max_size)
plt.title("Bubble sort Complexity")
plt.xlabel("Sizes")
plt.ylabel("Comparisons")

# Adding grid for better visibility of data points
plt.grid(True)

# Improved legend handling to ensure all labels are displayed correctly
plt.legend(loc='best')

# Better layout for plot
plt.tight_layout()

plt.legend([Algorithms[0], Algorithms[1], Algorithms[2], Algorithms[3], Algorithms[4], Algorithms[5], "n^2", "n"], loc='best')
# Display the plot
plt.show()




## https://www.angela1c.com/projects/cta_benchmarking/ctabenchmarkingproject