from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://example.com/over019"


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://example.com/over019"

    value: XmlDate = field(
        metadata={
            "required": True,
        }
    )
