import React, { useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, useNavigate } from 'react-router-dom';

import './Router.css'
import TableLog from '../TableLog/TableLog';
import TablePage from '../Pages/TablePage';

function AppRoutes() {
    return(
                      <Routes>
                        <Route path="/" element={<TablePage />} />
                      </Routes>
    );
  }

export default AppRoutes;