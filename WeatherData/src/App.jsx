import React from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import AppRoutes from './components/Router/Router';

function App() {
  return (
    <Router>
      <AppRoutes />
    </Router>
  );
}

export default App;
