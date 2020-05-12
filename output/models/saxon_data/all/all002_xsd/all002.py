from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class C:
    """
    :ivar any_element:
    """
    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class D:
    """
    :ivar any_element:
    """
    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class C:
    """
    :ivar any_element:
    """
    class Meta:
        name = "c"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class D:
    """
    :ivar any_element:
    """
    class Meta:
        name = "d"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class Doc:
    """
    :ivar a:
    :ivar b:
    :ivar c_element:
    :ivar c:
    :ivar d_element:
    :ivar d:
    """
    class Meta:
        name = "doc"

    a: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=5
        )
    )
    b: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=5
        )
    )
    c_element: List[C] = field(
        default_factory=list,
        metadata=dict(
            name="C",
            type="Element",
            min_occurs=2,
            max_occurs=9223372036854775807
        )
    )
    c: List[C] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=2,
            max_occurs=9223372036854775807
        )
    )
    d_element: Optional[D] = field(
        default=None,
        metadata=dict(
            name="D",
            type="Element",
            required=True
        )
    )
    d: Optional[D] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
