from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ComType:
    """
    :ivar value:
    :ivar attr:
    """
    class Meta:
        name = "comType"

    value: Optional[int] = field(
        default=None,
    )
    attr: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Root(ComType):
    class Meta:
        name = "root"
