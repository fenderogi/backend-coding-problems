from base import User, Post, Like, Follow, session

# users = [
#     {
#         "username": "mexapower",
#         "email": "zederick.antonio@hotmail.com",
#         "full_name": "Zederick Vargas",
#         "profile_picture": "Zederick's (user1) Profile Picture",
#         "bio": "Zederick's Bio",
#         "created_at": 1655713555
#     },
#     {
#         "username": "amiradz35",
#         "email": "a_hachache@yahoo.com",
#         "full_name": "Amira Hachache",
#         "profile_picture": "Amira's (user2) Profile Picture",
#         "bio": "Amira's Bio",
#         "created_at": 1655725943
#     },
#     {
#         "username": "Bernardo",
#         "email": "bernardomacara@gmail.com",
#         "full_name": "Bernardo Dias Macara",
#         "profile_picture": "Bernardo's (user3) Profile Picture",
#         "bio": "Bernardo's Bio",
#         "created_at": 1655819543
#     }
# ]
#
# for user in users:
#     new_user = User(
#         username=user["username"],
#         email=user["email"],
#         full_name=user["full_name"],
#         profile_picture=user["profile_picture"],
#         bio=user["bio"],
#         created_at=user["created_at"]
#     )
#     session.add(new_user)
#     session.commit()


# posts = [
#     {
#         "description": "Zederick's Post 1",
#         "user_id": 1,
#         "image": "Picture1",
#         "created_at": 1655878533
#     },
#     {
#         "description": "Amira's Post 1",
#         "user_id": 2,
#         "image": "Picture2",
#         "created_at": 1655887512
#     },
#     {
#         "description": "Zederick's Post 2",
#         "user_id": 1,
#         "image": "Picture3",
#         "created_at": 1655970104
#     },
#     {
#         "description": "Bernardo's Post 1",
#         "user_id": 3,
#         "image": "Picture4",
#         "created_at": 1655984504
#     },
#     {
#         "description": "Bernardo's Post 2",
#         "user_id": 3,
#         "image": "Picture5",
#         "created_at": 5
#     },
#     {"description": "Zederick Post 3",
#      "user_id": 1,
#      "image": "Picture6",
#      "created_at": 1656002504
#      },
#     {
#         "description": "Bernardo Post 3",
#         "user_id": 3,
#         "image": "Picture7",
#         "created_at": 1656042104
#     },
#     {
#         "description": "Amira Post 2",
#         "user_id": 2,
#         "image": "Picture8",
#         "created_at": 1656064914
#     },
#
#     {
#         "description": "Amira Post 3",
#         "user_id": 2,
#         "image": "Picture9",
#         "created_at": 1656102888
#     },
# ]
#
# for post in posts:
#     new_post = Post(
#         description=post["description"],
#         user_id=post["user_id"],
#         image=post["image"],
#         created_at=post["created_at"]
#
#     )
#     session.add(new_post)
#     session.commit()


# likes = [
#     {
#         "post_id": 3,
#         "user_id": 2,
#         "created_at": 1656109471
#     },
#     {
#         "post_id": 3,
#         "user_id": 3,
#         "created_at": 1656118784
#     },
#     {
#         "post_id": 5,
#         "user_id": 3,
#         "created_at": 1656123315
#     },
# {
#         "post_id": 2,
#         "user_id": 3,
#         "created_at": 1656127037
#     },
#     {
#         "post_id": 7,
#         "user_id": 2,
#         "created_at": 1656127157
#     },
#     {
#         "post_id": 9,
#         "user_id": 1,
#         "created_at": 1656128957
#     }
# ]
#
# for like in likes:
#     new_like = Like(
#         post_id=like["post_id"],
#         user_id=like["user_id"],
#         created_at=like["created_at"]
#
#     )
#     session.add(new_like)
#     session.commit()



# follows = [
#     {
#         "follower_id": 1,
#         "following_id": 2,
#         "created_at": 1656067777
#     },
#     {
#         "follower_id": 1,
#         "following_id": 3,
#         "created_at": 1656137572
#     },
#     {
#         "follower_id": 2,
#         "following_id": 1,
#         "created_at": 1656149771
#     }
# ]

# for follow in follows:
#     new_follow = Follow(
#         follower_id=follow["follower_id"],
#         following_id=follow["following_id"],
#         created_at=follow["created_at"]
#
#     )
#     session.add(new_follow)
#     session.commit()

# session.close()