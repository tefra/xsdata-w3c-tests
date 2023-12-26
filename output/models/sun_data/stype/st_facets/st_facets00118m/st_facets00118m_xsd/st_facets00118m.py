from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "ST_facets"


@dataclass
class Test:
    class Meta:
        name = "test"
        namespace = "ST_facets"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": XmlDate(2002, 2, 28),
        },
    )
