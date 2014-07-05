# import endpoints
from protorpc import messages
# from protorpc import message_types


# PROFILE_FORM_RESOURCE = endpoints.ResourceContainer(
#         message_types.VoidMessage,
#         display_name=messages.StringField(1),
#         teeshirt_size=messages.StringField(2)
# )


class ProfileForm(messages.Message):
    "Represents a profile form on the client side."
    displayName = messages.StringField(1)
    teeShirtSize = messages.StringField(2)

    # TeeShirtSize = [
    #     'NOT_SPECIFIED',
    #     'XS',
    #     'S',
    #     'M',
    #     'L',
    #     'XL',
    #     'XXL',
    #     'XXXL'
    # ]

    # def __init__(self, display_name, teeshirt_size):
    #     self.display_name = display_name
    #     self.teeshirt_size = teeshirt_size
