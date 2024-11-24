import React, { useState } from 'react';
import axios from 'axios';

function Explore() {
    const [searchTerm, setSearchTerm] = useState('');
    const [recommendations, setRecommendations] = useState([]);

    const handleSearch = async () => {
        try {
            const response = await axios.get(`http://localhost:5000/recommend?plant=${searchTerm}`);
            setRecommendations(response.data.recommendations);
        } catch (error) {
            console.error('Error fetching recommendations:', error);
        }
    };

    return (
        <div>
            <h2>Explore Ayurvedic Remedies</h2>
            <input
                type="text"
                placeholder="Enter plant name (e.g., Tulsi)"
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
            />
            <button onClick={handleSearch}>Search</button>
            <div>
                <h3>Recommendations:</h3>
                {recommendations.length > 0 ? (
                    <ul>
                        {recommendations.map((rec, index) => (
                            <li key={index}>{rec}</li>
                        ))}
                    </ul>
                ) : (
                    <p>No recommendations available. Try another plant.</p>
                )}
            </div>
        </div>
    );
}

export default Explore;
