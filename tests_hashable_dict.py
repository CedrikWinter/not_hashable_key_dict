from unittest import skip
from rest_framework.test import APITestCase
from .hashable_dict import HashableDict


class HistoryManagerTests(APITestCase):
    # mcore.data_monitoring.libs.tests_not_hashable_key_dict.HistoryManagerTests

    def setUp(self) -> None:

        # non hashable
        self.dad = HashableDict({"name": "dad"})
        self.mom = HashableDict({"name": "mom"})
        self.boy = HashableDict({"name": "son"})
        self.girl = HashableDict({"name": "daughter"})
        self.president = HashableDict({"name": "president"})
        self.first_lady = HashableDict({"name": "first_lady"})

        self.dad_age = {"age": 44}
        self.mom_age = {"age": 43}
        self.boy_age = {"age": 12}
        self.girl_age = {"age": 9}
        self.president_age = {"age": "old"}
        self.first_lady_age = {"age": "young"}

        self.family = HashableDict({
            self.dad: {"age": 44},
            self.mom: {"age": 43},
            self.boy: {"age": 12},
            self.girl: {"age": 9},
        })

    def test_init(self):
        # AAA
        # OK car pas de clef non hashable
        my_dict = HashableDict()
        real_dict = dict(my_dict)
        self.assertEqual(real_dict, {})

        # AAA
        # OK car pas de clef non hashable
        my_dict = HashableDict({"name": "dad"})
        real_dict = dict(my_dict)  # OK car pas de clef non hashable
        self.assertEqual(real_dict, {"name": "dad"})

        # AAA
        # KO car clef non hashable
        try:
            HashableDict({{"name": "dad"}: "clef non hashable"})

        except TypeError as e:
            self.assertTrue("unhashable type: 'dict'" in str(e))

    def test_setitem(self):
        # AAA
        family = HashableDict()
        family["dad"] = 44
        self.assertEqual(dict(family), {"dad": 44})

        # AAA HashableDict is mutable
        family = HashableDict()
        age = {"age": 44}
        new_family = family[self.dad] = age
        self.assertEqual(new_family, age)

    def test_getitem(self):
        # AAA
        age = 44
        family = HashableDict({self.dad: age})
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

    def test_in(self):
        # AAA
        family = self.family
        has_dad = self.dad in family
        not_member = self.president in family
        self.assertTrue(has_dad)
        self.assertFalse(not_member)

    def test_update(self):
        # AAA
        family = self.family
        new_age = 45
        family.update({self.dad: new_age})
        dad_age = family[self.dad]
        self.assertEqual(dad_age, new_age)

        # AAA
        family = self.family
        family.update({self.dad: {"age": 36}})
        # family.update(self.mom={"age": 36})  # SyntaxError
        pass  # add asserts

    @skip
    def test_set(self):
        pass

    def test_keys(self):
        # AAA
        family = self.family
        members = list(family.keys())
        self.assertEqual(members, [
            self.dad,
            self.mom,
            self.boy,
            self.girl
        ])

    def test_values(self):
        # AAA
        family = self.family
        ages = list(family.values())
        self.assertEqual(ages, [
            self.dad_age,
            self.mom_age,
            self.boy_age,
            self.girl_age
        ])

    def test_items(self):
        # AAA
        family = self.family
        members_ages= list(family.items())
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
        self.assertRaises(KeyError, family.pop, self.president) # not in family :'( !!
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
        dad = family.get(self.dad)
        self.assertEqual(dad, self.dad_age)

        # AAA no existing key
        family = self.family
        president = family.get(self.president) # not in family :'( !!
        self.assertEqual(president, None)

        # AAA no existing key
        family = self.family
        default_first_lady = "Lady Gaga"
        first_lady = family.get(self.first_lady, default_first_lady) # not in family too
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
