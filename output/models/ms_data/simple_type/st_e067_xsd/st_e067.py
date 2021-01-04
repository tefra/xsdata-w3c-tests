from dataclasses import dataclass, field
from decimal import Decimal
from typing import Union
from xsdata.models.datatype import Period


@dataclass
class Root:
    class Meta:
        name = "root"

    value: Union[Period, str, Decimal] = field(
        init=False,
        default="name",
    )
