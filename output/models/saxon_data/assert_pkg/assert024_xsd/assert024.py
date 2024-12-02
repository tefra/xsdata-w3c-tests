from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName


@dataclass
class Test:
    rule: list["Test.Rule"] = field(
        default_factory=list,
        metadata={
            "name": "Rule",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )

    @dataclass
    class Rule:
        name: Optional[QName] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )
