# GUIA.ME - Documentação de Design

**Projeto**: WebApp de Guia Turístico para Brasília  
**Tipo**: Trabalho de Conclusão de Curso (TCC)  
**Autor do Design**: Manus AI  
**Data**: 12 de Outubro de 2025

---

## 📋 Índice

1. [Visão Geral do Projeto](#visão-geral-do-projeto)
2. [Identidade Visual](#identidade-visual)
3. [Estrutura de Arquivos](#estrutura-de-arquivos)
4. [Protótipos Desenvolvidos](#protótipos-desenvolvidos)
5. [Documentação Técnica](#documentação-técnica)
6. [Como Visualizar](#como-visualizar)
7. [Próximos Passos](#próximos-passos)

---

## 🎯 Visão Geral do Projeto

O **GUIA.ME** é um WebApp inovador de guia turístico para Brasília que utiliza inteligência artificial para criar experiências personalizadas de exploração turística. O projeto foi desenvolvido como Trabalho de Conclusão de Curso (TCC) com foco em modernidade, inovação e usabilidade.

### Objetivos do Design

- Criar uma identidade visual forte inspirada em Brasília
- Desenvolver interfaces intuitivas e modernas
- Implementar experiências de usuário envolventes
- Garantir acessibilidade e responsividade
- Integrar inteligência artificial de forma natural

---

## 🎨 Identidade Visual

### Paleta de Cores

| Cor | Hex | Uso |
|-----|-----|-----|
| **Azul Brasília** | `#0047AB` | Cor primária, botões, links |
| **Azul Celeste** | `#4A90E2` | Cor secundária, gradientes |
| **Dourado Planalto** | `#D4AF37` | Destaques, badges |
| **Verde Cerrado** | `#6B8E23` | Sucesso, natureza |
| **Branco Puro** | `#FFFFFF` | Fundos principais |
| **Cinza Concreto** | `#F5F5F5` | Fundos secundários |

### Tipografia

- **Fonte Principal**: Inter (Google Fonts)
- **Pesos Utilizados**: 400, 500, 600, 700, 800
- **Hierarquia**: Bem definida para títulos, subtítulos e corpo de texto

### Princípios de Design

1. **Minimalismo**: Design limpo e focado
2. **Modernidade**: Uso de gradientes, sombras suaves e animações
3. **Brasilidade**: Inspiração na arquitetura de Oscar Niemeyer
4. **Acessibilidade**: Contraste adequado e tamanhos legíveis
5. **Responsividade**: Adaptação perfeita a todos os dispositivos

---

## 📁 Estrutura de Arquivos

```
guiame_design/
├── README.md (este arquivo)
│
├── Protótipos HTML
│   ├── prototipo.html                  # Telas de cadastro
│   ├── home_screen.html                # Tela inicial
│   ├── explore_categorias.html         # Exploração por categoria
│   ├── chatbot_interface.html          # Interface do chatbot
│   ├── perfil_usuario.html             # Perfil e gamificação
│   └── wireframes.html                 # Wireframes de baixa fidelidade
│
├── Documentação
│   ├── documentacao_design_cadastro.md
│   ├── documentacao_home_screen.md
│   ├── documentacao_explore_categorias.md
│   ├── documentacao_chatbot.md
│   └── documentacao_perfil_gamificacao.md
│
├── Pesquisa e Referências
│   ├── pesquisa_cadastro.md
│   ├── identidade_visual_brasilia.md
│   ├── identidade_visual_guiame.md
│   └── fluxo_cadastro_guiame.md
│
└── Ativos Visuais
    ├── brasilia_illustration.png
    ├── home_background.png
    ├── carousel_catedral.png
    ├── carousel_congresso.png
    ├── category_monumentos.png
    ├── category_gastronomia.png
    ├── icon_monuments.png
    ├── icon_culture.png
    ├── icon_nature.png
    └── [outras imagens de referência]
```

---

## 🖥️ Protótipos Desenvolvidos

### 1. Fluxo de Cadastro (`prototipo.html`)

Interface completa de cadastro de usuário com 10 telas interativas:

- **Tela de Splash**: Apresentação do app
- **Escolha de Método**: Login social ou e-mail
- **Formulário de Cadastro**: Coleta de dados essenciais
- **Verificação de E-mail**: Código de 6 dígitos
- **Onboarding**: 3 etapas de personalização
- **Boas-vindas**: Confirmação de cadastro
- **Login**: Acesso para usuários existentes
- **Recuperação de Senha**: Fluxo de reset

**Características**:
- Design minimalista e clean
- Validação em tempo real
- Indicador de força de senha
- Múltiplas opções de cadastro
- Animações suaves

### 2. Tela Inicial (`home_screen.html`)

Homepage completa com todos os elementos principais:

- **Hero Section**: Busca inteligente e filtros rápidos
- **Barra de Estatísticas**: Credibilidade e escopo
- **Destaques**: Carrossel de pontos turísticos
- **Recomendações por IA**: Seção destacada
- **Categorias**: Grid de exploração
- **Popular Agora**: Conteúdo dinâmico
- **Assistente Virtual**: FAB sempre acessível

**Características**:
- Layout moderno e responsivo
- Carrosséis interativos
- Animações de scroll
- Integração com IA visível
- Microinterações em todos os elementos

### 3. Explore por Categoria (`explore_categorias.html`)

Interface de navegação por categorias:

- **6 Categorias Principais**: Monumentos, Arte & Cultura, Gastronomia, Natureza, Compras, Eventos
- **Busca Global**: Pesquisa em todas as categorias
- **Estatísticas**: Números de locais e avaliações
- **Cards Interativos**: Efeitos de hover sofisticados

**Características**:
- Identidade visual única por categoria
- Cores vibrantes e diferenciadas
- Animações de entrada sequenciais
- Efeito ripple ao clicar
- Grid responsivo

### 4. Interface do Chatbot (`chatbot_interface.html`)

Assistente virtual completo e funcional:

- **FAB (Floating Action Button)**: Sempre acessível
- **Janela de Chat**: Interface conversacional
- **Estado de Boas-vindas**: Sugestões iniciais
- **Mensagens**: Bot e usuário diferenciados
- **Quick Replies**: Respostas rápidas
- **Suggestion Cards**: Recomendações clicáveis
- **Typing Indicator**: Feedback visual

**Características**:
- Animação de pulso no FAB
- Transições suaves
- Auto-resize do input
- Scroll automático
- Totalmente funcional (demo)

### 5. Perfil do Usuário e Gamificação (`perfil_usuario.html`)

Sistema completo de perfil com elementos de gamificação:

- **Header do Perfil**: Avatar, nível, estatísticas principais
- **Barra de Progresso**: XP atual e próximo nível
- **Sistema de Níveis**: 20 níveis progressivos com títulos
- **Conquistas**: 8+ medalhas desbloqueáveis por categoria
- **Desafios Diários**: 3 desafios que renovam a cada 24h
- **Ranking Semanal**: Top 5 exploradores com destaque
- **Linha do Tempo**: Atividades recentes do usuário

**Características**:
- Gamificação completa e motivadora
- Animações de progresso
- Sistema de XP e recompensas
- Competição social saudável
- Feedback visual imediato
- Design inspirador

### 6. Wireframes (`wireframes.html`)

Wireframes de baixa fidelidade para visualização da estrutura:

- Todas as telas do fluxo de cadastro
- Hierarquia de informações
- Estrutura de navegação
- Layout básico dos componentes

---

## 📚 Documentação Técnica

Cada protótipo possui documentação detalhada que inclui:

### Conteúdo das Documentações

1. **Visão Geral**: Contexto e objetivos
2. **Objetivos do Design**: Metas específicas
3. **Estrutura da Interface**: Componentes detalhados
4. **Paleta de Cores**: Cores utilizadas e justificativas
5. **Tipografia**: Hierarquia e tamanhos
6. **Interações e Animações**: Descrição de efeitos
7. **Responsividade**: Adaptações por dispositivo
8. **Acessibilidade**: Práticas implementadas
9. **Fluxo de Navegação**: Diagramas e descrições
10. **Próximos Passos**: Recomendações futuras
11. **Referências**: Fontes e inspirações

### Documentos Disponíveis

- `documentacao_design_cadastro.md` - Fluxo de cadastro completo
- `documentacao_home_screen.md` - Tela inicial detalhada
- `documentacao_explore_categorias.md` - Sistema de categorias
- `documentacao_chatbot.md` - Interface do assistente virtual

---

## 👁️ Como Visualizar

### Visualização Local

1. **Extraia o arquivo ZIP** em uma pasta de sua preferência

2. **Abra os arquivos HTML** diretamente no navegador:
   - Clique duas vezes no arquivo `.html`
   - Ou arraste para o navegador
   - Ou use "Abrir com..." e selecione seu navegador

3. **Arquivos recomendados para começar**:
   - `home_screen.html` - Visão geral do app
   - `prototipo.html` - Fluxo de cadastro
   - `chatbot_interface.html` - Assistente virtual

### Navegadores Recomendados

- Google Chrome (recomendado)
- Mozilla Firefox
- Microsoft Edge
- Safari

### Visualização da Documentação

Os arquivos `.md` (Markdown) podem ser visualizados:

1. **No GitHub**: Faça upload para um repositório
2. **Em editores**: VS Code, Typora, Obsidian
3. **Online**: Dillinger.io, StackEdit.io
4. **Convertidos para PDF**: Use Pandoc ou ferramentas online

---

## 🚀 Próximos Passos

### Desenvolvimento

1. **Backend**:
   - API REST para dados de pontos turísticos
   - Sistema de autenticação
   - Banco de dados de locais e eventos
   - Integração com IA (GPT/Claude)

2. **Frontend**:
   - Conversão para React ou Vue.js
   - Integração com APIs
   - Sistema de rotas
   - Estado global (Redux/Vuex)

3. **Funcionalidades**:
   - Geolocalização real
   - Mapas interativos (Google Maps/Mapbox)
   - Sistema de avaliações
   - Favoritos e listas personalizadas
   - Compartilhamento social
   - Notificações push

### Design

1. **Telas Adicionais**:
   - Detalhes de local
   - Perfil do usuário
   - Configurações
   - Histórico de visitas
   - Mapa interativo
   - Lista de favoritos

2. **Refinamentos**:
   - Modo escuro
   - Animações mais complexas
   - Ilustrações customizadas
   - Ícones próprios
   - Fotos profissionais

### Integração com IA

1. **Chatbot Inteligente**:
   - Processamento de linguagem natural
   - Recomendações personalizadas
   - Criação automática de roteiros
   - Respostas contextuais

2. **Personalização**:
   - Machine learning para preferências
   - Sugestões baseadas em histórico
   - Filtros inteligentes

---

## 📞 Suporte e Contato

Para dúvidas sobre o design ou sugestões de melhorias, entre em contato através do repositório do projeto ou com o desenvolvedor do TCC.

---

## 📄 Licença

Este projeto foi desenvolvido como Trabalho de Conclusão de Curso (TCC) e todos os direitos são reservados ao autor.

---

## 🙏 Agradecimentos

Agradecimentos especiais a:

- **Oscar Niemeyer**: Pela inspiração arquitetônica
- **Brasília**: Pela identidade visual única
- **Comunidade de Design**: Pelas referências e boas práticas
- **Orientadores do TCC**: Pelo suporte e direcionamento

---

**Desenvolvido com 💙 para Brasília**

*GUIA.ME - Explore a capital com inteligência artificial*

