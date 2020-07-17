from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "foo"


@dataclass
class A:
    """
    :ivar any_element:
    """
    class Meta:
        name = "a"
        namespace = "foo"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class B:
    """
    :ivar any_element:
    """
    class Meta:
        name = "b"
        namespace = "foo"

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
        namespace = "foo"

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
    :ivar mixed:
    :ivar element_only:
    """
    class Meta:
        name = "root"
        namespace = "foo"

    mixed: List["Root.Mixed"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    element_only: List["Root.ElementOnly"] = field(
        default_factory=list,
        metadata=dict(
            name="elementOnly",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )

    @dataclass
    class Mixed:
        """
        :ivar content:
        :ivar a:
        :ivar b:
        :ivar c:
        """
        content: List[object] = field(
            default_factory=list,
            metadata=dict(
                type="Wildcard",
                namespace="##any",
                mixed=True,
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        a: List[A] = field(
            default_factory=list,
            metadata=dict(
                type="Element",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        b: List[B] = field(
            default_factory=list,
            metadata=dict(
                type="Element",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        c: List[C] = field(
            default_factory=list,
            metadata=dict(
                type="Element",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )

    @dataclass
    class ElementOnly:
        """
        :ivar a:
        :ivar b:
        :ivar c:
        """
        a: List[A] = field(
            default_factory=list,
            metadata=dict(
                type="Element",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        b: List[B] = field(
            default_factory=list,
            metadata=dict(
                type="Element",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        c: List[C] = field(
            default_factory=list,
            metadata=dict(
                type="Element",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
