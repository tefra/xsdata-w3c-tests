from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Doc:
    class Meta:
        name = "doc"

    test: Optional["Doc.Test"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )

    @dataclass
    class Test:
        att_fix: int = field(
            init=False,
            default=37,
            metadata={
                "name": "attFix",
                "type": "Attribute",
            },
        )
        foo: Optional[object] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
