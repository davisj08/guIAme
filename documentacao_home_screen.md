# Documentação do Design da Tela Inicial - GUIA.ME

**Autor**: Manus AI  
**Data**: 12 de Outubro de 2025

## 1. Visão Geral

A tela inicial (home) do **GUIA.ME** foi projetada para ser o ponto de entrada principal da experiência do usuário, capturando imediatamente a atenção com uma proposta de valor clara e oferecendo acesso rápido aos principais recursos do aplicativo. O design combina modernidade, funcionalidade e a identidade visual única de Brasília, criando uma experiência imersiva e intuitiva.

## 2. Objetivos do Design

O design da tela inicial foi desenvolvido com os seguintes objetivos estratégicos:

1. **Transmitir Inovação**: Destacar o uso de inteligência artificial como diferencial competitivo
2. **Facilitar a Descoberta**: Permitir que usuários encontrem rapidamente pontos turísticos e experiências
3. **Personalização Visível**: Demonstrar as capacidades de personalização do aplicativo
4. **Engajamento Imediato**: Capturar o interesse do usuário nos primeiros segundos
5. **Identidade Local**: Refletir a essência arquitetônica e cultural de Brasília

## 3. Estrutura da Interface

A tela inicial foi organizada em uma hierarquia visual clara, seguindo princípios de design centrado no usuário e melhores práticas de UX para aplicativos de turismo.

### 3.1. Header (Cabeçalho)

O cabeçalho permanece fixo no topo da página, garantindo acesso constante à navegação principal.

**Componentes**:
- **Logo GUIA.ME**: Posicionado à esquerda, com tipografia bold e cor primária
- **Subtítulo "Guia Inteligente"**: Reforça a proposta de valor
- **Menu Hamburguer**: Ícone minimalista à direita para acesso ao menu completo

**Comportamento**:
- Efeito de sombra ao rolar a página, criando profundidade
- Transições suaves para melhor experiência visual

### 3.2. Hero Section (Seção Principal)

A seção hero ocupa a parte superior da página com um gradiente azul inspirado no céu de Brasília, estabelecendo imediatamente a identidade visual do aplicativo.

**Elementos Visuais**:
- **Fundo com Gradiente**: Transição de azul celeste para azul Brasília
- **Ilustração de Monumentos**: Silhuetas sutis dos principais marcos da cidade em baixa opacidade
- **Badge de IA**: Destaque para o uso de inteligência artificial

**Conteúdo Textual**:
- **Título Principal**: "Explore Brasília de forma inteligente" - comunicação direta e impactante
- **Subtítulo**: Explica brevemente a proposta de valor do aplicativo

**Barra de Busca Inteligente**:
- Design destacado com sombra pronunciada
- Campo de entrada amplo e convidativo
- Botão de busca com ícone e texto
- Efeito de elevação ao receber foco

**Filtros Rápidos**:
- Chips clicáveis para categorias principais
- Design translúcido com efeito de vidro (glassmorphism)
- Estado ativo visualmente diferenciado

### 3.3. Barra de Estatísticas

Seção que estabelece credibilidade através de números concretos sobre o conteúdo disponível no aplicativo.

| Métrica | Valor | Significado |
|---------|-------|-------------|
| Pontos Turísticos | 150+ | Amplitude de cobertura |
| Restaurantes | 500+ | Opções gastronômicas |
| Eventos Mensais | 50+ | Conteúdo dinâmico |
| Usuários Ativos | 10k+ | Prova social |

### 3.4. Seção de Destaques

Carrossel horizontal apresentando os principais pontos turísticos de Brasília com cards interativos.

**Estrutura dos Cards**:
- **Imagem de Destaque**: Fotografia de alta qualidade do local
- **Título**: Nome do ponto turístico
- **Descrição**: Breve texto explicativo (2-3 linhas)
- **Metadados**: Avaliação, distância e tempo estimado de visita

**Interatividade**:
- Scroll horizontal suave
- Efeito de elevação ao passar o mouse
- Scrollbar customizada nas cores do aplicativo

### 3.5. Recomendações Personalizadas por IA

Seção destacada que demonstra as capacidades de inteligência artificial do aplicativo, diferenciando o **GUIA.ME** de guias turísticos tradicionais.

**Design Visual**:
- Fundo com gradiente sutil azul
- Ícone de estrela decorativo em grande escala
- Grid responsivo de cards

**Funcionalidades Destacadas**:

1. **Roteiro Personalizado**: Criação automática de itinerários baseados em preferências
2. **Navegação Inteligente**: Otimização de rotas considerando múltiplos fatores
3. **Dicas Contextuais**: Sugestões adaptadas ao contexto do usuário
4. **Assistente Virtual**: Chatbot para dúvidas em tempo real

### 3.6. Exploração por Categoria

Grid de cards categorizando os tipos de experiências disponíveis em Brasília.

**Categorias Disponíveis**:
- 🏛️ Monumentos
- 🎨 Arte & Cultura
- 🍽️ Gastronomia
- 🌳 Natureza
- 🛍️ Compras
- 🎭 Eventos

**Design**:
- Layout em grid responsivo
- Ícones emoji para identificação rápida
- Interação com borda colorida e elevação

### 3.7. Popular Agora

Segunda seção de carrossel apresentando locais e eventos em alta no momento, criando senso de urgência e relevância.

**Diferencial**:
- Conteúdo dinâmico baseado em tendências
- Informações sobre gratuidade e horários
- Metadados específicos para cada tipo de local

### 3.8. Assistente Virtual (FAB)

Botão flutuante de ação (Floating Action Button) posicionado no canto inferior direito da tela.

**Características**:
- Design circular com gradiente azul
- Ícone de chat com badge "IA"
- Sempre acessível, independente da posição de scroll
- Efeito de escala ao hover

## 4. Paleta de Cores e Tipografia

### Cores Principais

A paleta mantém consistência com a identidade visual estabelecida no design de cadastro:

| Elemento | Cor | Uso |
|----------|-----|-----|
| Primária | `#0047AB` | Botões, links, elementos interativos |
| Secundária | `#4A90E2` | Gradientes, elementos de suporte |
| Acento | `#D4AF37` | Destaques especiais |
| Texto Principal | `#212121` | Títulos e conteúdo principal |
| Texto Secundário | `#757575` | Descrições e metadados |

### Tipografia

**Fonte**: Inter (Google Fonts)

- **Hero Title**: 48px, weight 800
- **Section Title**: 28px, weight 700
- **Card Title**: 18px, weight 600
- **Body Text**: 16px, weight 400
- **Small Text**: 14px, weight 400

## 5. Interações e Microanimações

O design incorpora diversas animações sutis para melhorar a experiência do usuário:

1. **Fade In Up**: Elementos aparecem suavemente ao entrar no viewport
2. **Hover States**: Elevação e mudança de sombra em cards
3. **Scroll Effects**: Header ganha sombra ao rolar
4. **Chip Selection**: Transição suave de estado ativo/inativo
5. **Button Interactions**: Escala e mudança de cor ao hover

## 6. Responsividade

O design foi concebido com abordagem mobile-first, garantindo experiência otimizada em todos os dispositivos:

**Breakpoints**:
- Desktop: > 768px
- Mobile: ≤ 768px

**Adaptações Mobile**:
- Redução de tamanhos de fonte
- Grid de categorias em 2 colunas
- Redução de padding em seções
- Carrosséis com cards menores

## 7. Acessibilidade

Práticas de acessibilidade implementadas:

- Contraste adequado entre texto e fundo (WCAG AA)
- Tamanhos de fonte legíveis
- Áreas de toque adequadas para mobile (mínimo 44x44px)
- Hierarquia semântica com tags HTML apropriadas
- Estados de foco visíveis em elementos interativos

## 8. Tecnologias e Implementação

**Stack Utilizado**:
- HTML5 semântico
- CSS3 com variáveis customizadas
- JavaScript vanilla para interatividade
- Google Fonts para tipografia

**Características Técnicas**:
- Código limpo e bem comentado
- Organização modular de estilos
- Performance otimizada
- Compatibilidade cross-browser

## 9. Próximos Passos

Para evolução do design da tela inicial, recomenda-se:

1. **Integração com Backend**: Conectar a dados reais de pontos turísticos
2. **Sistema de Busca**: Implementar busca com autocomplete e filtros avançados
3. **Personalização Dinâmica**: Adaptar conteúdo baseado no perfil do usuário
4. **Geolocalização**: Mostrar distâncias reais e rotas
5. **Sistema de Avaliações**: Permitir que usuários avaliem locais
6. **Integração com Assistente IA**: Implementar chatbot funcional

## 10. Conclusão

A tela inicial do **GUIA.ME** estabelece uma base sólida para a experiência do usuário, combinando estética moderna com funcionalidade intuitiva. O design reflete a inovação tecnológica do projeto enquanto mantém forte conexão com a identidade visual de Brasília. A estrutura modular permite fácil expansão e adaptação conforme o projeto evolui.

---

## Referências

1. Nielsen Norman Group. (2024). *Homepage Usability: 50 Websites Deconstructed*. [https://www.nngroup.com/reports/homepage-usability/](https://www.nngroup.com/reports/homepage-usability/)
2. Material Design. (2024). *Material Design Guidelines*. [https://material.io/design](https://material.io/design)
3. Smashing Magazine. (2024). *Best Practices for Mobile Form Design*. [https://www.smashingmagazine.com/](https://www.smashingmagazine.com/)

