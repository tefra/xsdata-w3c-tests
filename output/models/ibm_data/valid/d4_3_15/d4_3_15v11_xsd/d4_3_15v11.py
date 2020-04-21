from dataclasses import dataclass, field
from typing import Optional


@dataclass
class RootType:
    """
    :ivar ele:
    :ivar date:
    """
    class Meta:
        name = "rootType"

    ele: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    date: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Root(RootType):
    class Meta:
        name = "root"
