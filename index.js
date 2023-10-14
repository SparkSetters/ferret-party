import React, { useState, useEffect } from 'react';

function LLMResults() {
    const [results, setResults] = useState([]);

    useEffect(() => {
        fetch('/llm_results')
            .then(response => response.json())
            .then(data => setResults(data.results));
    }, []);

    return (
        <div>
            <h1>LLM Results</h1>
            <ul>
                {results.map((result, index) => (
                    <li key={index}>{result}</li>
                ))}
            </ul>
        </div>
    );
}

export default LLMResults;
