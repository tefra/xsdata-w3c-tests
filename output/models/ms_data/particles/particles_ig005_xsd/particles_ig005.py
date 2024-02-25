from dataclasses import dataclass, field
from typing import Optional, Type, Union

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Base:
    class Meta:
        name = "base"

    e2_or_e3_or_e4: Optional[Union["Base.E2", "Base.E3", "Base.E4"]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "e2",
                    "type": Type["Base.E2"],
                    "namespace": "http://xsdtesting",
                },
                {
                    "name": "e3",
                    "type": Type["Base.E3"],
                    "namespace": "http://xsdtesting",
                },
                {
                    "name": "e4",
                    "type": Type["Base.E4"],
                    "namespace": "http://xsdtesting",
                },
            ),
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
    class E3:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "http://xsdtesting",
                "required": True,
            },
        )

    @dataclass
    class E4:
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


@dataclass
class Doc(Testing):
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"
