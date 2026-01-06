# FAQ5A: Gerenciador de FAQ e Colinhas para Atendimento

O FAQ5A é uma aplicação web desenvolvida em Django, projetada para permitir que usuários criem e gerenciem seu próprio banco de dados de Perguntas Frequentes (FAQ), complementado por um sistema de "Colinhas" (cheat sheets) para auxiliar em processos de atendimento ou consulta rápida.

## Funcionalidades Principais

O sistema oferece as seguintes funcionalidades centrais, todas acessíveis após o login:

| Módulo | Funcionalidade | Descrição |
| :--- | :--- | :--- |
| **FAQ** | Criação de Tópicos | Estrutura o conhecimento em tópicos principais, cada um contendo múltiplas citações/respostas. |
| **FAQ** | Visualização de Tópicos | Permite navegar e consultar os tópicos de FAQ criados pelo usuário. |
| **Colinhas** | Criação e Gestão | Adiciona, edita e exclui colinhas de consulta rápida. |
| **Colinhas** | Favoritos | Marca colinhas como favoritas para acesso prioritário. |
| **Colinhas** | Reordenação | Permite reordenar as colinhas para personalizar a ordem de visualização. |

## Passo a Passo de Uso

Para começar a utilizar o FAQ5A, siga o fluxo de autenticação e, em seguida, explore as funcionalidades de FAQ e Colinhas.

### 1. Cadastro de Usuário

1.  Acesse a página de **Cadastro**.
2.  Preencha os campos necessários (nome de usuário, e-mail, senha).
3.  Após o preenchimento, o sistema criará sua conta e o redirecionará para a página de login.

### 2. Login

1.  Acesse a página principal, que é a tela de **Login**.
2.  Insira suas credenciais (nome de usuário e senha).
3.  Ao logar, você será direcionado para a área de gerenciamento do seu FAQ.

### 3. Criação e Gestão do FAQ

O módulo FAQ é onde você constrói seu banco de conhecimento.

#### Adicionar um Novo Tópico de FAQ

1.  Navegue para a página de **Adicionar FAQ**.
2.  Preencha o **Título** e a **Descrição** do novo tópico.
3.  Utilize o formulário de **Citações** (CitacaoFormSet) para adicionar as respostas ou informações detalhadas relacionadas a este tópico. Você pode adicionar múltiplas citações para um único tópico.
4.  Salve o tópico. Ele será imediatamente listado e acessível na sua área de FAQ.

#### Visualizar o FAQ

1.  A página principal do FAQ exibirá o primeiro tópico que você criou por padrão.
2.  Você pode navegar entre os tópicos existentes utilizando a URL específica de cada um.

### 4. Gestão de Colinhas

O módulo Colinhas é ideal para informações curtas e de alta frequência de uso.

#### Adicionar uma Colinha

1.  Acesse a página de **Colinhas**.
2.  Na seção de adição, preencha o **Título** e o **Conteúdo** da sua colinha.
3.  Salve para que ela apareça na lista.

#### Favoritar e Reordenar

1.  **Favoritar:** Na lista de colinhas, você pode marcar qualquer item como **Favorito**. As colinhas favoritas são exibidas com prioridade no topo da lista.
2.  **Reordenar:** O sistema permite que você altere a ordem de exibição das colinhas (tanto favoritas quanto normais) para que as mais importantes ou usadas fiquem mais acessíveis.

#### Editar e Excluir

1.  **Editar:** Utilize a funcionalidade de edição para atualizar o título ou o conteúdo de uma colinha existente.
2.  **Excluir:** Utilize a funcionalidade de exclusão para remover permanentemente uma colinha.