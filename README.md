# Huffman Codec (HufCodec)

## Requirements

You need to implement and test (using `pytest`) a Python class `HufCodec`. The constructor of this class should accept a dictionary of symbol frequencies and build an internal representation of the optimal Huffman code for that distribution.

### Class Structure

Your class `HufCodec` should contain the following methods:

- **`encode()`**: 
    - Takes a sequence of symbols and returns a sequence consisting only of `'0'` and `'1'`.
    
- **`decode()`**: 
    - Takes in a string of `'0'`s and `'1'`s and returns the corresponding sequence of symbols.

You can use any additional helper methods or internal structure to achieve this functionality.

## What to Submit

- Copy and paste your Python code, including tests, into the text area provided.

## Notes

### Overview

A Huffman code can be represented using a graph where:

- Each node has two outgoing edges labeled `0` and `1`.
- A node can store a symbol, and one node is designated as the "start" node.
- This graph represents a function that maps a sequence of bits to a sequence of symbols.
  
The basic idea of the algorithm is to create a binary tree where each leaf node represents a unique symbol. The path from the root to the leaf encodes the symbol as a sequence of bits (`0` or `1`). The length of the path depends on the frequency of the symbol. Symbols that occur more frequently are given shorter paths, while less frequent symbols have longer paths, optimizing the average bits per symbol.

### Detailed Algorithm

The algorithm for constructing an optimal Huffman code is a greedy algorithm:

1. Start by adding a leaf node for each symbol to a priority queue, with the priority being the symbol frequency.
2. Repeat until only one node remains in the queue:
    - Remove the two nodes with the lowest frequencies.
    - Create a new internal node with these two nodes as its children.
    - The frequency of the new node is the sum of its children's frequencies.
3. The final tree represents the Huffman encoding.

Using this tree, you can:
- **Encode**: To map symbols to bits, start at the appropriate leaf and follow the path to the root, recording the edge labels. Then reverse the sequence of labels.
- **Decode**: To map bits back to symbols, walk down the tree from the root, following the incoming bits until you reach a leaf, then output the symbol stored at that leaf.

### Performance

The performance of the Huffman encoding depends on the balance of the tree. If the tree is balanced and there are `N` symbols, the encoding will require about `log_2(N)` bits per symbol. However, if certain symbols are more frequent than others, the algorithm optimizes the encoding, producing an average bit length lower than `log_2(N)`.

This bit length approaches the entropy of the symbol distribution if the symbols are independent and identically distributed.
