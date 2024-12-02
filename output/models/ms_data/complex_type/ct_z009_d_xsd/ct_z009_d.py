from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union


@dataclass
class Root:
    class Meta:
        name = "root"

    element1: Optional["Root.Element1"] = field(
        default=None,
        metadata={
            "name": "Element1",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )

    @dataclass
    class Element1:
        group2_element1_or_group2_element2: list[
            Union[
                "Root.Element1.Group2Element1", "Root.Element1.Group2Element2"
            ]
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

        @dataclass
        class Group2Element1:
            value: Optional[str] = field(
                default=None,
                metadata={
                    "required": True,
                },
            )

        @dataclass
        class Group2Element2:
            value: Optional[str] = field(
                default=None,
                metadata={
                    "required": True,
                },
            )
