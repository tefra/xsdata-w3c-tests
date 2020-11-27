from dataclasses import dataclass, field
from typing import List, Union


@dataclass
class Root:
    class Meta:
        name = "root"

    value: List[Union[str, bool]] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
