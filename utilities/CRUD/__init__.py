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
                valor_pago decimal(4,2)
            ); 
            ''')
            self.cursor.execute(f'''
            INSERT INTO mesas_abertas VALUES 
            ('{numero_mesa}');
            ''')
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
    
    def lerCardapio(self):
        self.cursor.execute('''
        SELECT * FROM cardapio;
        ''')
        return self.cursor.fetchall()                
