from nltk.corpus import stopwords
from database import *
from agent_config import *
from parsers.select_parser import SelectParser
from parsers.where_parser import WhereParser


class Parser(object):
    """
    simple parser that converts normal question to a proper SQL query.
    """

    def __init__(self, table_config):
        self.db_config = table_config
        self.sp = SelectParser(table_config)
        self.wp = WhereParser()

    def parse(self, sentence):
        """
        :param sentence:
        :return:
        """

        print("sentence = {} \n".format(sentence))
        table = self.sp.db_config.get("table_name")
        table_cols = [ field for field in self.sp.db_config if field !=table]

        used_cols = self.sp.get_used_cols(sentence)
        print("used_cols", used_cols)
        # Passing raw query with select parser
        if used_cols:
            prepared_query = self.sp.form_query(table=table, cols=used_cols)
        else:
            prepared_query = self.sp.form_query(table=table)

        # Parsing raw query with where parser
        where_query = self.wp.parse(sentence,table_cols)
        print("where_query",where_query)
        if where_query:
            prepared_query += " where "
            prepared_query += where_query


        print(prepared_query)
