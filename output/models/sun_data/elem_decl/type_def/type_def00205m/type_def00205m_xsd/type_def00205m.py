from dataclasses import dataclass, field
from typing import Optional, Union

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

    any_type_element_or_default_type_element: Optional[Union[AnyTypeElement, DefaultTypeElement]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AnyTypeElement",
                    "type": AnyTypeElement,
                },
                {
                    "name": "DefaultTypeElement",
                    "type": DefaultTypeElement,
                },
            ),
        }
    )
