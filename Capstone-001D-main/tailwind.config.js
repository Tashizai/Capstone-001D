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
          500: '#00bfff',  // Cian intenso
          400: '#33ccff',
          300: '#66d9ff',
          200: '#99e6ff',
          100: '#ccf3ff',
        },
        blue: {
          900: '#0d3b66',  // Azul más intenso
          800: '#1155cc',
          700: '#1976d2',
          600: '#1e90ff',
          500: '#3399ff',
          400: '#66b3ff',
          300: '#99ccff',
          200: '#cce6ff',
          100: '#e6f2ff',
        },
        orange: {
          500: '#ff6f61', // Naranja vibrante para contrastar
          400: '#ff8576',
        },
        pink: {
          500: '#ff4081',  // Rosa vibrante
          400: '#ff79b0',
        },
      },
      backgroundImage: {
        'gradient-blue': 'linear-gradient(to right, #1976d2, #1e90ff, #66b3ff)',
        'gradient-purple-pink': 'linear-gradient(to right, #9c27b0, #ff4081, #ff79b0)',
        'gradient-cyan': 'linear-gradient(to right, #00bfff, #33ccff, #66d9ff)',
      },
    },
  },
  plugins: [],
}
