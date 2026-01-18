from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "particles"


@dataclass(kw_only=True)
class A:
    class Meta:
        name = "a"
        namespace = "particles"

    date_or_marked_or_num: None | XmlDate | bool | int = field(
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
                    "name": "marked",
                    "type": bool,
                    "namespace": "",
                },
                {
                    "name": "num",
                    "type": int,
                    "namespace": "",
                },
            ),
        },
    )
