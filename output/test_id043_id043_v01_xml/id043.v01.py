from decimal import Decimal
from output.models.saxon_data.id.id043_xsd.id043 import Chap
from output.models.saxon_data.id.id043_xsd.id043 import Doc


obj = Doc(
    chap_or_appx=[
        Doc.Chap(
            section=[
                Chap.Section(
                    value='',
                    nr=Decimal('1')
                ),
                Chap.Section(
                    value='',
                    nr=Decimal('2')
                ),
                Chap.Section(
                    value='',
                    nr=Decimal('3')
                ),
                Chap.Section(
                    value='',
                    nr=Decimal('4')
                ),
            ]
        ),
        Doc.Appx(
            section=[
                Chap.Section(
                    value='',
                    nr=Decimal('1')
                ),
                Chap.Section(
                    value='',
                    nr=Decimal('2')
                ),
                Chap.Section(
                    value='',
                    nr=Decimal('3')
                ),
                Chap.Section(
                    value='',
                    nr=Decimal('4')
                ),
            ]
        ),
    ]
)
