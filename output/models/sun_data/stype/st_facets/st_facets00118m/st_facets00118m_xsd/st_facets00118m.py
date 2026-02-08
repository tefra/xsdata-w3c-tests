from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "ST_facets"


@dataclass(kw_only=True)
class Test:
    class Meta:
        name = "test"
        namespace = "ST_facets"

    value: XmlDate = field(
        metadata={
            "max_inclusive": XmlDate(2002, 2, 28),
        }
    )
