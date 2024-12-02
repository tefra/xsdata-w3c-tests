from dataclasses import dataclass, field
from typing import Union


@dataclass
class Root:
    class Meta:
        name = "root"

    union_of_ids: list[Union[int, bool, str]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    idref: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
