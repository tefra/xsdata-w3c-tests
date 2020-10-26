from dataclasses import dataclass, field
from typing import List, Optional, Type

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
    :ivar mixed_or_element_only:
    """
    class Meta:
        name = "root"
        namespace = "foo"

    mixed_or_element_only: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "mixed",
                    "type": Type["Root.Mixed"],
                },
                {
                    "name": "elementOnly",
                    "type": Type["Root.ElementOnly"],
                },
            ),
        }
    )

    @dataclass
    class Mixed:
        """
        :ivar content:
        :ivar a_or_b_or_c:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        a_or_b_or_c: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "a",
                        "type": A,
                    },
                    {
                        "name": "b",
                        "type": B,
                    },
                    {
                        "name": "c",
                        "type": C,
                    },
                ),
            }
        )

    @dataclass
    class ElementOnly:
        """
        :ivar a_or_b_or_c:
        """
        a_or_b_or_c: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "a",
                        "type": A,
                    },
                    {
                        "name": "b",
                        "type": B,
                    },
                    {
                        "name": "c",
                        "type": C,
                    },
                ),
            }
        )
