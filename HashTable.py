def hash_string(keyword, buckets):
    sum = 0
    for e in keyword:
        sum += ord(e) % buckets
    return sum  # %buckets


def bad_hash_string(keyword, buckets):
    return ord(keyword[0]) % buckets


def hashtable_get_bucket(hastable, keyword):
    return hash_string(keyword, len(hastable))


def hashtable_add(table, key, value):
    hashtable_get_bucket(table, key).append([key, value])


def hashtable_lookup(table, key):
    bucket = hashtable_get_bucket(table, key)
    entry=check(bucket,key)
    if entry:
            return entry[1]
    return None


def hastable_update(table, key, value):
    bucket = hashtable_get_bucket(table, key)
    entry= check(bucket, key)
    if entry:
        entry[1] == value
    else:
        bucket.append([key, value])


def check(bucket, key):
    for entry in bucket:
        if entry[0] == key:
            return entry
    return None

