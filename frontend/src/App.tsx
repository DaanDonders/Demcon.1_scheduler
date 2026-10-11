import { useState } from "react";
import { ScheduleBoard } from "./components/ScheduleBoard";
import { mockSchedule, emptySchedule } from "./data/mockSchedule";
import "./App.css";

function App() {
  const [isDemoEmpty, setIsDemoEmpty] = useState(false);
  const currentSchedule = isDemoEmpty ? emptySchedule : mockSchedule;

  return (
    <div className="app-container">
      <header className="app-header">
        <div className="header-content">
          <h1>Festival Schedule</h1>
          <p className="subtitle">Interactive Stage & Show Timeline</p>
        </div>
        <div className="header-controls">
          <button 
            type="button"
            className="toggle-button"
            onClick={() => setIsDemoEmpty(!isDemoEmpty)}
          >
            {isDemoEmpty ? "Load Populated Schedule" : "Test Empty State"}
          </button>
        </div>
      </header>

      <main className="app-main">
        <ScheduleBoard schedule={currentSchedule} />
      </main>

      <footer className="app-footer">
        <p>DEMCON Challenge - Festival Stage Scheduler Frontend</p>
      </footer>
    </div>
  );
}

export default App;

