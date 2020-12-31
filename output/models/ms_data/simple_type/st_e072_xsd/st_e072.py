from dataclasses import dataclass, field
from typing import Optional, Union
from xsdata.models.datatype import Period


@dataclass
class Doc:
    class Meta:
        name = "doc"

    root: Optional[Union[Period, str, int]] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    value: Optional[Union[Period, str, int]] = field(
        default=None,
    )
