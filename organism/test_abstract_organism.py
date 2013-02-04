"""
Generic Tests for all Organism Classes.
"""


class MixinTestOrganism(object):

    def test_init(self):
        organism = self.Organism(self.value_0)
        self.assertEqual(organism.value, self.value_0)

        organism2 = self.Organism(self.value_1)
        self.assertEqual(organism2.value, self.value_1)

    def test_init_unnamed(self):
        with self.assertRaises(ValueError):
            self.Organism(self.value_0, None)

    def test_eq(self):
        g0 = self.Organism(self.value_0)
        g0_ = self.Organism(self.value_0)
        g1 = self.Organism(self.value_1)
        self.assertEqual(g0, g0_)
        self.assertNotEqual(g0, g1)

    def test_hash(self):
        set_of_organisms = {
            self.Organism(self.value_0), self.Organism(self.value_1)}
        set_of_organisms2 = {
            self.Organism(self.value_1), self.Organism(self.value_2)}
        set_of_organisms3 = set_of_organisms.union(set_of_organisms2)

        self.assertSetEqual(
            set_of_organisms3,
            {self.Organism(self.value_0),
             self.Organism(self.value_1),
             self.Organism(self.value_2)})

    def test_mutate(self):
        g0 = self.Organism(self.value_0)
        g_ = g0.mutate()
        self.assertNotEqual(g0, g_)
        self.assertTrue(isinstance(g_, self.Organism))

    def test_positive_fitness(self):
        orgs = [self.Organism(value) for value in
                [self.value_0, self.value_1, self.value_2]]
        for org in orgs:
            self.assertGreater(org.fitness, 0)

    def test_repr(self):
        org = self.Organism(self.value_0)
        expected_beginning = 'Organism(value={!r},'.format(self.value_0)
        self.assertIn(expected_beginning, repr(org))

    def test_parent(self):
        g0 = self.Organism(self.value_0)
        g_ = g0.mutate()
        self.assertEqual(g0.self_id, g_.parent_id)


class MixinTestModule(object):
    def test_default_organism(self):
        org = self.organism.default_organism
        self.assertTrue(isinstance(org, self.Organism))
