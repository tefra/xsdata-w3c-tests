from dataclasses import dataclass, field
from typing import Union

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_27_v03"


@dataclass
class Root:
    """
    :ivar ely_mdunion_a:
    :ivar ely_mdunion_b:
    :ivar ely_mdunion_c: Tests the simpleType dayTimeDuration used in a
        unions
    """

    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_27_v03"

    ely_mdunion_a: list[Union[XmlDuration, str]] = field(
        default_factory=list,
        metadata={
            "name": "elyMDUnionA",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    ely_mdunion_b: list[Union[XmlDuration, int]] = field(
        default_factory=list,
        metadata={
            "name": "elyMDUnionB",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    ely_mdunion_c: list[Union[XmlDuration, str, int]] = field(
        default_factory=list,
        metadata={
            "name": "elyMDUnionC",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
