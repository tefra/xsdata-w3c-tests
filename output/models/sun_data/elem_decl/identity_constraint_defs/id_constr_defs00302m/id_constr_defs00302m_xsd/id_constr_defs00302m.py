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
        metadata=dict(
            name="Element",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
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
            metadata=dict(
                name="ID",
                type="Attribute"
            )
        )
        idref: Optional[str] = field(
            default=None,
            metadata=dict(
                name="IDREF",
                type="Attribute"
            )
        )
        idrefs: List[str] = field(
            default_factory=list,
            metadata=dict(
                name="IDREFS",
                type="Attribute",
                tokens=True
            )
        )
