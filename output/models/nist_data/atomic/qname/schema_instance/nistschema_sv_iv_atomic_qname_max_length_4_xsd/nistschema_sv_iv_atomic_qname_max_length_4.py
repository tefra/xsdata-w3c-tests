from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-maxLength-4-NS"


@dataclass
class NistschemaSvIvAtomicQnameMaxLength4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-maxLength-4"
        namespace = "NISTSchema-SV-IV-atomic-QName-maxLength-4-NS"

    value: Optional[QName] = field(
        default=None,
        metadata=dict(
            required=True,
            max_length=61.0
        )
    )