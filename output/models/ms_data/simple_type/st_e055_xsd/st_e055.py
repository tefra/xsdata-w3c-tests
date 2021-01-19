from dataclasses import dataclass, field
from typing import Union


@dataclass
class Root:
    class Meta:
        name = "root"

    value: Union[bool, float, str] = field(
        init=False,
        default=1.0,
    )
