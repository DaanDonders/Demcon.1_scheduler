import React from "react";
import type { FestivalScheduleDto } from "../types/schedule";
import { StageColumn } from "./StageColumn";
import "./ScheduleBoard.css";

interface ScheduleBoardProps {
  schedule: FestivalScheduleDto;
}

export const ScheduleBoard: React.FC<ScheduleBoardProps> = ({ schedule }) => {
  if (!schedule.stages || schedule.stages.length === 0) {
    return (
      <div className="schedule-empty-state">
        <div className="empty-icon">📅</div>
        <h3>No Schedule Available</h3>
        <p>There are currently no stages or shows planned for this festival.</p>
      </div>
    );
  }

  return (
    <div className="schedule-board-container">
      <div className="schedule-stages-grid">
        {schedule.stages.map((stage) => (
          <StageColumn key={stage.stage_number} stage={stage} />
        ))}
      </div>
    </div>
  );
};
