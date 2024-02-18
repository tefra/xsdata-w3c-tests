from dataclasses import dataclass, field
from typing import List, Union

__NAMESPACE__ = "http://foo.com"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://foo.com"

    child1_or_child2: List[Union[str, bool]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "child1",
                    "type": List[str],
                    "default_factory": list,
                    "min_length": 5,
                    "tokens": True,
                },
                {
                    "name": "child2",
                    "type": Type["Root.Child2"],
                },
            ),
        },
    )

    @dataclass
    class Child2:
        value: Union[bool, str] = field(
            default="",
            metadata={
                "min_length": 5,
            },
        )
