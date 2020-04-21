from dataclasses import dataclass, field
from typing import Optional


@dataclass
class RootType:
    """
    :ivar value:
    :ivar attr:
    """
    class Meta:
        name = "rootType"

    value: Optional[str] = field(
        default=None,
    )
    attr: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Root(RootType):
    class Meta:
        name = "root"
