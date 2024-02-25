from dataclasses import dataclass, field
from typing import List, Optional, Type, Union, Any

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Base:
    class Meta:
        name = "base"

    e1_or_e2_or_e3: List[Union["Base.E1", "Base.E2", "Base.E3"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "e1",
                    "type": Type["Base.E1"],
                    "namespace": "http://xsdtesting",
                },
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
            ),
            "max_occurs": 2,
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
class Doc(Base):
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    e2_or_e3: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    e1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
