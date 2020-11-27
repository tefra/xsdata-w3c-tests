from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    a: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 200,
        }
    )
    b: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Doc(FooType):
    class Meta:
        name = "doc"
