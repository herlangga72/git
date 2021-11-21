# this used for social auth. this will get the picture profile from social auth. for now it only have google-OAuth2
# but it can handle pretty musch any social auth

def get_avatar(backend, strategy, details, response, user=None, *args, **kwargs):
    url = None
    
    # on googleOAuth2 this give on user scope an avatar link. but it only 96px so in order to make it more usable we need to cut the sizing on photo size by split the =
      
    if backend.name == 'google-oauth2':
        print(response)
        url = response['picture'].split('=')[0]
    if url:
        user.avatar = url
        user.save()