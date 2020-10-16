from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "ElemDecl/identityConstraintDefs"


@dataclass
class Root:
    """
    :ivar sernum:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/identityConstraintDefs"

    sernum: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 2,
        }
    )
