from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://importedXSD"


@dataclass
class B:
    """
    :ivar any_element:
    :ivar e2:
    """
    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )
    e2: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=5
        )
    )


@dataclass
class ImpElem1(B):
    class Meta:
        name = "impElem1"
        namespace = "http://importedXSD"
