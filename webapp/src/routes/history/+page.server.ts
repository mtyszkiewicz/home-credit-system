import type { ActivityRecordsHistory } from '../../types';

const API_BASE: string = "http://192.168.1.17:5055";

export async function load() {
  const historyRes = await fetch(`${API_BASE}/activity_records`);
  const history: ActivityRecordsHistory[] = await historyRes.json();

  return {
    history: history
  }
}
