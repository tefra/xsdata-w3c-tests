from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import Period


@dataclass
class Root:
    class Meta:
        name = "root"

    value: List[Period] = field(
        init=False,
        default_factory=lambda: [Period("2004"), Period("---04"), Period("--05")],
        metadata={
            "tokens": True,
        }
    )
