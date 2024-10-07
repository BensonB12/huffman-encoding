from pydantic import BaseModel
from __future__ import annotations
import heapq


class HufCode:
    def __init__(self, symbol_frequencies: dict[str, float]):
        self.symbol_frequencies = symbol_frequencies
        self.root_node = self._build_huff_tree(symbol_frequencies)

    def _build_huff_tree(self, symbol_frequencies: dict[str, float]):
        if len(symbol_frequencies) < 1:
            return None

        sorted_dict = sorted(
            symbol_frequencies.items(), key=lambda item: item[1], reverse=True
        )

        root = Node(binary_value=1, symbol_value=sorted_dict.keys()[0])

        for key, value in sorted_dict:
            if sorted_dict.keys()[0] != key:
                root(right=Node(binary_value=0, symbol_value=value))

    def encode(sequence_of_symbols: str):
        return "1001001001"

    def decode(binary_string: str):
        return "This is the final string"


class Node(BaseModel):
    left: Node | None = None
    right: Node | None = None
    symbol_value: str | None = None
    binary_value: int
