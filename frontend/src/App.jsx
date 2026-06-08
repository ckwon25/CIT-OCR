import { useState } from "react";

export default function App() {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  async function uploadFile(event) {
    const file = event.target.files[0];

    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    setLoading(true);

    try {
      const response = await fetch(
        "http://localhost:8000/scan",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();

      setResult(data);
    } catch (error) {
      console.error(error);
      alert("Upload failed");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="app">
      <div className="card">

        <h1>CIT OCR</h1>

        <p className="subtitle">
          Citizenship Document Scanner
        </p>

        <label className="upload-btn">
          Upload Document

          <input
            type="file"
            onChange={uploadFile}
            style={{ display: "none" }}
          />
        </label>

        {loading && (
          <p style={{ marginTop: "20px" }}>
            Scanning document...
          </p>
        )}

        {result && (
          <div className="result">

            <h2>
              {result.document_type}
            </h2>

            <p>
              Confidence: {result.confidence}
            </p>

            {Object.entries(result.fields).map(
              ([key, value]) => (
                <div
                  key={key}
                  className="field"
                >
                  <strong>
                    {key.replaceAll("_", " ")}
                  </strong>

                  <div>{value}</div>

                </div>
              )
            )}

          </div>
        )}

        <div className="supported">
          <p>Supported Documents</p>

          <ul>
            <li>Driver License</li>
            <li>Passport</li>
            <li>Birth Certificate</li>
            <li>Naturalization Certificate</li>
            <li>Social Security Card</li>
          </ul>
        </div>

      </div>
    </div>
  );
}