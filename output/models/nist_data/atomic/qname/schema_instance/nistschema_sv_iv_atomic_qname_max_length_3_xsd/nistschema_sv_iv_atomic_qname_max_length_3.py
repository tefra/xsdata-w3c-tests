from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-maxLength-3-NS"


@dataclass
class NistschemaSvIvAtomicQnameMaxLength3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-maxLength-3"
        namespace = "NISTSchema-SV-IV-atomic-QName-maxLength-3-NS"

    value: Optional[QName] = field(
        default=None,
        metadata=dict(
            required=True,
            max_length=57.0
        )
    )