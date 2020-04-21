from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Phonebill:
    """
    :ivar plan:
    :ivar rent:
    :ivar cust_id:
    """
    class Meta:
        name = "phonebill"

    plan: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    rent: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    cust_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="custId",
            type="Attribute"
        )
    )
