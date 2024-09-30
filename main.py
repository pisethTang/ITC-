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


 
# def run_exp(num_runs: int, size: int):
    # For each size, run it num_runs time on all 3 sorting algorithms.
    
    # Mean_Comps1, Mean_Comps2, Mean_Comps3 = [], [], []
    # Mean_Swaps1, Mean_Swaps2, Mean_Swaps3 = [], [], []
    
    sum_swaps1, sum_comps1 = 0, 0
    sum_swaps2, sum_comps2 = 0, 0
    sum_swaps3, sum_comps3 = 0, 0
    mean_swaps1, mean_swaps2, mean_swaps3 = 0,0,0    
    mean_comps1, mean_comps2, mean_comps3 = 0,0,0
    for _ in range(num_runs):
      # Create an array of the given size.
      rand_arr1 = random_array(size)
      rand_arr2 = rand_arr1[:]
      rand_arr3 = rand_arr1[:]
      

      rand_arr1, s1, c1 = bubble_sort_with_mésure(rand_arr1)
      rand_arr2, s2, c2 = bubble_sort_optimised(rand_arr2)
      rand_arr3, s3, c3 = bubble_sort_super_optimized(rand_arr3)
    
      sum_swaps1 += s1 
      sum_swaps2 += s2
      sum_swaps3 += s3
      
      sum_comps1 += c1
      sum_comps2 += c2
      sum_comps3 += c3
        
    mean_swaps1 = sum_swaps1/num_runs
    mean_swaps2 = sum_swaps2/num_runs
    mean_swaps3 = sum_swaps3/num_runs
    # Mean_Swaps1.append(mean_swaps1)
    # Mean_Swaps2.append(mean_swaps2)
    # Mean_Swaps3.append(mean_swaps3)
    
    
    mean_comps1 = sum_comps1/num_runs
    mean_comps2 = sum_comps2/num_runs
    mean_comps3 = sum_comps3/num_runs
    # Mean_Comps1.append(mean_comps1)
    # Mean_Comps2.append(mean_comps2)
    # Mean_Comps3.append(mean_comps3)
    
    return  (mean_swaps1, mean_swaps2, mean_swaps3), (mean_comps1, mean_comps2, mean_comps3)
    
 
# def experiences(sorting_algo, size, sample):pass 
 
 
# def test(Sizes): 
    print("Collecting sorting times for all sorting algorithms.")
    Mean_Comps1, Mean_Comps2, Mean_Comps3 = [], [], []
    Mean_Swaps1, Mean_Swaps2, Mean_Swaps3 = [], [], []
    
    for size in Sizes:
        print(f"Running all 3 on a random array of size {size} for {num_runs} times...")
        (ms1,ms2,ms3), (mc1,mc2,mc3) = run_exp(num_runs, size)
        Mean_Comps1.append(mc1)
        Mean_Comps2.append(mc2)
        Mean_Comps3.append(mc3)
        Mean_Swaps1.append(ms1)
        Mean_Swaps2.append(ms2)
        Mean_Swaps3.append(ms3)
        print(f"Result: {Mean_Comps1}\n{Mean_Comps2}\n{Mean_Comps3}")
        # input()
        
    return Mean_Comps1, Mean_Comps2, Mean_Comps3, Mean_Swaps1, Mean_Swaps2, Mean_Swaps3
    

# def isSorted()




A = [3,13, -20, 39, 210, 933, -20, -20, -200]
print(A)
# cocktail_sort(A)
# cocktail_sort_optimised(A)
cocktail_sort_super_optimised(A)
print(A)