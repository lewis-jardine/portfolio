// Styles
import "@mdi/font/css/materialdesignicons.css";
import "vuetify/styles";

// Vuetify
import { createVuetify } from "vuetify";

export default createVuetify({
  theme: {
    defaultTheme: "myCustomTheme",
    themes: {
      myCustomTheme: {
        dark: false,
        variables: {}, // this property is required to avoid Vuetify crash

        colors: {
          //green: '#00ff00' // cannot use primary color names here, so use a custom color name (such as 'greenish')
          // greenish: "#03DAC5",
          // Workaround: Custom colors seem to erase default colors, so we need to include the default colors (of `light` or `dark` theme)
          background: "#eee",
          // surface: "#212121",
          primary: "#ff8237",
          // "primary-darken-1": "#3700B3",
          secondary: "#d9336f",
          // "secondary-darken-1": "#03DAC5",
          // error: "#CF6679",
          // info: "#2196F3",
          // success: "#4CAF50",
          // warning: "#FB8C00",
        },
      },
    },
  },
});
