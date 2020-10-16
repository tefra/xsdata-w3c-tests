from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "foo"


@dataclass
class Scope:
    """
    :ivar key:
    :ivar ref:
    """
    class Meta:
        name = "scope"
        namespace = "foo"

    key: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    ref: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Root:
    """
    :ivar scope:
    """
    class Meta:
        name = "root"
        namespace = "foo"

    scope: List[Scope] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
