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
class B:
    """
    :ivar value:
    """
    class Meta:
        name = "b"
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
class D:
    """
    :ivar value:
    """
    class Meta:
        name = "d"
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
    :ivar b:
    :ivar any_element:
    :ivar c:
    """
    class Meta:
        name = "t"

    b: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="a",
            required=True
        )
    )
    any_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    c: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="a",
            required=True
        )
    )


@dataclass
class Root(T):
    class Meta:
        name = "root"
        namespace = "a"
