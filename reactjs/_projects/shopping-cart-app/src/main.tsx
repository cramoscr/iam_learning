import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.tsx'

// eslint-disable-next-line @typescript-eslint/no-unused-vars
import { CartProvider } from './context/CartContext.jsx';

import './index.css'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <CartProvider>
      <App />
    </CartProvider>
  </StrictMode>,
);
