from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-ID-length-3-NS"


@dataclass
class NistschemaSvIvListIdLength3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-ID-length-3"
        namespace = "NISTSchema-SV-IV-list-ID-length-3-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "length": 7,
            "tokens": True,
        }
    )


@dataclass
class Out:
    """
    :ivar any_element:
    """
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-list-ID-length-3-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
