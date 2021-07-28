from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "ST_facets"


@dataclass
class Test:
    class Meta:
        name = "test"
        namespace = "ST_facets"

    value: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": XmlPeriod("2002-02"),
        }
    )
