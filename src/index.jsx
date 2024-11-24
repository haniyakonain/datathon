import React, { useState } from 'react';

// Import your components (ensure these components are defined in their respective files)
import HomeRemedies from './HomeRemedies';
import Explore from './Explore';
import Practitioners from './Practitioners';
import FarmerIntegration from './FarmerIntegration';

function App() {
    const [tab, setTab] = useState(1); // State to manage the active tab

    return (
        <div>
            <nav>
                <button onClick={() => setTab(1)}>Home Remedies</button>
                <button onClick={() => setTab(2)}>Explore Remedies</button>
                <button onClick={() => setTab(3)}>Practitioners</button>
                <button onClick={() => setTab(4)}>Farmer Integration</button>
            </nav>
            <div>
                {/* Conditional rendering based on the selected tab */}
                {tab === 1 && <HomeRemedies />}
                {tab === 2 && <Explore />}
                {tab === 3 && <Practitioners />}
                {tab === 4 && <FarmerIntegration />}
            </div>
        </div>
    );
}

export default App;
