from dataclasses import dataclass, field
from typing import Optional, Union
from xsdata.models.datatype import Period


@dataclass
class Root:
    class Meta:
        name = "root"

    value: Optional[Union[Period, str]] = field(
        default=None,
    )
