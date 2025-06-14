# Quicksort Benchmark Suite (Python)

This project benchmarks two versions of the Quicksort algorithm:

- **Randomized Quicksort** — selects the pivot uniformly at random from the subarray.
- **Deterministic Quicksort** — always selects the first element as the pivot.

The benchmarks compare performance across different types of input arrays to analyze best-case, average-case, and worst-case behaviors.

---

## 📂 Benchmark Scenarios

The benchmark tests both implementations against the following input types:

1. **Random Array** — Elements are randomly shuffled integers.
2. **Sorted Array** — Increasing order; worst-case for deterministic Quicksort.
3. **Reverse-Sorted Array** — Decreasing order; also worst-case for deterministic Quicksort.
4. **Repeated Elements** — All elements are the same.

Each benchmark was run 100 times on arrays of size 1000.

---

## 📈 Summary of Results

| Input Type           | Randomized Quicksort (s) | Deterministic Quicksort (s) |
|----------------------|---------------------------|------------------------------|
| Random Array         | 0.0907                    | 0.0605                       |
| Sorted Array         | 0.0740                    | 1.0296                       |
| Reverse-Sorted Array | 0.0747                    | 1.7737                       |
| Repeated Elements    | 2.2840                    | 2.2527                       |

> **Interpretation:**
>
> - **Randomized Quicksort** performs consistently well across all input types, with relatively minor slowdowns for repeated elements.
> - **Deterministic Quicksort** is fast on random inputs but suffers drastically on sorted or reverse-sorted arrays, confirming the known worst-case `O(n²)` behavior.
> - Both implementations slow down significantly on repeated data due to poor partitioning efficiency (many equal elements). Optimizations like "three-way partitioning" could improve this.

---

## 🚀 How to Run

```
python3 quick_sort.py
```
