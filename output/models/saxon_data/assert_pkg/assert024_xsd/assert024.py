from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName


@dataclass(kw_only=True)
class Test:
    rule: list[Test.Rule] = field(
        default_factory=list,
        metadata={
            "name": "Rule",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class Rule:
        name: QName = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
