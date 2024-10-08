from dataclasses import dataclass, field
from typing import Optional, Union


@dataclass
class Root:
    class Meta:
        name = "root"

    union_of_ids: Optional[Union[int, bool, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    idref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
