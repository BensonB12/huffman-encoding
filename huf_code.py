from __future__ import annotations
from pydantic import BaseModel
from typing import Optional, Dict
import heapq


class Node(BaseModel):
    left: Optional[Node] = None
    right: Optional[Node] = None
    symbol_value: Optional[str] = None
    frequency: Optional[float] = None


class HufCode:
    def __init__(self, symbol_frequencies: Dict[str, float]):
        self.symbol_frequencies = symbol_frequencies
        self.root_node = self._build_huff_tree(symbol_frequencies)
        self.codes = {}
        if self.root_node:
            self._generate_codes(self.root_node, "")

    def _build_huff_tree(self, symbol_frequencies: Dict[str, float]) -> Node:
        heap = [
            [freq, Node(symbol_value=symbol, frequency=freq)]
            for symbol, freq in symbol_frequencies.items()
        ]
        heapq.heapify(heap)

        while len(heap) > 1:
            low1 = heapq.heappop(heap)
            low2 = heapq.heappop(heap)
            merged = Node(left=low1[1], right=low2[1], frequency=low1[0] + low2[0])
            heapq.heappush(heap, [merged.frequency, merged])

        return heapq.heappop(heap)[1] if heap else None

    def _generate_codes(self, node: Node, code: str):
        if node.symbol_value is not None:
            self.codes[node.symbol_value] = code
        else:
            if node.left:
                self._generate_codes(node.left, code + "0")
            if node.right:
                self._generate_codes(node.right, code + "1")

    def encode(self, sequence_of_symbols: str) -> str:
        return "".join(self.codes[symbol] for symbol in sequence_of_symbols)

    def decode(self, binary_string: str) -> str:
        decoded_symbols = []
        current_node = self.root_node
        for bit in binary_string:
            if bit == "0":
                current_node = current_node.left
            else:
                current_node = current_node.right
            if current_node.symbol_value is not None:
                decoded_symbols.append(current_node.symbol_value)
                current_node = self.root_node
        return "".join(decoded_symbols)

    def to_dict(self) -> Dict[str, str]:
        return self.codes


def test_huf1():
    huf = HufCode(dict(a=6.8, o=5.9))
    assert huf.to_dict() == {"o": "0", "a": "1"}
    assert "".join(huf.encode("oaaoo")) == "01100"
    assert "".join(huf.decode("01100")) == "oaaoo"


def test_huf2():
    huf = HufCode(dict(o=5.9, a=6.8, t=7.7, e=10.2, _=18.3))
    assert huf.to_dict() == {"_": "0", "o": "100", "a": "101", "t": "110", "e": "111"}
    assert "".join(huf.encode("ate_oat_too")) == "10111011101001011100110100100"
    assert "".join(huf.decode("10111011101001011100110100100")) == "ate_oat_too"


def test_huf3():
    huf = HufCode(
        dict(
            _=18.3,
            h=4.9,
            s=5.1,
            e=10.2,
            n=5.5,
            i=5.8,
            o=5.9,
            c=2.6,
            l=3.4,
            a=6.8,
            d=3.5,
            f=1.8,
            w=1.9,
            t=7.7,
            m=2.1,
            u=2.4,
            r=4.8,
        )
    )
    assert huf.to_dict() == dict(
        _="00",
        h="0100",
        s="0101",
        e="011",
        n="1000",
        i="1001",
        o="1010",
        c="10110",
        l="10111",
        a="1100",
        d="11010",
        f="110110",
        w="110111",
        t="1110",
        m="111100",
        u="111101",
        r="11111",
    )
    assert (
        "".join(huf.encode("what_is_this"))
        == "1101110100110011100010010101001110010010010101"
    )
    assert (
        "".join(huf.decode("1101110100110011100010010101001110010010010101"))
        == "what_is_this"
    )
