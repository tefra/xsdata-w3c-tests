from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/typeDef"


@dataclass
class AnyTypeElement:
    """
    :ivar any_element:
    """
    class Meta:
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
class DefaultTypeElement:
    """
    :ivar any_element:
    """
    class Meta:
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
    :ivar any_type_element:
    :ivar default_type_element:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/typeDef"

    any_type_element: Optional[AnyTypeElement] = field(
        default=None,
        metadata={
            "name": "AnyTypeElement",
            "type": "Element",
            "required": True,
        }
    )
    default_type_element: Optional[DefaultTypeElement] = field(
        default=None,
        metadata={
            "name": "DefaultTypeElement",
            "type": "Element",
            "required": True,
        }
    )
