from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef


@dataclass(kw_only=True)
class PseudoId:
    class Meta:
        name = "pseudoID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    a: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class PseudoIdref:
    class Meta:
        name = "pseudoIDREF"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    a: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Node:
    class Meta:
        name = "node"

    node_or_id_or_idref: list[Node | PseudoId | PseudoIdref] = field(
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
                    "type": PseudoId,
                },
                {
                    "name": "idref",
                    "type": PseudoIdref,
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
