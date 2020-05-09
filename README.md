# Python Algorithms

![Tests](https://github.com/jcockbain/python-algorithms/workflows/Python%20application/badge.svg)
![codecov](https://codecov.io/gh/jcockbain/python-algorithms/branch/master/graph/badge.svg)

Common data structures and algorithms, written in Python.

## Tests

To run the unit tests, with pytest:

```shell
# all tests
python3 -m pytest

# with coverage
python3 pytest --cov

# specific path (e.g backtracking)
python3 pytest backtracking
```

## Algorithm List

- [Backtracking](backtracking)

  - [generate_parentheses](backtracking/generate_parentheses.py)
  - [letter_combinations_of_a_phone_number](backtracking/letter_combinations_of_a_phone_number.py)
  - [permutations](backtracking/permutations.py)
  - [n_queens](backtracking/n_queens.py.py)
  - [sudoku_solver](backtracking/sudoku_solver.py)

- [Binary Tree](binary_tree)

  - [inorder_traversal](binary_tree/inorder_traversal.py)
  - [levelorder_traversal](binary_tree/levelorder_traversal.py)
  - [postorder_traversal](binary_tree/postorder_traversal.py)
  - [max_depth](binary_tree/max_depth.py)
  - [min_depth](binary_tree/min_depth.py)

- [Bit Manipulation](bit_manipulation)

  - [hamming_distance](bit_manipulation/hamming_distance.py)
  - [hamming_weight](bit_manipulation/hamming_weight.py)
  - [number_complement](bit_manipulation/find_complement.py)

- [Dynamic Programming](dynamic_programming)

  - [climb_stairs](dynamic_programming/climb_stairs.py.py)
  - [rob_houses](dynamic_programming/rob_houses.py)
  - [knapsack](dynamic_programming/knapsack.py)
  - [unbounded_knapsack](dynamic_programming/unbounded_knapsack.py)
  - [paint_houses](dynamic_programming/paint_houses.py)
  - [jump_game](dynamic_programming/jump_game.py)
  - [minimum_2d_path](dynamic_programming/minimum_2d_path.py)
  - [longest_palindromic_subsequence](dynamic_programming/longest_palindromic_subsequence.py)

- [Graphs](graphs)

  - [open_the_lock](graphs/open_the_lock)
  - [number_of_islands](graphs/number_of_islands.py)

- [Linked List](linked_list)

  - [add_two_numbers](linked_list/add_two_numbers.py)
  - [reverse_linked_list](linked_list/reverse_linked_list.py)

- [Queue](queue)

  - [circular_queue](queue/circular_queue.py)

- [Searching](searching)

  - [binary_search](searching/binary_search.py)

- [Sorting](sorting)

  - [insertion_sort](sorting/insertion_sort.py)
  - [selection_sort](sorting/selection_sort.py)

- [Stack](stack)

  - [valid_parentheses](stack/valid_parentheses.py)

- [Trie](trie)

  - [trie](trie/trie)
