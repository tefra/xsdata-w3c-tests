from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "ST_facets"


@dataclass(kw_only=True)
class Test:
    class Meta:
        name = "test"
        namespace = "ST_facets"

    value: XmlPeriod = field(
        metadata={
            "max_inclusive": XmlPeriod("--02"),
        }
    )
