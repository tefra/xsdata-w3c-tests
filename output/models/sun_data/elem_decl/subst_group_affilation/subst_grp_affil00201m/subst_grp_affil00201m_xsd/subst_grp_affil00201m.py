from dataclasses import dataclass, field
from typing import List, Optional, Union

__NAMESPACE__ = "ElemDecl/substGroupAffilation"


@dataclass
class Element:
    class Meta:
        namespace = "ElemDecl/substGroupAffilation"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class SuperElement:
    class Meta:
        namespace = "ElemDecl/substGroupAffilation"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class SuperSuperElement:
    class Meta:
        namespace = "ElemDecl/substGroupAffilation"

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
        namespace = "ElemDecl/substGroupAffilation"

    super_element_or_super_super_element: List[Union[SuperSuperElement, SuperElement]] = field(
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
        }
    )
    separator: Optional[object] = field(
        default=None,
        metadata={
            "name": "Separator",
            "type": "Element",
        }
    )
    element: List[Element] = field(
        default_factory=list,
        metadata={
            "name": "Element",
            "type": "Element",
        }
    )
