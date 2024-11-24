import React from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Routes, Link, NavLink } from 'react-router-dom';

// Import components for each route
import HomeRemedies from './HomeRemedies';
import Explore from './Explore';
import Practitioners from './Practitioners';
import FarmerIntegration from './FarmerIntegration';

function App() {
  return (
    <Router>
      <div>
        {/* Navigation Bar */}
        <nav style={navStyle}>
          <ul style={ulStyle}>
            <li style={liStyle}>
              <NavLink to="/home-remedies" style={linkStyle} activeStyle={activeLinkStyle}>Home Remedies</NavLink>
            </li>
            <li style={liStyle}>
              <NavLink to="/explore" style={linkStyle} activeStyle={activeLinkStyle}>Explore Remedies</NavLink>
            </li>
            <li style={liStyle}>
              <NavLink to="/practitioners" style={linkStyle} activeStyle={activeLinkStyle}>Practitioners</NavLink>
            </li>
            <li style={liStyle}>
              <NavLink to="/farmer-integration" style={linkStyle} activeStyle={activeLinkStyle}>Farmer Integration</NavLink>
            </li>
          </ul>
        </nav>

        {/* Routes */}
        <Routes>
          <Route path="/" element={<HomeRemedies />} /> {/* Default Route */}
          <Route path="/home-remedies" element={<HomeRemedies />} />
          <Route path="/explore" element={<Explore />} />
          <Route path="/practitioners" element={<Practitioners />} />
          <Route path="/farmer-integration" element={<FarmerIntegration />} />
        </Routes>
      </div>
    </Router>
  );
}

// Basic Styles (You can adjust these to your liking)
const navStyle = {
  backgroundColor: '#4CAF50', // Green background
  padding: '10px 0',
  textAlign: 'center',
};

const ulStyle = {
  listStyleType: 'none',
  margin: 0,
  padding: 0,
};

const liStyle = {
  display: 'inline',
  margin: '0 20px',
};

const linkStyle = {
  textDecoration: 'none',
  color: 'white',
  fontSize: '18px',
  fontWeight: 'bold',
};

const activeLinkStyle = {
  color: '#FFD700', // Gold color for active link
};

export default App;
