from dataclasses import dataclass, field
from typing import Optional, Union


@dataclass
class Doc:
    class Meta:
        name = "doc"

    root: Optional[Union[str, int]] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    value: Optional[Union[str, int]] = field(
        default=None,
    )
