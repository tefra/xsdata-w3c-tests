from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    A00 = "a00ପ"
    A0 = "a0-ଭ"
    A0_A = "a0Aର"
    A10 = "a10ଲ"
    A1 = "a1-ଲ"
    A1_A = "a1Aଳ"
    A20 = "a20ଶ"
    A2 = "a2-ଷ"
    A2_A = "a2Aହ"
    A30 = "a30ଽ"
    A40 = "a40ଡ଼"
    A4 = "a4-ଡ଼"
    A4_A = "a4Aଢ଼"
    A50 = "a50ୟ"
    A5 = "a5-ୠ"
    A5_A = "a5Aୡ"
    A60 = "a60அ"
    A6 = "a6-இ"
    A6_A = "a6Aஊ"
    A70 = "a70எ"
    A7 = "a7-ஏ"
    A7_A = "a7Aஐ"
    A80 = "a80ஒ"
    A8 = "a8-ஓ"
    A8_A = "a8Aக"
    A90 = "a90ங"
    A9 = "a9-ங"
    A9_A = "a9Aச"


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
