from dataclasses import dataclass, field
from decimal import Decimal
from typing import List

__NAMESPACE__ = "foo"


@dataclass
class Root:
    """
    :ivar key_or_ref:
    """
    class Meta:
        name = "root"
        namespace = "foo"

    key_or_ref: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "key",
                    "type": Decimal,
                },
                {
                    "name": "ref",
                    "type": Decimal,
                },
            ),
        }
    )
