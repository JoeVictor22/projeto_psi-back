class ClasseBase:
    _fields = []

    @staticmethod
    def from_dict(dicionario):
        return ClasseBase(**{key: dicionario[key] for key in ClasseBase._fields})

    def to_dict(self):
        return {key: getattr(self, key) for key in self._fields}

    @staticmethod
    def to_update(dicionario):
        fields_to_edit = {
            nome_campo: dicionario[nome_campo]
            for nome_campo in ClasseBase._fields
            if nome_campo in dicionario
        }
        return fields_to_edit
