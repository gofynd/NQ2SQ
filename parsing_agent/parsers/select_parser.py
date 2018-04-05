from nltk.corpus import stopwords
from database import *
from agent_config import *


class SelectParser(object):
    """
    simple parser that converts normal question to a proper SQL query.
    """

    def __init__(self, table_config):

        self.db_config = table_config

        self.keywords = ["select", "avg", "sum", "max", "min", "count", "greater", "less", "between"
            , "order", "asc", "desc", "group", "negation", "equal", "like", "distinct", "of", "from"]
        extra_words_to_remove = ["and"]
        # self.cachedStopWords = set(stopwords.words("english")) - set(self.keywords) - set(_agent_config.extra_words_to_remove)
        self.cachedStopWords = set(stopwords.words("english")) - set(self.keywords)
        self.cachedStopWords = list(self.cachedStopWords) + extra_words_to_remove
        self.cachedStopWords = set(self.cachedStopWords)

    def parse(self, sentence):
        """
        :param sentence:
        :return:
        """
        # text = 'hello bye the the hi'
        self.word_vec = [word for word in sentence.split() if word not in self.cachedStopWords]
        clean = ' '.join(self.word_vec)
        print("sentence = {} \n".format(sentence))
        table = self.db_config.get("table_name")
        used_cols = self.get_used_cols(sentence)
        if used_cols:
            print(self.form_query(table=table, cols=used_cols))
        else:
            print(self.form_query(table=table))

    def form_query(self, table=None, cols="*", conds=[], group_by=None, having=None, order_by=None):
        """
        format query based on given inputs
        :param table:
        :param conds:
        :param group_by:
        :param having:
        :param order_by:
        :return:
        """
        q = None
        if table and cols:
            cols = ",".join(cols)
            q = "SELECT"
            q += " {cols} FROM {table} ".format(table=table, cols=cols)
            if conds:
                t = "Where "
                for condn in conds:
                    t += " {col} {oprator} {val} ".format(col=condn.get("col"), oprator=condn.get("oprator"),
                                                          val=condn.get("val"))
                q += t
            return q

    def get_used_cols(self, sentence):
        self.word_vec = [word for word in sentence.split() if word not in self.cachedStopWords]
        print("self.word_vec",self.word_vec)
        cols = [col for col in self.db_config.keys() if col != "table_name"]
        print("cols",cols)
        used_cols = [used_col for used_col in cols if used_col in self.word_vec]
        print("used_cols",used_cols)
        if used_cols:
            return used_cols
