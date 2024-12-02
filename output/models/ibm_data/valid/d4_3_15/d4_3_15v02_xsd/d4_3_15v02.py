from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ArrayType:
    class Meta:
        name = "arrayType"

    ele: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    length: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Root(ArrayType):
    class Meta:
        name = "root"
