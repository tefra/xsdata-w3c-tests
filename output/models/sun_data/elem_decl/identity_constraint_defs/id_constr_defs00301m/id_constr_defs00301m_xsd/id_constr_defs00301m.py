from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "ElemDecl/identityConstraintDefs"


@dataclass
class Root:
    """
    :ivar element_or_element_ref_or_element_refs:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/identityConstraintDefs"

    element_or_element_ref_or_element_refs: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Element",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "ElementRef",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "ElementRefs",
                    "type": List[str],
                    "namespace": "",
                    "tokens": True,
                },
            ),
        }
    )
