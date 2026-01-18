from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlTime

__NAMESPACE__ = "compositor"


@dataclass(kw_only=True)
class A:
    class Meta:
        name = "a"
        namespace = "compositor"

    date_or_time: None | XmlDate | XmlTime = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "date",
                    "type": XmlDate,
                    "namespace": "",
                },
                {
                    "name": "time",
                    "type": XmlTime,
                    "namespace": "",
                },
            ),
        },
    )
