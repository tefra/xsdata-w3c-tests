from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "ElemDecl/identityConstraintDefs"


@dataclass
class Root:
    """
    :ivar element:
    :ivar element_ref:
    :ivar element_refs:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/identityConstraintDefs"

    element: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Element",
            "type": "Element",
            "namespace": "",
        }
    )
    element_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ElementRef",
            "type": "Element",
            "namespace": "",
        }
    )
    element_refs: List[List[str]] = field(
        default_factory=list,
        metadata={
            "name": "ElementRefs",
            "type": "Element",
            "namespace": "",
            "tokens": True,
        }
    )
