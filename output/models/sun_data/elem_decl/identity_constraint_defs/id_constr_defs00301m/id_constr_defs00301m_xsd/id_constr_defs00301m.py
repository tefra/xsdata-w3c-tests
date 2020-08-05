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
        metadata=dict(
            name="Element",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    element_ref: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="ElementRef",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    element_refs: List[List[str]] = field(
        default_factory=list,
        metadata=dict(
            name="ElementRefs",
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            tokens=True
        )
    )
