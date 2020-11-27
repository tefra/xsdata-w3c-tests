from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Phonebill:
    class Meta:
        name = "phonebill"

    plan: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    rent: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    cust_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "custId",
            "type": "Attribute",
        }
    )
