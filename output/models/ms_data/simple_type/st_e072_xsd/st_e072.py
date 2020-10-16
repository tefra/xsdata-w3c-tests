from dataclasses import dataclass, field
from typing import Optional, Union


@dataclass
class Doc:
    """
    :ivar root:
    """
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
    """
    :ivar value:
    """
    class Meta:
        name = "root"

    value: Optional[Union[str, int]] = field(
        default=None,
    )
