from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

__NAMESPACE__ = "http://importedXSD"


@dataclass(kw_only=True)
class Any1:
    class Meta:
        name = "any1"

    local_element_or_bbb_or_ccc: None | Any1.Bbb | Any1.Ccc | object = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "bbb",
                    "type": ForwardRef("Any1.Bbb"),
                    "namespace": "http://importedXSD",
                },
                {
                    "name": "ccc",
                    "type": ForwardRef("Any1.Ccc"),
                    "namespace": "http://importedXSD",
                },
                {
                    "wildcard": True,
                    "type": object,
                    "namespace": "##local",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Bbb:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "http://importedXSD",
            },
        )

    @dataclass(kw_only=True)
    class Ccc:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "http://importedXSD",
            },
        )


@dataclass(kw_only=True)
class Imp:
    class Meta:
        name = "imp"
        namespace = "http://importedXSD"

    att1: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    att2: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Doc1:
    class Meta:
        name = "doc1"
        namespace = "http://importedXSD"

    elem1: list[Any1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 100,
        },
    )
    elem2: list[Any1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 100,
        },
    )
