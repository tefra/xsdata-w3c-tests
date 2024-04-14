from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union

__NAMESPACE__ = "http://foo.com"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://foo.com"

    child1_or_child2: List[Union["Root.Child1", "Root.Child2"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "child1",
                    "type": ForwardRef("Root.Child1"),
                },
                {
                    "name": "child2",
                    "type": ForwardRef("Root.Child2"),
                },
            ),
        },
    )

    @dataclass
    class Child1:
        value: List[str] = field(
            default_factory=list,
            metadata={
                "min_length": 5,
                "tokens": True,
            },
        )

    @dataclass
    class Child2:
        value: Optional[Union[bool, str]] = field(
            default=None,
            metadata={
                "required": True,
                "min_length": 5,
            },
        )
