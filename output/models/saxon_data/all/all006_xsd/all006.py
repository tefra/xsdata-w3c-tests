from dataclasses import dataclass, field
from typing import Optional


@dataclass
class C:
    """
    :ivar value:
    """
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            pattern=r".*:00"
        )
    )


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
class C:
    """
    :ivar value:
    """
    class Meta:
        name = "c"

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
    :ivar b:
    :ivar target_namespace_element:
    :ivar other_ns_element:
    """
    class Meta:
        name = "doc"

    a: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    b: Optional[B] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    target_namespace_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##targetNamespace",
            required=True
        )
    )
    other_ns_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="http://other.ns/",
            required=True
        )
    )