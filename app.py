import instaloader

def instagramPostsLoader():
    loader = instaloader.Instaloader()
    username=input("Please enter username:")
    loader.download_profile(username, profile_pic=True)


instagramPostsLoader()