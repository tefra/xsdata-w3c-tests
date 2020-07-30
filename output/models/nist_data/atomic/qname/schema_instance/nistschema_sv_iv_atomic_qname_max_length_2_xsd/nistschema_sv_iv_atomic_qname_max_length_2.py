from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-maxLength-2-NS"


@dataclass
class NistschemaSvIvAtomicQnameMaxLength2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-maxLength-2"
        namespace = "NISTSchema-SV-IV-atomic-QName-maxLength-2-NS"

    value: Optional[QName] = field(
        default=None,
        metadata=dict(
            required=True,
            max_length=4
        )
    )
