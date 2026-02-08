from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    test: Doc.Test = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass(kw_only=True)
    class Test:
        att_fix: int = field(
            init=False,
            default=37,
            metadata={
                "name": "attFix",
                "type": "Attribute",
            },
        )
        foo: None | object = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
