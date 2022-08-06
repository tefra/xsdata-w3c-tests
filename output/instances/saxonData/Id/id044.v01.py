from decimal import Decimal
from output.models.saxon_data.id.id044_xsd.id044 import Chap
from output.models.saxon_data.id.id044_xsd.id044 import Doc
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Doc(
    chap_or_appx=[
        Chap(
            section=[
                Chap.Section(
                    value="",
                    nr=Decimal("1"),
                    ref=Decimal("4")
                ),
                Chap.Section(
                    value="",
                    nr=Decimal("2"),
                    ref=Decimal("3")
                ),
                Chap.Section(
                    value="",
                    nr=Decimal("3"),
                    ref=Decimal("2")
                ),
                Chap.Section(
                    value="",
                    nr=Decimal("4"),
                    ref=Decimal("1")
                ),
            ]
        ),
        DerivedElement(
            qname="{http://id044.ly/}appx",
            value=Chap(
                section=[
                    Chap.Section(
                        value="",
                        nr=Decimal("1"),
                        ref=Decimal("1")
                    ),
                    Chap.Section(
                        value="",
                        nr=Decimal("2"),
                        ref=Decimal("2")
                    ),
                    Chap.Section(
                        value="",
                        nr=Decimal("3"),
                        ref=Decimal("3")
                    ),
                    Chap.Section(
                        value="",
                        nr=Decimal("4"),
                        ref=Decimal("4")
                    ),
                ]
            ),
            type=None
        ),
    ]
)
