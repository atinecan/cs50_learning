# Week 3 – Algorithms

## Learning Objectives
- Understand what an algorithm is
- Learn basic searching and sorting algorithms
- Introduce Big O notation
- Practice algorithmic thinking in C

---

## 1. What Is an Algorithm?

An algorithm is a step-by-step procedure for solving a problem.

In computer science, different algorithms may solve the same problem, but they can vary greatly in:
- Speed
- Efficiency
- Scalability

This week helped me understand that writing correct code is not enough —  
**how efficient the solution is also matters.**

---

## 2. Searching Algorithms

### Linear Search

Linear search checks each element one by one until the target value is found.

### Binary Search

Binary search repeatedly divides a sorted list in half to locate a target value.

- Requires sorted data
- Much faster for large inputs
- Time complexity: **O(log n)**

**Key insight:**  
Sorting data first can enable much faster searching later.

---

## 3. Big O Notation

Big O notation describes how an algorithm’s runtime grows as input size increases.

Common examples:

| Big O | Description |
|------|------------|
| O(1) | Constant time |
| O(log n) | Logarithmic |
| O(n) | Linear |
| O(n²) | Quadratic |

Big O focuses on **growth trends**, not exact execution time.

---

## 4. Sorting Algorithms (Conceptual)

### Selection Sort
- Repeatedly finds the smallest element
- Places it at the beginning

Time complexity: **O(n²)**

---

### Bubble Sort
- Swaps adjacent elements if they are out of order
- Larger values move to the end

Time complexity: **O(n²)**

---

### Merge Sort
- Uses a divide-and-conquer approach
- Recursively splits and merges arrays

Time complexity: **O(n log n)**

Merge sort is significantly more efficient but more complex.

---

## 5. Programming Insights

This week emphasized:
- Breaking problems into smaller steps
- Writing clearer and more structured code
- Thinking in terms of algorithms rather than syntax

---

## 6. Reflection

Week 3 was more challenging than previous weeks.

At first, Big O notation felt abstract, but it helped me shift my mindset from:
> “Does this program work?”  
to  
> “Will this solution scale?”

I am beginning to think more like a computer scientist.

---

## 7. Next Steps
- Practice algorithm problems
- Write and analyze more C programs
- Prepare for deeper topics in memory and data structures
