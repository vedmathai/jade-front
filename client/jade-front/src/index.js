import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import JadeJobsQueue from './pages/jobs-queue/jobs-queue';
import JadeRequestsList from './pages/jade-requests/jade-requests';


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <Router>
    <Routes>
      <Route path="/jade-jobs-queue" element={<JadeJobsQueue />} />
      <Route path="/jade-requests" element={<JadeRequestsList />} />

    </Routes>
</Router>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();