from matplotlib import pyplot as plt 
import bubble 
import insertion 
import random_resources
import merge 
import selection
import quick_sort


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
      rand_arr1 = bubble.random_array(size)
      rand_arr2 = rand_arr1[:]
      rand_arr3 = rand_arr1[:]
      rand_arr4 = rand_arr1[:]
      rand_arr5 = rand_arr1[:]
      rand_arr6 = rand_arr1[:]
      

      rand_arr1, s1, c1 = bubble.bubble_sort_with_mésure(rand_arr1)
      rand_arr2, s2, c2 = bubble.bubble_sort_optimised(rand_arr2)
      rand_arr3, s3, c3 = bubble.bubble_sort_super_optimized(rand_arr3)
      rand_arr4, s4, c4 = bubble.cocktail_sort(rand_arr4)
      rand_arr5, s5, c5 = bubble.cocktail_sort_optimised(rand_arr5)
      rand_arr6, s6, c6 = bubble.cocktail_sort_super_optimised(rand_arr6)
      
    
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
Sizes = bubble.generate_sizes(min_size, max_size + num_steps, num_steps)
Mean_Comps1, Mean_Comps2, Mean_Comps3, Mean_Comps4, Mean_Comps5, Mean_Comps6, Mean_Swaps1, Mean_Swaps2, Mean_Swaps3, Mean_Swaps4, Mean_Swaps5, Mean_Swaps6 = test(Sizes)


Bubble_Names = ["Bubble (naïve)", 
              "Bubble (Optimized)", 
              "Bubble (Super Opt.)",
              "Cocktail (normal)", 
              "Cocktail (Optimized)", 
              "Cocktail (Super Opt.)"]
Insertion_Names = ["Insertion (Normal)", "Insertion (Optimized)",]
Merge_Names = ["Merge_Sort (Normal)", "Merge_Sort (Optimized)"]
Selection_Names = ["Selection (Normal)"]
QS_Names = ["Quick Sort(Normal)", "Quick Sort(Optimized)"]

Miscellaneous_Names = ["Linear Search", "Dichotomic Search"]

Algorithm_Names = [Bubble_Names,
                  Selection_Names,
                  Insertion_Names,
                  Merge_Names,
                  QS_Names,
                  Miscellaneous_Names
                ]


sorting_algorithms = {
    Algorithm_Names[0][0]: bubble.bubble_sort_with_mésure,
    Algorithm_Names[0][1]: bubble.bubble_sort_optimised,
    Algorithm_Names[0][2]: bubble.bubble_sort_super_optimized,
    Algorithm_Names[0][3]: bubble.cocktail_sort,
    Algorithm_Names[0][4]: bubble.cocktail_sort_optimised,
    Algorithm_Names[0][5]: bubble.cocktail_sort_super_optimised,
    
    Algorithm_Names[1][0]: selection.selection,
    Algorithm_Names[1][1]: selection.shell_sort,
    
    Algorithm_Names[2][0]: insertion.insertion_sort,
    Algorithm_Names[2][1]: insertion.insertion_sort_optimized,
    
    Algorithm_Names[3][0]: merge.merge_sort,
    Algorithm_Names[3][1]: merge.merge_sort_optimized,
    Algorithm_Names[3][2]: merge.merge_sort_super_optimized,
    
    Algorithm_Names[4][0]: quick_sort.quick_sort,
    Algorithm_Names[5][1]: quick_sort.quick_sort_optimised,
    
    # Algorithm_Names[][]: 
    
}



Algorithm_to_be_benchmarked = [sorting_algorithms[2], 
                               sorting_algorithms[5], 
                               sorting_algorithms[4]]




Squares = [n *n for n in Sizes]
Linear = [n for n in Sizes]

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

plt.legend([Algorithm_Name[0], Algorithm_Name[1], Algorithm_Name[2], Algorithm_Name[3], Algorithm_Name[4], Algorithm_Name[5], "n^2", "n"], loc='best')
# Display the plot
plt.show()




## https://www.angela1c.com/projects/cta_benchmarking/ctabenchmarkingproject