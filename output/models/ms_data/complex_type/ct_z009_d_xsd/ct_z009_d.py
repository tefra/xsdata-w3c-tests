from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    element1: Root.Element1 = field(
        metadata={
            "name": "Element1",
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass(kw_only=True)
    class Element1:
        group2_element1_or_group2_element2: list[
            Root.Element1.Group2Element1 | Root.Element1.Group2Element2
        ] = field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "Group2_Element1",
                        "type": ForwardRef("Root.Element1.Group2Element1"),
                        "namespace": "",
                    },
                    {
                        "name": "Group2_Element2",
                        "type": ForwardRef("Root.Element1.Group2Element2"),
                        "namespace": "",
                    },
                ),
            },
        )

        @dataclass(kw_only=True)
        class Group2Element1:
            value: str = field(default="")

        @dataclass(kw_only=True)
        class Group2Element2:
            value: str = field(default="")
