from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class A:
    """
    :ivar value:
    """
    class Meta:
        name = "a"

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

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Doc:
    """
    :ivar a:
    :ivar other_element:
    :ivar b:
    """
    class Meta:
        name = "doc"

    a: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=3,
            sequential=True
        )
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##other",
            min_occurs=0,
            max_occurs=3,
            sequential=True
        )
    )
    b: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=3,
            sequential=True
        )
    )


@dataclass
class E:
    """
    :ivar value:
    """
    class Meta:
        name = "e"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
