from dataclasses import dataclass, field
from typing import Optional, Type, Union

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Base:
    class Meta:
        name = "base"

    c1_or_c2: Optional[Union["Base.C1", "Base.C2"]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "c1",
                    "type": Type["Base.C1"],
                    "namespace": "http://xsdtesting",
                },
                {
                    "name": "c2",
                    "type": Type["Base.C2"],
                    "namespace": "http://xsdtesting",
                },
            ),
        },
    )

    @dataclass
    class C1:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "http://xsdtesting",
                "required": True,
            },
        )

    @dataclass
    class C2:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "http://xsdtesting",
                "required": True,
            },
        )


@dataclass
class Doc(Base):
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    g1_or_g2: Optional[Union["Doc.G1", "Doc.G2"]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "g1",
                    "type": Type["Doc.G1"],
                },
                {
                    "name": "g2",
                    "type": Type["Doc.G2"],
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
                "required": True,
            },
        )

    @dataclass
    class G2:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "required": True,
            },
        )
