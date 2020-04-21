from dataclasses import dataclass, field
from typing import Optional


@dataclass
class RootType:
    """
    :ivar ele:
    :ivar min:
    :ivar max:
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
    min: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    max: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Root(RootType):
    class Meta:
        name = "root"
