from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef


@dataclass(kw_only=True)
class Node:
    class Meta:
        name = "node"

    node_or_id: list[Node | str] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "node",
                    "type": ForwardRef("Node"),
                },
                {
                    "name": "id",
                    "type": str,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    node: list[Node] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
