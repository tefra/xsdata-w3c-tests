from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    A00 = "a00એ"
    A0 = "a0-ઐ"
    A0_A = "a0Aઑ"
    A10 = "a10ઓ"
    A1 = "a1-ઝ"
    A1_A = "a1Aન"
    A20 = "a20પ"
    A2 = "a2-ભ"
    A2_A = "a2Aર"
    A30 = "a30લ"
    A3 = "a3-લ"
    A3_A = "a3Aળ"
    A40 = "a40વ"
    A4 = "a4-ષ"
    A4_A = "a4Aહ"
    A50 = "a50ઽ"
    A60 = "a60ૠ"
    A70 = "a70ଅ"
    A7 = "a7-ଈ"
    A7_A = "a7Aଌ"
    A80 = "a80ଏ"
    A8 = "a8-ଏ"
    A8_A = "a8Aଐ"
    A90 = "a90ଓ"
    A9 = "a9-ଝ"
    A9_A = "a9Aନ"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "SType/ST_facets"

    value: list[S] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
