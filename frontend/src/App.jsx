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
    setResult(null);

    try {

      const response = await fetch(
        "http://localhost:8000/scan",
        {
          method: "POST",
          body: formData
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

        <h1 className="logo">
          CIT OCR
        </h1>

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

          <p className="loading">
            Scanning document...
          </p>

        )}

        {result && (

          <div className="result-card">

            <div className="result-header">

              <h2>
                {result.document_type
                  .replaceAll("_", " ")
                  .toUpperCase()}
              </h2>

              <div className="confidence">

                {(result.confidence * 100).toFixed(0)}%

              </div>

            </div>

            {Object.entries(result.fields).map(
              ([key, value]) => (

                <div
                  key={key}
                  className="field-row"
                >

                  <div className="field-label">

                    {key
                      .replaceAll("_", " ")
                      .replace(
                        /\b\w/g,
                        c => c.toUpperCase()
                      )}

                  </div>

                  <div className="field-value">

                    {value}

                  </div>

                </div>

              )
            )}

          </div>

        )}

        {!result && (

          <div className="supported">

            <p>
              Supported Documents
            </p>

            <ul>
              <li>Driver License</li>
              <li>Passport</li>
              <li>Birth Certificate</li>
              <li>Naturalization Certificate</li>
              <li>Social Security Card</li>
            </ul>

          </div>

        )}

      </div>

    </div>
  );
}