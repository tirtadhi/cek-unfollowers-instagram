import json

# Load data dari file followers
with open('/content/followers_1.json', 'r') as followers_file:
    followers_data = json.load(followers_file)

# Load data dari file following
with open('/content/following.json', 'r') as following_file:
    following_data = json.load(following_file)

# Ekstraksi username followers
followers = set()
for follower in followers_data:
    if follower.get("string_list_data"):
        followers.add(follower["string_list_data"][0]["value"])

# Ekstraksi username following
following = set()
for follow in following_data["relationships_following"]:
    if follow.get("string_list_data"):
        following.add(follow["string_list_data"][0]["value"])

# Temukan siapa yang tidak follow back
not_following_back = following - followers

# Tampilkan hasil
print("Daftar yang tidak mem-follow back:")
for username in sorted(not_following_back):
    print(username)
