from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://foo.com"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "http://foo.com"

    child: list[Root.Child] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 3,
            "max_occurs": 7,
        },
    )

    @dataclass(kw_only=True)
    class Child:
        value: str = field(
            default="",
            metadata={
                "required": True,
                "min_length": 3,
                "max_length": 10,
            },
        )
        attr: None | str = field(
            default=None,
            metadata={
                "type": "Attribute",
                "min_length": 5,
                "max_length": 10,
            },
        )
