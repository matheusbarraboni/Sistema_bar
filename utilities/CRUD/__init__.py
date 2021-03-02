import sqlite3
from time import sleep


class Crud:
    def __init__(self):
        self.conn = sqlite3.connect('sistema_bar')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS cardapio (
            cod int not null unique,
            nome varchar(40) not null,
            preco decimal(4,2) not null,
            descricao text
        );
        ''')
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS mesas (
            numero tinyint not null unique
        );
        ''')
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS pagamentos (
            forma varchar(10) not null,
            valor decimal(4,2) not null
        );
        ''')
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS mesas_abertas (
            numero int not null
        );
        ''')
    

    def criarMesa(self, numero_mesa):
        try:
            self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS '{str(numero_mesa)}' (
                cod_item int,
                valor_pago decimal(4,2),
                forma_pagamento tinyint
            ); 
            ''')
            self.cursor.execute(f'''
            INSERT INTO mesas_abertas VALUES 
            ('{numero_mesa}');
            ''')
            self.conn.commit()
        except:
            print('Não foi possivel abrir a mesa')
        else:
            print(f'Mesa {numero_mesa} aberta com sucesso!')
        

    def deletarMesa(self, numero_mesa):
        self.cursor.execute(f'''
        DROP TABLE IF EXISTS '{numero_mesa}'
        ''')
        self.cursor.execute(f'''
        DELETE FROM mesas_abertas
        WHERE numero = '{numero_mesa}';
        ''')
        self.conn.commit()

    
    def lerMesasAbertas(self):
        self.cursor.execute('''
        SELECT * FROM mesas_abertas
        ''')
        mesas_em_ordem = list()
        for i in self.cursor.fetchall():
            for j in i:
                mesas_em_ordem.insert(0, j)
        mesas_em_ordem.sort()
        return mesas_em_ordem

    
    def adicionarItemCardapio(self, nome, preco, cod='default', descricao=''):
        self.cursor.execute(f'''
        INSERT INTO cardapio VALUES 
        ('{cod}', '{nome}', '{preco}', '{descricao}');
        ''')
        self.conn.commit()
    
    def lerCardapio(self):
        self.cursor.execute('''
        SELECT * FROM cardapio
        ''')
        return self.cursor.fetchall()


    def deletarItemCardapio(self, cod_item):
        self.cursor.execute(f'''
        DELETE FROM cardapio
        WHERE cod = '{cod_item}';
        ''')
        self.conn.commit()

    
    def adicionarItemMesa(self, cod_item, numero_mesa):
        self.cursor.execute(f'''
        INSERT INTO '{numero_mesa}' (cod_item)
        VALUES ('{cod_item}');
        ''')
        self.conn.commit()


    def deletarItemMesa(self, cod_item, numero_mesa):
        self.cursor.execute(f'''
        DELETE FROM '{numero_mesa}'
        WHERE cod_item = '{cod_item}'
        ''')
        self.conn.commit()
    

    def lerValorConta(self, numero_mesa):
        self.cursor.execute(f'''
        SELECT * FROM '{numero_mesa}'
        ''')
        return self.cursor.fetchall()


    def lerContaMesa(self, numero_mesa):
        self.cursor.execute(f'''
        SELECT (cod_item) FROM '{numero_mesa}'
        ''')
        relacao_itens = list()
        for i in self.cursor.fetchall():
            for j in i:
                self.cursor.execute(f'''
                SELECT * FROM CARDAPIO
                WHERE cod = '{j}'
                ''')
                relacao_itens.append(self.cursor.fetchall()[0])
        return relacao_itens

    
    def adicionarPagamento(self, numero_mesa, valor_pago, forma_pagamento):
        self.cursor.execute(f'''
        INSERT INTO '{numero_mesa}' (valor_pago, forma_pagamento)
        VALUES ('{valor_pago}', '{forma_pagamento}')
        ''')
        self.conn.commit()

