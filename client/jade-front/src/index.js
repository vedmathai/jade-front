import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import JadeJobsQueue from './pages/jobs-queue/jobs-queue';
import JadeRequestsList from './pages/jade-requests/jade-requests';
import JadeProjectsList from './pages/jade-projects/jade-projects';
import JadeProject from './pages/jade-project/jade-project';
import JadeRequest from './pages/jade-request/jade-request';


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <Router>
    <Routes>
      <Route path="/jade-jobs-queue" element={<JadeJobsQueue />} />
      <Route path="/jade-requests" element={<JadeRequestsList />} />
      <Route path="/jade-request" element={<JadeRequest />} />
      <Route path="/jade-projects" element={<JadeProjectsList />} />
      <Route path="/jade-project" element={<JadeProject />} />

    </Routes>
</Router>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
