from utilities import CRUD

teste = CRUD.Crud()
# teste.criarMesa(1)
teste.adicionarPagamento(1, 30.00, 1)
print(teste.testepagamento())