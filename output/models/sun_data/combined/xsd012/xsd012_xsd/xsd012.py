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
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
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
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
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
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
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
        metadata={
            "type": "Element",
        }
    )
    element_only: List["Root.ElementOnly"] = field(
        default_factory=list,
        metadata={
            "name": "elementOnly",
            "type": "Element",
        }
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
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        a: List[A] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            }
        )
        b: List[B] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            }
        )
        c: List[C] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            }
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
            metadata={
                "type": "Element",
            }
        )
        b: List[B] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            }
        )
        c: List[C] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            }
        )
