from output.models.saxon_data.simple.simple001_xsd.simple001 import Chap
from output.models.saxon_data.simple.simple001_xsd.simple001 import Doc


obj = Doc(
    chap_or_appx=[
        Doc.Chap(
            section=[
                Chap.Section(
                    value='',
                    nr=1.0
                ),
                Chap.Section(
                    value='',
                    nr=2.0
                ),
                Chap.Section(
                    value=''
                ),
                Chap.Section(
                    value=''
                ),
            ]
        ),
        Doc.Appx(
            section=[
                Chap.Section(
                    value='',
                    nr=1.0
                ),
                Chap.Section(
                    value='',
                    nr=2.0
                ),
                Chap.Section(
                    value=''
                ),
                Chap.Section(
                    value=''
                ),
            ]
        ),
    ]
)
