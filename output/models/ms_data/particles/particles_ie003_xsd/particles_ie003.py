from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Base:
    class Meta:
        name = "base"

    e1_or_e2: list[Union["Base.E1", "Base.E2"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "e1",
                    "type": ForwardRef("Base.E1"),
                    "namespace": "http://xsdtesting",
                },
                {
                    "name": "e2",
                    "type": ForwardRef("Base.E2"),
                    "namespace": "http://xsdtesting",
                },
            ),
        },
    )

    @dataclass
    class E1:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "http://xsdtesting",
                "required": True,
            },
        )

    @dataclass
    class E2:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "http://xsdtesting",
                "required": True,
            },
        )


@dataclass
class Testing(Base):
    class Meta:
        name = "testing"

    e1_or_e2: list[Union["Testing.E1", "Testing.E2"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "e1",
                    "type": ForwardRef("Testing.E1"),
                    "namespace": "http://xsdtesting",
                    "max_occurs": 9999999,
                },
                {
                    "name": "e2",
                    "type": ForwardRef("Testing.E2"),
                    "namespace": "http://xsdtesting",
                    "max_occurs": 9999999,
                },
            ),
            "max_occurs": 9999999,
        },
    )

    @dataclass
    class E1:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "http://xsdtesting",
                "required": True,
            },
        )

    @dataclass
    class E2:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "http://xsdtesting",
                "required": True,
            },
        )


@dataclass
class Doc(Testing):
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"
