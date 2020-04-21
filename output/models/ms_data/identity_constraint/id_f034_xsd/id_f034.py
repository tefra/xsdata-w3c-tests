from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Tabletype:
    """
    :ivar r:
    :ivar c:
    """
    class Meta:
        name = "tabletype"

    r: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    c: Optional["Tabletype.C"] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )

    @dataclass
    class C:
        """
        :ivar content:
        :ivar val:
        """
        content: Optional[object] = field(
            default=None,
            metadata=dict(
                type="Wildcard",
                namespace="##any"
            )
        )
        val: Optional[str] = field(
            default=None,
            metadata=dict(
                type="Attribute"
            )
        )


@dataclass
class T(Tabletype):
    class Meta:
        name = "t"


@dataclass
class Root:
    """
    :ivar t:
    """
    class Meta:
        name = "root"

    t: List[T] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
