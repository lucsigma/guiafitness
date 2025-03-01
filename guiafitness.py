

import streamlit as st
import sqlite3

# Criar a conexão com o banco de dados SQLite3
conn = sqlite3.connect("dados_usuario.db")
cursor = conn.cursor()

# Excluir a tabela caso haja algum erro anterior, e recriar a tabela com a estrutura correta
cursor.execute("DROP TABLE IF EXISTS progresso;")
conn.commit()

# Criar a tabela com a estrutura correta, incluindo o campo grau_imc
cursor.execute('''CREATE TABLE IF NOT EXISTS progresso (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    peso REAL,
                    altura REAL,
                    idade INTEGER,
                    nivel_atividade TEXT,
                    objetivo TEXT,
                    grau_imc TEXT,
                    data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                 )''')
conn.commit()

# Captura de dados do usuário
st.title("Consultor de Emagrecimento Saudável")

# Adicionando campo para o nome do usuário
nome_usuario = st.text_input("Informe seu nome:")

# Verifica se o nome foi inserido
if nome_usuario:  # Verifica se o nome do usuário foi preenchido
    peso = st.number_input("Informe seu peso (kg):", min_value=30.0, max_value=200.0, step=0.1)
    altura = st.number_input("Informe sua altura (m):", min_value=1.2, max_value=2.5, step=0.01)
    idade = st.number_input("Informe sua idade:", min_value=10, max_value=100, step=1)
    nivel_atividade = st.selectbox("Nível de atividade física:", ["Sedentário", "Leve", "Moderado", "Intenso"])
    objetivo = st.selectbox("Objetivo:", ["Perder peso", "Manter peso", "Ganhar massa muscular"])

    # Cálculo do IMC
    if altura > 0:
        imc = peso / (altura ** 2)
        st.write(f"Seu IMC é: {imc:.2f}")

        # Exibindo o grau de IMC com as classificações
        if imc < 18.5:
            st.warning(f"Abaixo do peso ideal (IMC: {imc:.2f})")
            grau_imc = "Abaixo do peso"
        elif imc < 24.9:
            st.success(f"Peso ideal (IMC: {imc:.2f})")
            grau_imc = "Peso ideal"
        elif imc < 29.9:
            st.warning(f"Sobrepeso (IMC: {imc:.2f})")
            grau_imc = "Sobrepeso"
        elif imc < 34.9:
            st.warning(f"Obesidade grau 1 (IMC: {imc:.2f})")
            grau_imc = "Obesidade grau 1"
        elif imc < 39.9:
            st.warning(f"Obesidade grau 2 (IMC: {imc:.2f})")
            grau_imc = "Obesidade grau 2"
        else:
            st.error(f"Obesidade grau 3 (IMC: {imc:.2f})")
            grau_imc = "Obesidade grau 3"

    # Exibindo recomendações com base nas informações
    st.subheader(f"Recomendações para {nome_usuario}:")
    if imc < 18.5:
        st.write("Você está abaixo do peso ideal. Recomendamos uma dieta com maior ingestão calórica e acompanhamento profissional.")
    elif imc < 24.9:
        st.write("Você está no peso ideal! Continue com um estilo de vida saudável.")
    elif imc < 29.9:
        st.write("Você está com sobrepeso. Recomendamos focar na perda de peso de maneira gradual e saudável.")
        # Recomendações de Dietas Detox para sobrepeso
        st.subheader("Recomendações de Dietas Detox para Perda de Peso:")
        st.write("1. Dieta Detox de Suco Verde")
        st.write("   - Objetivo: Desintoxicar o organismo e auxiliar na perda de peso.")
        st.write("   - Período: 7 dias.")
        st.write("   - Receita: Suco verde de couve, pepino, gengibre e limão.")
        st.write("     Ingredientes: 1 folha de couve, 1/2 pepino, 1 pedaço de gengibre, suco de 1 limão e 200 ml de água.")
        st.write("     Modo de preparo: Bata tudo no liquidificador e tome pela manhã em jejum.")
        st.write("2. Dieta Detox de Suco de Beterraba")
        st.write("   - Objetivo: Auxiliar no emagrecimento e melhorar a saúde do fígado.")
        st.write("   - Período: 5 dias.")
        st.write("   - Receita: Suco de beterraba, cenoura e maçã.")
        st.write("     Ingredientes: 1 beterraba, 2 cenouras, 1 maçã e 200 ml de água.")
        st.write("     Modo de preparo: Bata tudo no liquidificador e consuma ao longo do dia.")
    else:
        st.write("Você está com obesidade. É importante procurar orientação de um profissional para elaborar um plano de emagrecimento saudável.")
        # Recomendações de Dietas Detox para obesidade
        st.subheader("Recomendações de Dietas Detox para Emagrecimento Acelerado:")
        st.write("1. Dieta Detox de Suco de Abacaxi e Hortelã")
        st.write("   - Objetivo: Acelerar o emagrecimento e desintoxicar.")
        st.write("   - Período: 10 dias.")
        st.write("   - Receita: Suco de abacaxi com hortelã.")
        st.write("     Ingredientes: 1/2 abacaxi, 1 punhado de hortelã, 200 ml de água.")
        st.write("     Modo de preparo: Bata tudo no liquidificador e consuma durante o dia.")
        st.write("2. Dieta Detox de Chá de Gengibre com Limão")
        st.write("   - Objetivo: Combater a retenção de líquidos e aumentar o metabolismo.")
        st.write("   - Período: 7 dias.")
        st.write("   - Receita: Chá de gengibre e limão.")
        st.write("     Ingredientes: 1 pedaço pequeno de gengibre, suco de 1 limão, 500 ml de água.")
        st.write("     Modo de preparo: Ferva a água com o gengibre, retire do fogo e adicione o suco de limão.")
        st.write("     Consumir ao longo do dia.")
        
    # Exibindo as informações do usuário
    st.subheader(f"Informações do Usuário:")
    st.write(f"Nome: {nome_usuario}")
    st.write(f"Peso: {peso} kg")
    st.write(f"Altura: {altura} m")
    st.write(f"Idade: {idade} anos")
    st.write(f"Nível de atividade: {nivel_atividade}")
    st.write(f"Objetivo: {objetivo}")
    st.write(f"Grau IMC: {grau_imc}")

    # Botão para salvar os dados no banco de dados
    if st.button("Salvar Progresso"):
        cursor.execute("INSERT INTO progresso (nome, peso, altura, idade, nivel_atividade, objetivo, grau_imc) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                       (nome_usuario, peso, altura, idade, nivel_atividade, objetivo, grau_imc))
        conn.commit()
        st.success("Progresso salvo com sucesso!")
        st.rerun()  # Recarregar a interface após salvar os dados

# Mostrar o progresso armazenado
st.subheader("Histórico de Peso")

cursor.execute("SELECT id, nome, data_registro, peso, grau_imc FROM progresso ORDER BY data_registro DESC LIMIT 5")
dados = cursor.fetchall()

if dados:
    # Edição e Exclusão de Registros
    st.subheader("Editar ou Excluir Registro")

    ids = [id for id, _, _, _, _ in dados]
    id_editar = st.selectbox("Escolha um registro para editar ou excluir:", ids)
    registro = cursor.execute("SELECT peso, altura, idade, nivel_atividade, objetivo, grau_imc FROM progresso WHERE id = ?", (id_editar,)).fetchone()

    if registro:
        novo_peso = st.number_input("Novo peso (kg):", min_value=30.0, max_value=200.0, value=registro[0], step=0.1)
        nova_altura = st.number_input("Nova altura (m):", min_value=1.2, max_value=2.5, value=registro[1], step=0.01)
        nova_idade = st.number_input("Nova idade:", min_value=10, max_value=100, value=registro[2], step=1)
        novo_nivel_atividade = st.selectbox("Novo nível de atividade física:", ["Sedentário", "Leve", "Moderado", "Intenso"], index=["Sedentário", "Leve", "Moderado", "Intenso"].index(registro[3]))
        novo_objetivo = st.selectbox("Novo objetivo:", ["Perder peso", "Manter peso", "Ganhar massa muscular"], index=["Perder peso", "Manter peso", "Ganhar massa muscular"].index(registro[4]))

        if st.button("Atualizar Registro"):
            cursor.execute('''UPDATE progresso SET peso = ?, altura = ?, idade = ?, nivel_atividade = ?, objetivo = ?, grau_imc = ? WHERE id = ?''', 
                           (novo_peso, nova_altura, nova_idade, novo_nivel_atividade, novo_objetivo, grau_imc, id_editar))
            conn.commit()
            st.success("Registro atualizado com sucesso!")
            st.rerun()  # Recarregar a interface após atualizar o registro

        if st.button("Excluir Registro"):
            cursor.execute("DELETE FROM progresso WHERE id = ?", (id_editar,))
            conn.commit()
            st.success("Registro excluído com sucesso!")
            st.rerun()  # Recarregar a interface após excluir o registro

else:
    st.write("Nenhum progresso registrado ainda.")

conn.close()