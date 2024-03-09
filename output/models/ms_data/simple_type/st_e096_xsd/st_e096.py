from dataclasses import dataclass, field
from typing import List

from xsdata.models.datatype import XmlPeriod


@dataclass
class Root:
    class Meta:
        name = "root"

    value: List[XmlPeriod] = field(
        init=False,
        default_factory=lambda: [
            XmlPeriod("2004"),
            XmlPeriod("---04"),
            XmlPeriod("--05"),
        ],
        metadata={
            "tokens": True,
        },
    )
