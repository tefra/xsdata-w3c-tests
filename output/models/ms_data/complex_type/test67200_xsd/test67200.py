from dataclasses import dataclass, field
from typing import Optional


@dataclass
class TypeAbstract:
    class Meta:
        name = "typeAbstract"


@dataclass
class Elt1(TypeAbstract):
    class Meta:
        name = "elt1"


@dataclass
class TypeA(TypeAbstract):
    class Meta:
        name = "typeA"

    elt2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
