from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-ID-length-4-NS"


@dataclass
class NistschemaSvIvListIdLength4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-ID-length-4"
        namespace = "NISTSchema-SV-IV-list-ID-length-4-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            length=8,
            tokens=True
        )
    )


@dataclass
class Out:
    """
    :ivar any_element:
    """
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-list-ID-length-4-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )
