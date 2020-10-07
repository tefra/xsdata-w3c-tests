from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional, Union


@dataclass
class Example:
    """
    :ivar x:
    """
    x: List[Union["Example.KindQuantity", "Example.KindPrice", "Example.KindMesg"]] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )

    @dataclass
    class KindQuantity:
        """
        :ivar value:
        :ivar kind:
        """
        value: Optional[int] = field(
            default=None,
        )
        kind: Optional[str] = field(
            default=None,
            metadata=dict(
                type="Attribute",
                required=True
            )
        )

    @dataclass
    class KindPrice:
        """
        :ivar value:
        :ivar kind:
        """
        value: Optional[Decimal] = field(
            default=None,
        )
        kind: Optional[str] = field(
            default=None,
            metadata=dict(
                type="Attribute",
                required=True
            )
        )

    @dataclass
    class KindMesg:
        """
        :ivar value:
        :ivar kind:
        """
        value: Optional[str] = field(
            default=None,
        )
        kind: Optional[str] = field(
            default=None,
            metadata=dict(
                type="Attribute",
                required=True
            )
        )
