from base import User, Post, Like, Follow, session


def get_posts(user_id, post_ids):
    query_result_for_followed_user = session.query(Follow).filter_by(following_id=user_id)

    followers_of_given_user_as_list = list()
    for followed_user_index in query_result_for_followed_user:
        if followed_user_index.following_id is not None:
            followers_of_given_user_as_list.append(followed_user_index.follower_id)

    query_result_for_information_of_given_user = session.query(User).filter_by(id=user_id)

    user_dict = dict()
    for user_index in query_result_for_information_of_given_user:
        user_dict["id"] = user_index.id
        user_dict["username"] = user_index.username
        user_dict["full_name"] = user_index.full_name
        user_dict["profile_picture"] = user_index.profile_picture

        user_dict["followed"] = False
        if len(followers_of_given_user_as_list) != 0:
            user_dict["followed"] = True

    posts_of_given_user = list()
    query_for_getting_post_of_given_user = session.query(Post).filter_by(user_id=user_id)
    for get_post_index in query_for_getting_post_of_given_user:
        if get_post_index.id is not None:
            posts_of_given_user.append(get_post_index.id)

    liked_post_of_given_user_as_list = list()

    for post_index_of_given_user in posts_of_given_user:
        query_result_for_liked_post = session.query(Like).filter_by(post_id=post_index_of_given_user)

        for inner_index in query_result_for_liked_post:
            if inner_index.post_id is not None:
                liked_post_of_given_user_as_list.append(inner_index.post_id)

    final_posts_list = list()

    for given_post_index in post_ids:
        query_result_for_post_of_given_user = session.query(Post).filter_by(id=given_post_index)
        for post_index in query_result_for_post_of_given_user:
            final_post_dict = dict()

            final_post_dict["id"] = post_index.id
            final_post_dict["description"] = post_index.description

            final_post_dict["owner"] = None

            if post_index.user_id == user_dict["id"]:
                final_post_dict["owner"] = user_dict

            final_post_dict["liked"] = False
            if post_index.id in liked_post_of_given_user_as_list:
                final_post_dict["liked"] = True

            final_posts_list.append(final_post_dict)

    return final_posts_list
