from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "zot"


@dataclass
class A:
    """
    :ivar value:
    """
    class Meta:
        name = "a"
        namespace = "zot"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class B:
    """
    :ivar value:
    """
    class Meta:
        name = "b"
        namespace = "zot"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class C:
    """
    :ivar value:
    """
    class Meta:
        name = "c"
        namespace = "zot"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
