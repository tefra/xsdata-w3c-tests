from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union


@dataclass
class Base:
    class Meta:
        name = "base"

    foo_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "foo",
            "max_occurs": 3,
            "process_contents": "skip",
        },
    )


@dataclass
class Foo:
    class Meta:
        name = "foo"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Doc(Base):
    class Meta:
        name = "doc"

    c1_or_c2: Optional[Union["Doc.C1", "Doc.C2"]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "c1",
                    "type": ForwardRef("Doc.C1"),
                },
                {
                    "name": "c2",
                    "type": ForwardRef("Doc.C2"),
                },
            ),
        },
    )

    @dataclass
    class C1:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "required": True,
            },
        )

    @dataclass
    class C2:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "required": True,
            },
        )
