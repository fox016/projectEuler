def merge_sort(v):
    print ' '.join(map(str, merge_sort_helper(v)))

def merge_sort_helper(v):
    if len(v) < 10:
        return sorted(v)
    half = len(v) / 2
    return merge(merge_sort_helper(v[0:half]), merge_sort_helper(v[half:]))

def merge(v1, v2):
    merged_list = []
    index_v1 = 0
    index_v2 = 0
    while len(merged_list) < len(v1) + len(v2):
        if index_v2 >= len(v2):
            merged_list.append(v1[index_v1])
            index_v1+=1
        elif index_v1 >= len(v1):
            merged_list.append(v2[index_v2])
            index_v2+=1
        elif v1[index_v1] <= v2[index_v2]:
            merged_list.append(v1[index_v1])
            index_v1+=1
        else:
            merged_list.append(v2[index_v2])
            index_v2+=1
    return merged_list
