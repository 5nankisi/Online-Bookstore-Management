class Livro:
    def __init__(self, titulo, isbn, autor, editora, anoDePubli, preco):
        self._titulo = titulo
        self._isbn = isbn
        self._autor = autor
        self._editora = editora
        self._anoDePubli = anoDePubli
        self._preco = preco

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, value):
        self._titulo = value

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, value):
        self._isbn = value

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, value):
        self._autor = value

    @property
    def editora(self):
        return self._editora

    @editora.setter
    def editora(self, value):
        self._editora = value

    @property
    def anoDePubli(self):
        return self._anoDePubli

    @anoDePubli.setter
    def anoDePubli(self, value):
        self._anoDePubli = value

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, value):
        self._preco = value
