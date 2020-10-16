from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/typeDef"


@dataclass
class Inline:
    """
    :ivar any_element:
    """
    class Meta:
        name = "inline"
        namespace = "ElemDecl/typeDef"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class Root:
    """
    :ivar value:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/typeDef"

    value: Optional[object] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
