from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/substGroupAffilation"


@dataclass(kw_only=True)
class Element:
    class Meta:
        namespace = "ElemDecl/substGroupAffilation"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class SuperElement:
    class Meta:
        namespace = "ElemDecl/substGroupAffilation"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class SuperSuperElement:
    class Meta:
        namespace = "ElemDecl/substGroupAffilation"

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
        namespace = "ElemDecl/substGroupAffilation"

    super_element_or_super_super_element: list[
        SuperElement | SuperSuperElement
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SuperElement",
                    "type": SuperElement,
                },
                {
                    "name": "SuperSuperElement",
                    "type": SuperSuperElement,
                },
            ),
        },
    )
    separator: None | object = field(
        default=None,
        metadata={
            "name": "Separator",
            "type": "Element",
        },
    )
    element: list[Element] = field(
        default_factory=list,
        metadata={
            "name": "Element",
            "type": "Element",
        },
    )
