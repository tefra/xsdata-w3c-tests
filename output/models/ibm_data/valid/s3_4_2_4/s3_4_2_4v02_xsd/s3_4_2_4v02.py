from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://xstest-tns/schema11_S3_4_2_4"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_S3_4_2_4"

    e1: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
