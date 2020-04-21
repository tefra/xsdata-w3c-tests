from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "IdConstrDefs/name"


@dataclass
class Name:
    """
    :ivar name:
    """
    class Meta:
        name = "name"
        namespace = "IdConstrDefs/name"

    name: List["Name.Name"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )

    @dataclass
    class Name:
        """
        :ivar value:
        :ivar name:
        """
        value: Optional[str] = field(
            default=None,
        )
        name: Optional[str] = field(
            default=None,
            metadata=dict(
                type="Attribute"
            )
        )
