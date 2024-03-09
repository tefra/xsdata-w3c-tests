from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "targetNS1"


@dataclass
class A1:
    class Meta:
        name = "A"

    c_or_date: Optional[Union[int, XmlDate]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "c",
                    "type": int,
                    "namespace": "",
                },
                {
                    "name": "date",
                    "type": XmlDate,
                    "namespace": "",
                },
            ),
        },
    )


@dataclass
class A(A1):
    class Meta:
        name = "a"
        namespace = "targetNS1"
