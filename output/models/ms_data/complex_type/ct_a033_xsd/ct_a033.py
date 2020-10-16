from dataclasses import dataclass, field
from typing import List


@dataclass
class FooType:
    """
    :ivar content:
    """
    class Meta:
        name = "fooType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
