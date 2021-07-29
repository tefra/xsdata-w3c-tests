from dataclasses import dataclass, field
from typing import List, Optional

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

    super_element: List[SuperElement] = field(
        default_factory=list,
        metadata={
            "name": "SuperElement",
            "type": "Element",
        }
    )
    super_super_element: List[SuperSuperElement] = field(
        default_factory=list,
        metadata={
            "name": "SuperSuperElement",
            "type": "Element",
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
