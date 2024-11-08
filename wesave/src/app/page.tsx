// app/page.tsx
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Card } from "@/components/ui/card";

const Home = () => {
  return (
    <div className="min-h-screen bg-black text-white">
      {/* Header */}
      <header className="fixed top-0 w-full p-6 flex justify-between items-center z-50">
        <div className="text-2xl font-bold">Logo</div>
        <nav className="space-x-4">
          <Button variant="ghost" className="text-white hover:text-gray-300">Uso</Button>
          <Button variant="ghost" className="text-white hover:text-gray-300">Tarifas</Button>
          <Button variant="ghost" className="text-white hover:text-gray-300">Recursos</Button>
          <Button variant="outline" className="text-white border-white hover:bg-white hover:text-black">Iniciar sesión</Button>
          <Button className="bg-white text-black hover:bg-gray-200">Registrarse</Button>
        </nav>
      </header>

      {/* Main content */}
      <main className="flex min-h-screen">
        {/* Left side - Upload form */}
        <div className="w-1/2 p-8 flex items-center justify-center">
          <Card className="w-full max-w-md bg-white/10 backdrop-blur-lg border-0 p-6 rounded-xl">
            <div className="space-y-4">
              <div className="flex items-center justify-between">
                <h2 className="text-lg font-medium">Añadir archivos</h2>
                <span className="text-sm text-gray-400">NUEVO</span>
              </div>
              
              <Button className="w-full bg-blue-600 hover:bg-blue-700 h-32 rounded-xl flex flex-col items-center justify-center space-y-2">
                <span className="text-3xl">+</span>
                <span className="text-sm">O selecciona una carpeta</span>
              </Button>

              <div className="space-y-4">
                <Input 
                  placeholder="Tu email" 
                  className="bg-transparent border border-white/20 text-white placeholder:text-gray-400"
                />
                <Input 
                  placeholder="Título" 
                  className="bg-transparent border border-white/20 text-white placeholder:text-gray-400"
                />
                <Input 
                  placeholder="Mensaje" 
                  className="bg-transparent border border-white/20 text-white placeholder:text-gray-400"
                />
                
                <div className="flex space-x-2">
                  <Button variant="ghost" className="flex-1 border border-white/20">
                    <span className="text-lg">📅</span>
                  </Button>
                  <Button variant="ghost" className="flex-1 border border-white/20">
                    <span className="text-lg">⏰</span>
                  </Button>
                  <Button variant="ghost" className="flex-1 border border-white/20">
                    <span className="text-lg">📎</span>
                  </Button>
                  <Button variant="ghost" className="flex-1 border border-white/20">
                    <span className="text-lg">🔒</span>
                  </Button>
                  <Button variant="ghost" className="flex-1 border border-white/20">
                    <span className="text-lg">⋮</span>
                  </Button>
                </div>

                <Button className="w-full bg-blue-600 hover:bg-blue-700">
                  Enviar
                </Button>
              </div>
            </div>
          </Card>
        </div>

        {/* Right side - Content */}
        <div className="w-1/2 p-8 flex items-center">
          <div className="space-y-6">
            <span className="text-sm bg-white/10 px-3 py-1 rounded-full">Experience our award winning features</span>
            <h1 className="text-6xl font-bold leading-tight">
              No volverás a<br />
              tener que estar<br />
              pendiente de<br />
              los pagos
            </h1>
            <p className="text-lg text-gray-300 max-w-md">
              Establece un precio para el trabajo que compartes y recibe el
              pago antes de cualquier descarga.
            </p>
            <Button className="bg-blue-600 hover:bg-blue-700 px-6 py-3">
              Más información
            </Button>
          </div>
        </div>
      </main>
    </div>
  );
};

export default Home;