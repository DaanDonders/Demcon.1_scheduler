import type { FestivalScheduleDto } from "../types/schedule";

export async function fetchSchedule(): Promise<FestivalScheduleDto> {
  const response = await fetch("/api/schedule");
  if (!response.ok) {
    throw new Error(`Failed to fetch schedule: ${response.status} ${response.statusText}`);
  }
  const data = await response.json();
  return data as FestivalScheduleDto;
}
