from dataclasses import dataclass, field
from typing import List, Optional
from xml.etree.ElementTree import QName


@dataclass
class Test:
    """
    :ivar rule:
    """
    rule: List["Test.Rule"] = field(
        default_factory=list,
        metadata={
            "name": "Rule",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Rule:
        """
        :ivar name:
        """
        name: Optional[QName] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
