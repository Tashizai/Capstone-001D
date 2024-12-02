module.exports = {
  content: [
    './Capstone-001-main/app/templates/**/*.html',  // Rutas de tus plantillas HTML
    './Capstone-001-main/app/static/app/js/**/*.js',  // Archivos JS si los tienes
    './Capstone-001-main/app/static/app/css/**/*.css',  // Archivos CSS que usas con Tailwind
  ],
  theme: {
    extend: {
      colors: {
        lavender: {
          DEFAULT: '#a29bfe', // Morado Claro
        },
        violet: {
          DEFAULT: '#6c5ce7', // Violeta
        },
        darkPurple: {
          DEFAULT: '#3d348b', // Púrpura Oscuro
        },
        darkBlue: {
          DEFAULT: '#2c2e43', // Negro Azuloso
        },
      },
    },
  },
  plugins: [],
}

