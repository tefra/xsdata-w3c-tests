from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Phonebill:
    class Meta:
        name = "phonebill"

    plan: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    rent: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    cust_id: None | str = field(
        default=None,
        metadata={
            "name": "custId",
            "type": "Attribute",
        },
    )
