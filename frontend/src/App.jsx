import { useState } from 'react'
import './App.css'

function App() {
  const [url, setUrl] = useState('');
  const [output, setOutput] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      // First, send the URL to generate summary
      const response = await fetch('http://localhost:5000/summary', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url }),
      });
      const data = await response.json();
      
      if (!response.ok) throw new Error(data.error);

      // Then fetch the generated summary
      const summaryResponse = await fetch(`http://localhost:5000/summary/${data.video_id}`);
      const summaryData = await summaryResponse.json();
      
      if (!summaryResponse.ok) throw new Error(summaryData.error);
      
      setOutput(summaryData.summary);
    } catch (error) {
      setOutput(`Error: ${error.message}`);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="container">
      <h1>YouTube Video Summarizer</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          placeholder="Enter YouTube URL"
          className="url-input"
        />
        <button type="submit" className="submit-btn" disabled={loading}>
          {loading ? 'Generating...' : 'Get Summary'}
        </button>
      </form>
      <textarea
        value={output}
        readOnly
        className="output-box"
        placeholder="Summary will appear here..."
      />
    </div>
  )
}

export default App