from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod


@dataclass
class Root:
    class Meta:
        name = "root"

    value: list[XmlPeriod] = field(
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
