from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-maxLength-5-NS"


@dataclass
class NistschemaSvIvAtomicQnameMaxLength5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-maxLength-5"
        namespace = "NISTSchema-SV-IV-atomic-QName-maxLength-5-NS"

    value: Optional[QName] = field(
        default=None,
        metadata=dict(
            required=True,
            max_length=64.0
        )
    )
