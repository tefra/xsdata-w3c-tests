from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "ElemDecl/identityConstraintDefs"


@dataclass
class Root:
    """
    :ivar element:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/identityConstraintDefs"

    element: List["Root.Element"] = field(
        default_factory=list,
        metadata={
            "name": "Element",
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class Element:
        """
        :ivar id:
        :ivar idref:
        :ivar idrefs:
        """
        id: Optional[str] = field(
            default=None,
            metadata={
                "name": "ID",
                "type": "Attribute",
            }
        )
        idref: Optional[str] = field(
            default=None,
            metadata={
                "name": "IDREF",
                "type": "Attribute",
            }
        )
        idrefs: List[str] = field(
            default_factory=list,
            metadata={
                "name": "IDREFS",
                "type": "Attribute",
                "tokens": True,
            }
        )
