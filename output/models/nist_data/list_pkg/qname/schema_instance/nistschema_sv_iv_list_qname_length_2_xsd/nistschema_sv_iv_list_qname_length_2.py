from dataclasses import dataclass, field
from lxml.etree import QName
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-QName-length-2-NS"


@dataclass
class NistschemaSvIvListQnameLength2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-QName-length-2"
        namespace = "NISTSchema-SV-IV-list-QName-length-2-NS"

    value: List[QName] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            length=6
        )
    )
