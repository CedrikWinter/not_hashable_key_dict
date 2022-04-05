import copy


def make_hash(o):
    """
    @see https://stackoverflow.com/a/8714242
    Makes a hash from a dictionary, list, tuple or set to any level, that contains
    only other hashable types (including any lists, tuples, sets, and
    dictionaries).
    """

    if isinstance(o, (set, tuple, list)):

        return tuple([make_hash(e) for e in o])

    elif not isinstance(o, dict):

        return hash(o)

    new_o = copy.deepcopy(o)
    for k, v in new_o.items():
        new_o[k] = make_hash(v)

    return hash(tuple(frozenset(sorted(new_o.items()))))


class HashableDict(dict):
    def __hash__(self):
        return make_hash(self)
