from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import Period


@dataclass
class Root:
    class Meta:
        name = "root"

    value: List[Period] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
