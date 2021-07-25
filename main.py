import instaloader
# python test.py arg1 arg2 arg3
import sys

print("Number of arguments:", len(sys.argv), "arguments.")
print('Argument List:', str(sys.argv))

bot = instaloader.Instaloader()
profile = instaloader.Profile
profile.username = sys.argv[1]

#print(bot.download_profilepic(profile))
print(bot.download_profile(profile.username, profile_pic_only=True))
