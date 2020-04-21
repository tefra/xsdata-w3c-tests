from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "pSubstitutions"


@dataclass
class A:
    """
    :ivar c:
    """
    c: List[int] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=3
        )
    )


@dataclass
class C:
    """
    :ivar c:
    """
    c: List[int] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=2
        )
    )


@dataclass
class B(A):
    """
    :ivar d:
    """
    d: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class E(A):
    class Meta:
        name = "e"
        namespace = "pSubstitutions"
