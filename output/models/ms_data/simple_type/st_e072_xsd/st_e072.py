from dataclasses import dataclass, field
from typing import Optional, Union


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


@dataclass
class Doc:
    """
    :ivar root:
    """
    class Meta:
        name = "doc"

    root: Optional[Root] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
