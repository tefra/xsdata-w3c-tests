from dataclasses import dataclass, field
from typing import List, Optional


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
        }
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
        }
    )


@dataclass
class Doc(Base):
    class Meta:
        name = "doc"

    c1_or_c2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "c1",
                    "type": object,
                },
                {
                    "name": "c2",
                    "type": object,
                },
            ),
        }
    )
