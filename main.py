# Importa módulos
import data, helpers

# Classe de testes do aplicativo Urban Routes
class TestUrbanRoutes:
    @classmethod
    # Faz a chamada do servidor e verifica se está online ou offline
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print('Não foi possível conectar ao Urban Routes. '
                  'Verifique se o servidor está ligado e ainda em execução')

    def test_set_route(self):
    # Adicionar em S8
        print("função criada para definir rota")
        pass

    def test_select_plan(self):
    # Adicionar em S8
        print("função criada para definir plano")
        pass

    def test_fill_phone_numer(self):
    # Adicionar em S8
        print("função criada para preencher número de telefone")
        pass

    def test_fill_card(self):
    # Adicionar em S8
        print("função criada para preencher número de cartão")
        pass

    def test_comment_for_driver(self):
    # Adicionar em S8
        print("função criada para mandar mensagem ao motorista")
        pass

    def test_order_blanket_and_handkerciefs(self):
    # Adicionar em S8
        print("função criada para selecionar cobertor e/ou lenços")
        pass

    # Testa o pedido de 2 sorvetes
    def test_order_2_ice_creams(self):
    # Adicionar em S8
        print("função criada para selecionar 2 sorvetes")
        # Itera sobre um objeto de range 2
        for _ in range(2):
            pass
        pass

    def test_car_search_model_appears(self):
    # Adicionar em S8
        print("função criada para verificar modelos de veículos ")
        pass
