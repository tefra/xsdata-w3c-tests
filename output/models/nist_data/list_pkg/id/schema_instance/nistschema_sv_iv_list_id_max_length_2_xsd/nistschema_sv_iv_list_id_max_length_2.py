from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-ID-maxLength-2-NS"


@dataclass
class NistschemaSvIvListIdMaxLength2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-ID-maxLength-2"
        namespace = "NISTSchema-SV-IV-list-ID-maxLength-2-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            max_length=6,
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
        namespace = "NISTSchema-SV-IV-list-ID-maxLength-2-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )
