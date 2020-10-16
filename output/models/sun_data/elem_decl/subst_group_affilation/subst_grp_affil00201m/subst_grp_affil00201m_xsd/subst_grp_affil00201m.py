from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "ElemDecl/substGroupAffilation"


@dataclass
class Element:
    """
    :ivar any_element:
    """
    class Meta:
        namespace = "ElemDecl/substGroupAffilation"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class SuperElement:
    """
    :ivar any_element:
    """
    class Meta:
        namespace = "ElemDecl/substGroupAffilation"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class SuperSuperElement:
    """
    :ivar any_element:
    """
    class Meta:
        namespace = "ElemDecl/substGroupAffilation"

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
    :ivar super_element:
    :ivar super_super_element:
    :ivar separator:
    :ivar element:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/substGroupAffilation"

    super_element: List[SuperElement] = field(
        default_factory=list,
        metadata={
            "name": "SuperElement",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    super_super_element: List[SuperSuperElement] = field(
        default_factory=list,
        metadata={
            "name": "SuperSuperElement",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    separator: Optional[object] = field(
        default=None,
        metadata={
            "name": "Separator",
            "type": "Element",
            "required": True,
        }
    )
    element: List[Element] = field(
        default_factory=list,
        metadata={
            "name": "Element",
            "type": "Element",
            "min_occurs": 1,
        }
    )
