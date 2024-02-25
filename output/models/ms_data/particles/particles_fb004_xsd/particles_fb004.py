from dataclasses import dataclass, field
from typing import Optional, Type, Union

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Base:
    class Meta:
        name = "base"

    g1_or_g2: Optional[Union["Base.G1", "Base.G2"]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "g1",
                    "type": Type["Base.G1"],
                    "namespace": "http://xsdtesting",
                },
                {
                    "name": "g2",
                    "type": Type["Base.G2"],
                    "namespace": "http://xsdtesting",
                },
            ),
        },
    )

    @dataclass
    class G1:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "http://xsdtesting",
                "required": True,
            },
        )

    @dataclass
    class G2:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "http://xsdtesting",
                "required": True,
            },
        )


@dataclass
class Foo:
    class Meta:
        name = "foo"
        namespace = "http://xsdtesting"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Doc(Base):
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    s1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    s2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
