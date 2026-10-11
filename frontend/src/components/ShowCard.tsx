import React from "react";
import type { ShowDto } from "../types/schedule";
import "./ShowCard.css";

interface ShowCardProps {
  show: ShowDto;
}

export const ShowCard: React.FC<ShowCardProps> = ({ show }) => {
  return (
    <div className="show-card">
      <h4 className="show-name">{show.name}</h4>
      <div className="show-time">
        <span className="time-badge">Hour {show.start_time} – {show.end_time}</span>
      </div>
    </div>
  );
};
