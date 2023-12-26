from dataclasses import dataclass, field
from typing import List, Union
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "particles"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "particles"

    date_or_marked_or_num: List[Union[XmlDate, bool, int]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "date",
                    "type": XmlDate,
                    "namespace": "",
                },
                {
                    "name": "marked",
                    "type": bool,
                    "namespace": "",
                },
                {
                    "name": "num",
                    "type": int,
                    "namespace": "",
                },
            ),
            "max_occurs": 2,
        },
    )
