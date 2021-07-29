from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/typeDef"


@dataclass
class AnyTypeElement:
    class Meta:
        namespace = "ElemDecl/typeDef"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class DefaultTypeElement:
    class Meta:
        namespace = "ElemDecl/typeDef"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/typeDef"

    any_type_element: Optional[AnyTypeElement] = field(
        default=None,
        metadata={
            "name": "AnyTypeElement",
            "type": "Element",
        }
    )
    default_type_element: Optional[DefaultTypeElement] = field(
        default=None,
        metadata={
            "name": "DefaultTypeElement",
            "type": "Element",
        }
    )
