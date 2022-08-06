from decimal import Decimal
from output.models.saxon_data.id.id040_xsd.id040 import Chap
from output.models.saxon_data.id.id040_xsd.id040 import Doc
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Doc(
    chap_or_appx=[
        Chap(
            section=[
                Chap.Section(
                    value="",
                    nr=Decimal("1")
                ),
                Chap.Section(
                    value="",
                    nr=Decimal("2")
                ),
                Chap.Section(
                    value="",
                    nr=Decimal("3")
                ),
                Chap.Section(
                    value="",
                    nr=Decimal("4")
                ),
            ]
        ),
        DerivedElement(
            qname="{http://id040.ly/}appx",
            value=Chap(
                section=[
                    Chap.Section(
                        value="",
                        nr=Decimal("1")
                    ),
                    Chap.Section(
                        value="",
                        nr=Decimal("2")
                    ),
                    Chap.Section(
                        value="",
                        nr=Decimal("3")
                    ),
                    Chap.Section(
                        value="",
                        nr=Decimal("4")
                    ),
                ]
            ),
            type=None
        ),
    ]
)
