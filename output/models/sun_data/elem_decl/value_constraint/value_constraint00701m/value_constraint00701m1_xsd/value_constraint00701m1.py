from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "ElemDecl/valueConstraint"


@dataclass
class Root:
    """
    :ivar content:
    :ivar separator:
    :ivar attr:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/valueConstraint"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    separator: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    attr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
