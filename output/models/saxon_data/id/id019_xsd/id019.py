from dataclasses import dataclass, field
from typing import List, Union


@dataclass
class Para:
    class Meta:
        name = "para"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    entity: Union[str, int] = field(
        default="entity1",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"

    para: List[Para] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
