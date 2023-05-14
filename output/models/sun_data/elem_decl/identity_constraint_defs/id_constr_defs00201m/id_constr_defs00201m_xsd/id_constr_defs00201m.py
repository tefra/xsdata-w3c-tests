from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "ElemDecl/identityConstraintDefs"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/identityConstraintDefs"

    account: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Account",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "sequence": 1,
        }
    )
    name: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "sequence": 1,
        }
    )
    manager: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Manager",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "sequence": 1,
        }
    )
