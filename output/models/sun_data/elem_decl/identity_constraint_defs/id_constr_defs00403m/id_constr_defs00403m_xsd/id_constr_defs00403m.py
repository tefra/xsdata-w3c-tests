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
        :ivar ssn:
        :ivar parents:
        """
        value: Optional[str] = field(
            default=None,
        )
        ssn: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        parents: List[str] = field(
            default_factory=list,
            metadata={
                "type": "Attribute",
                "tokens": True,
            }
        )
