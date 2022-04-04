from unittest import skip
from rest_framework.test import APITestCase
from .not_hashable_key_dict import NotHashableKeyDict, NotHashableKeyDictException


class HistoryManagerTests(APITestCase):
    # mcore.data_monitoring.libs.tests_not_hash_dict.HistoryManagerTests

    def setUp(self) -> None:

        # non hashable
        self.dad = {"name": "dad"}
        self.mom = {"name": "mom"}
        self.boy = {"name": "son"}
        self.girl = {"name": "daughter"}
        self.president = {"name": "president"}
        self.first_lady = {"name": "first_lady"}

        self.dad_age = {"age": 44}
        self.mom_age = {"age": 43}
        self.boy_age = {"age": 12}
        self.girl_age = {"age": 9}
        self.president_age = {"age": "old"}
        self.first_lady_age = {"age": "young"}

        self.family = NotHashableKeyDict(
            (self.dad, {"age": 44}),
            (self.mom, {"age": 43}),
            (self.boy, {"age": 12}),
            (self.girl, {"age": 9}),
        )

    @skip
    def test_init(self):
        # AAA
        # OK car pas de clef non hashable
        my_dict = NotHashableKeyDict()
        real_dict = dict(my_dict)
        self.assertEqual(real_dict, {})

        # AAA
        # OK car pas de clef non hashable
        my_dict = NotHashableKeyDict(("name", "dad"))
        real_dict = dict(my_dict)  # OK car pas de clef non hashable
        self.assertEqual(real_dict, {"name": "dad"})

        # AAA
        # KO car clef non hashable
        my_dict = NotHashableKeyDict(({"name": "dad"}, "clef non hashable"))
        self.assertRaises(NotHashableKeyDictException, dict(my_dict))

    def test_setitem(self):
        # AAA
        family = NotHashableKeyDict()
        family["dad"] = 44
        self.assertEqual(dict(family), {"dad": 44})

        # AAA NotHashableKeyDict is mutable
        family = NotHashableKeyDict()
        age = {"age": 44}
        new_family = family[self.dad] = age
        self.assertEqual(new_family, age)

    def test_getitem(self):
        # AAA
        age = 44
        family = NotHashableKeyDict((self.dad, age))
        self.assertEqual(family[self.dad], age)

    def test_len(self):
        # AAA
        family = self.family
        members = len(family)
        self.assertEqual(members, 4)

    def test_del(self):
        # AAA
        family = self.family
        members = len(family)
        self.assertEqual(members, 4)
        del family[self.dad]
        members = len(family)
        self.assertEqual(members, 3)

    def test_clear(self):
        # AAA
        family = self.family
        family.clear()
        self.assertFalse(family)  # bool([]) is False

    def test_copy(self):
        # AAA
        family = self.family
        same_family = family.copy()
        self.assertEqual(family.items(), same_family.items())

    def test_has_key(self):
        # AAA
        family = self.family
        has_dad = family.has_key(self.dad)
        not_member = family.has_key(self.president)
        self.assertTrue(has_dad)
        self.assertFalse(not_member)

    def test_update(self):
        # AAA
        family = self.family
        new_age = 45
        family.update((self.dad, new_age))
        dad_age = family[self.dad]
        self.assertEqual(dad_age, new_age)

        # AAA
        family = self.family
        self.assertRaises(NotHashableKeyDictException, family.update, self.dad, age=45)

    def test_updateKey(self):
        # AAA
        family = self.family
        new_age = {"age": 45}
        family.updateKey(self.dad, new_age)
        dad_age = family[self.dad]
        self.assertEqual(dad_age, new_age)

        # AAA
        family = self.family
        self.assertRaises(NotHashableKeyDictException, family.updateKey, self.dad, 45)


    @skip
    def test_set(self):
        pass

    def test_keys(self):
        # AAA
        family = self.family
        members = family.keys()
        self.assertEqual(members, [
            self.dad,
            self.mom,
            self.boy,
            self.girl
        ])

    def test_values(self):
        # AAA
        family = self.family
        ages = family.values()
        self.assertEqual(ages, [
            self.dad_age,
            self.mom_age,
            self.boy_age,
            self.girl_age
        ])

    def test_items(self):
        # AAA
        family = self.family
        members_ages= family.items()
        self.assertEqual(members_ages, [
            (self.dad, self.dad_age),
            (self.mom, self.mom_age),
            (self.boy, self.boy_age),
            (self.girl, self.girl_age)
        ])

    def test_pop(self):
        # AAA existing key
        family = self.family
        original_length = len(family)
        dad = family.pop(self.dad) # :'(
        self.assertEqual(dad, self.dad_age)
        self.assertEqual(len(family), original_length-1)

        # AAA no existing key
        family = self.family
        original_length = len(family)
        president = family.pop(self.president) # not in family :'( !!
        self.assertEqual(president, None)
        self.assertEqual(len(family), original_length)

        # AAA no existing key
        family = self.family
        default_first_lady = "Lady Gaga"
        original_length = len(family)
        first_lady = family.pop(self.first_lady, default_first_lady) # not in family too
        self.assertEqual(first_lady, default_first_lady)
        self.assertEqual(len(family), original_length)

    def test_get(self):
        # AAA existing key
        family = self.family
        dad = family.pop(self.dad)
        self.assertEqual(dad, self.dad_age)

        # AAA no existing key
        family = self.family
        president = family.pop(self.president) # not in family :'( !!
        self.assertEqual(president, None)

        # AAA no existing key
        family = self.family
        default_first_lady = "Lady Gaga"
        first_lady = family.pop(self.first_lady, default_first_lady) # not in family too
        self.assertEqual(first_lady, default_first_lady)

    def test_setdefault(self):
        # AAA existing key
        family = self.family
        behaviour = "cool"
        dad = family.setdefault(self.dad, behaviour)
        self.assertEqual(dad, self.dad_age)

        # AAA no existing key
        family = self.family
        president = family.setdefault(self.president, self.president_age) # now in family :+1 !!
        self.assertEqual(president, self.president_age)

        # AAA no existing key
        family = self.family
        first_lady = family.setdefault(self.first_lady) # now in family too
        self.assertEqual(first_lady, None)
