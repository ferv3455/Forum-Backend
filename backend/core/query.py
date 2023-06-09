from django.db.models import QuerySet, Q


def query_tag(query_set: QuerySet, tag: str):
    return query_set.filter(tags=tag)


def query_user(query_set: QuerySet, username: str):
    return query_set.filter(user__username=username)


def query_content(query_set: QuerySet, keyword: str):
    return query_set.filter(Q(title__icontains=keyword) | Q(content__icontains=keyword))


def query(query_set: QuerySet, query_string: str):
    filters = query_string.split()
    print(filters)

    for f in filters:
        print(query_set)
        if f.startswith('#'):
            query_set = query_tag(query_set, f[1:])
        elif f.startswith('$'):
            query_set = query_user(query_set, f[1:])
        else:
            query_set = query_content(query_set, f)

    return query_set
