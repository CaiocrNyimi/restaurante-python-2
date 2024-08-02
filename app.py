from modelos.restaurante import Restaurante

restaurante_fogodechao = Restaurante('Fogo de Chão', 'Churrascaria')
restaurante_fogodechao.receber_avaliacao('Larissa', 4)
restaurante_fogodechao.receber_avaliacao('Júlia', 3)
restaurante_fogodechao.receber_avaliacao('Emily', 5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()