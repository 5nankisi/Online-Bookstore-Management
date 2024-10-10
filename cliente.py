class Cliente:
    def __init__(self, nome, nacionalidade, email, password, numCartCred, profissao, bi, morada, telefone):
        self._nome = nome
        self._nacionalidade = nacionalidade
        self._email = email
        self._password = password
        self._numCartCred = numCartCred
        self._profissao = profissao
        self._bi = bi
        self._morada = morada
        self._telefone = telefone

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def nacionalidade(self):
        return self._nacionalidade

    @nacionalidade.setter
    def nacionalidade(self, value):
        self._nacionalidade = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def numCartCred(self):
        return self._numCartCred

    @numCartCred.setter
    def numCartCred(self, value):
        self._numCartCred = value

    @property
    def profissao(self):
        return self._profissao

    @profissao.setter
    def profissao(self, value):
        self._profissao = value

    @property
    def bi(self):
        return self._bi

    @bi.setter
    def bi(self, value):
        self._bi = value

    @property
    def morada(self):
        return self._morada

    @morada.setter
    def morada(self, value):
        self._morada = value

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, value):
        self._telefone = value
