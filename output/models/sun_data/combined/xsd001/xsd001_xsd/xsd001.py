from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://foo.com"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://foo.com"

    child: list["Root.Child"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 3,
            "max_occurs": 7,
        },
    )

    @dataclass
    class Child:
        value: str = field(
            default="",
            metadata={
                "required": True,
                "min_length": 3,
                "max_length": 10,
            },
        )
        attr: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "min_length": 5,
                "max_length": 10,
            },
        )
