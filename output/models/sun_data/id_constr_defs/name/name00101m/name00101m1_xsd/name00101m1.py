from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "IdConstrDefs/name"


@dataclass
class Root:
    """
    :ivar person:
    """
    class Meta:
        name = "root"
        namespace = "IdConstrDefs/name"

    person: List["Root.Person"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )

    @dataclass
    class Person:
        """
        :ivar value:
        :ivar parent:
        """
        value: Optional[str] = field(
            default=None,
        )
        parent: Optional[str] = field(
            default=None,
            metadata=dict(
                type="Attribute"
            )
        )
