from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.models.ponto_turistico import PontoTuristico


def seed_pontos_turisticos():
    """Popula o banco com pontos turísticos de Brasília"""
    db = SessionLocal()

    pontos = [
        {
            "nome": "Catedral Metropolitana Nossa Senhora Aparecida",
            "descricao": (
                "Projetada por Oscar Niemeyer, a Catedral de Brasília é um marco da arquitetura moderna. Com suas 16 colunas de concreto que se erguem para o céu, simbolizando mãos em prece, a catedral é um dos cartões-postais da capital. O interior é adornado por vitrais de Marianne Peretti e esculturas de anjos suspensos, de Alfredo Ceschiatti. A iluminação natural cria um ambiente de paz e contemplação. A catedral foi o primeiro monumento a ser criado em Brasília."
            ),
            "categoria": "Arquitetura",
            "endereco": "Esplanada dos Ministérios, Lote 12, Brasília - DF, 70050-000",
            "horario_funcionamento": "Segunda: Fechado. Terça a sexta: 8h às 16h45. Sábado: 8h às 16h45. Domingo: 7h às 18h",
            "telefone": "(61) 3224-4073",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Catedral_Metropolitana_de_Bras%C3%ADlia.jpg/1200px-Catedral_Metropolitana_de_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Museu do Catetinho",
            "descricao": (
                "Conhecido como 'Palácio de Tábuas', o Catetinho foi a primeira residência oficial de Juscelino Kubitschek em Brasília. Construído em apenas 10 dias, o local é um marco da história da construção da capital. A simplicidade da construção de madeira contrasta com a grandiosidade dos palácios de alvenaria que viriam a ser construídos. A visita ao Catetinho é uma viagem no tempo, que remete aos primórdios da nova capital."
            ),
            "categoria": "Arquitetura",
            "endereco": "BR 040 - Saída Sul, SMPW Setor de Mansões Park Way, Brasília - DF, 72401-970",
            "horario_funcionamento": "Segunda: Fechado. Terça a domingo: 9h às 17h",
            "telefone": "(61) 3338-8803",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Catetinho_Bras%C3%ADlia.jpg/1200px-Catetinho_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Congresso Nacional",
            "descricao": (
                "Sede do poder legislativo federal do Brasil, o Congresso Nacional é um dos edifícios mais emblemáticos de Brasília. Projetado por Oscar Niemeyer, o complexo é composto por duas cúpulas, uma côncava (Senado Federal) e outra convexa (Câmara dos Deputados), e duas torres de 28 andares que abrigam os gabinetes dos parlamentares. O Salão Verde, o Salão Azul e os plenários são alguns dos espaços que podem ser visitados."
            ),
            "categoria": "Arquitetura",
            "endereco": "Praça dos Três Poderes, s/n, Brasília - DF, 70160-900",
            "horario_funcionamento": "Segunda, quinta e sexta: 9h às 17h. Sábado, domingo e feriados: 9h às 17h. Terça e quarta: Apenas grupos agendados",
            "telefone": "(61) 3303-4671",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Congresso_do_Brasil.jpg/1200px-Congresso_do_Brasil.jpg"
        },
        {
            "nome": "Eixo Monumental",
            "descricao": (
                "O Eixo Monumental é a principal avenida de Brasília, que corta a cidade de leste a oeste e concentra os principais monumentos e edifícios governamentais. Com mais de 13 km de extensão, o Eixo Monumental é uma das avenidas mais largas do mundo e um exemplo do planejamento urbanístico de Lúcio Costa. É um local ideal para passeios de carro, bicicleta ou a pé, e oferece uma visão completa da arquitetura e do urbanismo de Brasília."
            ),
            "categoria": "Arquitetura",
            "endereco": "Eixo Monumental, Plano Piloto, Brasília - DF, 70070-000",
            "horario_funcionamento": "Acesso livre 24 horas",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Eixo_Monumental_Bras%C3%ADlia.jpg/1200px-Eixo_Monumental_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Esplanada dos Ministérios",
            "descricao": (
                "A Esplanada dos Ministérios é uma das principais avenidas de Brasília, onde estão localizados os edifícios dos ministérios do governo federal. Projetada por Oscar Niemeyer e Lúcio Costa, a esplanada é um exemplo da arquitetura modernista e do urbanismo planejado da capital. É um local ideal para caminhadas e para apreciar a arquitetura dos edifícios governamentais."
            ),
            "categoria": "Arquitetura",
            "endereco": "Esplanada dos Ministérios, s/n, Zona Cívico-Administrativa, Brasília - DF, 70170-900",
            "horario_funcionamento": "Acesso livre 24 horas",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Esplanada_dos_Minist%C3%A9rios_Bras%C3%ADlia.jpg/1200px-Esplanada_dos_Minist%C3%A9rios_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Palácio da Alvorada",
            "descricao": (
                "Residência oficial do Presidente do Brasil, o Palácio da Alvorada é um marco da arquitetura moderna brasileira projetado por Oscar Niemeyer. Suas colunas em forma de “L”, o espelho da água e os jardins de Burle Marx compõem uma das vistas mais emblemáticas de Brasília. Mesmo com as visitas internas suspensas, é possível admirar sua área externa à beira do Lago Paranoá, tirar fotos e, ocasionalmente, acompanhar a saída do Presidente. O palácio também abriga importantes obras de arte e mobiliário de designers renomados, reforçando seu valor cultural e histórico."
            ),
            "categoria": "Arquitetura",
            "endereco": "Zona Cívico-Administrativa Palácio da Alvorada - Plano Piloto, Brasília - DF, 70150-903",
            "horario_funcionamento": "Visitação pública suspensa temporariamente. Consultar site oficial para atualizações",
            "telefone": "(61) 3411-4000",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Pal%C3%A1cio_da_Alvorada_2006.jpg/1200px-Pal%C3%A1cio_da_Alvorada_2006.jpg"
        },
        {
            "nome": "Palácio da Justiça",
            "descricao": (
                "O Palácio da Justiça é a sede do Ministério da Justiça e Segurança Pública. Projetado por Oscar Niemeyer, o edifício é conhecido por suas cascatas de água que descem pela fachada principal, criando um efeito visual impressionante. O palácio possui arcos e espelhos d'água semelhantes aos do Palácio do Itamaraty, mas com características únicas que o tornam uma obra de arte arquitetônica. A área externa é de livre acesso, enquanto as visitas internas são guiadas e requerem agendamento prévio."
            ),
            "categoria": "Arquitetura",
            "endereco": "Esplanada dos Ministérios, Bloco T, Zona Cívico-Administrativa, Brasília - DF, 70064-900",
            "horario_funcionamento": "Área externa: Segunda a sexta, 8h às 18h. Visitas guiadas internas: Segundas, quartas e sextas, 10h ou 15h, com agendamento via cerimonial@mj.gov.br",
            "telefone": "(61) 2025-3000",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Pal%C3%A1cio_da_Justi%C3%A7a_Bras%C3%ADlia.jpg/1200px-Pal%C3%A1cio_da_Justi%C3%A7a_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Palácio do Itamaraty",
            "descricao": (
                "Sede do Ministério das Relações Exteriores, o Palácio do Itamaraty é uma das obras mais aclamadas de Oscar Niemeyer. O edifício é cercado por um espelho d'água com a escultura 'Meteoro', de Bruno Giorgi. O interior do palácio abriga um rico acervo de obras de arte de artistas brasileiros e estrangeiros, além de um belo jardim de inverno projetado por Roberto Burle Marx. As visitas são guiadas e proporcionam uma experiência cultural única, mostrando a diplomacia brasileira através da arte e da arquitetura."
            ),
            "categoria": "Arquitetura",
            "endereco": "Esplanada dos Ministérios, Bloco H, Zona Cívico-Administrativa, Brasília - DF, 70170-900",
            "horario_funcionamento": "Terça a domingo, 8h30 às 18h. Agendamento obrigatório com 24h de antecedência via plataforma online ou e-mail visita@itamaraty.gov.br",
            "telefone": "(61) 2030-8051",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Pal%C3%A1cio_Itamaraty_Bras%C3%ADlia_2019.jpg/1200px-Pal%C3%A1cio_Itamaraty_Bras%C3%ADlia_2019.jpg"
        },
        {
            "nome": "Palácio do Planalto",
            "descricao": (
                "Sede do Poder Executivo Federal, o Palácio do Planalto é o local de trabalho do Presidente da República. O edifício, projetado por Oscar Niemeyer, é caracterizado por suas colunas delgadas e pela rampa de acesso ao salão nobre. O palácio abriga um rico acervo de arte, com obras de artistas como Di Cavalcanti e Alfredo Ceschiatti. A troca da guarda presidencial, realizada em frente ao palácio, é uma atração à parte. Após restauração em 2024, o palácio foi reaberto para visitação pública com agendamento online."
            ),
            "categoria": "Arquitetura",
            "endereco": "Praça dos Três Poderes, s/n, Zona Cívico-Administrativa, Brasília - DF, 70150-900",
            "horario_funcionamento": "Domingos, mediante agendamento prévio obrigatório via visitapr.presidencia.gov.br. Horários disponíveis conforme agenda",
            "telefone": "(61) 3411-1221",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Pal%C3%A1cio_do_Planalto_2010.jpg/1200px-Pal%C3%A1cio_do_Planalto_2010.jpg"
        },
        {
            "nome": "Ponte JK",
            "descricao": (
                "A Ponte Juscelino Kubitschek, também conhecida como Ponte JK, é uma das mais belas e arrojadas construções de Brasília. Com seus três arcos assimétricos que se cruzam sobre o Lago Paranoá, a ponte é uma obra-prima da arquitetura e da engenharia. À noite, a iluminação cênica realça ainda mais a sua beleza, tornando-a um dos cartões-postais da cidade. É um local muito procurado para caminhadas, corridas e passeios de bicicleta, oferecendo vistas espetaculares do lago e do pôr do sol."
            ),
            "categoria": "Arquitetura",
            "endereco": "Ponte Juscelino Kubitschek, Lago Sul, Brasília - DF, 71680-000",
            "horario_funcionamento": "Acesso livre 24 horas",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Ponte_JK_Bras%C3%ADlia_2010.jpg/1200px-Ponte_JK_Bras%C3%ADlia_2010.jpg"
        },
        {
            "nome": "Quartel General do Exército",
            "descricao": (
                "O Quartel General do Exército é um complexo arquitetônico projetado por Oscar Niemeyer, composto por 10 edifícios e uma grande estrutura em forma de concha que simboliza o punho da espada de Duque de Caxias. O local é a sede do Comando do Exército Brasileiro e pode ser visitado mediante agendamento prévio. A visita oferece uma visão da história militar do Brasil e da arquitetura de Niemeyer, incluindo o monumento ao Marechal Caxias e os jardins projetados por Burle Marx."
            ),
            "categoria": "Arquitetura",
            "endereco": "Avenida do Exército, s/n, Setor de Garagens, SMU, Brasília - DF, 70630-901",
            "horario_funcionamento": "Visitas guiadas às quintas-feiras, às 14h. Agendamento obrigatório com 5 dias de antecedência via https://visitaqgex.eb.mil.br/agendamento. Limite de 20 vagas por visita",
            "telefone": "(61) 3415-5151",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Quartel_General_do_Ex%C3%A9rcito_Bras%C3%ADlia.jpg/1200px-Quartel_General_do_Ex%C3%A9rcito_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Pier 21",
            "descricao": (
                "O Pier 21 é um shopping e complexo de entretenimento localizado às margens do Lago Paranoá. Além de sua ampla variedade de restaurantes e bares, o local oferece diversas opções de lojas, serviços e espaços de convivência, tornando-se um destino ideal para compras, lazer e entretenimento. Com vista privilegiada do lago e da Ponte JK, o Pier 21 combina experiências de consumo, gastronomia e eventos em um ambiente agradável e moderno."
            ),
            "categoria": "Compras",
            "endereco": "SHTN Trecho 2, Lote 1, Asa Norte, Brasília - DF, 70800-200",
            "horario_funcionamento": "Horários variam por estabelecimento. Geralmente abertos todos os dias, das 11h à 0h",
            "telefone": "(61) 3426-2121",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Pier_21_Bras%C3%ADlia.jpg/1200px-Pier_21_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Brasília Shopping",
            "descricao": (
                "O Brasília Shopping é um dos shoppings mais completos da capital, com uma grande variedade de lojas, restaurantes, cinemas e serviços. Localizado na Asa Norte, o shopping atrai um público diversificado e oferece opções para todos os gostos e bolsos. O Brasília Shopping também conta com uma praça de eventos, teatro e um espaço kids para entretenimento infantil. Com mais de 150 lojas, é um dos principais centros de compras e lazer da cidade."
            ),
            "categoria": "Compras",
            "endereco": "SCN Quadra 05, Bloco A, Asa Norte, Brasília - DF, 70715-900",
            "horario_funcionamento": "Lojas: Segunda a sábado, 10h às 22h. Domingo, 13h às 19h. Alimentação e lazer: Segunda a domingo, 10h às 22h",
            "telefone": "(61) 2109-2122",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Bras%C3%ADlia_Shopping_fachada.jpg/1200px-Bras%C3%ADlia_Shopping_fachada.jpg"
        },
        {
            "nome": "Casa Park",
            "descricao": (
                "O Casa Park é um shopping center diferenciado, com um conceito de open mall que integra lojas, restaurantes e áreas de lazer ao ar livre. Com uma arquitetura moderna e sustentável, o shopping oferece uma experiência de compras agradável e relaxante. O Casa Park também conta com uma praça de alimentação gourmet, cinema, espaços para eventos culturais e pet friendly. É um dos shoppings mais charmosos de Brasília, com foco em design, decoração e gastronomia de qualidade."
            ),
            "categoria": "Compras",
            "endereco": "SGCV Sul, Lote 22, Guará, Brasília - DF, 71215-100",
            "horario_funcionamento": "Lojas: Segunda a sábado, 10h às 22h. Domingo, 12h às 20h. Cinema e gastronomia: Horários estendidos",
            "telefone": "(61) 3364-8300",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Casa_Park_Shopping_Bras%C3%ADlia.jpg/1200px-Casa_Park_Shopping_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Conjunto Nacional",
            "descricao": (
                "O Conjunto Nacional é o primeiro shopping center de Brasília, inaugurado em 1971. Com uma arquitetura modernista, o shopping é um marco histórico da cidade e abriga uma grande variedade de lojas, restaurantes, cinemas e serviços. O Conjunto Nacional também é conhecido por sua localização privilegiada, no coração da Asa Norte, e por sua importância cultural e comercial para Brasília. É um ponto de encontro tradicional dos brasilienses e oferece desde lojas populares até marcas de luxo."
            ),
            "categoria": "Compras",
            "endereco": "SDN, Conjunto A, Asa Norte, Brasília - DF, 70040-020",
            "horario_funcionamento": "Lojas: Segunda a sábado, 9h às 22h. Domingo e feriados, 14h às 20h. Alimentação: Segunda a sábado, 9h às 22h. Domingo, 12h às 20h",
            "telefone": "(61) 2106-9700",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Conjunto_Nacional_Bras%C3%ADlia.jpg/1200px-Conjunto_Nacional_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Feira da Torre de TV",
            "descricao": (
                "Localizada no térreo da Torre de TV, a Feira de Artesanato e Comidas Típicas é uma das mais tradicionais de Brasília. A feira reúne dezenas de barracas que vendem artesanato local, roupas, produtos coloniais, móveis, acessórios e uma grande variedade de comidas típicas de todo o Brasil. É um ótimo local para comprar lembrancinhas, provar a culinária regional, conhecer o trabalho de artesãos locais e vivenciar a cultura popular da capital. A feira é permanente e funciona ao longo da semana."
            ),
            "categoria": "Compras",
            "endereco": "Eixo Monumental, s/n, Torre de TV (térreo), Brasília - DF, 70070-300",
            "horario_funcionamento": "Terça a sexta-feira, 9h às 17h. Sábado, domingo e feriados, 9h às 18h",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Feira_Torre_TV_Bras%C3%ADlia.jpg/1200px-Feira_Torre_TV_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Feira dos Importados de Brasília (FIB)",
            "descricao": (
                "A Feira dos Importados de Brasília (FIB) é uma das maiores feiras de produtos importados da América Latina. Com mais de 1.000 lojas, a feira oferece uma enorme variedade de produtos, desde eletrônicos e roupas até brinquedos, artigos de decoração, acessórios e muito mais. É um local muito procurado para compras de produtos importados a preços competitivos, e atrai visitantes de todo o Brasil. A feira gera milhares de empregos diretos e indiretos e é reconhecida pela variedade e qualidade dos produtos oferecidos."
            ),
            "categoria": "Compras",
            "endereco": "SIA Trecho 7, Guará, Brasília - DF, 71200-010",
            "horario_funcionamento": "Terça a domingo, 9h às 18h. Em dezembro funciona todos os dias com horários especiais",
            "telefone": "(61) 3383-7070",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Feira_Importados_Bras%C3%ADlia.jpg/1200px-Feira_Importados_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "ParkShopping",
            "descricao": (
                "Um dos maiores e mais completos shoppings de Brasília, o ParkShopping oferece uma vasta gama de lojas, restaurantes e opções de entretenimento. Com mais de 400 lojas, o shopping atrai um público diversificado em busca de moda, tecnologia e gastronomia. Além das lojas, o shopping conta com um complexo de cinemas, teatro, pista de patinação no gelo e diversas opções de lazer para toda a família. É um dos principais destinos de compras e entretenimento da capital."
            ),
            "categoria": "Compras",
            "endereco": "SAI/SO Área 6580, Guará, Brasília - DF, 71219-900",
            "horario_funcionamento": "Lojas: Segunda a sábado, 10h às 22h. Domingo, 14h às 20h. Alimentação: Segunda a sábado, 10h às 22h. Domingo, 12h às 22h",
            "telefone": "(61) 3362-1300",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/ParkShopping_Bras%C3%ADlia.jpg/1200px-ParkShopping_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Pátio Brasil Shopping",
            "descricao": (
                "O Pátio Brasil Shopping é um dos principais centros de compras de Brasília, localizado no coração da Asa Sul. Com uma grande variedade de lojas de moda, eletrônicos, livrarias e serviços, o shopping atrai um público diversificado. O Pátio Brasil também conta com uma praça de alimentação com diversas opções gastronômicas, cinemas, teatro e espaços para eventos culturais. É um ponto de encontro tradicional dos brasilienses e oferece conveniência e diversidade em um só lugar."
            ),
            "categoria": "Compras",
            "endereco": "SCS Quadra 7, Bloco A, Asa Sul, Brasília - DF, 70307-902",
            "horario_funcionamento": "Lojas: Segunda a sábado, 10h às 22h. Domingo, 13h às 19h. Alimentação e lazer: Segunda a sábado, 10h às 22h. Domingo, 12h às 20h",
            "telefone": "(61) 2107-7400",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/P%C3%A1tio_Brasil_Shopping.jpg/1200px-P%C3%A1tio_Brasil_Shopping.jpg"
        },
        {
            "nome": "Shopping Iguatemi Brasília",
            "descricao": (
                "O Shopping Iguatemi Brasília é um dos shoppings mais sofisticados da capital, oferecendo uma seleção exclusiva de lojas de marcas nacionais e internacionais de luxo. Com uma arquitetura moderna e um ambiente agradável, o shopping conta com restaurantes de alta gastronomia, cinemas e espaços para eventos. É um destino ideal para quem busca compras de luxo, entretenimento de qualidade e experiências premium. O shopping está localizado no Lago Norte e atrai um público exigente."
            ),
            "categoria": "Compras",
            "endereco": "SHIN CA 4, Lote A, Lago Norte, Brasília - DF, 71503-504",
            "horario_funcionamento": "Lojas: Segunda a sábado, 10h às 22h. Domingo, 14h às 20h. Alimentação: Horários estendidos",
            "telefone": "(61) 3577-1000",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Shopping_Iguatemi_Bras%C3%ADlia.jpg/1200px-Shopping_Iguatemi_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Biblioteca Nacional de Brasília",
            "descricao": (
                "A Biblioteca Nacional de Brasília, projetada por Oscar Niemeyer, faz parte do Complexo Cultural da República. Com um acervo de mais de 300 mil volumes, a biblioteca é um importante centro de pesquisa e leitura. O edifício possui uma arquitetura moderna e minimalista, com grandes janelas que permitem a entrada de luz natural. A biblioteca também oferece exposições, eventos culturais, oficinas e atividades educativas. É um espaço democrático e acessível a todos os públicos, promovendo a leitura e o acesso à cultura."
            ),
            "categoria": "Cultura",
            "endereco": "Setor Cultural Sul, Lote 2, Esplanada dos Ministérios, Brasília - DF, 70070-150",
            "horario_funcionamento": "Segunda a sexta, 8h às 20h. Sábado e domingo, 8h às 14h. Fechada em feriados",
            "telefone": "(61) 3325-6165",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Biblioteca_Nacional_Bras%C3%ADlia.jpg/1200px-Biblioteca_Nacional_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Centro Cultural Banco do Brasil (CCBB)",
            "descricao": (
                "O CCBB de Brasília é um dos mais importantes espaços culturais da cidade. Com uma programação diversificada que inclui exposições de arte, peças de teatro, sessões de cinema e shows musicais, o CCBB atrai um público variado. O edifício, projetado por Oscar Niemeyer, é uma atração à parte, com seus jardins e espaços de convivência. O CCBB é um local vibrante e dinâmico, que oferece sempre novas experiências culturais aos seus visitantes. Há van gratuita saindo da Biblioteca Nacional de quinta a domingo."
            ),
            "categoria": "Cultura",
            "endereco": "SCES, Trecho 2, Lote 22, Asa Sul, Brasília - DF, 70200-002",
            "horario_funcionamento": "Terça a domingo, 9h às 21h",
            "telefone": "(61) 3108-7600",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/CCBB_Bras%C3%ADlia.jpg/1200px-CCBB_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Concha Acústica de Brasília",
            "descricao": (
                "A Concha Acústica de Brasília é um espaço ao ar livre dedicado a shows e eventos culturais. Localizada às margens do Lago Paranoá, ao lado do Museu de Arte de Brasília (MAB), a concha oferece uma vista privilegiada do lago e da cidade. Projetada por Oscar Niemeyer e inaugurada em 1969, foi o primeiro grande palco da cidade. Com uma programação variada que inclui shows de música, festivais e eventos comunitários, a Concha Acústica é um local democrático e acessível para todos os públicos."
            ),
            "categoria": "Cultura",
            "endereco": "SCE Trecho Enseada 01, projeto Orla, polo 03, lote 20, Brasília - DF, 70800-200",
            "horario_funcionamento": "Aberta à visitação diariamente, 9h às 18h. Eventos conforme programação específica",
            "telefone": "(61) 3306-1375",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Concha_Ac%C3%BAstica_Bras%C3%ADlia.jpg/1200px-Concha_Ac%C3%BAstica_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Espaço Lúcio Costa",
            "descricao": (
                "O Espaço Lúcio Costa é um museu subterrâneo localizado na Praça dos Três Poderes, dedicado ao urbanista Lúcio Costa, idealizador do Plano Piloto de Brasília. O museu abriga uma maquete gigante da cidade, que mostra o projeto urbanístico original, além de exposições sobre a história da construção de Brasília e a visão de Lúcio Costa para a capital. É um local essencial para compreender o planejamento urbano único de Brasília e sua importância histórica e arquitetônica."
            ),
            "categoria": "Cultura",
            "endereco": "Praça dos Três Poderes, s/n, Esplanada dos Ministérios, Brasília - DF, 70100-000",
            "horario_funcionamento": "Terça a domingo, 9h às 18h",
            "telefone": "(61) 3325-6244",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Espa%C3%A7o_L%C3%BAcio_Costa.jpg/1200px-Espa%C3%A7o_L%C3%BAcio_Costa.jpg"
        },
        {
            "nome": "Memorial JK",
            "descricao": (
                "O Memorial JK é um museu, mausoléu e centro cultural dedicado ao presidente Juscelino Kubitschek, fundador de Brasília. O edifício, projetado por Oscar Niemeyer, abriga o sarcófago de JK, uma biblioteca com seu acervo pessoal, e uma exposição permanente sobre sua vida e obra. O memorial é um local de grande importância histórica e cultural para a cidade, e oferece uma visão aprofundada sobre a construção de Brasília e a trajetória de seu idealizador. Pagamento exclusivamente em dinheiro."
            ),
            "categoria": "Cultura",
            "endereco": "Eixo Monumental, Lado Oeste, Praça do Cruzeiro, Brasília - DF, 70070-300",
            "horario_funcionamento": "Terça a domingo, 9h às 18h",
            "telefone": "(61) 3226-7860",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Memorial_JK_Bras%C3%ADlia.jpg/1200px-Memorial_JK_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Memorial dos Povos Indígenas",
            "descricao": (
                "O Memorial dos Povos Indígenas é um museu dedicado à preservação e divulgação da cultura indígena brasileira. Projetado por Oscar Niemeyer, o edifício tem formato de uma oca e abriga um rico acervo de artefatos, artesanato e objetos sagrados de diversas etnias indígenas. O memorial é um importante espaço de valorização e respeito à cultura dos povos originários do Brasil. Oferece exposições permanentes e temporárias, além de atividades educativas e visitas guiadas para escolas públicas."
            ),
            "categoria": "Cultura",
            "endereco": "Eixo Monumental Oeste, s/n, Brasília - DF, 70070-300",
            "horario_funcionamento": "Terça a domingo, 9h às 17h. Entrada franca",
            "telefone": "(61) 3344-9272",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Memorial_Povos_Ind%C3%ADgenas_Bras%C3%ADlia.jpg/1200px-Memorial_Povos_Ind%C3%ADgenas_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Museu Histórico de Brasília",
            "descricao": (
                "O Museu Histórico de Brasília, também conhecido como Museu da Cidade, é o museu mais antigo da capital, inaugurado em 21 de abril de 1960. Localizado na Praça dos Três Poderes, o museu possui uma exposição permanente com inscrições históricas sobre a construção de Brasília e os principais eventos que marcaram a história da cidade. O museu é um local de grande importância histórica e cultural para Brasília, preservando a memória da fundação da capital."
            ),
            "categoria": "Cultura",
            "endereco": "Praça dos Três Poderes, s/n, Esplanada dos Ministérios, Brasília - DF, 70100-000",
            "horario_funcionamento": "Terça a domingo, 9h às 18h. Entrada franca",
            "telefone": "(61) 3325-6244",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Museu_Hist%C3%B3rico_Bras%C3%ADlia.jpg/1200px-Museu_Hist%C3%B3rico_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Museu Nacional da República",
            "descricao": (
                "O Museu Nacional da República, com sua cúpula branca projetada por Oscar Niemeyer, é um dos principais espaços para exposições de arte e cultura em Brasília. O museu faz parte do Complexo Cultural da República, juntamente com a Biblioteca Nacional de Brasília. O espaço recebe exposições itinerantes de artistas brasileiros e estrangeiros, além de mostras de seu acervo permanente. É um dos cartões-postais mais icônicos da capital federal."
            ),
            "categoria": "Cultura",
            "endereco": "Setor Cultural Sul, Lote 2, Esplanada dos Ministérios, Brasília - DF, 70070-150",
            "horario_funcionamento": "Terça a domingo, 9h às 18h30. Entrada gratuita",
            "telefone": "(61) 3325-5220",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Museu_Nacional_Rep%C3%BAblica_Bras%C3%ADlia.jpg/1200px-Museu_Nacional_Rep%C3%BAblica_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Museu Vivo da Memória Candanga",
            "descricao": (
                "O Museu Vivo da Memória Candanga é dedicado à preservação da memória dos trabalhadores que construíram Brasília, conhecidos como 'candangos'. Instalado no antigo Hospital Juscelino Kubitschek de Oliveira, o primeiro hospital construído no novo Distrito Federal, o museu possui um acervo com fotografias, documentos e objetos que contam a história da construção da capital. É um local emocionante e educativo, que homenageia os heróis anônimos de Brasília e preserva o berço da construção da cidade."
            ),
            "categoria": "Cultura",
            "endereco": "Lote D, Setor Juscelino Kubitschek, Núcleo Bandeirante, Brasília - DF, 71739-020",
            "horario_funcionamento": "Segunda a sábado, 9h às 17h. Entrada gratuita",
            "telefone": "(61) 3301-3590",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Museu_Vivo_Mem%C3%B3ria_Candanga.jpg/1200px-Museu_Vivo_Mem%C3%B3ria_Candanga.jpg"
        },
        {
            "nome": "Museu de Arte de Brasília (MAB)",
            "descricao": (
                "O Museu de Arte de Brasília (MAB) possui um acervo com mais de 1.300 obras, incluindo pinturas, gravuras, esculturas, fotografias e desenhos de artistas brasileiros. O museu tem como foco a arte moderna e contemporânea, e realiza exposições temporárias e permanentes que valorizam a produção artística nacional. O MAB está localizado às margens do Lago Paranoá, ao lado da Concha Acústica, em uma área privilegiada de lazer e cultura. Foi o segundo prédio construído em Brasília."
            ),
            "categoria": "Cultura",
            "endereco": "SHTN, Trecho 1, Projeto Orla, polo 3, lote 5, Brasília - DF, 70800-200",
            "horario_funcionamento": "Quarta a segunda, 10h às 19h. Fechado às terças. Entrada gratuita",
            "telefone": "(61) 3306-1375",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Museu_Arte_Bras%C3%ADlia_MAB.jpg/1200px-Museu_Arte_Bras%C3%ADlia_MAB.jpg"
        },
        {
            "nome": "Museu de Valores do Banco Central",
            "descricao": (
                "O Museu de Valores do Banco Central é um museu dedicado à história do dinheiro no Brasil. O acervo inclui cédulas e moedas antigas, barras de ouro, e exposições interativas sobre a economia brasileira. O museu é uma atração educativa e interessante, que oferece uma visão única sobre a história econômica do país. A entrada é gratuita. ATENÇÃO: O museu está temporariamente fechado para reforma. Consulte o site oficial do Banco Central para informações sobre reabertura."
            ),
            "categoria": "Cultura",
            "endereco": "SBS Quadra 3, Bloco B, 1º Subsolo, Asa Sul, Brasília - DF, 70074-900",
            "horario_funcionamento": "Temporariamente fechado para reforma. Horário normal: Terça a sexta, 10h às 18h. Fechado sábados, domingos e feriados",
            "telefone": "(61) 3414-2093",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Museu_Valores_Banco_Central.jpg/1200px-Museu_Valores_Banco_Central.jpg"
        },
        {
            "nome": "Panteão da Pátria Tancredo Neves",
            "descricao": (
                "O Panteão da Pátria é um memorial dedicado aos heróis nacionais do Brasil. Localizado na Praça dos Três Poderes, o edifício em forma de pomba, projetado por Oscar Niemeyer, abriga o Livro de Aço, onde estão inscritos os nomes dos heróis da pátria. O local também possui um museu com exposições sobre a história do Brasil e seus personagens mais importantes. Faz parte do Centro Cultural Três Poderes, juntamente com o Espaço Lúcio Costa e o Museu Histórico de Brasília."
            ),
            "categoria": "Cultura",
            "endereco": "Praça dos Três Poderes, s/n, Esplanada dos Ministérios, Brasília - DF, 70100-000",
            "horario_funcionamento": "Terça a domingo, 9h às 18h. Entrada gratuita",
            "telefone": "(61) 3325-6244",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Pante%C3%A3o_P%C3%A1tria_Bras%C3%ADlia.jpg/1200px-Pante%C3%A3o_P%C3%A1tria_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Planetário de Brasília",
            "descricao": (
                "O Planetário de Brasília é um espaço dedicado à divulgação científica e à astronomia. Com uma cúpula de 14 metros de diâmetro, o planetário oferece sessões de projeção do céu estrelado e filmes educativos sobre o universo. É um local ideal para famílias com crianças e para quem tem interesse em aprender mais sobre os astros e os mistérios do cosmos. A entrada é gratuita, mas requer registro na chegada. O planetário possui dois níveis de exposições interativas."
            ),
            "categoria": "Cultura",
            "endereco": "Eixo Monumental, s/n, Setor de Divulgação Cultural, Brasília - DF, 70070-300",
            "horario_funcionamento": "Terça a domingo, 7h30 às 19h. Sessões na Cúpula: Terça a sexta 18h. Sábado, domingo e feriados: 11h, 14h30, 16h, 17h e 18h. Entrada gratuita",
            "telefone": "(61) 3225-7114",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Planet%C3%A1rio_Bras%C3%ADlia.jpg/1200px-Planet%C3%A1rio_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Teatro Nacional Claudio Santoro",
            "descricao": (
                "O Teatro Nacional Claudio Santoro é o principal teatro de Brasília e um dos mais importantes do Brasil. Projetado por Oscar Niemeyer, o teatro possui três salas de espetáculos (Villa-Lobos, Martins Pena e Alberto Nepomuceno) e recebe uma programação diversificada que inclui óperas, balés, concertos e peças de teatro. A arquitetura do teatro, com sua forma piramidal e jardins internos, é uma atração à parte. É considerado um dos teatros mais importantes da América Latina."
            ),
            "categoria": "Cultura",
            "endereco": "SCTS - Plano Piloto, Brasília - DF, 70297-400",
            "horario_funcionamento": "Varia de acordo com a programação. Bilheteria e visitação geralmente terça a domingo",
            "telefone": "(61) 3325-6239",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Teatro_Nacional_Bras%C3%ADlia.jpg/1200px-Teatro_Nacional_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Centros Olímpicos e Paralímpicos",
            "descricao": (
                "Os Centros Olímpicos e Paralímpicos de Brasília são espaços públicos dedicados à prática de esportes e atividades físicas. Com uma estrutura completa que inclui quadras poliesportivas, piscinas, academias e pistas de atletismo, os centros oferecem aulas gratuitas de diversas modalidades esportivas. É um local ideal para quem busca saúde, bem-estar e integração social através do esporte. O Distrito Federal possui múltiplas unidades distribuídas em diversas regiões administrativas."
            ),
            "categoria": "Esportes e Lazer",
            "endereco": "Diversas localidades no Distrito Federal.",
            "horario_funcionamento": "Varia por unidade. Geralmente segunda a sexta, 6h às 22h. Sábado e domingo, 8h às 18h",
            "telefone": "(61) 4042-1828",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Centros_Ol%C3%ADmpicos_Bras%C3%ADlia.jpg/1200px-Centros_Ol%C3%ADmpicos_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Ciclovia do Lago Paranoá",
            "descricao": (
                "A Ciclovia do Lago Paranoá é uma das mais belas ciclovias de Brasília, contornando todo o lago e oferecendo vistas espetaculares da cidade. Com mais de 40 km de extensão, a ciclovia é ideal para passeios de bicicleta, corridas e caminhadas. Ao longo do percurso, há diversos pontos de parada com bares, restaurantes e áreas de descanso. É um local muito procurado para atividades físicas e lazer ao ar livre, proporcionando contato direto com a natureza e paisagens únicas do cerrado."
            ),
            "categoria": "Esportes e Lazer",
            "endereco": "Ciclovia que contorna o Lago Paranoá, passando por Asa Sul, Lago Sul, Asa Norte e outras regiões, Brasília - DF",
            "horario_funcionamento": "Acesso livre 24 horas",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Ciclovia_Lago_Parano%C3%A1_Bras%C3%ADlia.jpg/1200px-Ciclovia_Lago_Parano%C3%A1_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Estádio Nacional Mané Garrincha",
            "descricao": (
                "Palco de grandes eventos esportivos e shows, o Estádio Nacional Mané Garrincha (também conhecido como Arena BRB) é uma das arenas mais modernas do Brasil. Com capacidade para mais de 70 mil pessoas, o estádio foi palco de jogos da Copa do Mundo de 2014 e das Olimpíadas de 2016. Além dos eventos esportivos e shows, o estádio oferece visitas guiadas, onde é possível conhecer os bastidores, vestiários e a história do local. É um dos principais cartões-postais de Brasília."
            ),
            "categoria": "Esportes e Lazer",
            "endereco": "SRPN (Setor de Recreação Pública Norte), Asa Norte, Brasília - DF, 70070-701",
            "horario_funcionamento": "Visitas guiadas geralmente aos sábados (consultar disponibilidade). Eventos conforme programação",
            "telefone": "(61) 3321-2002",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Est%C3%A1dio_Man%C3%A9_Garrincha_Bras%C3%ADlia.jpg/1200px-Est%C3%A1dio_Man%C3%A9_Garrincha_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Lago Paranoá",
            "descricao": (
                "O Lago Paranoá é um grande lago artificial que foi criado durante a construção de Brasília para melhorar a umidade do ar na capital. Hoje, o lago é um dos principais locais de lazer da cidade, onde é possível praticar esportes náuticos como stand-up paddle, caiaque, vela e jet ski. As margens do lago abrigam diversos bares, restaurantes, clubes e áreas de lazer, além de uma extensa ciclovia que contorna toda a sua orla. O lago possui aproximadamente 38 km² de área e é um dos símbolos de Brasília."
            ),
            "categoria": "Esportes e Lazer",
            "endereco": "Lago Paranoá, contornando Lago Sul, Lago Norte, Asa Sul, Asa Norte e outras regiões, Brasília - DF",
            "horario_funcionamento": "Acesso livre 24 horas",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Lago_Parano%C3%A1_Bras%C3%ADlia.jpg/1200px-Lago_Parano%C3%A1_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Chicago Prime",
            "descricao": (
                "O Chicago Prime é uma churrascaria premium especializada em carnes nobres e cortes especiais. Com um ambiente sofisticado e um serviço de primeira linha, o restaurante oferece um rodízio de carnes de alta qualidade, além de um buffet de saladas e acompanhamentos. O Chicago Prime também conta com uma adega com vinhos selecionados, sendo uma excelente opção para almoços de negócios e jantares especiais. Possui múltiplas unidades em Brasília, incluindo Asa Sul, Lago Sul e shoppings."
            ),
            "categoria": "Gastronomia",
            "endereco": "CLS 114, Bloco A, Loja 48, Asa Sul, Brasília - DF, 70377-510",
            "horario_funcionamento": "Todos os dias, 12h às 15h e 19h às 23h",
            "telefone": "(61) 3256-2187",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Chicago_Prime_Bras%C3%ADlia.jpg/1200px-Chicago_Prime_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Coco Bambu Lago",
            "descricao": (
                "Um dos restaurantes mais renomados de Brasília, o Coco Bambu é especializado em frutos do mar. Com um cardápio variado que inclui camarões, peixes, lagostas e moquecas, o restaurante é uma excelente opção para um almoço ou jantar especial. O ambiente é sofisticado e aconchegante, localizado no Ícone Parque, próximo ao Lago Paranoá. O Coco Bambu é conhecido por seus pratos generosos, drinks especiais e atendimento de qualidade. Possui também outras unidades em Brasília."
            ),
            "categoria": "Gastronomia",
            "endereco": "SCES Trecho 2, Conjunto 36, Ícone Parque, Asa Sul, Brasília - DF, 70200-002",
            "horario_funcionamento": "Segunda a quinta, 11h30 às 15h30 e 17h à 00h. Sexta a domingo, 11h30 à 00h",
            "telefone": "(61) 3224-5585",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Coco_Bambu_Bras%C3%ADlia.jpg/1200px-Coco_Bambu_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Dom Francisco Restaurante",
            "descricao": (
                "O Dom Francisco é um restaurante tradicional de Brasília, fundado em 1988 pelo chef Francisco Ansiliero. A casa é conhecida por sua culinária afetiva, que inclui pratos como picanha na brasa, tambaqui amazônico e diversas receitas de bacalhau. Possui duas unidades na cidade, uma na 402 Sul e outra na ASBAC, que oferece vista para o Lago Paranoá. A carta de vinhos do restaurante é uma das mais respeitadas do Brasil."
            ),
            "categoria": "Gastronomia",
            "endereco": "CLS 402 Bloco B, Lojas 9 a 15, Brasília - DF, 70236-050",
            "horario_funcionamento": "O Dom Francisco está aberto para recebê-lo de segunda a sexta-feira para o almoço (das 11h30 às 15h30) e o jantar (das 19h00 à meia-noite). Aos sábados, o atendimento é contínuo, das 11h30 até a meia-noite, e aos domingos, vai das 11h30 às 17h00.",
            "telefone": "(61) 3224-1634",
            "imagem_url": "https://media-cdn.tripadvisor.com/media/photo-o/1a/e0/b0/3b/dom-francisco.jpg"
        },
        {
            "nome": "New Koto",
            "descricao": (
                "O New Koto é um dos restaurantes japoneses mais tradicionais e conceituados de Brasília, localizado na 212 Sul. Reconhecido pela qualidade e autenticidade de sua culinária japonesa, o restaurante oferece desde sushis e sashimis frescos até pratos quentes tradicionais (teishoku). O New Koto é conhecido por manter os padrões da culinária japonesa autêntica, sendo frequentemente recomendado como um dos melhores sushis de Brasília. O ambiente é acolhedor e o restaurante participa de eventos gastronômicos importantes, como a Semana do Japão Gastronômico."
            ),
            "categoria": "Gastronomia",
            "endereco": "CLS 212, Bloco C, Loja 20, Asa Sul, Brasília - DF, 70275-530",
            "horario_funcionamento": "Terça a sábado, 12h às 15h e 19h às 22h. Domingo, 12h às 15h. Fechado às segundas-feiras",
            "telefone": "(61) 3346-9668",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/New_Koto_Bras%C3%ADlia.jpg/1200px-New_Koto_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Fogo de Chão",
            "descricao": (
                "O Fogo de Chão é uma churrascaria de renome internacional, conhecida por sua carne de alta qualidade e serviço impecável. Com um rodízio de carnes nobres preparadas no estilo gaúcho, o restaurante oferece uma experiência gastronômica completa, com um buffet de saladas, acompanhamentos quentes e uma adega com vinhos selecionados. O ambiente é sofisticado e acolhedor, ideal para almoços de negócios ou jantares especiais. A marca é reconhecida mundialmente e possui unidades em diversos países."
            ),
            "categoria": "Gastronomia",
            "endereco": "SCES Trecho 2, Lote 2/11, Asa Sul, Brasília - DF, 70200-002",
            "horario_funcionamento": "Segunda a quinta, 12h às 15h e 18h30 às 23h. Sexta e sábado, 12h às 16h e 18h30 à 0h. Domingo, 12h às 16h e 18h30 às 22h",
            "telefone": "(61) 3322-4666",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Fogo_de_Ch%C3%A3o_Bras%C3%ADlia.jpg/1200px-Fogo_de_Ch%C3%A3o_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "NAU Frutos do Mar",
            "descricao": (
                "O NAU Frutos do Mar é um dos restaurantes mais conceituados de Brasília, especializado em frutos do mar frescos e pratos da culinária mediterrânea. Com um ambiente elegante e sofisticado, o restaurante oferece um cardápio variado que inclui ostras, lagostas, peixes nobres e risotos. É uma excelente opção para um jantar romântico ou uma celebração especial. O NAU é conhecido por sua qualidade impecável e atendimento refinado."
            ),
            "categoria": "Gastronomia",
            "endereco": "SCLS 109, Bloco A, Loja 1/2, Asa Sul, Brasília - DF, 70347-510",
            "horario_funcionamento": "Segunda a quinta, 12h às 15h e 19h às 23h. Sexta e sábado, 12h às 16h e 19h à 0h. Domingo, 12h às 16h e 19h às 22h",
            "telefone": "(61) 3443-9999",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/NAU_Frutos_do_Mar_Bras%C3%ADlia.jpg/1200px-NAU_Frutos_do_Mar_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Restaurante Mangai",
            "descricao": (
                "O Mangai é um dos restaurantes mais famosos de Brasília, conhecido por sua culinária nordestina farta e saborosa. Com um buffet variado que inclui pratos como carne de sol, baião de dois, tapioca, e uma grande variedade de saladas e sobremesas típicas, o Mangai atrai um público diversificado. O ambiente é rústico e acolhedor, decorado com elementos que remetem ao Nordeste brasileiro. O restaurante é uma ótima opção para um almoço em família ou um jantar com amigos, oferecendo uma verdadeira experiência da cultura nordestina."
            ),
            "categoria": "Gastronomia",
            "endereco": "SCES Trecho 2, Lote 2, Asa Sul, Brasília - DF, 70200-002",
            "horario_funcionamento": "Segunda a domingo, 12h às 15h e 18h às 22h",
            "telefone": "(61) 3224-3079",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Restaurante_Mangai_Bras%C3%ADlia.jpg/1200px-Restaurante_Mangai_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Rubaiyat Brasília",
            "descricao": (
                "O Rubaiyat é um dos restaurantes mais sofisticados de Brasília, especializado em carnes nobres e vinhos de alta qualidade. Com um ambiente elegante e um serviço impecável, o restaurante oferece cortes especiais de carne bovina, cordeiro e frutos do mar. O Rubaiyat é uma excelente opção para jantares românticos, celebrações e almoços de negócios."
            ),
            "categoria": "Gastronomia",
            "endereco": "SHS Quadra 5, Bloco H - Asa Sul, Brasília - DF, 70322-900",
            "horario_funcionamento": "Segunda a sexta, das 12h às 15h e das 19h às 23h. Sábado, das 12h às 16h e das 19h à 0h. Domingo, das 12h às 16h.",
            "telefone": "(61) 3322-4747",
            "imagem_url": "https://media-cdn.tripadvisor.com/media/photo-o/1a/e0/b0/3b/rubaiyat-brasilia.jpg"
        },
        {
            "nome": "Mezanino",
            "descricao": (
                "O Mezanino é um rooftop gastronômico localizado na Torre de TV de Brasília, a 75 metros de altura, oferecendo uma das vistas mais privilegiadas da capital. O espaço combina gastronomia criativa, alta coquetelaria, música ao vivo e happy hour em um ambiente sofisticado. O menu à la carte apresenta entradas, pratos principais e sobremesas autorais, além de drinks exclusivos criados pela mixologista da casa. O Golden Hour (quarta a sábado) oferece 50% OFF em drinks selecionados. O Mezanino também abriga exposições de arte e eventos culturais, tornando-se um ponto de encontro para quem busca cultura, gastronomia e uma vista espetacular de Brasília."
            ),
            "categoria": "Gastronomia",
            "endereco": "Torre de TV de Brasília, Eixo Monumental, Brasília - DF, 70070-300",
            "horario_funcionamento": "Segunda e domingo, 11h30 às 16h. Terça a sábado, 11h30 às 15h30 e 17h30 à 0h",
            "telefone": "Consultar via Instagram @meza.nino",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Mezanino_Torre_TV_Bras%C3%ADlia.jpg/1200px-Mezanino_Torre_TV_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Restaurante Careca",
            "descricao": (
                "O Restaurante Careca é o restaurante chinês mais tradicional de Brasília, em atividade desde 1982. Com múltiplas unidades na Asa Norte, o estabelecimento é reconhecido pela autenticidade de sua culinária chinesa e sul-asiática, com pratos feitos na hora de forma rápida e saborosa. O ambiente é simples e acolhedor, com preços acessíveis que atraem tanto moradores locais quanto visitantes. O Careca é uma referência para quem busca comida chinesa tradicional e de qualidade em Brasília, mantendo há mais de 40 anos os padrões que conquistaram gerações de clientes."
            ),
            "categoria": "Gastronomia",
            "endereco": "CLN 407, Bloco B, Loja 1, Asa Norte, Brasília - DF, 70847-520",
            "horario_funcionamento": "Segunda a sexta, 11h30 às 15h e 18h às 22h30. Sábado e domingo, 11h30 às 15h30 e 19h às 22h30",
            "telefone": "(61) 3274-3291",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Restaurante_Careca_Bras%C3%ADlia.jpg/1200px-Restaurante_Careca_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Marzuk Empório Árabe",
            "descricao": (
                "O Marzuk Empório Árabe é uma referência em culinária árabe tradicional em Brasília, com receitas de família feitas artesanalmente. Com múltiplas unidades (Asa Sul, Asa Norte e Sudoeste), o Marzuk oferece uma ampla variedade de pratos árabes autênticos, incluindo esfihás, quibes, kaftas, homus, babaganuche e sobremesas típicas. O ambiente é acolhedor e familiar, refletindo a tradição e o cuidado na preparação de cada prato. O Marzuk é reconhecido como um dos melhores restaurantes de culinária do Oriente Médio da capital, sendo uma escolha popular tanto para refeições rápidas quanto para celebrações especiais."
            ),
            "categoria": "Gastronomia",
            "endereco": "SHCS CL Quadra 106, Bloco B, Loja 31, Asa Sul, Brasília - DF, 70345-520",
            "horario_funcionamento": "Consultar horários por unidade via Instagram @marzukemporioarabe",
            "telefone": "(61) 3443-0329",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Marzuk_Emp%C3%B3rio_%C3%81rabe_Bras%C3%ADlia.jpg/1200px-Marzuk_Emp%C3%B3rio_%C3%81rabe_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "El Paso - Cocina Mexicana",
            "descricao": (
                "O El Paso é um dos restaurantes mexicanos mais tradicionais e queridos de Brasília, com três unidades estrategicamente localizadas. Especializado em autêntica culinária mexicana, o El Paso oferece tacos, burritos, quesadillas, fajitas, nachos e outras delícias da gastronomia do México, além de margaritas e drinks típicos. O ambiente é decorado com elementos mexicanos que transportam os clientes para uma experiência cultural completa. O restaurante é conhecido por seus temperos equilibrados, porções generosas e ambiente festivo, sendo uma escolha popular para almoços executivos e jantares em grupo."
            ),
            "categoria": "Gastronomia",
            "endereco": "SCLS 404, Bloco C, Loja 19, Asa Sul, Brasília - DF, 70235-530",
            "horario_funcionamento": "Segunda a sexta, 12h às 15h e a partir das 18h. Sábado e domingo com horários estendidos",
            "telefone": "(61) 3323-4618",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/El_Paso_Cocina_Mexicana_Bras%C3%ADlia.jpg/1200px-El_Paso_Cocina_Mexicana_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Mané Mercado",
            "descricao": (
                "O Mané Mercado, também conhecido como Mercado Vírgula, é um complexo gastronômico central, perene e plural localizado no Eixo Monumental, ao lado da Arena BRB Mané Garrincha. Com mais de 13 operações gastronômicas diferentes, o Mané reúne chefs renomados de Brasília em um único lugar, oferecendo uma diversidade impressionante de sabores: desde gelato até cuscuz, de hambúrguer a frutos do mar, de massa a churrasco. O espaço conta com brinquedoteca, é pet friendly, oferece estacionamento, possui cardápio inclusivo com 39 opções (veganas, vegetarianas, low carb, sem lactose e sem glúten), e dispõe de espaço para comemorações de aniversário. O Mané também oferece Happy Hour de segunda a sexta (15h-20h) com chopp, long neck, drinks e taças de vinho com preços especiais. É um lugar plural, para família, amigos e até para o cachorro, combinando restaurante, bar, feira, cultura, diversão e diversidade em um único ambiente vibrante."
            ),
            "categoria": "Gastronomia",
            "endereco": "SRPN Mané Mercado, ST - Asa Norte, Brasília - DF, 70070-701",
            "horario_funcionamento": "Segunda a quinta, 12h à 0h. Sexta e sábado, 11h à 1h. Domingo, 11h às 23h. Happy Hour: segunda a sexta, 15h às 20h",
            "telefone": "(61) 99576-1646",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Man%C3%A9_Mercado_Bras%C3%ADlia.jpg/1200px-Man%C3%A9_Mercado_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Madre Teresa Deli",
            "descricao": (
                "A Madre Teresa Deli se autodenomina 'a hamburgueria mais pobre do mundo' e 'a última lanchonete da galáxia', mas é reconhecida como uma das melhores hamburguerias do Brasil. Localizada em Taguatinga Sul, a casa é comandada pelo chef Daniel Larsan e se destaca por seu ambiente rústico e maltrapilho, receitas artesanais e hambúrgueres preparados na lenha. A filosofia do estabelecimento une fé, fogo e amor, com forte presença de elementos religiosos e um atendimento acolhedor. A Madre Teresa foi indicada pela Veja Comer & Beber e oferece também um café da manhã especial aos sábados (8h33 às 11h33). O ambiente é descontraído e familiar, atraindo clientes que buscam autenticidade e qualidade."
            ),
            "categoria": "Gastronomia",
            "endereco": "Taguatinga Sul, Brasília - DF (Consultar endereço completo via Instagram)",
            "horario_funcionamento": "Terça a sábado 11:30 às 22:30",
            "telefone": "Consultar via Instagram @madreteresadeli",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Madre_Teresa_Deli_Bras%C3%ADlia.jpg/1200px-Madre_Teresa_Deli_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Taypá Sabores do Peru",
            "descricao": (
                "O Taypá Sabores do Peru é um aclamado restaurante que leva os sabores vibrantes e sofisticados da autêntica culinária peruana a Brasília. Sob o comando do Chef Marco Espinoza, o Taypá oferece uma experiência gastronômica de alta qualidade, com pratos clássicos como ceviches frescos, tiraditos e especialidades regionais, celebrando a diversidade dos ingredientes andinos e litorâneos do Peru. O ambiente é elegante e moderno, ideal para quem busca uma viagem culinária inesquecível e premiada."
            ),
            "categoria": "Gastronomia",
            "endereco": "Rua de Habitações Individuais Sul QI 17 BI.G, Lj.208 - Lago Sul, Brasília - DF, 71645-500",
            "horario_funcionamento": "Todos os dias, das 11h30 às 15h e das 18h30 às 0h.",
            "telefone": "(61) 98626-0235",
            "imagem_url": "https://media-cdn.tripadvisor.com/media/photo-o/1a/e0/b0/3b/taypa-sabores-do-brasil.jpg"
        },
        {
            "nome": "Toro Parrilla",
            "descricao": (
                "O Toro Parrilla é um restaurante especializado em carnes nobres e parrilla argentina. Com um ambiente elegante e acolhedor, o restaurante oferece cortes especiais de carne bovina, cordeiro e porco, preparados na brasa. O cardápio também inclui uma seleção de vinhos argentinos e chilenos. É uma excelente opção para os amantes de carne de qualidade."
            ),
            "categoria": "Gastronomia",
            "endereco": "SHCS CLS 104 BL C Loja 29 - Asa Sul, Brasília - DF, 70297-400",
            "horario_funcionamento": "Segunda a quinta, das 12h às 15h e das 19h às 23h. Sexta e sábado, das 12h às 16h e das 19h à 0h. Domingo, das 12h às 17h",
            "telefone": "(61) 3248-1672",
            "imagem_url": "https://media-cdn.tripadvisor.com/media/photo-o/1a/e0/b0/3b/toro-parrilla.jpg"
        },
        {
            "nome": "Trattoria da Rosário",
            "descricao": (
                "A Trattoria da Rosário é um restaurante italiano tradicional, conhecido por suas massas artesanais e pratos clássicos da culinária italiana. Com um ambiente acolhedor e familiar, o restaurante oferece uma experiência gastronômica autêntica, com receitas que remetem à Itália. A Trattoria da Rosário é uma excelente opção para almoços e jantares em família."
            ),
            "categoria": "Gastronomia",
            "endereco": "SHIS QI 17 Lj.215 - Lago Sul, Brasília - DF, 71645-500",
            "horario_funcionamento": "Terça a Sabado, das 12h às 16h e das 19h às 0h. Domingo, das 12h às 17h.",
            "telefone": "(61) 3443-7461",
            "imagem_url": "https://media-cdn.tripadvisor.com/media/photo-o/1a/e0/b0/3b/trattoria-da-rosario.jpg"
        },
        {
            "nome": "Villa Tevere",
            "descricao": (
                "O Villa Tevere é um restaurante italiano de alta gastronomia, conhecido por seus pratos autênticos e pela qualidade de seus ingredientes. Com um ambiente elegante e acolhedor, o restaurante oferece massas frescas, risotos, carnes e uma seleção de vinhos italianos. O Villa Tevere é uma excelente opção para jantares românticos e celebrações especiais."
            ),
            "categoria": "Gastronomia",
            "endereco": "Asa Sul Comércio Local Sul 115 Bloco A - Asa Sul, Brasília - DF, 70385-510",
            "horario_funcionamento": "Segunda a Sabado, das 12h às 15h e das 19h às 23h. Domingo, das 12h às 16h.",
            "telefone": "(61) 98434-8541",
            "imagem_url": "https://media-cdn.tripadvisor.com/media/photo-o/1a/e0/b0/3b/villa-tevere.jpg"
        },
        {
            "nome": "Praça do Cruzeiro",
            "descricao": (
                "A Praça do Cruzeiro é um marco histórico de Brasília, onde foi celebrada a primeira missa da cidade em 3 de maio de 1957. A praça abriga uma cruz de madeira que marca o local da celebração, e é um ponto de referência importante para a história da construção da capital. A Praça do Cruzeiro oferece uma vista panorâmica da cidade e é um local de contemplação e reflexão."
            ),
            "categoria": "Mirantes",
            "endereco": "Zona Cívico-Administrativa - Srg., Brasília - DF, 70655-775",
            "horario_funcionamento": "Acesso livre 24 horas",
            "imagem_url": "https://live.staticflickr.com/65535/51237893543_33b3c3c62a_b.jpg"
        },
        {
            "nome": "Praça dos Cristais",
            "descricao": (
                "A Praça dos Cristais é um espaço público localizado no Setor Militar Urbano, conhecido por seus jardins e pela escultura 'Os Guerreiros', de Bruno Giorgi. A praça é um local tranquilo e agradável para caminhadas e contemplação. Próximo à praça, encontram-se outros monumentos e edifícios importantes de Brasília, tornando-a um ponto de partida para explorar a região."
            ),
            "categoria": "Mirantes",
            "endereco": "SMU - Setor Militar Urbano, Brasília - DF, 70630-901",
            "horario_funcionamento": "Acesso livre 24 horas",
            "imagem_url": "https://live.staticflickr.com/65535/51237893543_33b3c3c62a_b.jpg"
        },
        {
            "nome": "Torre de TV de Brasília",
            "descricao": (
                "A Torre de TV de Brasília é um dos melhores locais para se ter uma vista panorâmica da cidade. Com 224 metros de altura, a torre oferece uma visão de 360 graus do Plano Piloto, do Lago Paranoá e dos principais monumentos de Brasília. No térreo, há uma feira de artesanato e comidas típicas, que é uma atração à parte. A torre é um dos pontos turísticos mais visitados da cidade, e um local imperdível para quem quer ter uma visão completa de Brasília."
            ),
            "categoria": "Mirantes",
            "endereco": "Torre de TV de Brasília - Esplanada da Torre - Plano Piloto, Brasília - DF, 70070-300",
            "horario_funcionamento": "Terça a domingo, das 9h às 19h.",
            "telefone": "(61) 3224-3590",
            "imagem_url": "https://www.viagensecaminhos.com/wp-content/uploads/2021/01/torre-de-tv-brasilia.jpg"
        },
        {
            "nome": "Burle Marx Park",
            "descricao": (
                "O Burle Marx Park é um parque urbano projetado pelo renomado paisagista Roberto Burle Marx. Com uma área de 45 hectares, o parque possui trilhas ecológicas, lagos artificiais, jardins temáticos e uma grande diversidade de plantas nativas e exóticas. É um local ideal para caminhadas, piqueniques e para apreciar a arte do paisagismo. O parque também abriga eventos culturais e esportivos."
            ),
            "categoria": "Natureza",
            "endereco": "SMAS Trecho 4, Conjunto 4 - Águas Claras, Brasília - DF, 71919-540",
            "horario_funcionamento": "Todos os dias, das 6h às 20h.",
            "imagem_url": "https://live.staticflickr.com/65535/51237893543_33b3c3c62a_b.jpg"
        },
        {
            "nome": "Jardim Botânico de Brasília",
            "descricao": (
                "O Jardim Botânico de Brasília é um oásis de tranquilidade e natureza, dedicado à preservação do Cerrado. Com uma área de mais de 5 mil hectares, o jardim abriga uma rica diversidade de plantas nativas, trilhas ecológicas, jardins temáticos e um orquidário. É um local ideal para caminhadas, piqueniques e para aprender mais sobre a flora do Cerrado."
            ),
            "categoria": "Natureza",
            "endereco": "SMDB, Área Especial, Lago Sul - Brasília, DF, 71680-001",
            "horario_funcionamento": "Terça a domingo, das 9h às 17h.",
            "telefone": "(61) 99359-0137",
            "imagem_url": "https://www.jardimbotanico.df.gov.br/wp-content/uploads/2020/05/jardim-botanico-de-brasilia-1.jpg"
        },
        {
            "nome": "Jardim Zoológico de Brasília",
            "descricao": (
                "O Jardim Zoológico de Brasília é uma importante instituição de conservação e educação ambiental. Com uma grande variedade de animais da fauna brasileira e de outras partes do mundo, o zoológico oferece uma experiência educativa e divertida para todas as idades. O local conta com serpentário, borboletário e um museu de ciências naturais."
            ),
            "categoria": "Natureza",
            "endereco": "Avenida das Nações, Via L4 Sul, s/n - Candangolândia, Brasília - DF, 71729-900",
            "horario_funcionamento": "Terça a domingo e feriados, das 9h às 17h.",
            "telefone": "(61) 3445-7048",
            "imagem_url": "https://live.staticflickr.com/65535/50972235832_0c6b1b1c6c_b.jpg"
        },
        {
            "nome": "Parque Ecológico Águas Claras",
            "descricao": (
                "O Parque Ecológico Águas Claras é uma área de preservação ambiental localizada na região administrativa de Águas Claras. Com trilhas ecológicas, lagos e uma rica fauna e flora do Cerrado, o parque é um local ideal para caminhadas, corridas e observação de aves. O parque também possui áreas de piquenique e playground para crianças."
            ),
            "categoria": "Natureza",
            "endereco": "Av. das Castanheiras - Águas Claras, Brasília - DF, 70297-400",
            "horario_funcionamento": "Todos os dias, das 6h às 22h.",
            "imagem_url": "https://live.staticflickr.com/65535/51237893543_33b3c3c62a_b.jpg"
        },
        {
            "nome": "Parque Nacional de Brasília (Água Mineral)",
            "descricao": (
                "O Parque Nacional de Brasília, conhecido como Água Mineral, é uma unidade de conservação que protege a fauna e a flora do Cerrado. O parque é famoso por suas piscinas de água mineral, que atraem visitantes em busca de lazer e contato com a natureza. Além das piscinas, o parque oferece trilhas ecológicas, onde é possível observar a vegetação nativa e animais silvestres. É um refúgio de tranquilidade e ar puro em meio à agitação da cidade."
            ),
            "categoria": "Natureza",
            "endereco": "Parque Nacional de Brasília BR 450 EPIA Norte km 8,5 - Zona Industrial, Brasília - DF, 70635-800",
            "horario_funcionamento": "Todos os dias, das 8h às 17h.",
            "telefone": "(62) 99108-4112",
            "imagem_url": "https://www.viagensecaminhos.com/wp-content/uploads/2021/01/parque-nacional-de-brasilia-agua-mineral.jpg"
        },
        {
            "nome": "Parque Olhos d'Água",
            "descricao": (
                "O Parque Olhos d'Água é um parque ecológico localizado na Asa Norte, que preserva uma área de Cerrado com nascentes de água cristalina. O parque possui trilhas ecológicas, áreas de piquenique e um lago artificial. É um local muito procurado para caminhadas, corridas e para relaxar em meio à natureza. O parque também abriga uma grande diversidade de aves e outros animais silvestres."
            ),
            "categoria": "Natureza",
            "endereco": "Quadra 413/414 - Asa Norte, Brasília - Distrito Federal, 70876-000",
            "horario_funcionamento": "Todos os dias, das 6h às 21h.",
            "imagem_url": "https://live.staticflickr.com/65535/51237893543_33b3c3c62a_b.jpg"
        },
        {
            "nome": "Parque da Cidade Sarah Kubitschek",
            "descricao": (
                "O Parque da Cidade é o maior parque urbano do mundo, superando até mesmo o Central Park, em Nova York. Com uma área de 420 hectares, o parque oferece uma ampla estrutura de lazer, com quadras de esporte, pistas de corrida e ciclismo, lagos artificiais, e uma grande área verde. O parque é um local muito procurado para a prática de atividades físicas, piqueniques e eventos culturais. É um verdadeiro oásis de lazer e bem-estar no coração de Brasília."
            ),
            "categoria": "Natureza",
            "endereco": "Eixo Monumental Sul, s/n - Brasília, DF, 70610-300",
            "horario_funcionamento": "Aberto 24 horas",
            "imagem_url": "https://www.viagensecaminhos.com/wp-content/uploads/2021/01/parque-da-cidade-brasilia.jpg"
        },
        {
            "nome": "Palácio do Buriti",
            "descricao": (
                "O Palácio do Buriti é a sede do Governo do Distrito Federal. Projetado por Mauro Jorge Esteves, o edifício possui uma arquitetura modernista e é cercado por jardins e esculturas. Em frente ao palácio, há uma réplica da Loba Romana e a escultura 'Forma Espacial do Plano'. Embora não ofereça visitação interna, o palácio conta com uma bela praça que foi revitalizada e é aberta ao público."
            ),
            "categoria": "Política",
            "endereco": "Praça do Buriti, s/n - Setor de Áreas Públicas, Brasília - DF, 70075-900",
            "horario_funcionamento": "Visitação somente na área externa.",
            "imagem_url": "https://live.staticflickr.com/65535/51237893543_33b3c3c62a_b.jpg"
        },
        {
            "nome": "Praça dos Três Poderes",
            "descricao": (
                "A Praça dos Três Poderes é o coração cívico de Brasília e do Brasil. Projetada por Oscar Niemeyer e Lúcio Costa, a praça abriga as sedes dos três poderes da República: o Palácio do Planalto (Executivo), o Congresso Nacional (Legislativo) e o Supremo Tribunal Federal (Judiciário). Além dos palácios, a praça conta com diversas esculturas, como 'Os Candangos', de Bruno Giorgi, e 'A Justiça', de Alfredo Ceschiatti."
            ),
            "categoria": "Política",
            "endereco": "Praça dos Três Poderes, s/n - Brasília, DF, 70100-000",
            "horario_funcionamento": "Acesso livre 24 horas",
            "telefone": "(61) 3410-9000",
            "imagem_url": "https://live.staticflickr.com/65535/51237893543_33b3c3c62a_b.jpg"
        },
        {
            "nome": "Supremo Tribunal Federal (STF)",
            "descricao": (
                "O Supremo Tribunal Federal é a mais alta instância do Poder Judiciário brasileiro. O edifício, projetado por Oscar Niemeyer, é um dos mais icônicos da Praça dos Três Poderes. O STF oferece visitas guiadas, onde é possível conhecer o Salão Branco, o Salão Nobre e o Plenário. A visita é uma oportunidade de aprender sobre a história e o funcionamento da justiça no Brasil."
            ),
            "categoria": "Política",
            "endereco": "Praça dos Três Poderes, s/n - Brasília, DF, 70175-900",
            "horario_funcionamento": "Visitas guiadas em dias úteis, com agendamento.",
            "telefone": "(61) 3217-3000",
            "imagem_url": "https://www.stf.jus.br/portal/cms/verNoticiaDetalhe.asp?idConteudo=455556"
        },
        {
            "nome": "Ermida Dom Bosco",
            "descricao": (
                "A Ermida Dom Bosco é uma pequena capela branca construída em homenagem ao santo italiano que teria sonhado com a construção de uma nova capital no Planalto Central. Localizada às margens do Lago Paranoá, a ermida oferece uma vista deslumbrante do lago e da cidade. É um local de paz e contemplação, muito procurado para meditação e para apreciar o pôr do sol."
            ),
            "categoria": "Religião",
            "endereco": "SHIS QL 30, s/n - Lago Sul, Brasília - DF, 71675-260",
            "horario_funcionamento": "Seg-Dom, 6h-20h",
            "imagem_url": "https://live.staticflickr.com/8016/7442145414_f7c4c3e33c_b.jpg"
        },
        {
            "nome": "Igreja Nossa Senhora de Fátima",
            "descricao": (
                "A Igreja Nossa Senhora de Fátima, também conhecida como 'Igrejinha da 307/308 Sul', foi a primeira igreja construída em Brasília. Projetada por Oscar Niemeyer, a igreja possui uma arquitetura simples e elegante, com um formato cônico e um chapéu de freira. É um local de grande importância histórica e religiosa para a cidade, e um exemplo da arquitetura sacra de Niemeyer."
            ),
            "categoria": "Religião",
            "endereco": "EQS 307/308 - Asa Sul, Brasília - DF, 70390-100",
            "horario_funcionamento": "Todos os dias, das 6h às 21h.",
            "telefone": "(61) 3242-0149",
            "imagem_url": "https://live.staticflickr.com/65535/51237893543_33b3c3c62a_b.jpg"
        },
        {
            "nome": "Santuário Dom Bosco",
            "descricao": (
                "O Santuário Dom Bosco é uma das igrejas mais impressionantes de Brasília. Projetada pelo arquiteto Carlos Alberto Naves, a igreja é famosa por seus 12 tons de azul em seus vitrais, que criam uma atmosfera de paz e serenidade. A iluminação noturna da igreja é um espetáculo à parte, que realça a beleza de sua arquitetura. O Santuário é um local de grande importância religiosa e arquitetônica na cidade."
            ),
            "categoria": "Religião",
            "endereco": "SEPS 702, Lote B - Asa Sul, Brasília - DF, 70330-710",
            "horario_funcionamento": "Todos os dias, das 7h às 20h.",
            "telefone": "(61) 3223-6542",
            "imagem_url": "https://www.viagensecaminhos.com/wp-content/uploads/2021/01/santuario-dom-bosco-brasilia.jpg"
        },
        {
            "nome": "Templo da Boa Vontade (TBV)",
            "descricao": (
                "O Templo da Boa Vontade é um monumento ecumênico que recebe pessoas de todas as crenças. Com sua pirâmide de sete faces, o templo é um local de paz, meditação e oração. No topo da pirâmide, há um cristal de 21 quilos, que, segundo os frequentadores, emana energias positivas. O templo também possui uma galeria de arte, um memorial e uma fonte sagrada."
            ),
            "categoria": "Religião",
            "endereco": "SGAS 915, Lote 75/76 - Asa Sul, Brasília - DF, 70390-150",
            "horario_funcionamento": "Todos os dias, das 8h às 20h.",
            "telefone": "(61) 3114-1070",
            "imagem_url": "https://www.tbv.com.br/wp-content/uploads/2020/05/templo-da-boa-vontade-1.jpg"
        },
        {
            "nome": "313 Drink Bar",
            "descricao": (
                "O 313 Drink Bar é um speakeasy moderno e sofisticado localizado na Asa Sul, conhecido por seus drinks autorais e ambiente intimista. Com uma carta de coquetéis criativos que começam a partir de R$ 35,90, o bar oferece uma experiência única para apreciadores de boa mixologia. O ambiente é acolhedor e descontraído, perfeito para encontros românticos ou happy hours com amigos. A decoração moderna e a iluminação cênica criam uma atmosfera especial, tornando o 313 um dos destinos mais procurados da vida noturna brasiliense. Além dos drinks autorais, o bar também serve clássicos da coquetelaria e oferece petiscos irresistíveis para acompanhar."
            ),
            "categoria": "Vida Noturna",
            "endereco": "CLS 313, Bloco B, Loja 1 - Asa Sul, Brasília - DF, 70382-520",
            "horario_funcionamento": "Terça a sábado, das 18h às 2h.",
            "telefone": "(61) 99671-6569",
            "imagem_url": "https://live.staticflickr.com/65535/51237893543_33b3c3c62a_b.jpg"
        },
        {
            "nome": "Bar Brasília",
            "descricao": (
                "O Bar Brasília é um dos bares mais tradicionais da cidade, famoso por ter o melhor chopp de Brasília. Com um ambiente descontraído e familiar, o bar é um ponto de encontro para happy hours e para assistir a jogos de futebol. O cardápio oferece petiscos variados, como porções de carne, frango e batata frita. É um local autêntico e muito frequentado pelos brasilienses."
            ),
            "categoria": "Vida Noturna",
            "endereco": "SCLS 106, Bloco C, Loja 34 - Asa Sul, Brasília - DF, 70345-530",
            "horario_funcionamento": "Todos os dias, das 11h à 0h.",
            "telefone": "(61) 3443-1578",
            "imagem_url": "https://live.staticflickr.com/65535/51237893543_33b3c3c62a_b.jpg"
        },
        {
            "nome": "Bar Responsa",
            "descricao": (
                "O Bar Responsa é um bar descontraído e acolhedor, conhecido por seu ambiente familiar e pela qualidade de suas cervejas e petiscos. Com uma decoração simples e autêntica, o bar atrai um público diversificado que busca um local tranquilo para conversar e relaxar. O Bar Responsa também oferece música ao vivo em alguns dias da semana."
            ),
            "categoria": "Vida Noturna",
            "endereco": "SCLS 403, Bloco B, Loja 34 - Asa Sul, Brasília - DF, 70330-515",
            "horario_funcionamento": "Segunda a sabado, 12h-1h.",
            "telefone": "(61) 99875-7211",
            "imagem_url": "https://live.staticflickr.com/65535/51237893543_33b3c3c62a_b.jpg"
        },
        {
            "nome": "Carcassonne Pub",
            "descricao": (
                "O Carcassonne Pub é um dos pubs mais tradicionais de Brasília, com um ambiente acolhedor e uma decoração que remete aos pubs ingleses. Com uma carta de cervejas artesanais e importadas, além de um cardápio com petiscos e pratos principais, o pub é um local ideal para happy hours e encontros com amigos. O Carcassonne também oferece música ao vivo em alguns dias da semana."
            ),
            "categoria": "Vida Noturna",
            "endereco": "CLN 407, Bloco E, Loja 37 - Asa Norte, Brasília - DF, 70855-550",
            "horario_funcionamento": "Quarta a domingo, das 17h à 0h.",
            "telefone": "(61) 99968-4186",
            "imagem_url": "https://live.staticflickr.com/65535/51237893543_33b3c3c62a_b.jpg"
        },
        {
            "nome": "Clube do Choro",
            "descricao": (
                "O Clube do Choro é um espaço cultural dedicado à preservação e divulgação do choro, gênero musical tipicamente brasileiro. Com uma programação regular de shows e rodas de choro, o clube atrai músicos e apreciadores do gênero de todo o país. O ambiente é intimista e acolhedor, e o Clube do Choro é um local imperdível para quem quer conhecer a música brasileira autêntica."
            ),
            "categoria": "Vida Noturna",
            "endereco": "SDC, Bloco G, Lote 30 - Setor de Divulgação Cultural, Brasília - DF, 70070-350",
            "horario_funcionamento": "Quinta a sábado, a partir das 20h.",
            "telefone": "(61) 3226-3969",
            "imagem_url": "https://live.staticflickr.com/65535/51237893543_33b3c3c62a_b.jpg"
        },
        {
            "nome": "Galpão 17",
            "descricao": (
                "O Galpão 17 é um espaço cultural e gastronômico localizado na Asa Norte, que reúne bares, restaurantes e food trucks em um ambiente descontraído e ao ar livre. Com música ao vivo e uma programação cultural variada, o Galpão 17 é um local ideal para happy hours, encontros com amigos e para curtir a noite em Brasília. O espaço também abriga feiras e eventos temáticos."
            ),
            "categoria": "Vida Noturna",
            "endereco": "SMAS Área Especial G Conjunto A Lotes 16 e 17, Brasília - DF, 71215-300",
            "horario_funcionamento": "Seg-Qui, 8h-18h, Sex-Sab 8h-1h",
            "imagem_url": "https://live.staticflickr.com/65535/51237893543_33b3c3c62a_b.jpg"
        },
        {
            "nome": "Mormaii Surf Bar",
            "descricao": (
                "O Mormaii Surf Bar é um bar temático inspirado na cultura do surf e do skate. Com um ambiente descontraído e ao ar livre, o bar oferece uma carta de drinks tropicais, cervejas artesanais e um cardápio com petiscos e hambúrgueres. O Mormaii Surf Bar também promove eventos com música ao vivo e DJs, sendo um local ideal para curtir a noite em Brasília."
            ),
            "categoria": "Vida Noturna",
            "endereco": "SHIS QL 10, Conjunto 1, Lote 1/30 - Lago Sul, Brasília - DF, 71630-100",
            "horario_funcionamento": "Terça a domingo, 11h-23h.",
            "telefone": "(61) 3364-0580",
            "imagem_url": "https://live.staticflickr.com/65535/51237893543_33b3c3c62a_b.jpg"
        },
        {
            "nome": "Arena BRB Mané Garrincha",
            "descricao": (
                "A Arena BRB Mané Garrincha, construída originalmente para eventos esportivos e reformada para a Copa do Mundo de 2014, tornou-se o principal palco de megashows e grandes atrações em Brasília. Além de sediar partidas de futebol, ligas como o NBB e eventos esportivos variados, o estádio se destaca por receber alguns dos maiores artistas do mundo, como Guns N Roses, Imagine Dragons, Bruno Mars, Linkin Park, Pink e Paul McCartney. Com capacidade para até 72.788 pessoas e estrutura moderna, a arena é hoje o centro do entretenimento de grande porte da capital, reunindo música, esporte e cultura em um único complexo."
            ),
            "categoria": "Vida Noturna",
            "endereco": "Estádio Nacional - Eixo Monumental - SRPN - 2º Andar, Asa Norte, Brasília - DF, 70070-701",
            "horario_funcionamento": "Horários variam conforme eventos. Consultar agenda em arenabsb.com.br/agenda/",
            "telefone": "(61) 4103-3553",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Arena_BRB_Man%C3%A9_Garrincha_Bras%C3%ADlia.jpg/1200px-Arena_BRB_Man%C3%A9_Garrincha_Bras%C3%ADlia.jpg"
        },
        {
            "nome": "Ordinário Bar e Música",
            "descricao": (
                "O Ordinário Bar e Música, situado na Asa Norte, rapidamente se estabeleceu como um dos polos culturais e boêmios mais efervescentes de Brasília, destacando-se por sua curadoria musical apurada. Diferente dos grandes clubes, este local oferece uma experiência mais intimista e acolhedora, com um ambiente que mescla o charme rústico de um bar de bairro com a sofisticação de uma casa de shows. A programação musical é o grande trunfo, abrangendo gêneros como MPB, samba, jazz e rock, frequentemente apresentando artistas locais e nacionais de destaque. O bar se orgulha de promover a cultura autêntica e ser um ponto de encontro da juventude e da comunidade artística. Além da música, o cardápio complementa a experiência com petiscos criativos e uma seleção de cervejas artesanais e coquetéis de qualidade. É o lugar ideal para quem busca uma noite culturalmente rica, longe da formalidade, oferecendo um vislumbre da vida noturna alternativa e vibrante da capital."
            ),
            "categoria": "Vida Noturna",
            "endereco": "Setor Bancário Sul, Quadra 2, Bloco S, Brasília, DF 70070-100",
            "horario_funcionamento": "Encerrado permanentemente (Julho/2024). Mantido para fins históricos e culturais.",
            "telefone": "(61) 3322-9588",
            "imagem_url": "https://img.example.com/brasilia/calaf_sbs_1200x800.jpg"
        }
    ]

    try:
        for ponto_data in pontos:
            # Verificar se já existe
            existing = db.query(PontoTuristico).filter(
                PontoTuristico.nome == ponto_data["nome"]
            ).first()

            if not existing:
                ponto = PontoTuristico(**ponto_data)
                db.add(ponto)
                print(f"✓ Adicionado: {ponto_data['nome']}")
            else:
                print(f"⊘ Já existe: {ponto_data['nome']}")

        db.commit()
        print(f"\n✅ Seed executado com sucesso!")
        print(f"✅ {len(pontos)} pontos turísticos processados!")
        
    except Exception as e:
        db.rollback()
        print(f"\n❌ Erro ao executar seed: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed_pontos_turisticos()