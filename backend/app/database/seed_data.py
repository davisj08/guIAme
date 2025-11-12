from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.models.ponto_turistico import PontoTuristico


def seed_pontos_turisticos():
    """Popula o banco com pontos turísticos de Brasília"""
    db = SessionLocal()

    pontos = [
        {
            "nome": "Catedral Metropolitana de Brasília",
            "descricao": (
                "A Catedral Metropolitana Nossa Senhora Aparecida é uma "
                "obra-prima da arquitetura moderna projetada por Oscar Niemeyer. "
                "Com sua estrutura hiperboloide de concreto e vitrais coloridos, "
                "é um dos principais símbolos de Brasília e Patrimônio Mundial "
                "da UNESCO."
            ),
            "categoria": "Arquitetura",
            "latitude": -15.7984,
            "longitude": -47.8755,
            "endereco": "Esplanada dos Ministérios, Brasília - DF",
            "horario_funcionamento": "Segunda a domingo, 8h às 18h",
            "telefone": "(61) 3224-4073",
            "site": "https://www.catedraldebrasilia.com.br",
            "imagem_url": "https://visitebrasilia.com.br/images/2022/05/20220503144800_l_CatedralMetropolitana.jpg"
        },
        {
            "nome": "Congresso Nacional",
            "descricao": (
                "Sede do Poder Legislativo brasileiro, o Congresso Nacional é "
                "composto pela Câmara dos Deputados e pelo Senado Federal. Sua "
                "arquitetura icônica, com as cúpulas invertidas e as torres "
                "gêmeas, foi projetada por Oscar Niemeyer."
            ),
            "categoria": "Política",
            "latitude": -15.7998,
            "longitude": -47.8643,
            "endereco": "Praça dos Três Poderes, Brasília - DF",
            "horario_funcionamento": "Visitas guiadas: sábado, domingo e feriados, 9h30 às 16h30",
            "site": "https://www2.camara.leg.br",
            "imagem_url": "https://live.staticflickr.com/4762/27948917069_4358129a7d_b.jpg"
        },
        {
            "nome": "Palácio da Alvorada",
            "descricao": (
                "Residência oficial do Presidente da República, o Palácio da "
                "Alvorada é uma das primeiras construções de Brasília. Projetado "
                "por Oscar Niemeyer, destaca-se por suas colunas externas em "
                "formato de V invertido."
            ),
            "categoria": "Política",
            "latitude": -15.7913,
            "longitude": -47.8270,
            "endereco": "SGAN 1, Brasília - DF",
            "horario_funcionamento": "Visitas externas permitidas",
            "site": "https://www.gov.br/planalto",
            "imagem_url": "https://www.df.gov.br/wp-conteudo/uploads/2016/02/palacio_da_alvorada_exterior__ricardo_stuckert_presidencia_da_republica-ebc.jpg"
        },
        {
            "nome": "Ponte JK",
            "descricao": (
                "A Ponte Juscelino Kubitschek é uma das pontes mais bonitas do "
                "mundo, com seus três arcos assimétricos que se cruzam. "
                "Inaugurada em 2002, tornou-se um cartão-postal de Brasília, "
                "especialmente à noite com sua iluminação."
            ),
            "categoria": "Arquitetura",
            "latitude": -15.8170,
            "longitude": -47.8953,
            "endereco": "Lago Sul/Lago Norte, Brasília - DF",
            "horario_funcionamento": "24 horas",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/1/13/Ponte_JK_Bras%C3%ADlia_Brazil.jpg"
        },
        {
            "nome": "Memorial JK",
            "descricao": (
                "O Memorial Juscelino Kubitschek é um monumento dedicado ao "
                "fundador de Brasília. Abriga o túmulo de JK, um museu com "
                "objetos pessoais e documentos históricos, além de uma biblioteca."
            ),
            "categoria": "Cultura",
            "latitude": -15.8122,
            "longitude": -47.9146,
            "endereco": "Eixo Monumental Oeste, Brasília - DF",
            "horario_funcionamento": "Terça a domingo, 9h às 18h",
            "telefone": "(61) 3225-9451",
            "site": "https://memorialjk.com.br",
            "imagem_url": "https://live.staticflickr.com/2411/5707399333_e7a447a2fd_b.jpg"
        },
        {
            "nome": "Jardim Botânico de Brasília",
            "descricao": (
                "Com mais de 5 mil hectares de área de preservação do Cerrado, "
                "o Jardim Botânico oferece trilhas ecológicas, jardins temáticos "
                "e um centro de visitantes. É ideal para quem busca contato com "
                "a natureza."
            ),
            "categoria": "Natureza",
            "latitude": -15.8705,
            "longitude": -47.8292,
            "endereco": "SMDB Conjunto 12, Lago Sul, Brasília - DF",
            "horario_funcionamento": "Terça a domingo, 9h às 17h",
            "telefone": "(61) 3366-3832",
            "site": "https://www.jardimbotanico.df.gov.br",
            "imagem_url": "https://www.quintoandar.com.br/guias/wp-content/uploads/2023/04/jardim-botanico-brasilia-2-1.jpg"
        },
        {
            "nome": "Torre de TV",
            "descricao": (
                "Com 224 metros de altura, a Torre de TV Digital oferece uma "
                "vista panorâmica de 360 graus de Brasília. Aos finais de semana, "
                "funciona a Feira da Torre, com artesanato e gastronomia local."
            ),
            "categoria": "Mirante",
            "latitude": -15.7906,
            "longitude": -47.8920,
            "endereco": "Eixo Monumental, Brasília - DF",
            "horario_funcionamento": "Segunda a domingo, 8h às 20h",
            "imagem_url": "https://visitebrasilia.com.br/images/2023/03/20230309135240_l_WhatsAppImage2023-03-09at11.55.48.jpg"
        },
        {
            "nome": "Santuário Dom Bosco",
            "descricao": (
                "Igreja com interior impressionante repleto de vitrais azuis "
                "que criam uma atmosfera única. Foi construída em homenagem a "
                "Dom Bosco, que profetizou a criação de Brasília."
            ),
            "categoria": "Religioso",
            "latitude": -15.8070,
            "longitude": -47.8836,
            "endereco": "SGAS 702, Asa Sul, Brasília - DF",
            "horario_funcionamento": "Segunda a domingo, 7h às 19h",
            "site": "https://www.santuariodombosco.org.br",
            "imagem_url": "https://arqbrasilia.com.br/wp-content/uploads/2023/05/Santuario-Dom-Bosco.jpg"
        },
        {
            "nome": "Parque da Cidade Sarah Kubitschek",
            "descricao": (
                "Um dos maiores parques urbanos do mundo, com 420 hectares. "
                "Oferece pistas para caminhada e ciclismo, áreas para piquenique, "
                "parquinhos, quadras esportivas e muito espaço verde."
            ),
            "categoria": "Natureza",
            "latitude": -15.7916,
            "longitude": -47.9140,
            "endereco": "Asa Sul, Brasília - DF",
            "horario_funcionamento": "24 horas",
            "imagem_url": "https://curtamais.com.br/brasilia/wp-content/uploads/sites/3/2021/05/2d6a41e02e012dd21a6028c9a5ba076e.jpg"
        },
        {
            "nome": "Museu Nacional",
            "descricao": (
                "Projetado por Oscar Niemeyer, o Museu Nacional Honestino "
                "Guimarães tem formato de cúpula e abriga exposições temporárias "
                "de arte, história e cultura brasileira."
            ),
            "categoria": "Cultura",
            "latitude": -15.7870,
            "longitude": -47.8823,
            "endereco": "Setor Cultural Sul, Brasília - DF",
            "horario_funcionamento": "Terça a domingo, 9h às 18h30",
            "telefone": "(61) 3325-5220",
            "site": "https://museu.df.gov.br",
            "imagem_url": "https://imgmd.net/images/v1/guia/4188111/museu-nacional-da-republica.jpg"
        },
        {
            "nome": "Praça dos Três Poderes",
            "descricao": (
                "Coração político de Brasília, reúne os três poderes da República: "
                "Executivo (Palácio do Planalto), Legislativo (Congresso Nacional) "
                "e Judiciário (Supremo Tribunal Federal). Possui monumentos e "
                "esculturas importantes."
            ),
            "categoria": "Política",
            "latitude": -15.7993,
            "longitude": -47.8603,
            "endereco": "Praça dos Três Poderes, Brasília - DF",
            "horario_funcionamento": "24 horas (visitas externas)",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/3/3c/Pra%C3%A7a_dos_Tr%C3%AAs_Poderes.jpg"
        },
        {
            "nome": "Pontão do Lago Sul",
            "descricao": (
                "Complexo de lazer às margens do Lago Paranoá com restaurantes, "
                "bares, lojas e espaços para eventos. É um dos principais pontos "
                "de encontro de Brasília, especialmente ao pôr do sol."
            ),
            "categoria": "Gastronomia",
            "latitude": -15.8392,
            "longitude": -47.8267,
            "endereco": "SHIS QI 9, Lago Sul, Brasília - DF",
            "horario_funcionamento": "Varia conforme estabelecimento",
            "site": "https://www.pontaodolagosul.com.br",
            "imagem_url": "https://www.melhoresdestinos.com.br/wp-content/uploads/2019/08/pontao-lago-sul-brasilia.jpg"
        },
        {
            "nome": "Ermida Dom Bosco",
            "descricao": (
                "Pequena capela construída no ponto exato onde Dom Bosco teria "
                "sonhado com a criação de Brasília. Oferece uma vista privilegiada "
                "do Lago Paranoá e é um local de contemplação e paz."
            ),
            "categoria": "Religioso",
            "latitude": -15.7867,
            "longitude": -47.8189,
            "endereco": "DF-001, Lago Sul, Brasília - DF",
            "horario_funcionamento": "24 horas",
            "imagem_url": "https://www.df.gov.br/wp-conteudo/uploads/2017/09/ermida-dom-bosco.jpg"
        },
        {
            "nome": "Catetinho",
            "descricao": (
                "Primeira residência oficial do presidente Juscelino Kubitschek "
                "durante a construção de Brasília. Hoje funciona como museu, "
                "preservando a história da construção da capital."
            ),
            "categoria": "Cultura",
            "latitude": -15.8833,
            "longitude": -47.9667,
            "endereco": "BR-040, Km 0, Brasília - DF",
            "horario_funcionamento": "Terça a domingo, 9h às 17h",
            "telefone": "(61) 3387-8949",
            "site": "https://www.catetinho.df.gov.br",
            "imagem_url": "https://www.df.gov.br/wp-conteudo/uploads/2017/09/catetinho.jpg"
        },
        {
            "nome": "Palácio do Planalto",
            "descricao": (
                "Sede do Poder Executivo federal e gabinete oficial do Presidente "
                "da República. Projetado por Oscar Niemeyer, é um dos edifícios "
                "mais importantes de Brasília."
            ),
            "categoria": "Política",
            "latitude": -15.7990,
            "longitude": -47.8613,
            "endereco": "Praça dos Três Poderes, Brasília - DF",
            "horario_funcionamento": "Visitas guiadas aos domingos, 9h30 às 14h",
            "site": "https://www.gov.br/planalto",
            "imagem_url": "https://upload.wikimedia.org/wikipedia/commons/3/3e/Pal%C3%A1cio_do_Planalto.jpg"
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