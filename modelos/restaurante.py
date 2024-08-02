from modelos.avaliacao import Avaliacao

class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        """
        Parâmetros:
        - nome (str) do restaurante.
        - categoria (str) do restaurante.
        """
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        """Lista formatada de todos os restaurantes."""
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Não Ativo'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """
        Registra avaliação para o restaurante.
        Parâmetros:
        - cliente (str) que fez a avaliação.
        - nota (float) atribuída ao restaurante (entre 1 e 5).
        """
        if 0 < nota <= 5: 
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        """Calcula e retorna a média das avaliações."""
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media