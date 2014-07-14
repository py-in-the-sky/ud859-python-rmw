# for google users api, see:
# https://developers.google.com/appengine/docs/python/users/


from endpoints import get_current_user
from protorpc import remote
from constants import *
from profile import Profile


package = 'conference'


def _extractDefaultDisplayNameFromEmail(email):
    """Get the display name from the user's email. For example, if the
    email is lemoncake@example.com, then the display name becomes
    "lemoncake."
    """
    return None if email is None else email[:email.index('@')]


@endpoints.api(name='conference', version='v1',
               allowed_client_ids=[WEB_CLIENT_ID, ANDROID_CLIENT_ID,
                                   IOS_CLIENT_ID, API_EXPLORER_CLIENT_ID],
               audiences=[ANDROID_AUDIENCE],
               scopes=[EMAIL_SCOPE],
               description='API for Conference Central backend app.')
class ConferenceApi(remote.Service):
    "Defines full Conference Central API."

    # @endpoints.method(ProfileForm, Profile, name='saveProfile', path='profile')
    @Profile.method(name='saveProfile', path='profile', user_required=True,
                    request_fields=('displayName', 'teeShirtSize'))
    def save_profile(self, profile):
        # above we have user_required=True, so we know user is authorized if
        # we're in the body of this method; otherwise, endpoints_proto_datastore
        # will have thrown a 401 error
        user = get_current_user()

        # if user is None:
        #     raise UnauthorizedException("Authorization required.")

        # see whether profile already exists and then update or insert new one
        query = Profile.query(Profile.userId == user.user_id()).get()
        if query:
            query.update(profile.displayName, profile.teeShirtSize)
            profile = query

        else:
            profile.userId = user.user_id()
            profile.mainEmail = user.email()
            profile.displayName = (profile.displayName or
                             _extractDefaultDisplayNameFromEmail(user.email()))
            profile.teeShirtSize = profile.teeShirtSize or 'NOT_SPECIFIED'

        profile.put()  # save to database

        return profile

        # user_id = user.user_id()
        # main_email = user.email()
        # display_name = (request.displayName or
        #                 _extractDefaultDisplayNameFromEmail(main_email))
        # teeshirt_size = request.teeShirtSize or 'NOT_SPECIFIED'
        #
        # return Profile(userId=user_id, displayName=display_name,
        #                mainEmail=main_email, teeShirtSize=teeshirt_size)

    @Profile.query_method(name='getProfile', path='profile',
                          user_required=True)
    def get_profile(self, query=None):
        # above we have user_required=True, so we know user is authorized if
        # we're in the body of this method; otherwise, endpoints_proto_datastore
        # will have thrown a 401 error
        user = get_current_user()
        return Profile.query(Profile.userId == user.user_id())


app = endpoints.api_server([ConferenceApi])
