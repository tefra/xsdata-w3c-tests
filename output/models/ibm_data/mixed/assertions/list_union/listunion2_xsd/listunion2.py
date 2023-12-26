from dataclasses import dataclass, field
from typing import Optional, Union
from xsdata.models.datatype import XmlDate


@dataclass
class Example:
    value: Optional[Union[int, XmlDate]] = field(default=None)
