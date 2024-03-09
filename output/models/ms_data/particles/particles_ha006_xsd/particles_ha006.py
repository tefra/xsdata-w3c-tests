from dataclasses import dataclass, field
from typing import Any, Optional, Type, Union

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Base:
    class Meta:
        name = "base"

    e2_or_e3: Optional[Union["Base.E2", "Base.E3"]] = field(
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
class Doc(Base):
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    e2: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
