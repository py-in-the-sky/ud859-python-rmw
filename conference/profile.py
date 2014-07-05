from protorpc import messages


class Profile(messages.Message):
    "Represents a user profile."
    userId = messages.StringField(1)
    displayName = messages.StringField(2)
    mainEmail = messages.StringField(3)
    teeShirtSize = messages.StringField(4)

    # def __init__(self, user_id, display_name, main_email, tee_shirt_size):
    #     self.user_id = user_id
    #     self.display_name = display_name
    #     self.main_email = main_email
    #     self.tee_shirt_size = tee_shirt_size
