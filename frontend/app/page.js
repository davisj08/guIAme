import { MapIcon, ChatBubbleLeftRightIcon, TrophyIcon, SparklesIcon } from '@heroicons/react/24/outline'

// Assumindo que estes componentes estão disponíveis no escopo do projeto
// import MainLayout from '@/components/layout/MainLayout'
// import Button from '@/components/ui/Button'
// import Card from '@/components/ui/Card'

// Para fins de demonstração em um único arquivo, vou criar stubs simples para Button e Card.
// O 'next/link' foi substituído por uma tag <a> para evitar o erro de compilação.
const Button = ({ children, href, variant = 'primary', size = 'md', className = '' }) => {
  const baseClasses = "font-semibold rounded-lg shadow transition duration-300 ease-in-out px-6 py-3 text-center";
  const variants = {
    primary: "bg-indigo-600 text-white hover:bg-indigo-700",
    secondary: "bg-white text-indigo-600 border border-indigo-600 hover:bg-indigo-50",
  };
  const classes = `${baseClasses} ${variants[variant]} ${className}`;

  if (href) {
    // Usando <a> nativo em vez de next/link para compatibilidade no ambiente
    return <a href={href} className={classes}>{children}</a>;
  }
  return <button className={classes}>{children}</button>;
};

const Card = ({ children, className = '' }) => (
  <div className={`p-6 bg-white rounded-xl shadow-lg hover:shadow-xl transition duration-300 ${className}`}>
    {children}
  </div>
);

export default function HomePage() {
  const features = [
    {
      icon: MapIcon,
      title: 'Pontos Turísticos',
      description: 'Descubra os melhores lugares de Brasília com informações detalhadas e avaliações.',
    },
    {
      icon: ChatBubbleLeftRightIcon,
      title: 'Chat com IA',
      description: 'Converse com nosso assistente inteligente para obter recomendações personalizadas.',
    },
    {
      icon: SparklesIcon,
      title: 'Recomendações Personalizadas',
      description: 'Receba sugestões de roteiros baseadas em seus interesses e preferências.',
    },
    {
      icon: TrophyIcon,
      title: 'Gamificação',
      description: 'Ganhe pontos e conquistas explorando a capital federal.',
    },
  ]

  // Nota: O MainLayout foi omitido aqui, pois o código deve ser autocontido.
  return (
    <div className="min-h-screen bg-gray-50 font-sans">
      
      {/* Hero Section */}
      <section className="bg-white pt-20 pb-32 md:pt-28 md:pb-40 shadow-inner">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 text-center">
          
          <h1 className="text-4xl sm:text-5xl lg:text-6xl font-extrabold text-gray-900 mb-4 tracking-tight">
            Explore Brasília com Inteligência Artificial
          </h1>
          
          <p className="max-w-3xl mx-auto text-xl text-gray-600 mb-10">
            Descubra os tesouros da capital federal de forma personalizada e interativa
          </p>
          
          <div className="flex flex-col sm:flex-row justify-center space-y-4 sm:space-y-0 sm:space-x-4">
            <Button href="/pontos-turisticos" variant="primary">
              Ver Pontos Turísticos
            </Button>
            <Button href="/chat-ia" variant="secondary">
              Conversar com IA
            </Button>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-20 bg-gray-50">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          
          <div className="text-center mb-12">
            <h2 className="text-3xl sm:text-4xl font-bold text-gray-900 mb-3">
              Funcionalidades
            </h2>
            <p className="text-lg text-gray-600">
              Tudo que você precisa para uma experiência turística completa
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            {features.map((feature, index) => (
              <Card key={index} className="flex flex-col items-center text-center">
                <feature.icon className="h-10 w-10 text-indigo-500 mb-4" />
                
                <h3 className="text-xl font-semibold text-gray-900 mb-2">
                  {feature.title}
                </h3>
                
                <p className="text-gray-500 text-sm">
                  {feature.description}
                </p>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 bg-indigo-600">
        <div className="mx-auto max-w-3xl px-4 sm:px-6 lg:px-8 text-center">
          
          <h2 className="text-3xl sm:text-4xl font-bold text-white mb-4">
            Pronto para explorar?
          </h2>
          
          <p className="text-xl text-indigo-100 mb-8">
            Cadastre-se gratuitamente e comece sua jornada por Brasília
          </p>
          
          <Button href="/registro" variant="secondary" className="bg-white text-indigo-600 hover:bg-indigo-50">
            Criar Conta Grátis
          </Button>
        </div>
      </section>

    </div>
  )
}