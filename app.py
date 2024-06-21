import os
import psycopg2

# Função para obter a conexão com o PostgreSQL
def get_postgresql_connection():
    try:
        # Obtém a string de conexão a partir da variável de ambiente DATABASE_URL
        conn = psycopg2.connect(os.environ['DATABASE_URL'])
        return conn
    except Exception as e:
        print("Erro ao conectar ao PostgreSQL:", e)
        return None

# Dados fictícios de produtos de supermercado
produtos = [
    ("Maçã", "Frutas", 2.5, 100),
    ("Leite", "Laticínios", 3.0, 50),
    ("Pão", "Padaria", 2.0, 75),
    ("Ovos", "Laticínios", 4.5, 30),
    ("Arroz", "Grãos", 10.0, 40),
    ("Feijão", "Grãos", 8.0, 45),
    ("Carne", "Carnes", 20.0, 20),
    ("Café", "Bebidas", 15.0, 60),
    ("Azeite", "Molhos", 12.0, 25),
    ("Chocolate", "Doces", 5.0, 80)
]

def criar_tabela_produto(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos (
                id SERIAL PRIMARY KEY,
                nome TEXT NOT NULL,
                categoria TEXT NOT NULL,
                preco NUMERIC(10, 2) NOT NULL,
                quantidade INTEGER NOT NULL
            )
        ''')
        conn.commit()
        print("Tabela criada com sucesso.")
    except Exception as e:
        print("Erro ao criar tabela:", e)

def inserir_dados_produto(conn, produto):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO produtos (nome, categoria, preco, quantidade)
            VALUES (%s, %s, %s, %s)
        ''', produto)
        conn.commit()
        print(f"Dados inseridos para {produto[0]}")
    except Exception as e:
        print("Erro ao inserir dados:", e)

def main():
    conn = get_postgresql_connection()
    if conn:
        criar_tabela_produto(conn)
        for produto in produtos:
            inserir_dados_produto(conn, produto)
        conn.close()

if __name__ == "__main__":
    main()