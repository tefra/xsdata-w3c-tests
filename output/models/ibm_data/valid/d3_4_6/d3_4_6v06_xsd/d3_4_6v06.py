from dataclasses import dataclass, field
from typing import List, Optional, Type, Union

__NAMESPACE__ = "a"


@dataclass
class Nametest:
    choice: List[
        Union[
            "Nametest.Ele",
            "Nametest.TypeType",
            "Nametest.Type1",
            "Nametest.Type9",
            "Nametest.Type2",
            "Nametest.AA",
            "Nametest.AA1",
            "Nametest.Ele1",
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "_ele",
                    "type": Type["Nametest.Ele"],
                    "namespace": "a",
                },
                {
                    "name": "_-",
                    "type": Type["Nametest.TypeType"],
                    "namespace": "a",
                },
                {
                    "name": "_.",
                    "type": Type["Nametest.Type1"],
                    "namespace": "a",
                },
                {
                    "name": "_9",
                    "type": Type["Nametest.Type9"],
                    "namespace": "a",
                },
                {
                    "name": "___",
                    "type": Type["Nametest.Type2"],
                    "namespace": "a",
                },
                {
                    "name": "a_a",
                    "type": Type["Nametest.AA"],
                    "namespace": "a",
                },
                {
                    "name": "a.a",
                    "type": Type["Nametest.AA1"],
                    "namespace": "a",
                },
                {
                    "name": "ele",
                    "type": Type["Nametest.Ele1"],
                    "namespace": "a",
                },
            ),
        },
    )

    @dataclass
    class Ele:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class TypeType:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class Type1:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class Type9:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class Type2:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class AA:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class AA1:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class Ele1:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )


@dataclass
class Root(Nametest):
    class Meta:
        name = "root"
        namespace = "a"
