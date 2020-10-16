from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-ID-maxLength-4-NS"


@dataclass
class NistschemaSvIvAtomicIdMaxLength4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-ID-maxLength-4"
        namespace = "NISTSchema-SV-IV-atomic-ID-maxLength-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "max_length": 22,
        }
    )


@dataclass
class Out:
    """
    :ivar any_element:
    """
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-atomic-ID-maxLength-4-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
