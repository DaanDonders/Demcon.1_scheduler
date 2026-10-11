export interface ShowDto {
  name: string;
  start_time: number;
  end_time: number;
}

export interface StageDto {
  stage_number: number;
  shows: ShowDto[];
}

export interface FestivalScheduleDto {
  stages: StageDto[];
}
