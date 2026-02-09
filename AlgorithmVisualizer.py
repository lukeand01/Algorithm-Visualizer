
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

def swap(A, i, j):
    A[i], A[j] = A[j], A[i]

# --- Sorting Algorithms (Generators) ---

def bubble_sort(A):
    n = len(A)
    for i in range(n):
        for j in range(0, n - i - 1):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)
            yield A

def selection_sort(A):
    for i in range(len(A)):
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[j] < A[min_idx]:
                min_idx = j
            yield A
        swap(A, i, min_idx)
        yield A

def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
            yield A
        A[j + 1] = key
        yield A

def quick_sort(A, start, end):
    if start >= end:
        return
    pivot = A[end]
    pivot_idx = start
    for i in range(start, end):
        if A[i] < pivot:
            swap(A, i, pivot_idx)
            pivot_idx += 1
        yield A
    swap(A, pivot_idx, end)
    yield A
    yield from quick_sort(A, start, pivot_idx - 1)
    yield from quick_sort(A, pivot_idx + 1, end)

def merge_sort(A, start, end):
    if end <= start:
        return
    mid = start + (end - start) // 2
    yield from merge_sort(A, start, mid)
    yield from merge_sort(A, mid + 1, end)
    
    # Merge logic
    left = A[start:mid + 1]
    right = A[mid + 1:end + 1]
    i = j = 0
    for k in range(start, end + 1):
        if i < len(left) and (j >= len(right) or left[i] <= right[j]):
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        yield A

# --- Visualization Logic ---

def run_visualizer():
    N = 30 
    methods = ["Bubble", "Selection", "Insertion", "Quick", "Merge"]
    print(f"Available methods: {methods}")
    choice = input("Choose an algorithm: ").capitalize()
    
    data = list(range(1, N + 1))
    random.shuffle(data)
    
    # Select generator
    if choice == "Bubble": generator = bubble_sort(data)
    elif choice == "Selection": generator = selection_sort(data)
    elif choice == "Insertion": generator = insertion_sort(data)
    elif choice == "Quick": generator = quick_sort(data, 0, N - 1)
    elif choice == "Merge": generator = merge_sort(data, 0, N - 1)
    else: 
        print("Invalid choice, defaulting to Bubble Sort.")
        generator = bubble_sort(data)

    fig, ax = plt.subplots()
    ax.set_title(f"{choice} Sort Visualizer")
    bar_rects = ax.bar(range(len(data)), data, align="edge", color="skyblue")
    
    # Update function for animation
    def update(data):
        for rect, val in zip(bar_rects, data):
            rect.set_height(val)
        return bar_rects

    
    anim = animation.FuncAnimation(fig, func=update, frames=generator, 
                                   interval=20, repeat=False, cache_frame_data=False)
    plt.show()

    run_visualizer()



if __name__ == "__main__":
    run_visualizer()