# Python distribution containing tools for working with Redis
# https://github.com/andymccurdy/redis-py
import redis

db = redis.Redis(host='redis.talentbuddy.co', port=6379, db=0)

def follow(user_id1, user_id2):
    friends = db.get(user_id1)
    if not friends:
        db.set(user_id1, [user_id2])
    else:
        friends = eval(friends)
        friends.append(user_id2)
        db.set(user_id1, friends)

def num_followers(user_id):
    count = 0
    for key in db.keys('*'):
        friends = eval(db.get(key))
        if user_id in friends:
            count +=1
    print count

def list_friends(user_id):
    print '\n'.join(sorted(get_friends(user_id)))
    
def get_friends(user_id):
    friend_list = set()
    friends = db.get(user_id)
    if not friends:
        return friend_list
    friends = eval(friends)
    for friend_id in friends:
        other_list = db.get(friend_id)
        if not other_list:
            continue
        other_list = eval(other_list)
        if user_id in other_list:
            friend_list.add(friend_id)
    return friend_list

def most_friendly_users(n):
    count_map = {}
    for key in db.keys('*'):
        count_map[key] = len(get_friends(key))
    print_count = 0
    for user in sorted(count_map, key = count_map.get)[::-1]:
        print user
        print_count += 1
        if print_count == n:
            break
