from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "a"


@dataclass
class C:
    """
    :ivar a:
    :ivar any_element:
    """
    class Meta:
        name = "c"

    a: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    any_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            min_occurs=1,
            max_occurs=2
        )
    )


@dataclass
class D:
    """
    :ivar a:
    :ivar any_element:
    """
    class Meta:
        name = "d"

    a: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class Root:
    """
    :ivar value:
    """
    class Meta:
        name = "root"
        namespace = "a"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )