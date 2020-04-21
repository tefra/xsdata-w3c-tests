from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "a"


@dataclass
class A:
    """
    :ivar value:
    """
    class Meta:
        name = "a"
        namespace = "a"

    value: Optional[int] = field(
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
        namespace = "a"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class T:
    """
    :ivar any_element:
    """
    class Meta:
        name = "t"

    any_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Root(T):
    class Meta:
        name = "root"
        namespace = "a"
