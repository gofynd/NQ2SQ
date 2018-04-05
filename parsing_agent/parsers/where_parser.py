import re

regex = '(\w+)[\s]*(=|is|from)+[\s]*(\w+|\d+)'


class WhereParser(object):

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        return False

    def parse(self, input_string, cols):
        where_clause = []

        matched_clauses = re.findall(regex, input_string)

        for each_clause_key, _, each_clause_value in matched_clauses:

            is_value_number = self.is_number(each_clause_value)
            if not is_value_number:
                each_clause_value = "'{}'".format(each_clause_value)
            if each_clause_key in cols:
                where_clause.append('{}={}'.format(each_clause_key, each_clause_value))

        if len(where_clause) == 1:
            where_clause_string = where_clause[0]
        else:
            where_clause_string = ' and '.join(where_clause)

        return where_clause_string
