posts_list_as_input = [
    {"id": 1, "owner_id": 2},
    {"id": 2, "owner_id": 2},
    {"id": 3, "owner_id": 2},
    {"id": 5, "owner_id": 3},
    {"id": 7, "owner_id": 3},
    {"id": 4, "owner_id": 4}
]


def mix_by_owners(posts):
    iterated_posts_list = list()

    for input_post_list_index in posts:
        iterated_posts_list.append((input_post_list_index["id"], input_post_list_index["owner_id"]))

    mixed_post_list = list()
    for first_index in sorted(iterated_posts_list, key=lambda p: p[::-1]):
        for second_index in mixed_post_list:
            if second_index[-1][1] < first_index[1]:
                second_index.append(first_index)
                break
        else:
            mixed_post_list.append([first_index])

    result = sum(mixed_post_list, [])

    mixed_posts = list()

    for result_post_list_index in result:
        output_posts_dict = dict()

        output_posts_dict["id"] = result_post_list_index[0]
        output_posts_dict["owner_id"] = result_post_list_index[1]
        mixed_posts.append(output_posts_dict)

    return mixed_posts
