module.exports = {
  content: [
    './app/templates/**/*.html',  // Rutas de tus plantillas HTML
    './app/static/app/js/**/*.js',  // Archivos JS si los tienes
    './app/static/app/css/**/*.css',  // Archivos CSS que usas con Tailwind
  ],
  theme: {
    extend: {
      colors: {
        cyan: {
          500: '#00c6ff', // El color cyan que estás usando
        },
      },
    },
  },
  plugins: [],
}