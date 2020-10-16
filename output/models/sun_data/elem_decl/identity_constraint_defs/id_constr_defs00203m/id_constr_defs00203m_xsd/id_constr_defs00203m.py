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
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Person:
        """
        :ivar value:
        :ivar birthday:
        """
        value: Optional[str] = field(
            default=None,
        )
        birthday: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )
