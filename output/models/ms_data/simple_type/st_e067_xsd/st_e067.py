from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union
from xsdata.models.datatype import Period


@dataclass
class Root:
    class Meta:
        name = "root"

    value: Optional[Union[Period, str, Decimal]] = field(
        default=None,
    )
