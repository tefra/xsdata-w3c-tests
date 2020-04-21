from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-length-4-NS"


@dataclass
class NistschemaSvIvAtomicQnameLength4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-length-4"
        namespace = "NISTSchema-SV-IV-atomic-QName-length-4-NS"

    value: Optional[QName] = field(
        default=None,
        metadata=dict(
            required=True,
            length=34
        )
    )
