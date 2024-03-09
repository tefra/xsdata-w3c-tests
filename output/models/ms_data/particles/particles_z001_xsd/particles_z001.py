from dataclasses import dataclass, field
from typing import Any, List, Optional, Type, Union

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Base:
    annotation: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    element_or_any: List[Union["Base.Element", "Base.AnyType"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "element",
                    "type": Type["Base.Element"],
                    "namespace": "",
                },
                {
                    "name": "any",
                    "type": Type["Base.AnyType"],
                    "namespace": "",
                },
            ),
        },
    )

    @dataclass
    class Element:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class AnyType:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )


@dataclass
class Derived(Base):
    any: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: Optional[Derived] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
