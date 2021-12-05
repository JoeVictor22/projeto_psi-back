class ClasseBase:
    _fields = []

    def to_dict(self):
        return {key: getattr(self, key) for key in self._fields}

    @staticmethod
    def from_dict(dicionario, classe):
        return classe(**{key: dicionario[key] for key in classe._fields})

    @staticmethod
    def to_update(dicionario, classe):
        fields_to_edit = {
            nome_campo: dicionario[nome_campo]
            for nome_campo in classe._fields
            if nome_campo in dicionario
        }
        return fields_to_edit
