from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/typeDef"


@dataclass(kw_only=True)
class AnyTypeElement:
    class Meta:
        namespace = "ElemDecl/typeDef"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class DefaultTypeElement:
    class Meta:
        namespace = "ElemDecl/typeDef"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/typeDef"

    any_type_element_or_default_type_element: (
        None | AnyTypeElement | DefaultTypeElement
    ) = field(
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
        },
    )
