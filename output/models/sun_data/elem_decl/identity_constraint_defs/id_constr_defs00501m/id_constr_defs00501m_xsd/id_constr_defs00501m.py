from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "ElemDecl/identityConstraintDefs"


@dataclass
class Root:
    """
    :ivar person:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/identityConstraintDefs"

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
        :ivar ssn:
        """
        value: Optional[str] = field(
            default=None,
        )
        ssn: Optional[str] = field(
            default=None,
            metadata=dict(
                type="Attribute",
                required=True
            )
        )
