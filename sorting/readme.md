## I. Comparison-based sorting algorithms
1. Selection sort **O(n<sup>2</sup>)** [Tham khảo...](https://www.geeksforgeeks.org/selection-sort/)

2. Insertion sort **O(n<sup>2</sup>)** [Tham khảo...](https://www.geeksforgeeks.org/insertion-sort/)

3. Bubble sort **O(n<sup>2</sup>)** [Tham khảo...](https://www.geeksforgeeks.org/bubble-sort/)

4. Quick sort **O(n * log<sub>n</sub>)**, `worst case:` **O(n<sup>2</sup>)** [Tham khảo...](https://www.geeksforgeeks.org/quick-sort/)

5. Merge sort **O(n * log<sub>n</sub>)** [Tham khảo...](https://www.geeksforgeeks.org/merge-sort/)

6. Heap sort **O(n * log<sub>n</sub>)** [Tham khảo...](https://www.geeksforgeeks.org/heap-sort/)

## II. Other
7. Counting sort **O(n + k)** `0 <= arr[index] <= k` [Tham khảo...](https://www.geeksforgeeks.org/counting-sort/)

8. Radix sort **O(d * (n + b))** [Tham khảo...](https://www.geeksforgeeks.org/radix-sort/)
> b - the base for representing numbers (binary, decimal,...)
> d - digits in input integers
> k is maximum value -> d = **O(log<sub>b</sub>(k))**
> -> Time complexity = **O(log<sub>b</sub>(k) * (n + b))**

> The lower bound for the Comparison based sorting algorithm (Merge Sort, Heap Sort, Quick-Sort .. etc) is **Ω(n * log<sub>n</sub>)**, i.e., they cannot do better than **n * log<sub>n</sub>**
> Counting sort is a linear time sorting algorithm that sort in **O(n+k)** time when elements are in the range from 1 to k.
> **When** element are in range from 1 to n<sup>2</sup>, We can’t use counting sort because counting sort will take O(n2) which is worse than comparison-based sorting algorithms.
> **Radix Sort** is the answer. The idea of Radix Sort is to do digit by digit sort starting from least significant digit to most significant digit. Radix sort uses counting sort as a subroutine to sort.

> **Note:** Thuật toán Counting sort dùng trong Radix sort phải sắp xếp các phần tử xuất hiện trước lên trước. (Bình thường thuật toán Counting sort có thể sắp xếp phần tử xuất hiện trước phía sau, phần tử xuất hiện sau lên trước vẫn trả ra đáp áp đúng **nhưng không sử dụng được trong Radix sort**)

`Còn tiếp...`

## III. [Time complexities of all sorting algorithms](https://www.geeksforgeeks.org/time-complexities-of-all-sorting-algorithms/)