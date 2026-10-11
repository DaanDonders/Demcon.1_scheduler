import type { FestivalScheduleDto } from "../types/schedule";

export const mockSchedule: FestivalScheduleDto = {
  stages: [
    {
      stage_number: 1,
      shows: [
        { name: "Opening Ceremony", start_time: 1, end_time: 4 },
        { name: "Indie Rockers", start_time: 14, end_time: 21 },
        { name: "Acoustic Sunset", start_time: 30, end_time: 36 },
      ],
    },
    {
      stage_number: 2,
      shows: [
        { name: "Synth Wave", start_time: 5, end_time: 10 },
        { name: "Electro Party", start_time: 20, end_time: 28 },
        { name: "Late Night Beats", start_time: 33, end_time: 36 },
      ],
    },
    {
      stage_number: 3,
      shows: [
        { name: "Brass Band", start_time: 2, end_time: 9 },
        { name: "Jazz Ensemble", start_time: 15, end_time: 20 },
        { name: "Festival Finale", start_time: 37, end_time: 41 },
      ],
    },
  ],
};

export const emptySchedule: FestivalScheduleDto = {
  stages: [],
};
