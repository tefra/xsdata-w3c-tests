from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "targetNS1"


@dataclass(kw_only=True)
class A1:
    class Meta:
        name = "A"

    c_or_date: None | int | XmlDate = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "c",
                    "type": int,
                    "namespace": "",
                },
                {
                    "name": "date",
                    "type": XmlDate,
                    "namespace": "",
                },
            ),
        },
    )


@dataclass(kw_only=True)
class A(A1):
    class Meta:
        name = "a"
        namespace = "targetNS1"
