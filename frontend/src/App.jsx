import { useState } from "react";

export default function App() {

  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [history, setHistory] = useState([]);
  const [dragging, setDragging] = useState(false);

  async function processFile(file) {

    if (!file) return;

    const formData = new FormData();

    formData.append("file", file);

    setLoading(true);

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

      setHistory(prev => [
        data,
        ...prev
      ]);

    } catch (error) {

      console.error(error);

      alert("Upload failed");

    } finally {

      setLoading(false);
    }
  }

  async function uploadFile(event) {

    const file = event.target.files[0];

    processFile(file);
  }

  function handleDrop(event) {

    event.preventDefault();

    setDragging(false);

    const file = event.dataTransfer.files[0];

    processFile(file);
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

        <label
          className={`drop-zone ${dragging ? "dragging" : ""}`}

          onDragOver={(e) => {
            e.preventDefault();
            setDragging(true);
          }}

          onDragLeave={() => {
            setDragging(false);
          }}

          onDrop={handleDrop}
        >

          <label className="upload-btn">

            Upload Document

            <input
              type="file"
              onChange={uploadFile}
              style={{ display: "none" }}
            />

          </label>

          <p className="drop-text">
            or drag and drop a document here
          </p>

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

            <div className="section-title">
              Identity
            </div>

            <div className="field-row">

              <div className="field-label">
                Name
              </div>

              <div className="field-value">

                {result.fields.first_name || ""}
                {" "}
                {result.fields.last_name || ""}

              </div>

            </div>

            {result.fields.date_of_birth && (

              <div className="field-row">

                <div className="field-label">
                  Date of Birth
                </div>

                <div className="field-value">
                  {result.fields.date_of_birth}
                </div>

              </div>

            )}

            {result.fields.document_number && (

              <div className="field-row">

                <div className="field-label">
                  Document Number
                </div>

                <div className="field-value">
                  {result.fields.document_number}
                </div>

              </div>

            )}

            {result.fields.expiration_date && (

              <div className="field-row">

                <div className="field-label">
                  Expiration Date
                </div>

                <div className="field-value">
                  {result.fields.expiration_date}
                </div>

              </div>

            )}

          </div>

        )}

        {history.length > 0 && (

          <div className="result-card">

            <div className="section-title">
              Recent Scans
            </div>

            {history.map((scan, idx) => (

              <div
                key={idx}
                className="field-row"
              >

                <div className="field-value">

                  {scan.document_type
  .replaceAll("_", " ")
  .replace(/\b\w/g, c => c.toUpperCase())}

                </div>

              </div>

            ))}

          </div>

        )}

      </div>

    </div>
  );
}