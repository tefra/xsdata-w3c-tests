from decimal import Decimal
from output.models.saxon_data.id.id040_xsd.id040 import Chap
from output.models.saxon_data.id.id040_xsd.id040 import Doc


obj = Doc(
    chap_or_appx=[
        Doc.Chap(
            section=[
                Chap.Section(
                    nr=Decimal('1')
                ),
                Chap.Section(
                    nr=Decimal('2')
                ),
                Chap.Section(
                    nr=Decimal('3')
                ),
                Chap.Section(
                    nr=Decimal('4')
                ),
            ]
        ),
        Doc.Appx(
            section=[
                Chap.Section(
                    nr=Decimal('1')
                ),
                Chap.Section(
                    nr=Decimal('2')
                ),
                Chap.Section(
                    nr=Decimal('3')
                ),
                Chap.Section(
                    nr=Decimal('4')
                ),
            ]
        ),
    ]
)
