import { useState, useEffect } from "react";
import { ScheduleBoard } from "./components/ScheduleBoard";
import { mockSchedule, emptySchedule } from "./data/mockSchedule";
import { fetchSchedule } from "./services/api";
import type { FestivalScheduleDto } from "./types/schedule";
import "./App.css";

function App() {
  const [useMock, setUseMock] = useState(false);
  const [mockType, setMockType] = useState<"populated" | "empty">("populated");

  const [liveSchedule, setLiveSchedule] = useState<FestivalScheduleDto | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!useMock) {
      setLoading(true);
      setError(null);
      fetchSchedule()
        .then((data) => {
          setLiveSchedule(data);
          setLoading(false);
        })
        .catch((err) => {
          setError(err.message || "Failed to load live schedule from backend.");
          setLoading(false);
        });
    }
  }, [useMock]);

  let currentSchedule: FestivalScheduleDto = { stages: [] };
  if (useMock) {
    currentSchedule = mockType === "empty" ? emptySchedule : mockSchedule;
  } else if (liveSchedule) {
    currentSchedule = liveSchedule;
  }

  return (
    <div className="app-container">
      <header className="app-header">
        <div className="header-content">
          <h1>Festival Schedule</h1>
          <p className="subtitle">
            {useMock
              ? `Displaying Mock Data (${mockType})`
              : "Displaying Live Schedule from Python Backend"}
          </p>
        </div>
        <div className="header-controls">
          <button
            type="button"
            className="toggle-button"
            onClick={() => {
              if (useMock) {
                setUseMock(false);
              } else {
                setUseMock(true);
                setMockType("populated");
              }
            }}
          >
            {useMock ? "Switch to Live Backend" : "Switch to Mock Data"}
          </button>
          {useMock && (
            <button
              type="button"
              className="toggle-button secondary"
              onClick={() => setMockType(mockType === "populated" ? "empty" : "populated")}
            >
              {mockType === "populated" ? "Test Mock Empty State" : "Test Mock Populated"}
            </button>
          )}
        </div>
      </header>

      <main className="app-main">
        {loading && !useMock ? (
          <div className="schedule-loading-state">
            <div className="spinner">⏳</div>
            <p>Loading schedule from Python backend...</p>
          </div>
        ) : error && !useMock ? (
          <div className="schedule-error-state">
            <h3>⚠️ Connection Error</h3>
            <p>{error}</p>
            <p className="error-hint">Make sure the Python API server is running on port 8000 (`python src/server.py`).</p>
            <button
              type="button"
              className="toggle-button"
              onClick={() => {
                setUseMock(true);
                setMockType("populated");
              }}
            >
              Switch to Mock Data Fallback
            </button>
          </div>
        ) : (
          <ScheduleBoard schedule={currentSchedule} />
        )}
      </main>

      <footer className="app-footer">
        <p>DEMCON Challenge - Festival Stage Scheduler Frontend & Python Backend</p>
      </footer>
    </div>
  );
}

export default App;
