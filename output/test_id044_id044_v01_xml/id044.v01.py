from decimal import Decimal
from output.models.saxon_data.id.id044_xsd.id044 import Chap
from output.models.saxon_data.id.id044_xsd.id044 import Doc


obj = Doc(
    chap_or_appx=[
        Doc.Chap(
            section=[
                Chap.Section(
                    nr=Decimal('1'),
                    ref=Decimal('4')
                ),
                Chap.Section(
                    nr=Decimal('2'),
                    ref=Decimal('3')
                ),
                Chap.Section(
                    nr=Decimal('3'),
                    ref=Decimal('2')
                ),
                Chap.Section(
                    nr=Decimal('4'),
                    ref=Decimal('1')
                ),
            ]
        ),
        Doc.Appx(
            section=[
                Chap.Section(
                    nr=Decimal('1'),
                    ref=Decimal('1')
                ),
                Chap.Section(
                    nr=Decimal('2'),
                    ref=Decimal('2')
                ),
                Chap.Section(
                    nr=Decimal('3'),
                    ref=Decimal('3')
                ),
                Chap.Section(
                    nr=Decimal('4'),
                    ref=Decimal('4')
                ),
            ]
        ),
    ]
)
