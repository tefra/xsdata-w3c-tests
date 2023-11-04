from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional, Type, Union

__NAMESPACE__ = "foo"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "foo"

    key_or_ref: List[Union[Decimal, "Root.Key"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "key",
                    "type": Type["Root.Key"],
                },
                {
                    "name": "ref",
                    "type": Decimal,
                },
            ),
        }
    )

    @dataclass
    class Key:
        id: Optional[Decimal] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )
