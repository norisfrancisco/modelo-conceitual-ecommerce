from graphviz import Digraph

# Criar um grafo direcionado
dot = Digraph(comment='Modelo Conceitual E-commerce')

# Estilo comum para entidades
node_attr = {'shape': 'record', 'style': 'filled', 'fillcolor': '#f9f9f9'}

# Entidades
dot.node('Cliente', '''{Cliente|+ id_cliente (PK)\\l- nome\\l- email\\l- telefone\\l}''', **node_attr)
dot.node('Pessoa_Fisica', '''{Pessoa_Fisica|+ id_cliente (PK, FK)\\l- cpf\\l- data_nascimento\\l}''', **node_attr)
dot.node('Pessoa_Juridica', '''{Pessoa_Juridica|+ id_cliente (PK, FK)\\l- cnpj\\l- razao_social\\l}''', **node_attr)
dot.node('Forma_Pagamento', '''{Forma_Pagamento|+ id_pagamento (PK)\\l- id_cliente (FK)\\l- tipo\\l- dados_pagamento\\l}''', **node_attr)
dot.node('Pedido', '''{Pedido|+ id_pedido (PK)\\l- id_cliente (FK)\\l- data_pedido\\l- valor_total\\l}''', **node_attr)
dot.node('Pagamento_Pedido', '''{Pagamento_Pedido|+ id_pagamento_pedido (PK)\\l- id_pedido (FK)\\l- id_pagamento (FK)\\l- valor_pago\\l}''', **node_attr)
dot.node('Entrega', '''{Entrega|+ id_entrega (PK)\\l- id_pedido (FK)\\l- status\\l- codigo_rastreio\\l}''', **node_attr)

# Relacionamentos
dot.edge('Cliente', 'Pessoa_Fisica', label='1:1')
dot.edge('Cliente', 'Pessoa_Juridica', label='1:1')
dot.edge('Cliente', 'Pedido', label='1:N')
dot.edge('Cliente', 'Forma_Pagamento', label='1:N')
dot.edge('Pedido', 'Pagamento_Pedido', label='1:N')
dot.edge('Forma_Pagamento', 'Pagamento_Pedido', label='1:N')
dot.edge('Pedido', 'Entrega', label='1:1')

# Exportar como PNG
dot.format = 'png'
dot.render('modelo_conceitual_ecommerce', cleanup=True)
