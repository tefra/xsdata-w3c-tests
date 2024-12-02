from dataclasses import dataclass, field
from typing import List, Union

from xsdata.models.datatype import XmlPeriod


@dataclass
class Root:
    class Meta:
        name = "root"

    value: List[Union[XmlPeriod, int]] = field(
        init=False,
        default_factory=lambda: [
            1,
            2,
            3,
            4,
            20,
            100,
        ],
        metadata={
            "tokens": True,
        },
    )
