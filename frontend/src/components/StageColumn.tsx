import React from "react";
import type { StageDto } from "../types/schedule";
import { ShowCard } from "./ShowCard";
import "./StageColumn.css";

interface StageColumnProps {
  stage: StageDto;
}

export const StageColumn: React.FC<StageColumnProps> = ({ stage }) => {
  return (
    <div className="stage-column">
      <div className="stage-header">
        <h3 className="stage-title">Stage {stage.stage_number}</h3>
        <span className="stage-count">{stage.shows.length} {stage.shows.length === 1 ? 'Show' : 'Shows'}</span>
      </div>
      <div className="stage-shows-list">
        {stage.shows.length === 0 ? (
          <p className="no-shows">No shows scheduled on this stage.</p>
        ) : (
          stage.shows.map((show, index) => (
            <ShowCard key={`${show.name}-${index}`} show={show} />
          ))
        )}
      </div>
    </div>
  );
};
