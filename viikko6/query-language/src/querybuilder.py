from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, Or, All

class QueryBuilder:
    def __init__(self, matcher = All()):
        self._matchers = [matcher]

    def build(self):
        retval = And(*self._matchers)
        self._matchers = []
        return retval

    def playsIn(self, team):
        self._matchers.append(PlaysIn(team))
        return self

    def hasAtLeast(self, value, attr):
        self._matchers.append(HasAtLeast(value, attr))
        return self

    def hasFewerThan(self, value, attr):
        self._matchers.append(HasFewerThan(value, attr))
        return self

    def oneOf(self, *matcherLists):
        self._matchers = [Or(*matcherLists)]
        return self
